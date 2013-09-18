from .forms import LoginForm


def get_login_form(request):
    context = {'login_form': None}

    if not request.user.is_authenticated():
        context['login_form'] = LoginForm()

    return context