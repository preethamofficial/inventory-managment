

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imsApp', '0005_product_price_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction', models.CharField(max_length=250)),
                ('customer', models.CharField(max_length=250)),
                ('total', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0)),
                ('quantity', models.FloatField(default=0)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imsApp.invoice')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imsApp.product')),
                ('stock', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='imsApp.stock')),
            ],
        ),
    ]
