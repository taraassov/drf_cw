# Generated by Django 4.2.7 on 2023-11-17 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='period',
            field=models.CharField(choices=[('DAILY', 'каждый день'), ('WEEKLY', 'раз в неделю')], default='DAILY', max_length=10, verbose_name='Периодичность'),
        ),
    ]
