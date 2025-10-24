from django.db import models

# Create your models here.
class User(models.Model):  #users
    #id (inherited)
    firstname = models.CharField(max_length=50)  #varchar(255)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=10)
    password = models.CharField(max_length=25)
    created_at = models.DateTimeField( auto_now_add=True )
    updated_At = models.DateTimeField( auto_now=True )
    #objects (inherited)
    #addresses
    
class Address(models.Model):
    #id
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    user = models.ForeignKey(User,  related_name="addresses"  ,    on_delete=models.DO_NOTHING  ) 
    created_at = models.DateTimeField( auto_now_add=True )
    updated_At = models.DateTimeField( auto_now=True )
    #objects

def create_user( postData ):
    firstname  = postData['firstname'] 
    lastname = postData['lastname']
    phone = postData['phone']
    email = postData['email']
    form_name = postData['form_name']
    password = postData['password']
    User.objects.create( firstname = firstname , lastname = lastname , email = email , phonenumber = phone, password = password)
    
def get_all_users():
    return User.objects.all()

def get_user_by_id( id): 
    return User.objects.get( id = id )

def delete_user(id):
    user = User.objects.get( id = id)
    user.delete()
    
    
def add_new_address(postData):
    
    user_id = postData["user_id"]
    city = postData["city"]
    country = postData["country"]
    street = postData["street"]
    
    user = get_user_by_id(user_id)
    
    Address.objects.create( country = country , city = city , street = street, user = user  )
    

def get_all_addresss(id):
    return get_user_by_id(id)