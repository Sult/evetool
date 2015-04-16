from django import forms

from .models import CharacterJournal, RefType


class FilterJournalForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.characterapi = kwargs.pop("characterapi")
        super(FilterJournalForm, self).__init__(*args, **kwargs)
        self.fields['filter'] = forms.ChoiceField(
            required=False,
            choices=self.filter_choices(),
        )

    def filter_choices(self):
        choices = []
        reftypes = CharacterJournal.objects.filter(
            characterapi=self.characterapi
        ).order_by().values_list("reftypeid", flat=True).distinct()
        for reftypeid in reftypes:
            try:
                name = RefType.objects.get(reftypeid=reftypeid).reftypename
            except RefType.DoesNotExist:
                name = "Unknown"
            choices.append([reftypeid, name])
            print reftypeid, name

        #sort alfabeticly and ad first
        choices = sorted(choices, key=lambda x: x[1])
        choices.insert(0, [None, "Everything"])
        return choices
