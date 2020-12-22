# Generated by Django 2.1.1 on 2019-08-04 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_paidusers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tokens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('validity', models.IntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='paidusers',
            name='valid_until',
            field=models.DateTimeField(null=True),
        ),
    ]
