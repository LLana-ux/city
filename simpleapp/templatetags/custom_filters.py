from django import template


register = template.Library()



@register.filter()
def currency(value):
   """
   value: значение, к которому нужно применить фильтр
   """

   return f'{value} Р'

from django import template


register = template.Library()


CURRENCIES_SYMBOLS = {
   'rub': 'Р',
   'usd': '$',
}


@register.filter()
def currency(value, code='rub'):

   postfix = CURRENCIES_SYMBOLS[code]

   return f'{value} {postfix}'
