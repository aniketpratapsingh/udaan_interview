# Generated by Django 3.2.5 on 2021-07-24 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoRefresherApp', '0004_user_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='covid_status',
            field=models.CharField(default='not_tested', max_length=20),
        ),
    ]
