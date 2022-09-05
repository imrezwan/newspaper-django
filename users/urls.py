from . import views
from django.urls import path, include

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name = 'signup'),
]
