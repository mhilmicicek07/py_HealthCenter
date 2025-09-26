from django.contrib import admin
from .models import Category, News, Author

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ('baslik','tarih','yazar','kategori')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('ad','pozisyon','bilgi')

admin.site.register(Category)
admin.site.register(News,NewsAdmin)
admin.site.register(Author,AuthorAdmin)