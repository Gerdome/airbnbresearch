from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = 'player'
    form_fields = ['name', 'age','gender']


class Results(Page):
    pass

class VrPage(Page):
    pass

class RegularPage(Page):
    pass

class VRQuestionnaire(Page):
    pass

class RegularQuestionnaire(Page):
    pass

page_sequence = [
    MyPage,
    RegularPage,
    RegularQuestionnaire,
    VrPage,
    VRQuestionnaire,
    Results
]