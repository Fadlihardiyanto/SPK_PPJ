import django_filters
from django_filters.widgets import RangeWidget
from django import forms
from .models import MyUser

class OrderFilter(django_filters.FilterSet):
    IS_ACTIVE_CHOICES = (
        (True, 'Aktif'),
        (False, 'Tidak Aktif'),
    )
    
    IS_STAFF_CHOICES = (
        (True, 'Admin'),
        (False, 'Mahasiswa'),
    )
    
    NimOrNip = django_filters.CharFilter(field_name='NimOrNip', lookup_expr='icontains', label='Nim/Nip')
    nama = django_filters.CharFilter(field_name='name', lookup_expr='icontains', label='Nama Pengguna') 
    active = django_filters.ChoiceFilter(field_name='is_active', choices=IS_ACTIVE_CHOICES, label='Status')
    role = django_filters.ChoiceFilter(field_name='is_staff', choices=IS_STAFF_CHOICES, label='Role')
        
    class Meta:
        model = MyUser
        fields = "__all__"
