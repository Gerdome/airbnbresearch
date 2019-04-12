from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = 'player'
    form_fields = ['name', 'age']


class Results(Page):
    pass

class VrPage(Page):
    pass


page_sequence = [
    MyPage,
    VrPage,
    Results
]