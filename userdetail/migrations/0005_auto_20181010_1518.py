# Generated by Django 2.0.7 on 2018-10-10 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdetail', '0004_activitysubmittion_accountid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='newsid',
            field=models.AutoField(db_column='NewsID', primary_key=True, serialize=False),
        ),
    ]
