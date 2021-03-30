from django.urls import path, include


app_name = 'account'

urlpatterns = [
    path('v1.0/', include('account.api.urls'))
]