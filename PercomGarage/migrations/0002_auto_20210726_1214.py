# Generated by Django 3.2 on 2021-07-26 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PercomGarage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='vehicule',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='PercomGarage.vehicules'),
        ),
        migrations.AlterField(
            model_name='commande',
            name='client',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='PercomGarage.client'),
        ),
        migrations.AlterField(
            model_name='commande',
            name='employer',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='PercomGarage.employe'),
        ),
        migrations.AlterField(
            model_name='commande',
            name='stocks',
            field=models.ManyToManyField(blank=True, to='PercomGarage.Stock'),
        ),
        migrations.AlterField(
            model_name='employe',
            name='Garage',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='PercomGarage.garage'),
        ),
        migrations.AlterField(
            model_name='facturation',
            name='client',
            field=models.ManyToManyField(blank=True, to='PercomGarage.Client'),
        ),
        migrations.AlterField(
            model_name='facturation',
            name='employer',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='PercomGarage.employe'),
        ),
        migrations.AlterField(
            model_name='garage',
            name='employer',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='PercomGarage.employe'),
        ),
        migrations.AlterField(
            model_name='garage',
            name='vehicule',
            field=models.ManyToManyField(blank=True, to='PercomGarage.Vehicules'),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='client',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='PercomGarage.client'),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='employer',
            field=models.ManyToManyField(blank=True, to='PercomGarage.Employe'),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='vehicule',
            field=models.ManyToManyField(blank=True, to='PercomGarage.Vehicules'),
        ),
        migrations.AlterField(
            model_name='laverie',
            name='employer',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='PercomGarage.employe'),
        ),
        migrations.AlterField(
            model_name='laverie',
            name='vehicule',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='PercomGarage.vehicules'),
        ),
        migrations.AlterField(
            model_name='locations',
            name='client',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='PercomGarage.client'),
        ),
        migrations.AlterField(
            model_name='locations',
            name='vehicule',
            field=models.ManyToManyField(blank=True, to='PercomGarage.Vehicules'),
        ),
        migrations.AlterField(
            model_name='rendezvous',
            name='clients',
            field=models.ManyToManyField(blank=True, to='PercomGarage.Client'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='employer',
            field=models.ManyToManyField(blank=True, to='PercomGarage.Employe'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='piece',
            field=models.ManyToManyField(blank=True, to='PercomGarage.Pieces'),
        ),
    ]
