# Generated by Django 3.0.2 on 2020-05-31 14:33

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='gallery')),
                ('liked', models.ManyToManyField(blank=True, default=None, related_name='liked', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserMoreInfoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobby', user.models.ListField(max_length=300)),
                ('do_you_take_alcohol', models.CharField(choices=[('Never', 'Never'), ('On special occasion', 'On special occasion'), ('Once a week', 'Once a week'), ('Few times a week', 'Few times a week'), ('Daily', 'Daily')], default='Never', max_length=500)),
                ('do_you_smoke', models.CharField(choices=[('Non-smoker', 'Non-smoker'), ('Occasional smoker', 'Occasional smoker'), ('Smoker', 'Smoker')], default='Non-smoker', max_length=500)),
                ('sport', user.models.ListField(max_length=300)),
                ('music', user.models.ListField(max_length=300)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='profile_pics')),
                ('user', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OthersProfiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=10)),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.GalleryNew')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_image', models.ImageField(default='image.png', upload_to=user.models.Gallery.image_directory_path)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BioDataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.CharField(choices=[('< 60inches(152.40cm)', '< 60inches(152.40cm)'), ('> 60inches(152.40cm) but < 65inches(165.10cm)', '> 60inches(152.40cm) but < 65inches(165.10cm)'), ('> 65inches(165.10cm) but < 70inches(177.80cm)', '> 65inches(165.10cm) but < 70inches(177.80cm)'), ('> 70inches(177.80) but < 75inches(190.50cm)', '> 70inches(177.80) but < 75inches(190.50cm)'), ('> 75inches(190.50cm) but < 80inches(203.20cm)', '> 75inches(190.50cm) but < 80inches(203.20cm)'), ('> 80inches(203.20cm) but < 85inches(215.90cm)', '> 80inches(203.20cm) but < 85inches(215.90cm)'), ('> 85inches(215.90cm) but < 90inches(228.6)', '> 85inches(215.90cm) but < 90inches(228.6cm)'), ('> 90inches(228.6cm)', '> 90inches(228.6cm))')], max_length=100)),
                ('eye_color', models.CharField(choices=[('light', 'light'), ('brown', 'brown'), ('black', 'black')], max_length=100)),
                ('hair_color', models.CharField(choices=[('light', 'light'), ('brown', 'brown'), ('black', 'black')], max_length=100)),
                ('complexion', models.CharField(choices=[('very light', 'very light'), ('light', 'light'), ('brown/chocolate', 'brown/chocolate'), ('dark brown', 'dark brown'), ('very dark', 'very dark')], max_length=100)),
                ('date_of_birth', models.DateField()),
                ('age', models.IntegerField()),
                ('sex', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=100)),
                ('religion', models.CharField(choices=[('christainity', 'christainity'), ('islam', 'islam'), ('traditional', 'traditional'), ('atheist', 'atheist')], max_length=100)),
                ('institution', models.CharField(default='Funaab', max_length=100)),
                ('describe', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
