# Generated by Django 3.2.18 on 2023-05-11 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0002_auto_20230509_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='terms',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.payment_terms'),
        ),
    ]
