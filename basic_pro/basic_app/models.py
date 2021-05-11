from django.db import models


# Create your models here.
class Bjp(models.Model):
    name = models.CharField(max_length=264, unique= True)
    email = models.EmailField(unique=True)
    text = models.CharField(max_length=2000)

    def __str__(self):
        return self.name

class Access(models.Model):
    name = models.ForeignKey(Bjp , on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
