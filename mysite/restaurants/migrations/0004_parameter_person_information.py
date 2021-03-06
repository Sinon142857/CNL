# Generated by Django 2.2.1 on 2019-05-26 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_remove_restaurant_address1'),
    ]

    operations = [
        migrations.CreateModel(
            name='parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_number', models.IntegerField(default=0)),
                ('timeout', models.IntegerField(default=0.0)),
                ('skip_probability', models.FloatField(default=0.0)),
                ('arrive_time', models.IntegerField(default=0)),
                ('average_dining_time', models.IntegerField(default=0)),
                ('table_number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='person_information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('ID_number', models.CharField(blank=True, max_length=50)),
                ('place', models.IntegerField(default=0)),
                ('waiting_time', models.FloatField(default=0.0)),
            ],
        ),
    ]
