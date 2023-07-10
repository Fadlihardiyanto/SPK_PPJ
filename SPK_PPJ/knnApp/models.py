from django.db import models
from django.conf import settings

# Create your models here.

class Peminatan(models.Model):
    id_peminatan = models.IntegerField(primary_key=True)
    peminatan = models.CharField(max_length=15)
    def __str__(self):
        return f"{self.peminatan}"
    
    class Meta:
        db_table = 'Peminatan'

class DataTesting(models.Model):
    id_testing = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nim = models.CharField(max_length=10)
    Algoritma_dan_Pemrograman = models.FloatField(null=True, blank=True, default=None)
    Aljabar_Linier_dan_Matriks = models.FloatField(null=True, blank=True, default=None)
    Fisika_Listrik_dan_Magnet = models.FloatField(null=True, blank=True, default=None)
    Grafik_Komputer = models.FloatField(null=True, blank=True, default=None)
    Kalkulus = models.FloatField(null=True, blank=True, default=None)
    Keamanan_Info_dan_Jaringan = models.FloatField(null=True, blank=True, default=None)
    Kom_Data_dan_Jaringan_Komputer = models.FloatField(null=True, blank=True, default=None)
    Logika_Informatika = models.FloatField(null=True, blank=True, default=None)
    Manajemen_Proyek = models.FloatField(null=True, blank=True, default=None)
    Matematika_Diskrit = models.FloatField(null=True, blank=True, default=None)
    Metode_Numerik = models.FloatField(null=True, blank=True, default=None)
    Multimedia = models.FloatField(null=True, blank=True, default=None)
    Organisasi_dan_Arsitektur_Komp = models.FloatField(null=True, blank=True, default=None)
    Pemrograman_Berorientasi_Obyek = models.FloatField(null=True, blank=True, default=None)
    Pemrograman_Lanjut = models.FloatField(null=True, blank=True, default=None)
    Pemrograman_Web = models.FloatField(null=True, blank=True, default=None)
    Pengantar_Kriptografi = models.FloatField(null=True, blank=True, default=None)
    Prak_Pemrog_Berorient_Obyek = models.FloatField(null=True, blank=True, default=None)
    Prak_Sistem_Basis_Data = models.FloatField(null=True, blank=True, default=None)
    Prak_Algoritma_dan_Pemrograman = models.FloatField(null=True, blank=True, default=None)
    Praktikum_Pemrograman_Lanjut = models.FloatField(null=True, blank=True, default=None)
    Praktikum_Pemrograman_Web = models.FloatField(null=True, blank=True, default=None)
    Praktikum_Struktur_Data = models.FloatField(null=True, blank=True, default=None)
    Rekayasa_Perangkat_Lunak = models.FloatField(null=True, blank=True, default=None)
    Sistem_Basis_Data = models.FloatField(null=True, blank=True, default=None)
    Sistem_Digital_dan_Gelombang = models.FloatField(null=True, blank=True, default=None)
    Sistem_Informasi = models.FloatField(null=True, blank=True, default=None)
    Sistem_Operasi = models.FloatField(null=True, blank=True, default=None)
    Statistika_Probabilitas = models.FloatField(null=True, blank=True, default=None)
    Struktur_Data = models.FloatField(null=True, blank=True, default=None)
    Teknik_Perancangan_Sistem = models.FloatField(null=True, blank=True, default=None)
    Teori_Bahasa_Automata_and_Komp = models.FloatField(null=True, blank=True, default=None)
    Testing_and_Implementation = models.FloatField(null=True, blank=True, default=None)
    peminatan = models.ForeignKey(Peminatan, on_delete=models.CASCADE)

    def __str__(self):
        return f"Data Testing {self.pk}"
    
    class Meta:
        db_table = 'Data_Testing'
        
class DataTraining(models.Model):
    id_training = models.AutoField(primary_key=True)
    NIM = models.CharField(max_length=10)        
    Algoritma_dan_Pemrograman = models.FloatField(null=True, blank=True, default=None)
    Aljabar_Linier_dan_Matriks = models.FloatField(null=True, blank=True, default=None)
    Fisika_Listrik_dan_Magnet = models.FloatField(null=True, blank=True, default=None)
    Grafik_Komputer = models.FloatField(null=True, blank=True, default=None)
    Kalkulus = models.FloatField(null=True, blank=True, default=None)
    Keamanan_Info_dan_Jaringan = models.FloatField(null=True, blank=True, default=None)
    Kom_Data_dan_Jaringan_Komputer = models.FloatField(null=True, blank=True, default=None)
    Logika_Informatika = models.FloatField(null=True, blank=True, default=None)
    Manajemen_Proyek = models.FloatField(null=True, blank=True, default=None)
    Matematika_Diskrit = models.FloatField(null=True, blank=True, default=None)
    Metode_Numerik = models.FloatField(null=True, blank=True, default=None)
    Multimedia = models.FloatField(null=True, blank=True, default=None)
    Organisasi_dan_Arsitektur_Komp = models.FloatField(null=True, blank=True, default=None)
    Pemrograman_Berorientasi_Obyek = models.FloatField(null=True, blank=True, default=None)
    Pemrograman_Lanjut = models.FloatField(null=True, blank=True, default=None)
    Pemrograman_Web = models.FloatField(null=True, blank=True, default=None)
    Pengantar_Kriptografi = models.FloatField(null=True, blank=True, default=None)
    Prak_Pemrog_Berorient_Obyek = models.FloatField(null=True, blank=True, default=None)
    Prak_Sistem_Basis_Data = models.FloatField(null=True, blank=True, default=None)
    Prak_Algoritma_dan_Pemrograman = models.FloatField(null=True, blank=True, default=None)
    Praktikum_Pemrograman_Lanjut = models.FloatField(null=True, blank=True, default=None)
    Praktikum_Pemrograman_Web = models.FloatField(null=True, blank=True, default=None)
    Praktikum_Struktur_Data = models.FloatField(null=True, blank=True, default=None)
    Rekayasa_Perangkat_Lunak = models.FloatField(null=True, blank=True, default=None)
    Sistem_Basis_Data = models.FloatField(null=True, blank=True, default=None)
    Sistem_Digital_dan_Gelombang = models.FloatField(null=True, blank=True, default=None)
    Sistem_Informasi = models.FloatField(null=True, blank=True, default=None)
    Sistem_Operasi = models.FloatField(null=True, blank=True, default=None)
    Statistika_Probabilitas = models.FloatField(null=True, blank=True, default=None)
    Struktur_Data = models.FloatField(null=True, blank=True, default=None)
    Teknik_Perancangan_Sistem = models.FloatField(null=True, blank=True, default=None)
    Teori_Bahasa_Automata_and_Komp = models.FloatField(null=True, blank=True, default=None)
    Testing_and_Implementation = models.FloatField(null=True, blank=True, default=None)
    peminatan = models.CharField(max_length=10)
   
    def __str__(self):
        return f"{self.peminatan}"
    
    class Meta:
        db_table = 'Data_Training'
