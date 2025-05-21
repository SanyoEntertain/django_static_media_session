from django.urls import path
from . import views


urlpatterns = [
    # READ
    path('', views.home, name='home'),
    # DETAIL READ
    path('blog/<int:blog_id>', views.detail, name='detail'),
    # CREATE
    path('blog/create', views.create, name='create'),
    # EDIT
    path('blog/<int:blog_id>/edit', views.edit, name='edit'),
    path('blog/<int:blog_id>/update', views.update, name='update'),
]