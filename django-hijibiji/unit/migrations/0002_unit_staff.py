# Generated by Django 5.0.2 on 2024-02-27 20:42

from django.conf import settings
from django.db import migrations, models


def transfer_unitassignment_staff(apps, schema_editor):
    UnitAssignment = apps.get_model('staff', 'UnitAssignment')
    Unit = apps.get_model('unit', 'Unit')
    
    for assignment in UnitAssignment.objects.all():
        unit = assignment.unit
        unit.staff.add(assignment.staff)

class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='staff',
            field=models.ManyToManyField(related_name='unit_staff', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RunPython(transfer_unitassignment_staff),
    ]