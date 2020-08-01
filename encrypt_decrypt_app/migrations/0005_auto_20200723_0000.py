# Generated by Django 3.0.8 on 2020-07-23 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('encrypt_decrypt_app', '0004_remove_user_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorite_encryption',
            field=models.ForeignKey(choices=[('CAESAR CIPHER', 'CAESAR CIPHER'), ('ATBASH CIPHER', 'ATBASH CIPHER'), ('VIGENERE CIPHER', 'VIGENERE CIPHER'), ('MORSE CODE', 'MORSE CODE'), ('NATO CODE', 'NATO CODE'), ('REVERSE CIPHER', 'REVERSE CIPHER')], null=True, on_delete=django.db.models.deletion.CASCADE, to='encrypt_decrypt_app.Encryption'),
        ),
        migrations.AddField(
            model_name='user',
            name='score',
            field=models.IntegerField(default=0, null=True),
        ),
    ]