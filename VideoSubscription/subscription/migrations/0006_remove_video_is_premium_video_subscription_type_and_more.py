# Generated by Django 4.0.4 on 2022-06-02 05:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0005_video_image_video_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='is_premium',
        ),
        migrations.AddField(
            model_name='video',
            name='subscription_type',
            field=models.CharField(blank=True, choices=[('free', 'Free'), ('monthly', 'Monthly'), ('yearly', 'yearly')], default='free', max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='image',
            field=models.ImageField(default='images/thumbnail.jpg', upload_to='images/'),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membership_type', models.CharField(choices=[('free', 'free'), ('monthly', 'monthly'), ('yearly', 'yearly')], default='free', max_length=10)),
                ('expiry_date', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
