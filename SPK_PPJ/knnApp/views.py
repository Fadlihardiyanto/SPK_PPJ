from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, FileResponse
from django.views.decorators.http import require_POST
from joblib import load
import numpy as np
from .models import DataTesting, DataTraining, Peminatan
from account.models import MyUser # import the Mahasiswa model
from .forms import PredictionForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import OrderFilter, OrderFilterTraining
import pandas as pd
import os
import csv
import codecs
import locale
import joblib
from joblib import dump
from django.http import HttpResponse
from sklearn.preprocessing import LabelEncoder
from django.contrib import messages
from sklearn.neighbors import KNeighborsClassifier
from sklearn.impute import SimpleImputer
from django.http import HttpResponseRedirect
from .forms import UpdateModelForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from scipy.spatial.distance import euclidean
from .forms import PredictionForm, PredictionFormCsv, PeminatanForm
from django.conf import settings
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from sklearn.preprocessing import StandardScaler


# Create your views here.


@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(lambda u: u.is_staff, login_url=settings.LOGIN_URL)
def peminatan(request):
    peminatan_list = Peminatan.objects.all()
    
    context = {
        "peminatan_list": peminatan_list,
    }
    return render(request, 'knnApp/peminatan.html', context)
    


@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(lambda u: u.is_staff, login_url=settings.LOGIN_URL)
def tambah_peminatan(request):
    if request.method == 'POST':
        form = PeminatanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('peminatan')
    else:
        form = PeminatanForm()
    return render(request, 'knnApp/tambah_peminatan.html', {'form': form})

@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(lambda u: u.is_staff, login_url=settings.LOGIN_URL)
def edit_peminatan(request, id_peminatan):
    peminatan = Peminatan.objects.get(id_peminatan=id_peminatan)
    if request.method == 'POST':
        form = PeminatanForm(request.POST, instance=peminatan)
        if form.is_valid():
            peminatan = form.save()
            return redirect('peminatan')
    else:
        form = PeminatanForm(instance=peminatan)
    return render(request, 'knnApp/edit_peminatan.html', {'form': form})

       
@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(lambda u: u.is_staff, login_url=settings.LOGIN_URL)
@require_POST
def delete_peminatan(request, id_peminatan):
    peminatan = Peminatan.objects.get(id_peminatan=id_peminatan)
    if request.method == 'POST':    
        peminatan.delete()
        messages.success(request, 'Peminatan deleted successfully.')
        return HttpResponseRedirect(reverse('peminatan'))
    else:
        messages.error(request, 'Peminatan failed to delete. Please try again.')
        return HttpResponseRedirect(reverse('peminatan'))



