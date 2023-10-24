# Generated by Django 4.2.6 on 2023-10-24 04:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comunicado',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=150)),
                ('detalle', models.CharField(max_length=1000)),
                ('detalle_corto', models.CharField(max_length=200)),
                ('tipo', models.CharField(choices=[('S', 'Suspension de actividad'), ('C', 'Suspension de clase'), ('I', 'Informacion')], max_length=1)),
                ('visible', models.BooleanField()),
                ('fecha_publicacion', models.DateTimeField()),
                ('entidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.entidad')),
                ('modificado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modificaciones', to=settings.AUTH_USER_MODEL)),
                ('publicado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publicaciones', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
