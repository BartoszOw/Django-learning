# Generated by Django 5.0.6 on 2024-06-01 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_author_id_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/%d'),
        ),
    ]

