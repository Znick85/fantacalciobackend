# Generated by Django 5.1.6 on 2025-06-12 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_squadre_serie_a_user_alter_squadre_serie_a_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='squadre_serie_a',
            name='mercato',
            field=models.JSONField(default=list),
        ),
    ]
