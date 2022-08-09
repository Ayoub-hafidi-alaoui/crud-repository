# Generated by Django 4.1 on 2022-08-08 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Github',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('repositoryName', models.CharField(max_length=100)),
                ('repositoryDescription', models.TextField(max_length=1000)),
                ('stars', models.IntegerField()),
                ('tags', models.CharField(max_length=100)),
                ('issues', models.CharField(max_length=100)),
                ('followers', models.IntegerField()),
                ('following', models.IntegerField()),
                ('pullRequestsName', models.CharField(max_length=100)),
                ('pullRequestsStatus', models.CharField(max_length=100)),
            ],
        ),
    ]