from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.ista_canchas, name='index'),
    path('detalle_cancha/<int:pk>/', views.detalle_cancha, name='detalle_cancha'),
    path('editar_reserva/<int:pk>/' , views.editar_reserva, name='editar_reserva'),
    path('crear_reserva/<int:pk>/', views.crear_reserva , name='crear_reserva'),
    path('borrar/<int:pk>/', views.borrar, name='borrar')

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
