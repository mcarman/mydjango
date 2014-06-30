#apps.snippets.admin
import models
from django.contrib import admin
from django.contrib.auth.models import User


# class SnippetAdmin(admin.ModelAdmin):
#     fields = ('title', ('language', 'style'))
#     exclude = ('owner',)

#     def save_model(self, request, obj, form, change):
#         obj.owner = request.user
#         obj.save()

admin.site.register(models.Snippet)
