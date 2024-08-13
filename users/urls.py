from django.urls import path, include
from .views import RegisterView, LoginView, LogoutView, UserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('user/', UserView.as_view(), name="user"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('farmers/', include('farmers_milk.urls'))
]
