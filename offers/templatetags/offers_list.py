from django import template
from offers.models import Offer

register = template.Library()

@register.inclusion_tag('offers/components/offers_list.html', takes_context=True)
def offers_list(context):
    user = context['user']
    return {'offers': Offer.objects.filter(status='active'), 'user': user}