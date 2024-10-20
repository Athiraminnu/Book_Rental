from . import views
from django . urls import path
app_name = "library"
urlpatterns = [
    path('', views.dashboard, name='dashBoard'),
    path('/fiction', views.fiction, name='fictionBooks'),
]