@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(lambda u: u.is_staff, login_url=settings.LOGIN_URL)
def import_data_training(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        decoded_file = csv_file.read().decode('utf-8')
        csv_data = csv.reader(decoded_file.splitlines(), delimiter=',')

        # Skip the header row
        next(csv_data)
        for row in csv_data:
            NIM = row[0]
            Algoritma_dan_Pemrograman = float(row[1].replace(',', '.')) if row[1] else 0
            Aljabar_Linier_dan_Matriks = float(row[2].replace(',', '.')) if row[2] else 0
            Fisika_Listrik_dan_Magnet = float(row[3].replace(',', '.')) if row[3] else 0
            Grafik_Komputer = float(row[4].replace(',', '.')) if row[4] else 0
            Kalkulus = float(row[5].replace(',', '.')) if row[5] else 0
            Keamanan_Info_dan_Jaringan = float(row[6].replace(',', '.')) if row[6] else 0
            Kom_Data_dan_Jaringan_Komputer = float(row[7].replace(',', '.')) if row[7] else 0
            Logika_Informatika = float(row[8].replace(',', '.')) if row[8] else 0
            Manajemen_Proyek = float(row[9].replace(',', '.')) if row[9] else 0
            Matematika_Diskrit = float(row[10].replace(',', '.')) if row[10] else 0
            Metode_Numerik = float(row[11].replace(',', '.')) if row[11] else 0
            Multimedia = float(row[12].replace(',', '.')) if row[12] else 0
            Organisasi_dan_Arsitektur_Komp = float(row[13].replace(',', '.')) if row[13] else 0
            Pemrograman_Berorientasi_Obyek = float(row[14].replace(',', '.')) if row[14] else 0
            Pemrograman_Lanjut = float(row[15].replace(',', '.')) if row[15] else 0
            Pemrograman_Web = float(row[16].replace(',', '.')) if row[16] else 0
            Pengantar_Kriptografi = float(row[17].replace(',', '.')) if row[17] else 0
            Prak_Pemrog_Berorient_Obyek = float(row[18].replace(',', '.')) if row[18] else 0
            Prak_Sistem_Basis_Data = float(row[19].replace(',', '.')) if row[19] else 0
            Prak_Algoritma_dan_Pemrograman = float(row[20].replace(',', '.')) if row[20] else 0
            Praktikum_Pemrograman_Lanjut = float(row[21].replace(',', '.')) if row[21] else 0
            Praktikum_Pemrograman_Web = float(row[22].replace(',', '.')) if row[22] else 0
            Praktikum_Struktur_Data = float(row[23].replace(',', '.')) if row[23] else 0
            Rekayasa_Perangkat_Lunak = float(row[24].replace(',', '.')) if row[24] else 0
            Sistem_Basis_Data = float(row[25].replace(',', '.')) if row[25] else 0
            Sistem_Digital_dan_Gelombang = float(row[26].replace(',', '.')) if row[26] else 0
            Sistem_Informasi = float(row[27].replace(',', '.')) if row[27] else 0
            Sistem_Operasi = float(row[28].replace(',', '.')) if row[28] else 0
            Statistika_Probabilitas = float(row[29].replace(',', '.')) if row[29] else 0
            Struktur_Data = float(row[30].replace(',', '.')) if row[30] else 0
            Teknik_Perancangan_Sistem = float(row[31].replace(',', '.')) if row[31] else 0
            Teori_Bahasa_Automata_and_Komp = float(row[32].replace(',', '.')) if row[32] else 0
            Testing_and_Implementation = float(row[33].replace(',', '.')) if row[33] else 0
            peminatan = row[34]

            new_training = DataTraining(
                NIM=NIM,
                Algoritma_dan_Pemrograman=Algoritma_dan_Pemrograman,
                Aljabar_Linier_dan_Matriks=Aljabar_Linier_dan_Matriks,
                Fisika_Listrik_dan_Magnet=Fisika_Listrik_dan_Magnet,
                Grafik_Komputer=Grafik_Komputer,
                Kalkulus=Kalkulus,
                Keamanan_Info_dan_Jaringan=Keamanan_Info_dan_Jaringan,
                Kom_Data_dan_Jaringan_Komputer=Kom_Data_dan_Jaringan_Komputer,
                Logika_Informatika=Logika_Informatika,
                Manajemen_Proyek=Manajemen_Proyek,
                Matematika_Diskrit=Matematika_Diskrit,
                Metode_Numerik=Metode_Numerik,
                Multimedia=Multimedia,
                Organisasi_dan_Arsitektur_Komp=Organisasi_dan_Arsitektur_Komp,
                Pemrograman_Berorientasi_Obyek=Pemrograman_Berorientasi_Obyek,
                Pemrograman_Lanjut=Pemrograman_Lanjut,
                Pemrograman_Web=Pemrograman_Web,
                Pengantar_Kriptografi=Pengantar_Kriptografi,
                Prak_Pemrog_Berorient_Obyek=Prak_Pemrog_Berorient_Obyek,
                Prak_Sistem_Basis_Data=Prak_Sistem_Basis_Data,
                Prak_Algoritma_dan_Pemrograman=Prak_Algoritma_dan_Pemrograman,
                Praktikum_Pemrograman_Lanjut=Praktikum_Pemrograman_Lanjut,
                Praktikum_Pemrograman_Web=Praktikum_Pemrograman_Web,
                Praktikum_Struktur_Data=Praktikum_Struktur_Data,
                Rekayasa_Perangkat_Lunak=Rekayasa_Perangkat_Lunak,
                Sistem_Basis_Data=Sistem_Basis_Data,
                Sistem_Digital_dan_Gelombang=Sistem_Digital_dan_Gelombang,
                Sistem_Informasi=Sistem_Informasi,
                Sistem_Operasi=Sistem_Operasi,
                Statistika_Probabilitas=Statistika_Probabilitas,
                Struktur_Data=Struktur_Data,
                Teknik_Perancangan_Sistem=Teknik_Perancangan_Sistem,
                Teori_Bahasa_Automata_and_Komp=Teori_Bahasa_Automata_and_Komp,
                Testing_and_Implementation=Testing_and_Implementation,
                peminatan=peminatan,
            )

            new_training.save()
            
        messages.success(request, 'Data training berhasil diimport.')
        return redirect('updatemodel')
    else:
        return render(request, 'knnApp/update_data_training.html')
    


@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(lambda u: u.is_staff, login_url=settings.LOGIN_URL)
def update_model(request):
    if request.method == 'POST':
        form = UpdateModelForm(request.POST)
        if form.is_valid():
            k_model = form.cleaned_data['k_model']
            k_value = k_model  # Get the value of k from the selected KTabel instance

            # Load the training dataset from the database
            training_data = DataTraining.objects.all()

            # Extract features and target variables
            X_train = np.array([
                [
                    row.Algoritma_dan_Pemrograman,
                    row.Aljabar_Linier_dan_Matriks,
                    row.Fisika_Listrik_dan_Magnet,
                    row.Grafik_Komputer,
                    row.Kalkulus,
                    row.Keamanan_Info_dan_Jaringan,
                    row.Kom_Data_dan_Jaringan_Komputer,
                    row.Logika_Informatika,
                    row.Manajemen_Proyek,
                    row.Matematika_Diskrit,
                    row.Metode_Numerik,
                    row.Multimedia,
                    row.Organisasi_dan_Arsitektur_Komp,
                    row.Pemrograman_Berorientasi_Obyek,
                    row.Pemrograman_Lanjut,
                    row.Pemrograman_Web,
                    row.Pengantar_Kriptografi,
                    row.Prak_Pemrog_Berorient_Obyek,
                    row.Prak_Sistem_Basis_Data,
                    row.Prak_Algoritma_dan_Pemrograman,
                    row.Praktikum_Pemrograman_Lanjut,
                    row.Praktikum_Pemrograman_Web,
                    row.Praktikum_Struktur_Data,
                    row.Rekayasa_Perangkat_Lunak,
                    row.Sistem_Basis_Data,
                    row.Sistem_Digital_dan_Gelombang,
                    row.Sistem_Informasi,
                    row.Sistem_Operasi,
                    row.Statistika_Probabilitas,
                    row.Struktur_Data,
                    row.Teknik_Perancangan_Sistem,
                    row.Teori_Bahasa_Automata_and_Komp,
                    row.Testing_and_Implementation,
                ]
                for row in training_data
            ])

            y_train = np.array([
                row.peminatan
                for row in training_data
            ])

            # Flatten the target array if needed
            y_train = y_train.flatten()

            # Perform label encoding on the target variable
            le = LabelEncoder()
            y_train = le.fit_transform(y_train)

            # Standardize features using StandardScaler
            scaler = StandardScaler()
            X_train = scaler.fit_transform(X_train)

            # Initialize and train the KNN model
            model = KNeighborsClassifier(n_neighbors=k_value)
            model.fit(X_train, y_train)

            # Save the model using joblib
            model_path = os.path.join(os.path.dirname(__file__), '../saveModels/model_knn_new.joblib')
            joblib.dump(model, model_path)

            # Save the scaler using joblib
            scaler_path = os.path.join(os.path.dirname(__file__), '../saveModels/scaler_new.joblib')
            joblib.dump(scaler, scaler_path)

            messages.success(request, 'Model berhasil diperbarui.')
            return HttpResponseRedirect('/datatraining/')  # Change to the appropriate URL

    else:
        form = UpdateModelForm()

    return render(request, 'knnApp/update_model.html', {'form': form})




@login_required(login_url=settings.LOGIN_URL)
def predict(request):
    # Path to the saved model and scaler files
    model_path = os.path.join(os.path.dirname(__file__), '../saveModels/model_knn_new.joblib')
    scaler_path = os.path.join(os.path.dirname(__file__), '../saveModels/scaler_new.joblib')

    # Load the existing model and scaler
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)

    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            X_new = np.array([data['Algoritma_dan_Pemrograman'], data['Aljabar_Linier_dan_Matriks'], data['Fisika_Listrik_dan_Magnet'], data['Grafik_Komputer'], data['Kalkulus'], data['Keamanan_Info_dan_Jaringan'], data['Kom_Data_dan_Jaringan_Komputer'], data['Logika_Informatika'], data['Manajemen_Proyek'], data['Matematika_Diskrit'], data['Metode_Numerik'], data['Multimedia'], data['Organisasi_dan_Arsitektur_Komp'], data['Pemrograman_Berorientasi_Obyek'], data['Pemrograman_Lanjut'], data['Pemrograman_Web'], data['Pengantar_Kriptografi'], data['Prak_Pemrog_Berorient_Obyek'], data['Prak_Sistem_Basis_Data'], data['Prak_Algoritma_dan_Pemrograman'], data['Praktikum_Pemrograman_Lanjut'], data['Praktikum_Pemrograman_Web'], data['Praktikum_Struktur_Data'], data['Rekayasa_Perangkat_Lunak'], data['Sistem_Basis_Data'], data['Sistem_Digital_dan_Gelombang'], data['Sistem_Informasi'], data['Sistem_Operasi'], data['Statistika_Probabilitas'], data['Struktur_Data'], data['Teknik_Perancangan_Sistem'], data['Teori_Bahasa_Automata_and_Komp'], data['Testing_and_Implementation']])
            X_new = X_new.reshape(1, -1)
            X_new = scaler.transform(X_new)  # Normalize the data

            y_new = model.predict(X_new)
            if y_new == 0:
                peminatan_id = 0  # ID peminatan Jarkom dalam model Peminatan
            elif y_new == 1:
                peminatan_id = 1  # ID peminatan MM dalam model Peminatan
            elif y_new == 2:
                peminatan_id = 2  # ID peminatan RPL dalam model Peminatan

            peminatan = Peminatan.objects.get(id_peminatan=peminatan_id)

            result = DataTesting(
                Algoritma_dan_Pemrograman=data['Algoritma_dan_Pemrograman'],
                Aljabar_Linier_dan_Matriks=data['Aljabar_Linier_dan_Matriks'],
                Fisika_Listrik_dan_Magnet=data['Fisika_Listrik_dan_Magnet'],
                Grafik_Komputer=data['Grafik_Komputer'],
                Kalkulus=data['Kalkulus'],
                Keamanan_Info_dan_Jaringan=data['Keamanan_Info_dan_Jaringan'],
                Kom_Data_dan_Jaringan_Komputer=data['Kom_Data_dan_Jaringan_Komputer'],
                Logika_Informatika=data['Logika_Informatika'],
                Manajemen_Proyek=data['Manajemen_Proyek'],
                Matematika_Diskrit=data['Matematika_Diskrit'],
                Metode_Numerik=data['Metode_Numerik'],
                Multimedia=data['Multimedia'],
                Organisasi_dan_Arsitektur_Komp=data['Organisasi_dan_Arsitektur_Komp'],
                Pemrograman_Berorientasi_Obyek=data['Pemrograman_Berorientasi_Obyek'],
                Pemrograman_Lanjut=data['Pemrograman_Lanjut'],
                Pemrograman_Web=data['Pemrograman_Web'],
                Pengantar_Kriptografi=data['Pengantar_Kriptografi'],
                Prak_Pemrog_Berorient_Obyek=data['Prak_Pemrog_Berorient_Obyek'],
                Prak_Sistem_Basis_Data=data['Prak_Sistem_Basis_Data'],
                Prak_Algoritma_dan_Pemrograman=data['Prak_Algoritma_dan_Pemrograman'],
                Praktikum_Pemrograman_Lanjut=data['Praktikum_Pemrograman_Lanjut'],
                Praktikum_Pemrograman_Web=data['Praktikum_Pemrograman_Web'],
                Praktikum_Struktur_Data=data['Praktikum_Struktur_Data'],
                Rekayasa_Perangkat_Lunak=data['Rekayasa_Perangkat_Lunak'],
                Sistem_Basis_Data=data['Sistem_Basis_Data'],
                Sistem_Digital_dan_Gelombang=data['Sistem_Digital_dan_Gelombang'],
                Sistem_Informasi=data['Sistem_Informasi'],
                Sistem_Operasi=data['Sistem_Operasi'],
                Statistika_Probabilitas=data['Statistika_Probabilitas'],
                Struktur_Data=data['Struktur_Data'],
                Teknik_Perancangan_Sistem=data['Teknik_Perancangan_Sistem'],
                Teori_Bahasa_Automata_and_Komp=data['Teori_Bahasa_Automata_and_Komp'],
                Testing_and_Implementation=data['Testing_and_Implementation'],
                peminatan=peminatan,
                user=request.user
            )

            if request.user.is_staff:
                result.nim = data['nim']
            else:
                result.nim = request.user.NimOrNip
            result.save()

            return redirect('/hasil/')

    else:
        form = PredictionForm()
    return render(request, 'knnApp/rekomendasi.html', {'form': form})



