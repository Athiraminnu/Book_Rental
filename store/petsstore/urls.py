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
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]