from django.shortcuts import render, get_object_or_404,redirect
from .models import Proyect
from .form import ProyectForm,ObjetiveForm,ObstacleForm

def proyect_name(request):

	proyects=Proyect.objects.all()
	return render(request,'Proyectos/proyect.html',{'proyects':proyects})


def proyect_description(request,primary_key):

	proyect=get_object_or_404(Proyect,pk=primary_key)
	return render(request,'Proyectos/proyect_description.html',{'proyect':proyect})

def create_proyect(request):

	if request.method=="POST":
		form=ProyectForm(request.POST)
		if form.is_valid():
			proyect=form.save(commit=False)
			proyect.start_proyect() 
			proyect.add_goal_time(form.cleaned_data["add_goal_time"])
			proyect.save()
			proyect.obstacles.set(form.cleaned_data["obstacles"])
			proyect.objetives.set(form.cleaned_data["objetives"])
			proyect.save()
			return redirect('proyect_description', primary_key=proyect.pk)
	else:
		new_proyect=ProyectForm()
		new_objetive=ObjetiveForm()
		new_obstacle=ObstacleForm()

		return render(request,'Proyectos/new_proyect.html',{'new_proyect':new_proyect,'new_objetive':new_objetive,'new_obstacle':new_obstacle})


	
