from django import forms
from knnApp.models import Peminatan
from django import forms

class PredictionForm(forms.Form):
    nim = forms.CharField(max_length=10)
    Algoritma_dan_Pemrograman = forms.FloatField()
    Aljabar_Linier_dan_Matriks = forms.FloatField()
    Fisika_Listrik_dan_Magnet = forms.FloatField()
    Grafik_Komputer = forms.FloatField()
    Kalkulus = forms.FloatField()
    Keamanan_Info_dan_Jaringan = forms.FloatField()
    Kom_Data_dan_Jaringan_Komputer = forms.FloatField()
    Logika_Informatika = forms.FloatField()
    Manajemen_Proyek = forms.FloatField()
    Matematika_Diskrit = forms.FloatField()
    Metode_Numerik = forms.FloatField()
    Multimedia = forms.FloatField()
    Organisasi_dan_Arsitektur_Komp = forms.FloatField()
    Pemrograman_Berorientasi_Obyek = forms.FloatField()
    Pemrograman_Lanjut = forms.FloatField()
    Pemrograman_Web = forms.FloatField()
    Pengantar_Kriptografi = forms.FloatField()
    Prak_Pemrog_Berorient_Obyek = forms.FloatField()
    Prak_Sistem_Basis_Data = forms.FloatField()
    Prak_Algoritma_dan_Pemrograman = forms.FloatField()
    Praktikum_Pemrograman_Lanjut = forms.FloatField()
    Praktikum_Pemrograman_Web = forms.FloatField()
    Praktikum_Struktur_Data = forms.FloatField()
    Rekayasa_Perangkat_Lunak = forms.FloatField()
    Sistem_Basis_Data = forms.FloatField()
    Sistem_Digital_dan_Gelombang = forms.FloatField()
    Sistem_Informasi = forms.FloatField()
    Sistem_Operasi = forms.FloatField()
    Statistika_Probabilitas = forms.FloatField()
    Struktur_Data = forms.FloatField()
    Teknik_Perancangan_Sistem = forms.FloatField()
    Teori_Bahasa_Automata_and_Komp = forms.FloatField()
    Testing_and_Implementation = forms.FloatField()

class PredictionFormCsv(forms.Form):
    csv_file = forms.FileField(label='CSV File')

    def clean_csv_file(self):
        csv_file = self.cleaned_data['csv_file']
        if not csv_file.name.endswith('.csv'):
            raise forms.ValidationError('Invalid file format. Please upload a CSV file.')
        return csv_file

    
    
class UpdateDataForm(forms.Form):
    csv_file = forms.FileField(label='Upload CSV File')
    

class UpdateModelForm(forms.Form):
    k_model = forms.IntegerField(label='K Model', initial=5)
    


class PeminatanForm(forms.ModelForm):
    class Meta:
        model = Peminatan
        fields = ['id_peminatan', 'peminatan']
        labels = {
            'id_peminatan': 'ID Peminatan',
            'peminatan': 'Peminatan',
        }
