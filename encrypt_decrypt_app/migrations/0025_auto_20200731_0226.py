# Generated by Django 3.0.8 on 2020-07-31 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encrypt_decrypt_app', '0024_auto_20200731_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='../media/'),
        ),
    ]
