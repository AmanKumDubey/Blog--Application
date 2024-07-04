from django.contrib import admin
from .models import Post,Contact_us
# Register your models here.

@admin.register(Post)
class postmodelAdmin(admin.ModelAdmin):
    list_display = ['id','title','desc']
    # list_filter=('is_published','created_at')
    search_fields=('title','desc')
    actions=['publish_posts']
    
    def publish_posts(self,request,queryset):
        self.message_user(request,f'Selected posthave been published .')
        
    publish_posts.short_description='Public selected posts '
# admin.site.register(Post)

# admin.site.register(Category)
# admin.site.register(Post)
admin.site.register(Contact_us)