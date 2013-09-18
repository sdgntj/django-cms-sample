from django.utils.translation import ugettext_lazy as _
import floppyforms as forms


class LoginForm(forms.Form):
    user_or_email = forms.CharField()
    password = forms.CharField()
    remember = forms.BooleanField(label=_('Remember me?'), required=False)
