from django import forms
from .models import Review



class ReviewForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"  #widget - za spravuvanje so prikazuvanje na html i izvlekuvane podatoci od GET/POST

    class Meta:
        model = Review
        exclude = ("users",)
