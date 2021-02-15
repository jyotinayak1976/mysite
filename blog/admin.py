from django.contrib import admin

from .models import Post


#class ContactInline(admin.StackedInline):
#    model = Contact

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish','status')
    list_filter = ('status','created','publish', 'author')
    search_fields = ('title','body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status','publish')

#    inlines = [ContactInline]

#class ContactAdmin(admin.ModelAdmin):

#    list_display = ('Name','Email_Address','Phone_Number','message')
#    search_fields = ('Name','Email_Address')
#    ordering = ('Name')

# Register your models here.
