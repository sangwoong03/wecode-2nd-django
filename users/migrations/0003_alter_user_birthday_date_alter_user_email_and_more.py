# Generated by Django 4.0.6 on 2022-07-07 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_kakao_id_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday_date',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