@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(lambda u: u.is_staff, login_url=settings.LOGIN_URL)
def predictcsv(request):
    # Path to the saved model and scaler files
    model_path = os.path.join(os.path.dirname(__file__), '../saveModels/model_knn_new.joblib')
    scaler_path = os.path.join(os.path.dirname(__file__), '../saveModels/scaler_new.joblib')

    # Load the existing model and scaler
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)

    if request.method == 'POST':
        form = PredictionFormCsv(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            
            # Read the CSV file
            csv_data = csv.reader(codecs.iterdecode(csv_file, 'utf-8'))
            next(csv_data)  # Skip the header row
            
            results = []
            for row in csv_data:
                nim = row[0]  # Assuming 'nim' is in the first column
                
                # Set locale
                locale.setlocale(locale.LC_ALL, '')
                
                # Function to convert string to float using appropriate decimal separator
                def str_to_float(value):
                    return locale.atof(value)
                
                # Convert feature values to floats using the custom function
                features = [str_to_float(value) for value in row[1:]]
                
                X_new = np.array(features).reshape(1, -1)
                X_new = scaler.transform(X_new)  # Normalize the data
                y_new = model.predict(X_new)
                if y_new == 0:
                    peminatan_id = 0  # ID peminatan Jarkom dalam model Peminatan
                elif y_new == 1:
                    peminatan_id = 1  # ID peminatan MM dalam model Peminatan
                elif y_new == 2:
                    peminatan_id = 2  # ID peminatan RPL dalam model Peminatan

                peminatan = Peminatan.objects.get(id_peminatan=peminatan_id)
                
                result = DataTesting(
                    Algoritma_dan_Pemrograman='{:0.2f}'.format(features[0]),
                    Aljabar_Linier_dan_Matriks='{:0.2f}'.format(features[1]),
                    Fisika_Listrik_dan_Magnet='{:0.2f}'.format(features[2]),
                    Grafik_Komputer='{:0.2f}'.format(features[3]),
                    Kalkulus='{:0.2f}'.format(features[4]),
                    Keamanan_Info_dan_Jaringan='{:0.2f}'.format(features[5]),
                    Kom_Data_dan_Jaringan_Komputer='{:0.2f}'.format(features[6]),
                    Logika_Informatika='{:0.2f}'.format(features[7]),
                    Manajemen_Proyek='{:0.2f}'.format(features[8]),
                    Matematika_Diskrit='{:0.2f}'.format(features[9]),
                    Metode_Numerik='{:0.2f}'.format(features[10]),
                    Multimedia='{:0.2f}'.format(features[11]),
                    Organisasi_dan_Arsitektur_Komp='{:0.2f}'.format(features[12]),
                    Pemrograman_Berorientasi_Obyek='{:0.2f}'.format(features[13]),
                    Pemrograman_Lanjut='{:0.2f}'.format(features[14]),
                    Pemrograman_Web='{:0.2f}'.format(features[15]),
                    Pengantar_Kriptografi='{:0.2f}'.format(features[16]),
                    Prak_Pemrog_Berorient_Obyek='{:0.2f}'.format(features[17]),
                    Prak_Sistem_Basis_Data='{:0.2f}'.format(features[18]),
                    Prak_Algoritma_dan_Pemrograman='{:0.2f}'.format(features[19]),
                    Praktikum_Pemrograman_Lanjut='{:0.2f}'.format(features[20]),
                    Praktikum_Pemrograman_Web='{:0.2f}'.format(features[21]),
                    Praktikum_Struktur_Data='{:0.2f}'.format(features[22]),
                    Rekayasa_Perangkat_Lunak='{:0.2f}'.format(features[23]),
                    Sistem_Basis_Data='{:0.2f}'.format(features[24]),
                    Sistem_Digital_dan_Gelombang='{:0.2f}'.format(features[25]),
                    Sistem_Informasi='{:0.2f}'.format(features[26]),
                    Sistem_Operasi='{:0.2f}'.format(features[27]),
                    Statistika_Probabilitas='{:0.2f}'.format(features[28]),
                    Struktur_Data='{:0.2f}'.format(features[29]),
                    Teknik_Perancangan_Sistem='{:0.2f}'.format(features[30]),
                    Teori_Bahasa_Automata_and_Komp='{:0.2f}'.format(features[31]),
                    Testing_and_Implementation='{:0.2f}'.format(features[32]),
                    peminatan=peminatan,
                    user=request.user
                )

                result.nim = nim
                
                results.append(result)
            
            # Bulk create the DataTesting objects
            DataTesting.objects.bulk_create(results)
            
            return redirect('datatesting')
    else:
        form = PredictionFormCsv()
    
    return render(request, 'knnApp/rekomendasi_csv.html', {'form': form})


@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(lambda u: u.is_staff, login_url=settings.LOGIN_URL)
def datatraining(request):
    rows = DataTraining.objects.all()
    training_filter = OrderFilterTraining(request.GET, queryset=rows)

    # Pagination
    page = request.GET.get('page')
    paginator = Paginator(training_filter.qs, 10) # Menampilkan 10 item per halaman

    try:
        rows = paginator.page(page)
    except PageNotAnInteger:
        # Jika halaman bukan bilangan bulat, tampilkan halaman pertama.
        rows = paginator.page(1)
    except EmptyPage:
        # Jika halaman diluar jangkauan, tampilkan halaman terakhir.
        rows = paginator.page(paginator.num_pages)

    context = {
    'name' : 'datatraining',
    'page_title': 'Halaman Utama',
    'rows': rows,
    'paginator': paginator,
    'page_obj': rows,
    'MyFilter': training_filter,
    }
    return render(request, 'knnApp/datatraining.html', context)

@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(lambda u: u.is_staff, login_url=settings.LOGIN_URL)
@require_POST
def delete_training_data(request, id_training):
    rows = DataTraining.objects.get(id_training=id_training)
    if request.method == 'POST':
        rows.delete()
        messages.success(request, 'Training data deleted successfully.')
        return HttpResponseRedirect(reverse('datatraining'))
    else:
        messages.error(request, 'Failed to delete training data. Please try again.')
        return HttpResponseRedirect(reverse('datatraining'))
    

@login_required(login_url=settings.LOGIN_URL)
def hasil(request):
    # Show data testing
    data = DataTesting.objects.filter(user=request.user).order_by('-id_testing').first()
    nim = data.nim if data else None
    peminatan = data.peminatan if data else None

    # Retrieve closest data points
    closest_data = None
    if data:
        data_training = DataTraining.objects.all()
        data_jarak = [euclidean([
            data.Algoritma_dan_Pemrograman,
            data.Aljabar_Linier_dan_Matriks,
            data.Fisika_Listrik_dan_Magnet,
            data.Grafik_Komputer,
            data.Kalkulus,
            data.Keamanan_Info_dan_Jaringan,
            data.Kom_Data_dan_Jaringan_Komputer,
            data.Logika_Informatika,
            data.Manajemen_Proyek,
            data.Matematika_Diskrit,
            data.Metode_Numerik,
            data.Multimedia,
            data.Organisasi_dan_Arsitektur_Komp,
            data.Pemrograman_Berorientasi_Obyek,
            data.Pemrograman_Lanjut,
            data.Pemrograman_Web,
            data.Pengantar_Kriptografi,
            data.Prak_Pemrog_Berorient_Obyek,
            data.Prak_Sistem_Basis_Data,
            data.Prak_Algoritma_dan_Pemrograman,
            data.Praktikum_Pemrograman_Lanjut,
            data.Praktikum_Pemrograman_Web,
            data.Praktikum_Struktur_Data,
            data.Rekayasa_Perangkat_Lunak,
            data.Sistem_Basis_Data,
            data.Sistem_Digital_dan_Gelombang,
            data.Sistem_Informasi,
            data.Sistem_Operasi,
            data.Statistika_Probabilitas,
            data.Struktur_Data,
            data.Teknik_Perancangan_Sistem,
            data.Teori_Bahasa_Automata_and_Komp,
            data.Testing_and_Implementation
        ], [
            row.Algoritma_dan_Pemrograman,
            row.Aljabar_Linier_dan_Matriks,
            row.Fisika_Listrik_dan_Magnet,
            row.Grafik_Komputer,
            row.Kalkulus,
            row.Keamanan_Info_dan_Jaringan,
            row.Kom_Data_dan_Jaringan_Komputer,
            row.Logika_Informatika,
            row.Manajemen_Proyek,
            row.Matematika_Diskrit,
            row.Metode_Numerik,
            row.Multimedia,
            row.Organisasi_dan_Arsitektur_Komp,
            row.Pemrograman_Berorientasi_Obyek,
            row.Pemrograman_Lanjut,
            row.Pemrograman_Web,
            row.Pengantar_Kriptografi,
            row.Prak_Pemrog_Berorient_Obyek,
            row.Prak_Sistem_Basis_Data,
            row.Prak_Algoritma_dan_Pemrograman,
            row.Praktikum_Pemrograman_Lanjut,
            row.Praktikum_Pemrograman_Web,
            row.Praktikum_Struktur_Data,
            row.Rekayasa_Perangkat_Lunak,
            row.Sistem_Basis_Data,
            row.Sistem_Digital_dan_Gelombang,
            row.Sistem_Informasi,
            row.Sistem_Operasi,
            row.Statistika_Probabilitas,
            row.Struktur_Data,
            row.Teknik_Perancangan_Sistem,
            row.Teori_Bahasa_Automata_and_Komp,
            row.Testing_and_Implementation
        ]) for row in data_training]

        # Sort the distances and retrieve the closest data points
        closest_data = sorted(zip(data_training, data_jarak), key=lambda x: x[1])[:11]

    return render(request, 'knnApp/hasil.html', {'peminatan': peminatan, 'closest_data': closest_data, 'nim': nim})




@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(lambda u: u.is_staff, login_url=settings.LOGIN_URL)
def datatesting(request):
    rows = DataTesting.objects.all().order_by('-id_testing')
    users = MyUser.objects.all()
    testing_filter = OrderFilter(request.GET, queryset=rows)

    # Pagination
    page = request.GET.get('page')
    paginator = Paginator(testing_filter.qs, 10) # Menampilkan 10 item per halaman

    try:
        rows = paginator.page(page)
    except PageNotAnInteger:
        # Jika halaman bukan bilangan bulat, tampilkan halaman pertama.
        rows = paginator.page(1)
    except EmptyPage:
        # Jika halaman diluar jangkauan, tampilkan halaman terakhir.
        rows = paginator.page(paginator.num_pages)

    context = {
    'name' : 'datatesting',
    'page_title': 'Halaman Utama',
    'rows': rows,
    'paginator': paginator,
    'page_obj': rows,
    'MyFilter': testing_filter,
    'users': users,
    'is_admin': request.user.is_staff,
    }
    
    return render(request, 'knnApp/datatesting.html', context)

@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(lambda u: u.is_staff, login_url=settings.LOGIN_URL)
@require_POST
def delete_testing_data(request, id_testing):
    rows = DataTesting.objects.get(id_testing=id_testing)
    if request.method == 'POST':
        rows.delete()
        messages.success(request, 'Testing data deleted successfully.')
        return HttpResponseRedirect(reverse('datatesting'))
    else:
        messages.error(request, 'Failed to delete testing data. Please try again.')
        return HttpResponseRedirect(reverse('datatesting'))

@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(lambda u: u.is_staff, login_url=settings.LOGIN_URL)
def export_csv(request):
    data_testing = DataTesting.objects.select_related('user').all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data_testing.csv"'

    writer = csv.writer(response)

    # Define column headers
    field_names = [field.name for field in DataTesting._meta.fields if field.name != 'id_testing' and field.name != 'user']
    writer.writerow(field_names)

    # Write data rows
    for item in data_testing:
        row_data = [getattr(item, field.name) for field in DataTesting._meta.fields if field.name != 'id_testing' and field.name != 'user']
        writer.writerow(row_data)

    return response
