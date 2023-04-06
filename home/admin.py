from django.contrib import admin
from .models import *

# Register your models here.
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('username','email','password')

class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title','description','creation_date','is_public')

class LikeModelAdmin(admin.ModelAdmin):
    list_display = ('user_id','post_id')

admin.site.register(UserModel, UserModelAdmin)
admin.site.register(PostModel, PostModelAdmin)
admin.site.register(LikeModel, LikeModelAdmin)