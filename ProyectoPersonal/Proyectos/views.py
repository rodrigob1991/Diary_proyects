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
		form=ProyectForm()
		
		return render(request,'Proyectos/new_proyect.html',{'form':form})

def create_objetive(request):

	if request.method=="POST":
		form=ObjetiveForm(request.POST)
		if form.is_valid():
			objetive=form.save(commit=True)
			return redirect('create_objetive')
	else:
		form=ObjetiveForm()
		return render(request,'Proyectos/new_relation.html',{'form':form})


def create_obstacle(request):

	if request.method=="POST":
		form=ObstacleForm(request.POST)
		if form.is_valid():
			obstacle=form.save(commit=True)
			return redirect('create_obstacle')
	else: 
		form=ObstacleForm()
		return render(request,'Proyectos/new_relation.html',{'form':form})

def edit_proyect(request,primary_key):
	proyect=get_object_or_404(Proyect,pk=primary_key)
	if request.method=="POST":
		form=ProyectForm(request.POST,instance=proyect)
		if form.is_valid():
			proyect=form.save(commit=False)
			proyect.add_goal_time(form.cleaned_data["add_goal_time"])
			proyect.save()
			return redirect('proyect_description',primary_key=proyect.pk)
	else:
		form=ProyectForm(instance=proyect)
		return render(request,'Proyectos/new_proyect.html',{'form':form})


		