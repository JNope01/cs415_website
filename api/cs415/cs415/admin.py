from django.contrib import admin
from .models import User, Userdaylog, Usergoals, Userinfo

admin.site.register(User)
admin.site.register(Userdaylog)
admin.site.register(Usergoals)
admin.site.register(Userinfo)
