# Generated by Django 2.2.5 on 2020-01-09 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support_ticket', '0002_remove_ticket_customername'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='customerName',
            field=models.CharField(default='NULL', max_length=100),
        ),
    ]