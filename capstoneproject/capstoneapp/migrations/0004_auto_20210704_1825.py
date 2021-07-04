# Generated by Django 3.1.8 on 2021-07-04 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstoneapp', '0003_auto_20210704_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='state',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='zipcode',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]