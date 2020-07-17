# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 13:59:14 2020

@author: lokesh
"""


from django import forms
from .models import Topic,Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}
        
        
class EntryForm(forms.ModelForm):
    class Meta:
        model=Entry
        fields =['text']
        labels={'text':'entry:'}
        widgets={'text': forms.Textarea(attrs={'cols':80})}