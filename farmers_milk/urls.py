from django.urls import path
from .views import CreateCowView, GetCowsView

urlpatterns = [
    path('create_cow/', CreateCowView.as_view(), name='create cow'),
    path('see_cows/', GetCowsView.as_view(), name='get cows')
]
