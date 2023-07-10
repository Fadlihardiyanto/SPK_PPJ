import django_filters
from django_filters.widgets import RangeWidget
from django import forms
from .models import *
from account.models import MyUser

class MyUserFilter(django_filters.FilterSet):
    class Meta:
        model = MyUser
        fields = ['NimOrNip']

class OrderFilter(django_filters.FilterSet):
    IS_PEMINATAN_CHOICES = (
        ('RPL', 'RPL'),
        ('MM', 'MM'),
        ('Jarkom', 'Jarkom'),
    )

    peminatan = django_filters.ChoiceFilter(field_name='peminatan', choices=IS_PEMINATAN_CHOICES, label='Peminatan')
    nim = django_filters.CharFilter(field_name='nim', label='NIM', lookup_expr='icontains')
    class Meta:
        model = DataTesting
        fields = ['peminatan', 'nim']
        
        
class OrderFilterTraining(django_filters.FilterSet):
    IS_PEMINATAN_CHOICES = (
        ('RPL', 'RPL'),
        ('MM', 'MM'),
        ('Jarkom', 'Jarkom'),
    )

    peminatan = django_filters.ChoiceFilter(field_name='peminatan', choices=IS_PEMINATAN_CHOICES, label='Peminatan')
    NIM = django_filters.CharFilter(field_name='NIM', label='NIM', lookup_expr='icontains')
    class Meta:
        model = DataTraining
        fields = ['peminatan', 'NIM']

