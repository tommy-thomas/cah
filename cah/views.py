from django.views.generic import FormView

from cah.forms import CAHForm


class CAHFormView(FormView):
    form_class = CAHForm
    template_name = "cah/index.html"