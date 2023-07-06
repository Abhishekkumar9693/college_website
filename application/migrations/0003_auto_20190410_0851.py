# Generated by Django 2.1.5 on 2019-04-10 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_auto_20190409_0331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newstudent',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('fname', models.CharField(max_length=100)),
                ('mname', models.CharField(max_length=100)),
                ('no', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pictures/')),
                ('email', models.CharField(max_length=100)),
                ('pwd', models.CharField(max_length=100)),
                ('dob', models.CharField(max_length=100)),
                ('class1', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='NewUser',
        ),
    ]
