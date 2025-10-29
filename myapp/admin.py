
from django.contrib import admin
from .models import User
from .models import Address
from .models import Boat

admin.site.register(User)
admin.site.register(Address)
admin.site.register(Boat)