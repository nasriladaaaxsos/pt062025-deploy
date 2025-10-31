from django.db import models
import re 

class UserManager(models.Manager):
                                #request.POST
    def validate_sign_up(self, postData ):
        errors = { } 
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['firstname']) < 5 :
            errors['firstname_error'] = "Firstname should be more than 5 chars."
        if len(postData['lastname']) < 5 :
            errors['lastname_error'] = "Lastname should be more than 5 chars."
        if   len(postData['phone']) < 11 :
            errors['phone_error'] = "Phonenumber should be more than 10 chars."
        if len(postData['email']) == 0:
            errors['email_error'] = "Email should be filled."
        if len(postData['password']) == 0:
            errors['password_error'] = "Password should be filled."
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        return errors 
    

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
    objects = UserManager()
    #addresses
    #boats 

class Address(models.Model):
    #id
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    user = models.ForeignKey(User,  related_name="addresses"  ,    on_delete=models.DO_NOTHING  ) 
    created_at = models.DateTimeField( auto_now_add=True )
    updated_At = models.DateTimeField( auto_now=True )
    #objects (inherited)
    

class Boat(models.Model):
    #id
    name = models.CharField(max_length=30)
    type_of_boat = models.CharField(max_length=30)
    created_at = models.DateTimeField( auto_now_add=True )
    updated_At = models.DateTimeField( auto_now=True )
    users = models.ManyToManyField(User , related_name="boats")
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

