def reprova_comentarios(modeladim, request, queryset):
    queryset.update(aprovado=False)


def aprova_comentarios(modeladim, request, queryset):
    queryset.update(aprovado=True)


reprova_comentarios.short_description = 'Reprova Comentarios'
aprova_comentarios.short_description = 'Aprova Comentarios'
