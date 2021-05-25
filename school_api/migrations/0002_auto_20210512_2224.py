# Generated by Django 3.2 on 2021-05-12 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='address',
            name='street_address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='address',
            name='zipcode',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='building',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='dayofweek',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=255),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='persontype',
            name='person_type',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_number',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='semester',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='start_time',
            field=models.CharField(choices=[('07:00:00', '7 am'), ('08:00:00', '8 am'), ('09:00:00', '9 am'), ('11:00:00', '10 am'), ('12:00:00', '11 am'), ('13:00:00', '12 am'), ('14:00:00', '1 pm'), ('15:00:00', '2 pm'), ('16:00:00', '3 pm')], max_length=255),
        ),
    ]