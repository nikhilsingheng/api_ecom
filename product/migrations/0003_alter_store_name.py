# Generated by Django 4.1 on 2022-08-04 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_store_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
