# Generated by Django 5.0.4 on 2024-04-20 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='named_url',
            field=models.CharField(blank=True, help_text='Введите именованную ссылку', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='url',
            field=models.CharField(blank=True, help_text='Введите ссылку', max_length=200, null=True),
        ),
    ]
