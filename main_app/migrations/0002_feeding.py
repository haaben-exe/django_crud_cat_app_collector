# Generated by Django 5.1.7 on 2025-04-03 14:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('meal', models.CharField(choices=[('B', 'Breakfast'), ('L', 'Lunch'), ('D', 'Dinner'), ('S', 'Snacks')], default='B', max_length=1)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.cat')),
            ],
        ),
    ]
