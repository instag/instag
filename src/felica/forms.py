# # -*- coding: utf-8 -*-
# from django import forms
#
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
# from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
# from . import models
#
# class ShopForm(forms.ModelForm):
#
#     def __init__(self, *args, **kwargs):
#         super(ShopForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_tag = False
#         self.helper.layout = Layout(
#             Field('shop_title'),
#             Field('shop_description'),
#             Submit('update', 'Update', css_class="btn-success"),
#             )
#
#     class Meta:
#         model = models.Shop
#         fields = ['shop_title', 'shop_description']
