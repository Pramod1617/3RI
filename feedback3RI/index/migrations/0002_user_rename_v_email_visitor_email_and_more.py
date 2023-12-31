# Generated by Django 4.2.5 on 2023-10-11 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Rating', models.IntegerField()),
                ('Message', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='visitor',
            old_name='v_email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='visitor',
            old_name='v_message',
            new_name='Message',
        ),
        migrations.RenameField(
            model_name='visitor',
            old_name='v_name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='visitor',
            old_name='v_number',
            new_name='Phone_number',
        ),
    ]
