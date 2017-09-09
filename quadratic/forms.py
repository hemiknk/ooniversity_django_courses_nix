from django import forms


class QuadraticForm(forms.Form):
    a = forms.CharField(max_length=100, label='коэффициент a', required=True)
    b = forms.CharField(max_length=100, label='коэффициент b', required=True)
    c = forms.CharField(max_length=100, label='коэффициент c', required=True)

    def clean(self):
        cleaned_data = super(QuadraticForm, self).clean()
        print(cleaned_data)
        self.clean_a(cleaned_data)
        return cleaned_data

    def clean_a(self, cleaned_data):
        a = cleaned_data['a']
        if 0 == a:
            self.errors.a = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
            raise forms.ValidationError("коэффициент при первом слагаемом уравнения не может быть равным нулю")
        return cleaned_data
