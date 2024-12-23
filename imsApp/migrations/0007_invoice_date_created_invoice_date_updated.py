#

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('imsApp', '0006_invoice_invoice_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='invoice',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
