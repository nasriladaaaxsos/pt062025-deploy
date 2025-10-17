from django.db import models

# Create your models here.
class User(models.Model):  #users
    #id (inherited)
    firstname = models.CharField(max_length=50)  #varchar(255)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=10)
    created_at = models.DateTimeField( auto_now_add=True )
    updated_At = models.DateTimeField( auto_now=True )
    #objects (inherited)
    
    
def create_user( postData ):
    firstname  = postData['firstname'] 
    lastname = postData['lastname']
    phone = postData['phone']
    email = postData['email']
    form_name = postData['form_name']
    User.objects.create( firstname = firstname , lastname = lastname , email = email , phonenumber = phone)
    

def get_all_users():
    return User.objects.all()


def get_user_by_id( id): 
    return User.objects.get( id = id )