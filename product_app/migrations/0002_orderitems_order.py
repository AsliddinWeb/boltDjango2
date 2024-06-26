# Generated by Django 5.0 on 2023-12-12 16:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soni', models.BigIntegerField(default=1)),
                ('foydalanuvchi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('maxsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_app.maxsulot')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jami_maxsulot', models.BigIntegerField()),
                ('status', models.CharField(choices=[('1', 'Buyurtma berildi'), ('2', 'Bajarildi'), ('3', 'Bekor qilindi')], default='1', max_length=255)),
                ('bekor_qilish_sababi', models.TextField(blank=True, null=True)),
                ('foydalanuvchi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('maxsulotlar', models.ManyToManyField(to='product_app.orderitems')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
