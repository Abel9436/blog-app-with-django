from django.contrib import admin
from BLogapp.models import Catagory,Post,Comment
# Register your models here.
class CatagoryAdmin(admin.ModelAdmin):
    pass
class PostAdmin(admin.ModelAdmin):
    pass
class CommentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Catagory,CatagoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)