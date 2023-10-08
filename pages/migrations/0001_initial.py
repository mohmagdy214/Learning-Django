# Generated by Django 4.2.5 on 2023-10-05 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Female',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_female', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Male',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_male', models.CharField(max_length=50, null=True)),
                ('girls', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pages.female')),
            ],
        ),
    ]
