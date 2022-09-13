from django import forms
from secondapp.models import add_product

class add_product_form(forms.ModelForm):
    class Meta:
        model = add_product
        
        # exclude = ["product_name","details"]
        fields = ["product_name","product_category","product_price","sale_price","product_image","details"]