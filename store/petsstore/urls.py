from . import views
from django . urls import path
app_name = "library"
urlpatterns = [
    path('', views.dashboard, name='dashBoard'),
    path('about', views.aboutUs, name='aboutUs'),
    path('fiction', views.fiction, name='fictionBooks'),
    path('anime', views.anime, name='animeBooks'),
    path('horror', views.horror, name='horrorBooks'),
    path('novels', views.novels, name='novelBooks'),
    path('datails/<int:id>/', views.details, name='booksDetails'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('register', views.user_register, name='register'),
    path('rent', views.rent, name='rent'),
]