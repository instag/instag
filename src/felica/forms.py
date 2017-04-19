# -*- coding: utf-8 -*-
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from . import models

class FelicaMemberForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FelicaMemberForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('company_name'),
            Field('member_name'),
            Field('hour_price'),
            Submit('update', 'Update', css_class="btn-success"),
            )

    class Meta:
        model = models.FelicaMember
        fields = ['company_name', 'member_name', 'hour_price']


class FelicaTimeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FelicaTimeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('company_name'),
            Field('member_name'),
            Field('work_start'),
            Field('work_end'),
            Field('work_time_hour'),
            Field('work_time_minute'),
            Field('felica_id'),
            Submit('update', 'Update', css_class="btn-success"),
            )

    class Meta:
        model = models.FelicaTime
        fields = ['company_name', 'member_name', 'felica_id', 'work_start', 'work_end', 'work_time_hour', 'work_time_minute']