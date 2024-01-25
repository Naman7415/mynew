from django import forms

# class UploadForm(forms.Form):
#     title = forms.CharField(max_length=100)
#     file=forms.FileField()
    
# class MultipleFileinput(forms.ClearableFileInput):
#     allow_multiple_selected = True
    
# class MultipleFileField(forms.FileField):
#     def __init__(self,*args, **kwargs):
#         kwargs.setdefault("widget",MultipleFileinput)
#         super().__init__(*args, **kwargs)
        
#     def clean(self,data,initial=None):
#         single_file_clean = super().clean
#         if isinstance(data,(list,tuple)):
#             result = [single_file_clean(d,initial)for d in data]
#         else:
#             result = single_file_clean(data,initial)
#         return result
    
# class FileFieldform(forms.Form):
#     file_field = MultipleFileField()


from django import forms


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class FileFieldForm(forms.Form):
    files = MultipleFileField()