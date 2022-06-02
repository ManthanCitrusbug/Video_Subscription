# Generated by Django 4.0.4 on 2022-05-27 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0003_alter_user_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('discription', models.TextField()),
                ('is_premium', models.BooleanField(default=False)),
            ],
        ),
    ]