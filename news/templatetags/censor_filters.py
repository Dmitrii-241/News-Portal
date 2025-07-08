from django import template
import re

register = template.Library()

BAD_WORDS = ['редиска', 'дурень', 'глупец']  # Добавьте свои слова

@register.filter
def censor(value):
    if not isinstance(value, str):
        raise ValueError("Фильтр 'censor' применяется только к строкам")

    def replace(match):
        word = match.group()
        return word[0] + '*' * (len(word) - 1)

    for bad in BAD_WORDS:
        # Первая буква — верхний или нижний регистр, остальные — только нижний
        pattern = re.compile(r'\b[' + bad[0].lower() + bad[0].upper() + ']' + bad[1:] + r'\b')
        value = pattern.sub(replace, value)

    return value