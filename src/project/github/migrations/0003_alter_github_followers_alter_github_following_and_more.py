# Generated by Django 4.0 on 2022-08-09 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0002_github_commits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='github',
            name='followers',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='github',
            name='following',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='github',
            name='stars',
            field=models.IntegerField(null=True),
        ),
    ]
