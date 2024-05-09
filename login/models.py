from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=150)

    def __str__(self):
        return self.username

# Aún no tengo definido como sería el comportamiento, si es entre dos Apps el intercambio
# o es entre dos proyectos distintos e independientes

# class Send(models.Model):
#     uuid = model.CharField(max_length=100)
#     body = model.TextField()
#     email = model.CharField(max_length=100)
#     title = model.CharField(max_length=150)

#     def __str__(self): 
#         #return self.email
#         return self.uuid,self.body,self.email,self.title
