# Generated by Django 2.2.11 on 2020-04-19 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conteo', '0003_auto_20200419_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.PositiveSmallIntegerField(unique=True)),
                ('descripcion', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Resultados',
            },
        ),
        migrations.AlterField(
            model_name='paciente',
            name='asma',
            field=models.ForeignKey(on_delete='SET_NULL', related_name='asma', to='conteo.CatSiNo', to_field='clave'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='cardiovascular',
            field=models.ForeignKey(on_delete='SET_NULL', related_name='cardiovascular', to='conteo.CatSiNo', to_field='clave'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='diabetes',
            field=models.ForeignKey(on_delete='SET_NULL', related_name='diabetes', to='conteo.CatSiNo', to_field='clave'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='embarazo',
            field=models.ForeignKey(on_delete='SET_NULL', related_name='embarazo', to='conteo.CatSiNo', to_field='clave'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='epoc',
            field=models.ForeignKey(on_delete='SET_NULL', related_name='epoc', to='conteo.CatSiNo', to_field='clave'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='habla_lengua_indig',
            field=models.ForeignKey(on_delete='SET_NULL', related_name='lenguaindigena', to='conteo.CatSiNo', to_field='clave'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='hipertension',
            field=models.ForeignKey(on_delete='SET_NULL', related_name='hipertension', to='conteo.CatSiNo', to_field='clave'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='inmusupr',
            field=models.ForeignKey(on_delete='SET_NULL', related_name='inmusupr', to='conteo.CatSiNo', to_field='clave'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='migrante',
            field=models.ForeignKey(on_delete='SET_NULL', related_name='migrante', to='conteo.CatSiNo', to_field='clave'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='obesidad',
            field=models.ForeignKey(on_delete='SET_NULL', related_name='obesidad', to='conteo.CatSiNo', to_field='clave'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='otra_com',
            field=models.ForeignKey(on_delete='SET_NULL', related_name='otra_com', to='conteo.CatSiNo', to_field='clave'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='otro_caso',
            field=models.ForeignKey(on_delete='SET_NULL', related_name='otro_caso', to='conteo.CatSiNo', to_field='clave'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='renal_cronica',
            field=models.ForeignKey(on_delete='SET_NULL', related_name='renal_cronica', to='conteo.CatSiNo', to_field='clave'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='resultado',
            field=models.ForeignKey(on_delete='SET_NULL', related_name='resultado', to='conteo.Resultado', to_field='clave'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='tabaquismo',
            field=models.ForeignKey(on_delete='SET_NULL', related_name='tabaquismo', to='conteo.CatSiNo', to_field='clave'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='uci',
            field=models.ForeignKey(on_delete='SET_NULL', related_name='uci', to='conteo.CatSiNo', to_field='clave'),
        ),
    ]
