# Generated by Django 4.1.1 on 2022-10-01 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('altura', models.FloatField(default=0.0)),
            ],
        ),
    ]
