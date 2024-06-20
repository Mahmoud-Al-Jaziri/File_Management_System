from django.contrib import admin
from django.urls import path
from DocumentFlow import views
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path("admin/", admin.site.urls),
    #path('', views.homePage,name="homePage"),
    path('login/',views.loginPage,name="loginPage"),
    path('logout/',views.logoutUser,name="logout"),
    path('upload/', views.upload_file, name='upload_file'),
    path('', views.file_list, name='file_list'),
    path('file/<int:pk>/', views.file_detail, name='file_detail'),
    path('managerFiles/', views.manager_file_list, name='manager_file_list'),
    path('files/<int:pk>/review/', views.review, name='review'),
    path('files/<int:pk>/ask-for-update/', views.ask_for_update, name='ask_for_update'),
    path('files/<int:pk>/reject/', views.reject_file, name='reject_file'),
    path('serve-file/<int:pk>/', views.serve_file, name='serve_file'),
    path('files/<int:pk>/update/', views.update_file, name='update_file'),
    path('request-file/', views.request_file, name='request_file'),
    path('file-requests/', views.file_request_list, name='file_request_list'),
    path('files/<int:pk>/accept/', views.accept, name='accept'),
    path('acceptedFiles/', views.accepted_file_list, name='accepted_file_list'),
    path('files/<int:pk>/SupervisorReview/', views.supervisor_review, name='supervisor_review'),

]
