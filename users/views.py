from django.views import generic
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

class SignUpView(generic.CreateView):
    template_name: str = 'signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
