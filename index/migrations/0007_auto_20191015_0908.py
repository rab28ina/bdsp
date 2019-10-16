# Generated by Django 2.2.4 on 2019-10-15 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20191013_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='Contents',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='Result',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='orgbaseinfo',
            name='Address',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='orgbaseinfo',
            name='OfficeHour',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='orgbaseinfo',
            name='PR',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='orgbaseinfo',
            name='Region',
            field=models.CharField(blank=True, choices=[('Addis Ababa', 'Addis Ababa'), ('Afar', 'Afar'), ('Amhara', 'Amhara'), ('Benishangul-Gumuz', 'Benishangul-Gumuz'), ('Dire Dawa', 'Dire Dawa'), ('Gambela', 'Gambela'), ('Harari', 'Harari'), ('Oromia', 'Oromia'), ('Somali', 'Somali'), ('Tigray', 'Tigray')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='orgbaseinfo',
            name='Telephone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='orgbaseinfo',
            name='Url',
            field=models.URLField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='Contents',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='Service',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
