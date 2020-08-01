# Generated by Django 3.0.8 on 2020-07-29 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encrypt_decrypt_app', '0021_auto_20200729_0441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rank',
            field=models.CharField(blank=True, choices=[('Cipher Lord', 'Cipher Lord'), ('Senior Cryptographer', 'Senior Cryptographer'), ('Junior Cryptographer', 'Junior Cryptographer'), ('Analyst', 'Analyst'), ('Rookie Analyst', 'Rookie Analyst')], default='Rookie Analyst', max_length=150, null=True),
        ),
    ]