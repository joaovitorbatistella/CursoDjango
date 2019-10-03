from django.contrib import admin
from livros.models import Autor, Livro
from rangefilter.filter import DateRangeFilter

class AdminAutor(admin.ModelAdmin):
    list_display = ( 'nome',)
    list_filter = ( 'nome',)
    search_fields = ['nome']
admin.site.register(Autor, AdminAutor)

class AdminLivro(admin.ModelAdmin):
    list_display = ( 'titulo', 'data_publicacao', 'isbn', 'autor')
    list_filter = ( 'titulo', ('data_publicacao', DateRangeFilter), 'categoria')
    search_fields = ['titulo', 'autor__nome', 'data_publicacao']
admin.site.register(Livro, AdminLivro)

admin.site.site_header = 'My Project'
admin.site.index_title = 'Meu Projeto'
admin.site.site_title = "Mi Projeto"

