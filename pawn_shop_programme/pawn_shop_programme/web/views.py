from django.urls import reverse_lazy
from django.views import generic as views

from pawn_shop_programme.web.forms import BuyEuroForm, BuyPoundForm, BuyOtherValueForm, SellOtherValueForm, \
    SellEuroForm, SellPoundForm
from pawn_shop_programme.web.utils import get_total_sum_euro_bought, get_total_sum_euro_sold, get_total_sum_pound_sold, \
    get_total_sum_pound_bought, get_total_sum_other_values_bought, get_total_sum_other_values_sold, get_total


class IndexView(views.TemplateView):
    template_name = 'common/index.html'


class Report(views.TemplateView):
    template_name = 'common/daily-report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['total-euro-bought'] = get_total_sum_euro_bought()
        context['total-euro-sold'] = get_total_sum_euro_sold()
        context['total-pound-bought'] = get_total_sum_pound_bought()
        context['total-pound-sold'] = get_total_sum_pound_sold()
        context['total-other-bought'] = get_total_sum_other_values_bought()
        context['total-other-sold'] = get_total_sum_other_values_sold()
        context['total-turnover'] = get_total()

        return context


class BuyingChoice(views.TemplateView):
    template_name = 'common/buying-choice.html'


class SellingChoice(views.TemplateView):
    template_name = 'common/selling-choice.html'


class BuyEuro(views.CreateView):
    template_name = 'buy/buy-euro.html'
    form_class = BuyEuroForm

    def get_success_url(self):
        return reverse_lazy('index')


class SellEuro(views.CreateView):
    template_name = 'sell/sell-euro.html'
    form_class = SellEuroForm


class BuyPound(views.CreateView):
    template_name = 'buy/buy-pound.html'
    form_class = BuyPoundForm


class SellPound(views.CreateView):
    template_name = 'sell/sell-pound.html'
    form_class = SellPoundForm


class BuyOtherValue(views.CreateView):
    template_name = 'buy/buy-other.html'
    form_class = BuyOtherValueForm


class SellOtherValue(views.CreateView):
    template_name = 'sell/sell-other.html'
    form_class = SellOtherValueForm
