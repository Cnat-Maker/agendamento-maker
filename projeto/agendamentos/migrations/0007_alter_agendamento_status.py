# Generated by Django 5.2 on 2025-04-08 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0006_agendamento_data_prevista_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='status',
            field=models.CharField(choices=[('S', 'Solicitado'), ('A', 'Andamento'), ('F', 'Finalizado')], default='S', max_length=1),
        ),
    ]
