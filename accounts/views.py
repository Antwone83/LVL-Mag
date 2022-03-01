from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("Login")
    template_name = "registration/signup.html"

# Create your views here.
