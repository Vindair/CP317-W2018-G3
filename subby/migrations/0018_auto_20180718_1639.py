# Generated by Django 2.0.6 on 2018-07-18 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subby', '0017_auto_20180718_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subletimage',
            name='sublet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sublet', to='subby.Sublet'),
        ),
    ]
