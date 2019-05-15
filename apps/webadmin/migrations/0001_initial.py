# Generated by Django 2.2.1 on 2019-05-14 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoletinModelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('resumen', models.CharField(max_length=250)),
                ('detalle', models.TextField()),
                ('fecha', models.DateField(max_length=10)),
                ('tipo', models.CharField(choices=[('N', 'Noticias'), ('E', 'Eventos')], default='N', max_length=1)),
            ],
        ),
    ]