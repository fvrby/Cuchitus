from django.db import models
from django.utils import timezone
from django import forms

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Cliente(models.Model):
	correo = models.EmailField()
	run = models.CharField(max_length=10, primary_key=True)#validators=[run_validation])
	nombreCompleto = models.CharField(max_length=100)
	telefono = models.CharField(max_length=9)
	def __str__(self):
		return self.correo