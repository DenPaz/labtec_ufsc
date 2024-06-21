# Generated by Django 4.2.13 on 2024-06-21 23:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("reservas", "0001_initial"),
        ("recursos", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="reservatablet",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Usuário",
            ),
        ),
        migrations.AddField(
            model_name="reservasalareuniao",
            name="sala_reuniao",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="reservas_salas_reuniao",
                to="recursos.salareuniao",
                verbose_name="Sala de reunião",
            ),
        ),
        migrations.AddField(
            model_name="reservasalareuniao",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Usuário",
            ),
        ),
        migrations.AddField(
            model_name="reservaoculusvr",
            name="oculus_vr",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="reservas_oculus_vr",
                to="recursos.oculusvr",
                verbose_name="Oculus VR",
            ),
        ),
        migrations.AddField(
            model_name="reservaoculusvr",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Usuário",
            ),
        ),
        migrations.AddField(
            model_name="reservamesatrabalho",
            name="mesa_trabalho",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="reservas_mesas_trabalho",
                to="recursos.mesatrabalho",
                verbose_name="Mesa de trabalho",
            ),
        ),
        migrations.AddField(
            model_name="reservamesatrabalho",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Usuário",
            ),
        ),
        migrations.AddField(
            model_name="reservakittablet",
            name="kit_tablet",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="reservas_kits_tablet",
                to="recursos.kittablet",
                verbose_name="Kit de tablet",
            ),
        ),
        migrations.AddField(
            model_name="reservakittablet",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Usuário",
            ),
        ),
        migrations.AddField(
            model_name="reservacomputador",
            name="computador",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="reservas_computadores",
                to="recursos.computador",
                verbose_name="Computador",
            ),
        ),
        migrations.AddField(
            model_name="reservacomputador",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Usuário",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="reservatablet",
            unique_together={("data", "horario", "tablet")},
        ),
        migrations.AlterUniqueTogether(
            name="reservasalareuniao",
            unique_together={("data", "horario", "sala_reuniao")},
        ),
        migrations.AlterUniqueTogether(
            name="reservaoculusvr",
            unique_together={("data", "horario", "oculus_vr")},
        ),
        migrations.AlterUniqueTogether(
            name="reservamesatrabalho",
            unique_together={("data", "horario", "mesa_trabalho")},
        ),
        migrations.AlterUniqueTogether(
            name="reservakittablet",
            unique_together={("data", "horario", "kit_tablet")},
        ),
        migrations.AlterUniqueTogether(
            name="reservacomputador",
            unique_together={("data", "horario", "computador")},
        ),
    ]
