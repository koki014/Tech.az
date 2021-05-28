from django.urls import path, include


app_name = 'account'

urlpatterns = [
    path('user/', include('account.api.urls'))
]