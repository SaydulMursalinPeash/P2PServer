# Generated by Django 4.2 on 2023-06-13 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_remove_method_symbol_method_buy_rate_and_more'),
        ('order', '0003_order_order_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='wtd',
        ),
        migrations.AddField(
            model_name='order',
            name='account_details',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='coin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_method', to='payment.method'),
        ),
        migrations.AlterField(
            model_name='order',
            name='method',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
