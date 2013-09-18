import logging
from django.shortcuts import (
    HttpResponse, render_to_response, RequestContext, \
    HttpResponseRedirect, Http404
)
from django.utils import simplejson
from django.contrib.auth import authenticate, login
from django.forms.util import ErrorList
from django.utils.translation import ugettext_lazy as _
from app.utils.decorators import ajax_view
from .forms import LoginForm


logger = logging.getLogger(__name__)


@ajax_view(FormClass=LoginForm, login_required=False)
def ajax_login_view(request):
    form = LoginForm(request.POST)
    r={}
    if form.is_valid():
        user_or_email = form.cleaned_data['user_or_email']
        password = form.cleaned_data['password']
        remember = form.cleaned_data['remember']
        user = authenticate(username=user_or_email, email=user_or_email, password=password)
        if user:
            if user.is_active:
                login(request, user)
                if not remember:
                    request.session.set_expiry(0)
                r['redirect'] = '/'
        else:
            form._errors['user_or_email'] = ErrorList([unicode(_('Invalid user, email or password'))])
    else:
        form._errors['login_button'] = ErrorList([unicode(_('Login failed'))])

    if form.errors:
        r['errors'] = form.errors

    return HttpResponse(simplejson.dumps(r), mimetype='application/json; charset=UTF-8')


def action_view(request, action):
    if request.method == 'POST':
        pass
    if request.method == 'GET':
        cx = {
            'action': action,
            'page_title': _('Social login'),
        }
        if action == 'redirect':
            return HttpResponseRedirect("/")
        if action in ['error', 'new', 'disconnect', 'inactive']:
            return render_to_response('account/action.html', cx, RequestContext(request))
    
    raise Http404('Unknown action %s' % action)
