# Generated by Django 3.0.8 on 2020-07-23 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encrypt_decrypt_app', '0010_auto_20200723_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encryption',
            name='encryption_technique',
            field=models.CharField(choices=[('CAESAR CIPHER', 'Caesar Cipher'), ('ATBASH CIPHER', 'Atbash Cipher'), ('VIGENERE CIPHER', 'Vigenere Cipher'), ('MORSE CODE', 'Morse Code'), ('NATO CODE', 'NATO Code'), ('REVERSE CIPHER', 'Reverse Cipher')], default='MORSE CODE', max_length=30, verbose_name='Encryption Name'),
        ),
    ]
