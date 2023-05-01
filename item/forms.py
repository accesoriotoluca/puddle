from django import forms
from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

# estos formularios pueden ya tener la lógica de validación de su modelo

"""
?utiliza Django ModelForms 
*para crear un formulario basado en un modelo específico. 
Esto significa que el formulario se creará automáticamente 
con campos correspondientes al modelo, 
* y también se generará automáticamente la validación de los datos de entrada 
* y la creación de objetos del modelo correspondiente. 
?Este enfoque es útil: 
cuando se desea una integración completa entre la base de datos y el formulario, 
y cuando se desea aprovechar la capacidad de Django de crear formularios a partir de modelos.

! si no especificas campos, widgets, validación
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
* Django crea automáticamente campos para cada campo del modelo especificado en el atributo model de la clase Meta.
* Además, los campos creados tendrán automáticamente los widgets correspondientes a cada tipo de campo del modelo.
* y se encargará de la validación de los datos ingresados.
? si deseas personalizar la forma en que se muestran los campos 
? o cómo se valida la entrada del usuario, 
? puedes especificar los widgets y la validación manualmente"""

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')
        widgets = {
            'category': forms.Select(attrs={
            'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
            'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
            'class': INPUT_CLASSES
            })
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')
        widgets = {
            'name': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
            'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
            'class': INPUT_CLASSES
            }),
        }