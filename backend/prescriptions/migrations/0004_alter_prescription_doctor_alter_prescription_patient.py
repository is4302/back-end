# Generated by Django 4.1.7 on 2023-04-10 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("prescriptions", "0003_alter_appointment_doctor_alter_appointment_patient"),
    ]

    operations = [
        migrations.AlterField(
            model_name="prescription",
            name="doctor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="prescriptions.doctorinformation",
            ),
        ),
        migrations.AlterField(
            model_name="prescription",
            name="patient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="prescriptions.patientinformation",
            ),
        ),
    ]