from django.contrib import admin
from .models import Post, Contact


# Register your models here.

admin.site.register(Post)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
