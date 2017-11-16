from django import forms
from .models import Proyect,Objetive,Obstacle
from django.forms import inlineformset_factory

class ProyectForm(forms.ModelForm):
	class Meta:
		model=Proyect
		fields= ('name','obstacles','objetives','description')

	add_goal_time=forms.IntegerField()

class ObjetiveForm(forms.ModelForm):
	class Meta:
		model=Objetive
		fields=('name','completed')

class ObstacleForm(forms.ModelForm):
	class Meta:
		model=Obstacle
		fields=('name','difficulty')
