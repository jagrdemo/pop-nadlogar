# Generated by Django 4.1.9 on 2023-05-09 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0026_kvadratnaizracunajnicle_kvadratnaneenacba_neenacba_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SistemEnacbZDvemaSpremenljivkama',
            fields=[
                ('problem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='problems.problem')),
                ('minimalna_vrednost', models.SmallIntegerField(default=-20, help_text='Najmanjša možna vrednost koeficientov enačbe', verbose_name='minimalna vrednost')),
                ('maksimalna_vrednost', models.SmallIntegerField(default=20, help_text='Največja možna vrednost koeficientov enačbe', verbose_name='maksimalna vrednost')),
            ],
            options={
                'verbose_name': 'Sistemi enačb / reševanje sistema enačb z dvema neznankama',
            },
            bases=('problems.problem',),
        ),
    ]
