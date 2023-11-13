# Generated by Django 4.2.6 on 2023-11-11 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0010_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='EDUCATION',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=255, verbose_name='Год')),
                ('title', models.CharField(max_length=255, verbose_name='Научная степень')),
                ('place', models.CharField(max_length=255, verbose_name='Место')),
                ('description', models.TextField(verbose_name='Что вы делали')),
            ],
            options={
                'verbose_name': 'Годы обучение',
                'verbose_name_plural': 'Год обучение',
            },
        ),
        migrations.AlterModelOptions(
            name='experience',
            options={'verbose_name': 'Годы опата', 'verbose_name_plural': 'Год опыта'},
        ),
    ]