from django.contrib import admin
from .models import Category,Article,Review,Portal

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = [field.name for field in Category._meta.fields if field.name != "id"]
   
admin.site.register(Category, CategoryAdmin)

class  ArticleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Article._meta.fields if field.name != "id"]

admin.site.register(Article,ArticleAdmin)
admin.site.register(Review)
admin.site.register(Portal)
