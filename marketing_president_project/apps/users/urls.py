# apps/users/urls.py
from django.urls import path
from .views import (
    login_view, 
    logout_view, 
    registrar_approvals_view,
    user_add_view,
    user_edit_view,
    user_delete_view
)

app_name = 'users'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('approvals/', registrar_approvals_view, name='approvals'),
    # URL untuk CRUD
    path('add/', user_add_view, name='user_add'),
    path('<int:pk>/edit/', user_edit_view, name='user_edit'),
    path('<int:pk>/delete/', user_delete_view, name='user_delete'),
]
