# Generated by Django 4.2.5 on 2023-10-05 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-name']},
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('phone', 'phone'), ('computer', 'computer'), ('ipad', 'ipad'), ('playstation', 'playstation')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='megzz', max_length=50, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=10.0, max_digits=5),
        ),
    ]
