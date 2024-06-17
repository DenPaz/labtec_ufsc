from django.core.management.base import BaseCommand

from ...models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        default_password = "2305"
        test_super_users = [
            {
                "id": 1,
                "email": "dppazlopez@gmail.com",
                "first_name": "Dennis",
                "last_name": "Paz",
                "is_superuser": True,
            },
            {
                "id": 2,
                "email": "alissonpereira@gmail.com",
                "first_name": "Alisson",
                "last_name": "Pereira",
                "is_superuser": True,
            },
        ]
        test_staff_users = [
            {
                "id": 3,
                "email": "joaopereira@gmail.com",
                "first_name": "João",
                "last_name": "Pereira",
                "is_staff": True,
            },
            {
                "id": 4,
                "email": "crismetsen@gmail.com",
                "first_name": "Cris",
                "last_name": "Metsen",
                "is_staff": True,
            },
        ]
        test_users = [
            {
                "id": 5,
                "email": "xavieroliveira@gmail.com",
                "first_name": "Xavier",
                "last_name": "Oliveira",
            },
            {
                "id": 6,
                "email": "andresilva@gmail.com",
                "first_name": "Andre",
                "last_name": "Silva",
            },
        ]
        all_test_users = test_super_users + test_staff_users + test_users

        for test_user in all_test_users:
            obj, created = User.objects.get_or_create(
                email=test_user["email"],
                defaults={**test_user},
            )
            if created:
                obj.set_password(default_password)
                obj.save(update_fields=["password"])
                self.stdout.write(self.style.SUCCESS(f"User {obj.email} created successfully!"))
            else:
                self.stdout.write(self.style.WARNING(f"User {obj.email} already exists!"))
