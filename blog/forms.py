from django import forms

from .models import Alquiler

class ReservaForm(forms.ModelForm):

	class Meta:
		model = Alquiler
		fields = ('cancha','cliente','empleado','fechaReserva','fechaHora',)