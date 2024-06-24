from django.core.management.base import BaseCommand
from django.db import connection

from ...models import User, UserProfile


class Command(BaseCommand):
    def handle(self, *args, **options):
        default_password = "2305"
        test_users = [
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
        for test_user in test_users:
            obj, created = User.objects.update_or_create(
                email=test_user["email"],
                defaults={**test_user},
            )
            if created:
                obj.set_password(default_password)
                obj.save(update_fields=["password"])

        test_user_profiles = [
            {
                "user": User.objects.get(email="dppazlopez@gmail.com"),
                "curso": "EC",
                "nacionalidade": "EC",
                "data_nascimento": "1994-05-23",
            },
            {
                "user": User.objects.get(email="alissonpereira@gmail.com"),
                "curso": "EC",
                "nacionalidade": "BR",
                "data_nascimento": "2001-02-13",
            },
            {
                "user": User.objects.get(email="joaopereira@gmail.com"),
                "curso": "EE",
                "nacionalidade": "BR",
                "data_nascimento": "1998-08-10",
            },
            {
                "user": User.objects.get(email="crismetsen@gmail.com"),
                "curso": "FISIO",
                "nacionalidade": "US",
                "data_nascimento": "2003-11-15",
            },
            {
                "user": User.objects.get(email="xavieroliveira@gmail.com"),
                "curso": "MED",
                "nacionalidade": "AR",
                "data_nascimento": "2000-12-11",
            },
            {
                "user": User.objects.get(email="andresilva@gmail.com"),
                "curso": "TIC",
                "nacionalidade": "CO",
                "data_nascimento": "1990-02-01",
            },
        ]
        for test_user_profile in test_user_profiles:
            UserProfile.objects.update_or_create(
                user=test_user_profile["user"],
                defaults={**test_user_profile},
            )

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT setval(pg_get_serial_sequence('users_user', 'id'), coalesce(max(id), 1) + 1, false) FROM users_user;"
            )
