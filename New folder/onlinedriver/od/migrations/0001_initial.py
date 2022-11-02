# Generated by Django 3.2.5 on 2022-10-31 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rid', models.CharField(max_length=264, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='driverdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=264, unique=True)),
                ('name', models.CharField(max_length=264)),
                ('password', models.CharField(max_length=264)),
                ('experience', models.CharField(max_length=264)),
                ('dlno', models.CharField(max_length=264)),
                ('inride', models.CharField(max_length=264)),
                ('inrideid', models.CharField(max_length=264)),
                ('inridewith', models.CharField(max_length=264)),
                ('addharno', models.CharField(max_length=264)),
                ('address', models.CharField(max_length=264)),
                ('pin', models.CharField(max_length=264)),
                ('totalrides', models.CharField(max_length=264)),
                ('ratings', models.CharField(max_length=264)),
                ('profilepic', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ownerdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=264, unique=True)),
                ('name', models.CharField(max_length=264)),
                ('password', models.CharField(max_length=264)),
                ('experience', models.CharField(max_length=264)),
                ('dlno', models.CharField(max_length=264)),
                ('addharno', models.CharField(max_length=264)),
                ('inride', models.CharField(max_length=264)),
                ('address', models.CharField(max_length=264)),
                ('pin', models.CharField(max_length=264)),
                ('inrideid', models.CharField(max_length=264)),
                ('inridewith', models.CharField(max_length=264)),
                ('profilepic', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ridedetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rid', models.CharField(max_length=264, unique=True)),
                ('driveremail', models.CharField(max_length=264)),
                ('owneremail', models.CharField(max_length=264)),
                ('startdate', models.CharField(max_length=264)),
                ('enddate', models.CharField(max_length=264)),
                ('starttime', models.CharField(max_length=264)),
                ('endtime', models.CharField(max_length=264)),
                ('status', models.CharField(max_length=264)),
            ],
        ),
    ]
