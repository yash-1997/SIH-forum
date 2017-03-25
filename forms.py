
from django import forms
from forums.models import Topic, Post

from settings import *

class TopicForm(forms.ModelForm):

    title = forms.CharField(max_length=60, required=True)

    class Meta():
        model = Topic
exclude = ('asker','updated', 'asked', 'answered', 'forum',)


class PostForm(forms.ModelForm):
    
    class Meta():
        model = Post
        exclude = ('asker', 'updated', 'asked','topic', 'employee_id',)

     

