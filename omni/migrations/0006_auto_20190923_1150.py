# Generated by Django 2.2.5 on 2019-09-23 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('omni', '0005_auto_20190923_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outcome',
            name='loser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loser', to='omni.Team'),
        ),
        migrations.RemoveField(
            model_name='outcome',
            name='winner',
        ),
        migrations.AddField(
            model_name='outcome',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='omni.Team'),
        ),
    ]