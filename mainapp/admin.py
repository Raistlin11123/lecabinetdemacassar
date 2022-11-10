from unicodedata import category
from django.contrib import admin
from .models import Furniture, FurnitureImage
# Register your models here.

"""class FurnitureAdmin(admin.ModelAdmin):
    list_display   = ('title', 'date', 'for_sale', 'category', 'caracteristic')
    list_filter    = ('caracteristic', 'category')
    ordering       = ('date', 'title')

admin.site.register(Furniture, FurnitureAdmin)"""

#Ajouter des tris

class FurnitureImageAdmin(admin.StackedInline):
    model = FurnitureImage
 
@admin.register(Furniture)
class FurnitureAdmin(admin.ModelAdmin):
    inlines = [FurnitureImageAdmin]
 
    class Meta:
       model = Furniture
 
@admin.register(FurnitureImage)
class PostImageAdmin(admin.ModelAdmin):
    pass