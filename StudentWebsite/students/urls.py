from django.urls import path

from students import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add/', views.add_student, name='add'),
    path('delete/<int:id>/', views.delete_student, name='delete'),
    path('update/<int:id>/', views.update_student, name='update'),
    path('topper/', views.topper, name='topper'),
]