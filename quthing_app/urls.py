from django.urls import path
from . import views

urlpatterns = [
    path('', views.Showemp, name='show_emp'),
    path('inserttemp', views.Inserttemp, name='Inserttemp'),
    path('edit/<int:id>', views.Editemp, name="edit_emp"),
    path('update/<int:id>', views.Updateemp, name="update_emp"),
    path('delete/<int:id>/', views.Delemp, name='delete_emp'),
]