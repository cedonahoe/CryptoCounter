# Generated by Django 2.0.2 on 2018-04-05 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptocounter', '0002_auto_20180316_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='block_chain',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='coin',
            name='coin_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ico',
            name='end',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='ico',
            name='ico_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ico',
            name='start',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='overallsocial',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='price',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='socialcoin',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='socialico',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='watchitem',
            name='date_added',
            field=models.DateTimeField(),
        ),
    ]
