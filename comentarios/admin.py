from django.contrib import admin

from .actions import aprova_comentarios, reprova_comentarios
from .models import Comentario

# Register your models here.


class ComentariosAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'data', 'aprovado']
    actions = [reprova_comentarios, aprova_comentarios]


admin.site.register(Comentario, ComentariosAdmin)
