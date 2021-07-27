# Generated by Django 3.2.5 on 2021-07-25 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='listing',
            name='current_bid',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='image_url',
            field=models.URLField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='listing',
            name='starting_bid',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=155)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='auctions.listing')),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.DecimalField(decimal_places=2, max_digits=5)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='auctions.listing')),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.category'),
        ),
    ]
