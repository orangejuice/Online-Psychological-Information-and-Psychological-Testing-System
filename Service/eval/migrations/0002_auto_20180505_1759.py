# Generated by Django 2.0.4 on 2018-05-05 09:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eval', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scalerecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='scaleitemopt',
            name='bonus',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='eval.ScaleResult'),
        ),
        migrations.AddField(
            model_name='scaleitemopt',
            name='option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eval.ScaleOption'),
        ),
        migrations.AddField(
            model_name='scaleitemopt',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eval.ScaleItem'),
        ),
        migrations.AddField(
            model_name='scaleitem',
            name='opts',
            field=models.ManyToManyField(related_name='options', through='eval.ScaleItemOpt', to='eval.ScaleOption'),
        ),
        migrations.AddField(
            model_name='scaleitem',
            name='scale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eval.Scale'),
        ),
        migrations.AddField(
            model_name='scaleconclusion',
            name='scale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eval.Scale'),
        ),
    ]
