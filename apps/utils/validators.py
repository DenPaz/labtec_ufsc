from datetime import date

from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from django.utils.translation import gettext_lazy as _


class FileSizeValidator(BaseValidator):
    message = _("O arquivo não pode exceder %(limit_value)s %(unit)s.")
    code = "limit_value"
    units_in_bytes = {
        "KB": 1024,
        "MB": 1024 * 1024,
        "GB": 1024 * 1024 * 1024,
    }

    def __init__(self, limit_value, unit="MB"):
        if unit not in self.units_in_bytes:
            raise ValueError(f"Unit '{unit}' is not supported. Use 'KB', 'MB' or 'GB'.")
        self.unit = unit
        self.max_size_bytes = limit_value * self.units_in_bytes[unit]
        super().__init__(limit_value)

    def __call__(self, value):
        if value.size > self.max_size_bytes:
            raise ValidationError(
                self.message,
                code=self.code,
                params={
                    "limit_value": self.limit_value,
                    "unit": self.unit,
                },
            )


class DateValidator(BaseValidator):
    message_1 = _("Não é possível escolher uma data anterior à de hoje.")
    message_2 = _("Escolha um dia útil da semana.")

    def __init__(self):
        super().__init__(limit_value=None)

    def __call__(self, value):
        today = date.today()
        week_day = value.weekday()
        if value < today:
            raise ValidationError(self.message_1)
        if week_day in [5, 6]:
            raise ValidationError(self.message_2)
