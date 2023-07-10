from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('rekomendasi/', views.predict, name='rekomendasi'),
    path('rekomendasi_csv/', views.predictcsv, name='rekomendasi_csv'),
    path('result/', views.predict, name='result'),
    path('datatraining/', views.datatraining, name='datatraining'),
    path('hasil/', views.hasil, name='hasil'),
    path('datatesting/', views.datatesting, name='datatesting'),
    path('datatesting/csv/', views.export_csv, name='export_csv'),
    path('tambah_data_training/', views.import_data_training, name='updatedatatraining'),
    path('update_model/', views.update_model, name='updatemodel'),
    path('delete_training_data/<int:id_training>/', views.delete_training_data, name='delete_data_training'),
    path('delete_testing_data/<int:id_testing>/', views.delete_testing_data, name='delete_data_testing'),
    path('peminatan/', views.peminatan, name='peminatan'),
    path('tambah_peminatan/', views.tambah_peminatan, name='tambah_peminatan'),
    path('edit_peminatan/<int:id_peminatan>/', views.edit_peminatan, name='edit_peminatan'),
    path('delete_peminatan/<int:id_peminatan>/', views.delete_peminatan, name='delete_peminatan'),

    
]
