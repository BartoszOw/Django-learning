# Generated by Django 5.0.6 on 2024-05-19 17:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maths', '0002_alter_math_operation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(blank=True, null=True, unique=True)),
                ('error', models.CharField(blank=True, max_length=255, null=True, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='math',
            name='result',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='maths.result'),
        ),
    ]
