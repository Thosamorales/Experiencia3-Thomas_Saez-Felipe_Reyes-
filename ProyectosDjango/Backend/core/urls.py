from django.urls import path
from .views import home, formulario, formularioRE, Galeria, herramienta, moneda, quinesSomos, tierra, mostrar, inicioAdmin, form_crear_colaborador, form_del_colaborador, form_mod_colaborador,  inventario, inventarioCrear, inventarioMod, inventario_del

urlpatterns = [
    path('', home,name="home"),
    path('formulario/',formulario, name="formulario"),
    path('formularioRE/',formularioRE, name="formularioRE"),
    path('Galeria/',Galeria, name="Galeria"),
    path('herramienta/',herramienta, name="herramienta"),
    path('moneda/',moneda, name="moneda"),
    path('quinesSomos/',quinesSomos, name="quinesSomos"),
    path('tierra/',tierra, name="tierra"),
    path('mostrar/',mostrar, name="mostrar"),
    path('inicioAdmin/',inicioAdmin, name="inicioAdmin"),
    path('form_crear_colaborador/',form_crear_colaborador, name="form_crear_colaborador"),
    path('form_del_colaborador/<id>', form_del_colaborador, name="form_del_colaborador"),
    path('form_mod_colaborador/<id>', form_mod_colaborador, name="form_mod_colaborador"),
    path('inventario/', inventario, name="inventario"),
    path('inventarioCrear/',inventarioCrear, name="inventarioCrear"),
    path('inventarioMod/<id>', inventarioMod, name="inventarioMod"),
    path('inventario_del/<id>', inventario_del, name="inventario_del"),
    

]