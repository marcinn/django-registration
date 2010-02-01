"""
URLConf for Django user registration and authentication.

If the default behavior of the registration views is acceptable to
you, simply use a line like this in your root URLConf to set up the
default URLs for registration::

    (r'^accounts/', include('registration.urls')),

This will also automatically set up the views in
``django.contrib.auth`` at sensible default locations.

But if you'd like to customize the behavior (e.g., by passing extra
arguments to the various views) or split up the URLs, feel free to set
up your own URL patterns for these views instead. If you do, it's a
good idea to use the names ``registration_activate``,
``registration_complete`` and ``registration_register`` for the
various steps of the user-signup process.

"""


from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib.auth import views as auth_views

from registration.views import activate
from registration.views import register
from django.views.generic.simple import direct_to_template

from registration.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm

urlpatterns = patterns('',
                       # Activation keys get matched by \w+ instead of the more specific
                       # [a-fA-F0-9]{40} because a bad activation key should still get to the view;
                       # that way it can return a sensible "invalid key" message instead of a
                       # confusing 404.
                       url(r'^$',
                            direct_to_template,
                            {'template': 'registration/root.html',
                            'extra_context': { 'register_form': RegistrationForm,
                                                'login_form': AuthenticationForm } },
                            name='registration_root'),
                       url(r'^ativar/(?P<activation_key>\w+)/$',
                           activate,
                           name='registration_activate'),
                       url(r'^login/$',
                           auth_views.login,
                           {'template_name': 'registration/login.html'},
                           name='auth_login'),
                       url(r'^logout/$',
                           auth_views.logout,
                           {'template_name': 'registration/logout.html'},
                           name='auth_logout'),
                       url(r'^senha/mudar/$',
                           auth_views.password_change,
                           name='auth_password_change'),
                       url(r'^senha/mudar/feito/$',
                           auth_views.password_change_done,
                           name='auth_password_change_done'),
                       url(r'^senha/resetar/$',
                           auth_views.password_reset,
                           name='auth_password_reset'),
                       url(r'^senha/resetar/confirmar/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
                           auth_views.password_reset_confirm,
                           name='auth_password_reset_confirm'),
                       url(r'^senha/resetar/completo/$',
                           auth_views.password_reset_complete,
                           name='auth_password_reset_complete'),
                       url(r'^senha/resetar/feito/$',
                           auth_views.password_reset_done,
                           name='auth_password_reset_done'),
                       url(r'^registrar/$',
                           register,
                           name='registration_register'),
                       url(r'^registrar/completo/$',
                           direct_to_template,
                           {'template': 'registration/registration_complete.html'},
                           name='registration_complete'),
                       )
