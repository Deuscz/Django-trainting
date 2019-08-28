from django import forms
from .models import Goods

# class CreateGoods(forms.ModelForm):
#     class Meta:
#         model = Goods
#         fields = [
#             'title',
#             'description',
#             'image',
#             'price',
#             'date_pub',
#             'is_offer',
#         ]
    
class CreateGoods(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    image = forms.ImageField(required=False)
    price = forms.IntegerField()