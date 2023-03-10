# Generated by Django 4.1.7 on 2023-03-10 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0003_alter_chart_chart_name_persona_unique_ego_per_chart'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='bio_father',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children_bio_father', to='charts.persona'),
        ),
        migrations.AddField(
            model_name='persona',
            name='bio_mother',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children_bio_mother', to='charts.persona'),
        ),
        migrations.AddField(
            model_name='persona',
            name='non_bio_fathers',
            field=models.ManyToManyField(blank=True, related_name='children_non_bio_father', to='charts.persona'),
        ),
        migrations.AddField(
            model_name='persona',
            name='non_bio_mothers',
            field=models.ManyToManyField(blank=True, related_name='children_non_bio_mother', to='charts.persona'),
        ),
        migrations.AlterField(
            model_name='chart',
            name='chart_name',
            field=models.CharField(default='qydcdakoyb', max_length=200, unique=True),
        ),
    ]
