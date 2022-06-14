from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Categoria, Colaborador, Inventario


class ColaboradorForm(forms.ModelForm):

    class Meta: 
        model= Colaborador
        fields = ['rut', 'nombre', 'correo', 'categoria']
        labels ={
            'rut': 'Rut', 
            'nombre': 'Nombre', 
            'correo': 'Correo', 
            'categoria': 'Categoría',
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': '11222333-4', 
                    'id': 'rut'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su nombre', 
                    'id': 'nombre'
                }
            ), 
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'correo@dominio.cl/com', 
                    'id': 'correo'
                }
            ), 
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria',
                }
            )

        }

class InventarioForm(forms.ModelForm):

    class Meta: 
        model= Inventario
        fields = ['codigo', 'nombreIn', 'Cantidad', 'imagen']
        labels ={
            'codigo': 'Codigo', 
            'nombreIn': 'Nombre', 
            'Cantidad': 'Cantidad', 
           
        }
        widgets={
            'Codigo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Codigo', 
                    'id': 'codigo'
                }
            ), 
            'nombreIn': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre del Producto', 
                    'id': 'nombreIn'
                }
            ), 
            'Cantidad': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Cantidad', 
                    'id': 'Cantidad'
                }
            ),
        }
