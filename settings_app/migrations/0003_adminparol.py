# Generated by Django 5.0 on 2024-02-27 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings_app', '0002_alter_sitesettings_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminParol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parol', models.BigIntegerField()),
            ],
        ),
    ]
