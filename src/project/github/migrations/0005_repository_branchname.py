# Generated by Django 4.0 on 2022-08-09 20:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0004_rename_github_repository'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='branchName',
            field=models.TextField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
