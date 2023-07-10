from django.shortcuts import render, redirect
from account.models import MyUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.conf import settings
from .forms import RegistrationAdminForm
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import OrderFilter


# Create your views here.

from django.core.paginator import Paginator

@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(lambda u: u.is_staff, login_url=settings.LOGIN_URL)
def manajemen_pengguna(request):
    pengguna_list = MyUser.objects.all()
    MyFilter = OrderFilter(request.GET, queryset=pengguna_list)
    pengguna_list = MyFilter.qs  # Get the filtered queryset

    paginator = Paginator(pengguna_list, 10)
    page_number = request.GET.get('page')
    pengguna_page = paginator.get_page(page_number)

    context = {
        'pengguna_list': pengguna_page,
        'MyFilter': MyFilter,
    }
    return render(request, 'account/manajemen_pengguna.html', context)


@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(lambda u: u.is_staff, login_url=settings.LOGIN_URL)
def update_status(request, id):
    if request.method == 'POST':
        user = MyUser.objects.get(id=id)
        is_active = int(request.POST.get('is_active'))
        if user != request.user:  # tambahkan kondisi untuk memeriksa apakah pengguna mencoba menonaktifkan akun mereka sendiri
            user.is_active = bool(is_active)
            user.save()
            messages.success(request, 'Status updated successfully.')
        else:
            messages.error(request, 'You cannot deactivate your own account.')
            
    return redirect('manajemen_pengguna')



@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(lambda u: u.is_staff, login_url=settings.LOGIN_URL)
def tambahdatapengguna(request):
    if request.method == 'POST':
        form = RegistrationAdminForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manajemen_pengguna')
    else:
        form = RegistrationAdminForm()
    return render(request, 'account/tambah_data_pengguna.html', {'form': form})

@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(lambda u: u.is_staff, login_url=settings.LOGIN_URL)
@require_POST
def delete_pengguna(request, id):
    pengguna = MyUser.objects.get(id=id)
    if request.method == 'POST':
        # Periksa apakah pengguna adalah pengguna yang sama dengan pengguna yang akan dihapus
        if request.user.id == pengguna.id:
            messages.error(request, 'You cannot delete your own account.')
        else:
            pengguna.delete()
            messages.success(request, 'Data deleted successfully.')
        return HttpResponseRedirect(reverse('manajemen_pengguna'))
    else:
        messages.error(request, 'Data failed to delete. Please try again.')
        return HttpResponseRedirect(reverse('manajemen_pengguna'))


def edit_pengguna(request, id):
    pengguna = MyUser.objects.get(id=id)
    if request.method == 'POST':
        form = RegistrationAdminForm(request.POST, instance=pengguna)
        if form.is_valid():
            pengguna = form.save()
            messages.success(request, 'Data updated successfully.')
            return redirect('manajemen_pengguna')
        else:
            messages.error(request, 'Data failed to update. Please check the details and try again.')
    else:
        form = RegistrationAdminForm(instance=pengguna)
    return render(request, 'account/edit_pengguna.html', {'form': form})

