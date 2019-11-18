# Generated by Django 2.1.11 on 2019-11-18 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0001_initial'),
        ('mocks', '0005_mock_content_onetoone'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='tenant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tenants.Tenant'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='content',
            name='tenant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tenants.Tenant'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='endpoint',
            name='tenant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tenants.Tenant'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='header',
            name='tenant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tenants.Tenant'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='headertype',
            name='tenant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tenants.Tenant'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='httpverb',
            name='tenant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tenants.Tenant'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='params',
            name='tenant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tenants.Tenant'),
            preserve_default=False,
        ),
    ]
