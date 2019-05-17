from django.db import models

# Create your models here.


class Condo(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    superuser = models.EmailField(max_length=64, unique=True, null=True)
    
    def __str__(self):
        return f"{self.id}: {self.name} located at {self.address}"


class Facility(models.Model):
    name = models.CharField(max_length=64)
    open_time = models.TimeField(null=True)
    close_time = models.TimeField(null=True)
    condo = models.ForeignKey(
        Condo, on_delete=models.CASCADE, related_name="condo")
        

    def __str__(self):
        return f"{self.origin} to {self.destination} in {self.duration} mins"


# class Passenger(models.Model):
#     fname = models.CharField(max_length=64)
#     lname = models.CharField(max_length=64)
#     trains = models.ManyToManyField(
#         Train, blank=True, related_name="passengers")

#     def __str__(self):
#         return f"{self.fname} {self.lname}"