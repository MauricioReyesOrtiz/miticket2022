# Generated by Django 4.1.2 on 2022-10-27 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('paterno', models.CharField(max_length=50)),
                ('materno', models.CharField(max_length=50)),
                ('fechanac', models.DateTimeField(max_length=50)),
            ],
        ),
    ]
