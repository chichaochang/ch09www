# Generated by Django 3.2 on 2021-05-03 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_diary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
