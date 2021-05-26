from django.urls import path
from . import views

urlpatterns = [
    path('tvshow/tvshow', views.tvshow),
    path('tvshow/new_show', views.new_show),
    path('tvshow/create', views.create),
    path('tvshow/<int:id>', views.show),
    path('tvshow/<int:id>/edit', views.edit_show),
    path('tvshow/<int:id>/destroy', views.destroy),
    path('tvshow/update', views.update)
]