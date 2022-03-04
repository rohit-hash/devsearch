#from dataclasses import field
#from pyexpat import model
#from tkinter.tix import Form

#import django


from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
      class Meta:
          model = Project
          fields = ['title','featured_image','description','demo_link','source_link','tags']