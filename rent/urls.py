from django.urls import path
from rent.views import index, image_upload_view, by_area


urlpatterns = [
    path('', index, name='index'),
    path('areas/', index, name='areas'),
    path('add/', image_upload_view, name='add'),
    path('<int:area_id>/', by_area, name='by_area')

]