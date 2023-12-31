# Generated by Django 4.1.6 on 2023-07-06 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DataTraining',
            fields=[
                ('id_training', models.AutoField(primary_key=True, serialize=False)),
                ('NIM', models.CharField(max_length=10)),
                ('Algoritma_dan_Pemrograman', models.FloatField(blank=True, default=None, null=True)),
                ('Aljabar_Linier_dan_Matriks', models.FloatField(blank=True, default=None, null=True)),
                ('Fisika_Listrik_dan_Magnet', models.FloatField(blank=True, default=None, null=True)),
                ('Grafik_Komputer', models.FloatField(blank=True, default=None, null=True)),
                ('Kalkulus', models.FloatField(blank=True, default=None, null=True)),
                ('Keamanan_Info_dan_Jaringan', models.FloatField(blank=True, default=None, null=True)),
                ('Kom_Data_dan_Jaringan_Komputer', models.FloatField(blank=True, default=None, null=True)),
                ('Logika_Informatika', models.FloatField(blank=True, default=None, null=True)),
                ('Manajemen_Proyek', models.FloatField(blank=True, default=None, null=True)),
                ('Matematika_Diskrit', models.FloatField(blank=True, default=None, null=True)),
                ('Metode_Numerik', models.FloatField(blank=True, default=None, null=True)),
                ('Multimedia', models.FloatField(blank=True, default=None, null=True)),
                ('Organisasi_dan_Arsitektur_Komp', models.FloatField(blank=True, default=None, null=True)),
                ('Pemrograman_Berorientasi_Obyek', models.FloatField(blank=True, default=None, null=True)),
                ('Pemrograman_Lanjut', models.FloatField(blank=True, default=None, null=True)),
                ('Pemrograman_Web', models.FloatField(blank=True, default=None, null=True)),
                ('Pengantar_Kriptografi', models.FloatField(blank=True, default=None, null=True)),
                ('Prak_Pemrog_Berorient_Obyek', models.FloatField(blank=True, default=None, null=True)),
                ('Prak_Sistem_Basis_Data', models.FloatField(blank=True, default=None, null=True)),
                ('Prak_Algoritma_dan_Pemrograman', models.FloatField(blank=True, default=None, null=True)),
                ('Praktikum_Pemrograman_Lanjut', models.FloatField(blank=True, default=None, null=True)),
                ('Praktikum_Pemrograman_Web', models.FloatField(blank=True, default=None, null=True)),
                ('Praktikum_Struktur_Data', models.FloatField(blank=True, default=None, null=True)),
                ('Rekayasa_Perangkat_Lunak', models.FloatField(blank=True, default=None, null=True)),
                ('Sistem_Basis_Data', models.FloatField(blank=True, default=None, null=True)),
                ('Sistem_Digital_dan_Gelombang', models.FloatField(blank=True, default=None, null=True)),
                ('Sistem_Informasi', models.FloatField(blank=True, default=None, null=True)),
                ('Sistem_Operasi', models.FloatField(blank=True, default=None, null=True)),
                ('Statistika_Probabilitas', models.FloatField(blank=True, default=None, null=True)),
                ('Struktur_Data', models.FloatField(blank=True, default=None, null=True)),
                ('Teknik_Perancangan_Sistem', models.FloatField(blank=True, default=None, null=True)),
                ('Teori_Bahasa_Automata_and_Komp', models.FloatField(blank=True, default=None, null=True)),
                ('Testing_and_Implementation', models.FloatField(blank=True, default=None, null=True)),
                ('peminatan', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'Data_Training',
            },
        ),
        migrations.CreateModel(
            name='Peminatan',
            fields=[
                ('id_peminatan', models.IntegerField(primary_key=True, serialize=False)),
                ('peminatan', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'Peminatan',
            },
        ),
        migrations.CreateModel(
            name='DataTesting',
            fields=[
                ('id_testing', models.AutoField(primary_key=True, serialize=False)),
                ('nim', models.CharField(max_length=10)),
                ('Algoritma_dan_Pemrograman', models.FloatField(blank=True, default=None, null=True)),
                ('Aljabar_Linier_dan_Matriks', models.FloatField(blank=True, default=None, null=True)),
                ('Fisika_Listrik_dan_Magnet', models.FloatField(blank=True, default=None, null=True)),
                ('Grafik_Komputer', models.FloatField(blank=True, default=None, null=True)),
                ('Kalkulus', models.FloatField(blank=True, default=None, null=True)),
                ('Keamanan_Info_dan_Jaringan', models.FloatField(blank=True, default=None, null=True)),
                ('Kom_Data_dan_Jaringan_Komputer', models.FloatField(blank=True, default=None, null=True)),
                ('Logika_Informatika', models.FloatField(blank=True, default=None, null=True)),
                ('Manajemen_Proyek', models.FloatField(blank=True, default=None, null=True)),
                ('Matematika_Diskrit', models.FloatField(blank=True, default=None, null=True)),
                ('Metode_Numerik', models.FloatField(blank=True, default=None, null=True)),
                ('Multimedia', models.FloatField(blank=True, default=None, null=True)),
                ('Organisasi_dan_Arsitektur_Komp', models.FloatField(blank=True, default=None, null=True)),
                ('Pemrograman_Berorientasi_Obyek', models.FloatField(blank=True, default=None, null=True)),
                ('Pemrograman_Lanjut', models.FloatField(blank=True, default=None, null=True)),
                ('Pemrograman_Web', models.FloatField(blank=True, default=None, null=True)),
                ('Pengantar_Kriptografi', models.FloatField(blank=True, default=None, null=True)),
                ('Prak_Pemrog_Berorient_Obyek', models.FloatField(blank=True, default=None, null=True)),
                ('Prak_Sistem_Basis_Data', models.FloatField(blank=True, default=None, null=True)),
                ('Prak_Algoritma_dan_Pemrograman', models.FloatField(blank=True, default=None, null=True)),
                ('Praktikum_Pemrograman_Lanjut', models.FloatField(blank=True, default=None, null=True)),
                ('Praktikum_Pemrograman_Web', models.FloatField(blank=True, default=None, null=True)),
                ('Praktikum_Struktur_Data', models.FloatField(blank=True, default=None, null=True)),
                ('Rekayasa_Perangkat_Lunak', models.FloatField(blank=True, default=None, null=True)),
                ('Sistem_Basis_Data', models.FloatField(blank=True, default=None, null=True)),
                ('Sistem_Digital_dan_Gelombang', models.FloatField(blank=True, default=None, null=True)),
                ('Sistem_Informasi', models.FloatField(blank=True, default=None, null=True)),
                ('Sistem_Operasi', models.FloatField(blank=True, default=None, null=True)),
                ('Statistika_Probabilitas', models.FloatField(blank=True, default=None, null=True)),
                ('Struktur_Data', models.FloatField(blank=True, default=None, null=True)),
                ('Teknik_Perancangan_Sistem', models.FloatField(blank=True, default=None, null=True)),
                ('Teori_Bahasa_Automata_and_Komp', models.FloatField(blank=True, default=None, null=True)),
                ('Testing_and_Implementation', models.FloatField(blank=True, default=None, null=True)),
                ('peminatan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='knnApp.peminatan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Data_Testing',
            },
        ),
    ]
