from django.db import models
from datetime import datetime, date, time, timedelta



class Proyect(models.Model):
	name=models.CharField(max_length=50,unique=True)
	description=models.TextField(max_length=200)
	goal_time=models.DateField(blank=True,null=True)
	started_time=models.DateField(blank=True,null=True)
	obstacles=models.ManyToManyField('Obstacle',blank=True)
	objetives=models.ManyToManyField('Objetive',blank=True)
	finished=models.BooleanField(default=False,editable=False)

	def start_proyect(self):
		self.started_time=datetime.now()

	def add_goal_time(self,days):
		if days!=None:
			self.goal_time=datetime.now()+timedelta(days=days)


	def __str__(self):
		return self.name

class Obstacle(models.Model):
	name=models.CharField(max_length=50)
	options=(('0',""),('mild','Mild'),('medium','Medium'),('strong','Strong'))
	difficulty=models.CharField(max_length=20,choices=options,default="")

	def __str__(self):
		return self.name

class Objetive(models.Model):
	name=models.CharField(max_length=50)
	completed=models.BooleanField(default=False)

	def __str__(self):
		return self.name

	




