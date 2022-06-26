from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('signin', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('upload/', views.upload, name='upload'),
    path('purify/', views.purify, name='purify'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    