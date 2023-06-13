# rules_app/admin.py
from django.contrib import admin
from .models import Rule, Example
from .forms import ExampleForm

class ExampleAdmin(admin.ModelAdmin):
    form = ExampleForm

    class Media:
        js = ('example_admin.js',)  # Path to your JavaScript file

admin.site.register(Rule)
admin.site.register(Example, ExampleAdmin)