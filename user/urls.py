from django.urls import path
from .views import UserDetailsView, Userview, Loginview

urlpatterns = [
    path('user/<uuid:id>', Userview.as_view()),
    path('login', Loginview.as_view()),
    path('userdetails/', UserDetailsView.as_view())
]
