from django.contrib import admin
from forums.model import Forum, Topic, Post

class TopicAdmin(admin.ModelAdmin):
	list_display=["title","forum","asker","asked"]
	list_filter=["forum","asked"]
class PostAdmin(admin.ModelAdmin):
	search_fields=["title","asked"]
	lisy_display=["title","topic","asker","asked"]

#admin.site.register(Forum, ForumAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)
#admin.site.register(ProfaneWord, ProfaneWordAdmin)
# Register your models here.
