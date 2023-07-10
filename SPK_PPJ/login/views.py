from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import LoginForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            request.session['NimOrNip'] = user.NimOrNip
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid email or password, or your account is not active.')
    else:
        form = LoginForm()
    
    return render(request, 'login/login_view.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/login/')


# class MyPasswordResetView(FormView):
#     template_name = 'login/password_reset.html'
#     form_class = PasswordResetForm
#     success_url = reverse_lazy('password_reset_done')

#     def form_valid(self, form):
#         form.save(
#             domain_override='localhost:8000',
#             email_template_name='login/password_reset_email.html',
#             use_https=self.request.is_secure(),
#             request=self.request,
#         )
#         return super().form_valid(form)
