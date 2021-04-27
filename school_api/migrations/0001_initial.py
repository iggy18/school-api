# Generated by Django 3.2 on 2021-04-26 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('street_address', models.CharField(max_length=90)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('building_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_api.address')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='DayOfWeek',
            fields=[
                ('day_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_api.address')),
            ],
        ),
        migrations.CreateModel(
            name='PersonType',
            fields=[
                ('person_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('person_type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('semester_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('slot_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.CharField(choices=[('07:00:00', '7 am'), ('08:00:00', '8 am'), ('09:00:00', '9 am'), ('11:00:00', '10 am'), ('12:00:00', '11 am'), ('13:00:00', '12 am'), ('14:00:00', '1 pm'), ('15:00:00', '2 pm'), ('16:00:00', '3 pm')], max_length=8)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_api.course')),
                ('day_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_api.dayofweek')),
                ('semester_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_api.semester')),
            ],
        ),
        migrations.CreateModel(
            name='StudentEnrollment',
            fields=[
                ('student_enrollment_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_api.course')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_api.person')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('school_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_api.address')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.AutoField(primary_key=True, serialize=False)),
                ('room_number', models.CharField(max_length=3)),
                ('building_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_api.building')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='person_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_api.persontype'),
        ),
        migrations.AddField(
            model_name='course',
            name='room_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_api.room'),
        ),
        migrations.AddField(
            model_name='course',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_api.subject'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_api.person'),
        ),
        migrations.AddField(
            model_name='building',
            name='school_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_api.school'),
        ),
    ]