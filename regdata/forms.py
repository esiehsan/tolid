from django import forms
from .models import Part
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget
import datetime

class PartForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ['partNumber', 'castDate', 'caster1','caster2', 'caster3', 'mold_Id']

    def __init__(self, *args, **kwargs):
        super(PartForm, self).__init__(*args, **kwargs)
        self.fields['castDate'] = JalaliDateField(label=('castDate'), # date format is  "yyyy-mm-dd"
        #     widget=AdminJalaliDateWidget # optional, to use default datepicker
        )
        self.fields['castDate'].initial = datetime.date.today()

        # you can added a "class" to this field for use your datepicker!
        # self.fields['castDate'].widget.attrs.update({'class': 'jalali_date-date'})
