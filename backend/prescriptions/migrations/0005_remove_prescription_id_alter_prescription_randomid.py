# Generated by Django 4.1.7 on 2023-04-10 09:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("prescriptions", "0004_alter_prescription_doctor_alter_prescription_patient"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="prescription",
            name="id",
        ),
        migrations.AlterField(
            model_name="prescription",
            name="randomId",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
