# Generated by Django 2.0.3 on 2018-04-01 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_auto_20180331_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_num',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]