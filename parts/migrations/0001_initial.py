# Generated by Django 5.0.6 on 2024-06-17 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('sku', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=1024)),
                ('weight_ounces', models.IntegerField()),
                ('is_active', models.BooleanField()),
            ],
            options={
                'db_table': 'parts',
            },
        ),
        migrations.RunSQL( #Create initial entries for 'parts' table
            '''
            INSERT INTO parts (name, sku, description, weight_ounces, is_active) VALUES
            ('Heavy coil', 'SDJDDH8223DHJ', 'Tightly wound nickel-gravy alloy spring', 22, 1),
            ('Reverse lever', 'DCMM39823DSJD', 'Attached to provide inverse leverage', 9, 0),
            ('Macrochip', 'OWDD823011DJSD', 'Used for heavy-load computing', 2, 1);
            '''
        ),
    ]