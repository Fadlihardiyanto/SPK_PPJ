# urls.py


from django.urls import path
from . import views

urlpatterns = [
    path('manajemen_pengguna/', views.manajemen_pengguna, name='manajemen_pengguna'),
    path('update_status/<int:id>/', views.update_status, name='update_status'),
    path('tambah_data_pengguna/', views.tambahdatapengguna, name='tambah_data_pengguna'),
    path('delete_pengguna/<int:id>/', views.delete_pengguna, name='delete_pengguna'),
    path('edit_pengguna/<int:id>/', views.edit_pengguna, name='edit_pengguna'),
]
