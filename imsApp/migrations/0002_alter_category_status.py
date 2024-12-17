

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('1', 'Active'), ('2', 'Inactive')], default=1, max_length=2),
        ),
    ]
