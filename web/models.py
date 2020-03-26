from django.db import models

# Create your models here.
class Contact(models.Model):
    """A contact model
    Attributes:
        name
        addresss
        number
        dob
    """
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    dob = models.IntegerField()


    def __str__(self):
        return self.name

class ContactNumber(models.Model):
    """A contact number for inidividual model
    
    Arguments:
        models {[type]} -- [description]
    """
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    number = models.IntegerField()
    type = models.CharField(max_length=50,default="Primary", null=True, blank=True)

    def __str__(self):
        return f"{self.contact.name} {self.number} {self.type}"

