# Generated by Django 2.2.5 on 2019-09-24 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('omni', '0010_auto_20190924_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outcome',
            name='event',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='outcome', to='omni.Event'),
        ),
    ]
