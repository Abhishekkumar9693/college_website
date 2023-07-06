# Generated by Django 2.1.5 on 2019-04-15 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_newevent_newnotice_newresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eventimg',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('e_name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='events/')),
            ],
        ),
        migrations.AlterField(
            model_name='newevent',
            name='img',
            field=models.ImageField(upload_to='event/'),
        ),
    ]
