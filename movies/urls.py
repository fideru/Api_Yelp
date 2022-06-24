from django.urls import path
# the . before import specifies imports from the project folder/package
from . import views

# movies/
# movies/1/details

urlpatterns = [
    path('', views.index, name='index')
]