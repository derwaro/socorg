# Generated by Django 4.1.7 on 2023-03-07 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0002_alter_chart_chart_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chart',
            name='chart_name',
            field=models.CharField(default='ptyyjyvzam', max_length=200, unique=True),
        ),
        migrations.AddConstraint(
            model_name='persona',
            constraint=models.UniqueConstraint(condition=models.Q(('is_ego', True)), fields=('chart',), name='unique_ego_per_chart'),
        ),
    ]
