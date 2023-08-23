from django.urls import path, include
from pawn_shop_programme.web.views import IndexView, Report, SellPound, SellOtherValue, SellEuro, BuyEuro, BuyPound, \
    BuyOtherValue, BuyingChoice, SellingChoice, delete_daily_report

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('report/', Report.as_view(), name='report'),
    path('finish-the-day', delete_daily_report, name='delete daily report'),
    path('buy-dashboard/', BuyingChoice.as_view(), name='buy dashboard'),
    path('sell-dashboard/', SellingChoice.as_view(), name='sell dashboard'),
    path('buy/', include([
        path('pound/', BuyPound.as_view(), name='buy pound'),
        path('euro/', BuyEuro.as_view(), name='buy euro'),
        path('other/', BuyOtherValue.as_view(), name='buy other'),
    ])),
    path('sell/', include([
        path('pound/', SellPound.as_view(), name='sell pound'),
        path('euro/', SellEuro.as_view(), name='sell euro'),
        path('other/', SellOtherValue.as_view(), name='sell other'),
    ]))
)
