# Generated by Django 5.0 on 2023-12-20 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0005_order_created_at_order_updated_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartitems',
            options={'verbose_name_plural': 'Foydalanuvchi savatchasi'},
        ),
        migrations.AlterModelOptions(
            name='maxsulot',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Maxsulotlar'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Buyurtmalar'},
        ),
        migrations.AlterModelOptions(
            name='orderitems',
            options={'verbose_name_plural': 'Buyurtma maxsulotlari'},
        ),
    ]
