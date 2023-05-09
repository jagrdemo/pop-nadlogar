# Generated by Django 4.1.9 on 2023-05-09 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0025_temegorisceenacba_premaknjena'),
    ]

    operations = [
        migrations.CreateModel(
            name='KvadratnaIzracunajNicle',
            fields=[
                ('problem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='problems.problem')),
                ('kompleksni_nicli', models.BooleanField(choices=[(True, 'Da'), (False, 'Ne')], default=False, help_text='Ali sta ničli lahko kompleksni?', verbose_name='Kompleksni ničli')),
            ],
            options={
                'verbose_name': 'Kvadratna funkcija / Ničle kvadratne funkcije',
            },
            bases=('problems.problem',),
        ),
        migrations.CreateModel(
            name='KvadratnaNeenacba',
            fields=[
                ('problem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='problems.problem')),
                ('primerjava_s_stevilom', models.BooleanField(choices=[(True, 'Da'), (False, 'Ne')], default=True, help_text='Ali naj na le na eni strani enačbe nastopa kvadratna funkcija?', verbose_name='konstanta')),
            ],
            options={
                'verbose_name': 'Kvadratna funkcija / Reševanje kvadratnih neenačb',
            },
            bases=('problems.problem',),
        ),
        migrations.CreateModel(
            name='Neenacba',
            fields=[
                ('problem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='problems.problem')),
                ('kvadratna', models.BooleanField(choices=[(True, 'Da (kvadratna člena se odštejeta)'), (False, 'Ne')], default=False, help_text='Ali naj bosta enačbi kvadratni?', verbose_name='Kvadratna enačba')),
            ],
            options={
                'verbose_name': 'Linearna funkcija / Linearne neenačbe',
            },
            bases=('problems.problem',),
        ),
        migrations.CreateModel(
            name='OblikeEnacbPremice',
            fields=[
                ('problem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='problems.problem')),
            ],
            options={
                'verbose_name': 'Linearna funkcija / Odsekovna in eksplicitna oblika',
            },
            bases=('problems.problem',),
        ),
        migrations.CreateModel(
            name='PremicaSkoziTocki',
            fields=[
                ('problem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='problems.problem')),
            ],
            options={
                'verbose_name': 'Linearna funkcija / Enačba premice skozi dve točki',
            },
            bases=('problems.problem',),
        ),
        migrations.CreateModel(
            name='PremiceTrikotnik',
            fields=[
                ('problem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='problems.problem')),
            ],
            options={
                'verbose_name': 'Linearna funkcija / Ploščina trikotnika',
            },
            bases=('problems.problem',),
        ),
        migrations.CreateModel(
            name='Presecisce',
            fields=[
                ('problem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='problems.problem')),
            ],
            options={
                'verbose_name': 'Kvadratna funkcija / Presečišče parabole in premice',
            },
            bases=('problems.problem',),
        ),
        migrations.CreateModel(
            name='RazdaljaMedTockama',
            fields=[
                ('problem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='problems.problem')),
            ],
            options={
                'verbose_name': 'Linearna funkcija / Računanje razdalje med dvema točkama',
            },
            bases=('problems.problem',),
        ),
        migrations.CreateModel(
            name='SistemDvehEnacb',
            fields=[
                ('problem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='problems.problem')),
                ('racionalno', models.BooleanField(choices=[(True, 'Da'), (False, 'Ne (samo cela števila)')], default=False, help_text='Ali smejo biti rešitve racionalne?', verbose_name='Racionalne rešitve')),
            ],
            options={
                'verbose_name': 'Linearna funkcija / Sistem dveh linearnih enačb',
            },
            bases=('problems.problem',),
        ),
        migrations.CreateModel(
            name='SistemTrehEnacb',
            fields=[
                ('problem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='problems.problem')),
                ('manjsi_koeficienti', models.BooleanField(choices=[(True, 'Da'), (False, 'Ne')], default=True, help_text='Ali naj bodo koeficienti omejeni na manjša števila?', verbose_name='Manjša števila')),
            ],
            options={
                'verbose_name': 'Linearna funkcija / Sistem treh linearnih enačb',
            },
            bases=('problems.problem',),
        ),
        migrations.CreateModel(
            name='SkoziTocke',
            fields=[
                ('problem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='problems.problem')),
                ('presecisca', models.BooleanField(choices=[(True, 'Da'), (False, 'Ne (podane bodo tri naključne točke)')], default=True, help_text='Ali naj bosta podani presečišči s koordinatnima osema?', verbose_name='Presečišče z osema')),
            ],
            options={
                'verbose_name': 'Kvadratna funkcija / Predpis kvadratne funkcije iz točk',
            },
            bases=('problems.problem',),
        ),
        migrations.CreateModel(
            name='SplosniClenAritmeticnegaEnacbi',
            fields=[
                ('problem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='problems.problem')),
            ],
            options={
                'verbose_name': 'Zaporedja / enačbi aritmetičnega',
            },
            bases=('problems.problem',),
        ),
        migrations.CreateModel(
            name='SplosniClenAritmeticnegaZaporedja',
            fields=[
                ('problem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='problems.problem')),
                ('od', models.IntegerField(default=1, verbose_name='najmanjša možna vrednost za prvi člen in diferenco')),
                ('do', models.IntegerField(default=10, verbose_name='največja možna vrednost za prvi člen in diferenco')),
            ],
            options={
                'verbose_name': 'Zaporedja / dva člena aritmetičnega',
            },
            bases=('problems.problem',),
        ),
        migrations.CreateModel(
            name='TemenskaOblika',
            fields=[
                ('problem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='problems.problem')),
            ],
            options={
                'verbose_name': 'Kvadratna funkcija / Temenska oblika kvadratne funkcije',
            },
            bases=('problems.problem',),
        ),
        migrations.CreateModel(
            name='VrednostiLinearne',
            fields=[
                ('problem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='problems.problem')),
            ],
            options={
                'verbose_name': 'Linearna funkcija / Vrednosti linearne funkcije',
            },
            bases=('problems.problem',),
        ),
    ]
