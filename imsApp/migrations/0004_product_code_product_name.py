
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imsApp', '0003_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
