# Generated by Django 2.2.6 on 2019-10-26 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='college',
            field=models.CharField(default='no college provided', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='subject',
            field=models.CharField(default='no subject provided', max_length=50),
            preserve_default=False,
        ),
    ]