# Generated by Django 2.0.2 on 2018-04-19 21:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cryptocounter', '0008_auto_20180412_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralMarket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('market_cap', models.BigIntegerField(default=0)),
                ('volume', models.BigIntegerField(default=0)),
                ('btc_dominance', models.IntegerField(default=0)),
                ('date_added', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='WatchIco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField()),
                ('ico_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cryptocounter.Ico')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
