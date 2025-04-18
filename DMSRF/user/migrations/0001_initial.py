# Generated by Django 5.2 on 2025-04-08 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=50)),
                ('user_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('user_age', models.PositiveIntegerField()),
                ('user_phone', models.CharField(max_length=15)),
                ('user_state', models.CharField(choices=[('Barisal', 'Barisal'), ('Chattogram', 'Chattogram'), ('Dhaka', 'Dhaka'), ('Khulna', 'Khulna'), ('Mymensingh', 'Mymensingh'), ('Rajshahi', 'Rajshahi'), ('Rangpur', 'Rangpur'), ('Sylhet', 'Sylhet')], max_length=100)),
                ('user_address', models.TextField()),
            ],
        ),
    ]
