# Generated by Django 2.1.7 on 2019-05-27 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mhuser', '0004_auto_20190311_0638'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chgpasswd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, default='', max_length=50, null=True)),
                ('vertification', models.CharField(blank=True, default='', max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='mhuser',
            name='blinduser',
            field=models.CharField(blank=True, default='', max_length=150, null=True),
        ),
    ]
