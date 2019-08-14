from django import template
from translate import Translator

register = template.Library()

@register.filter
def to_class_name(value):
    return value.__class__.__name__

@register.filter
def orientation(image):
    orientation = 'landscape' if image.width > image.height else 'portrait'
    return orientation

@register.filter
def split_list(value,toSplit):
    toReturn = value.split(toSplit)
    return toReturn

@register.simple_tag
def translate(value, language, toTitle):
    # translator = Translator(to_lang=language)
    # toReturn = translator.translate(value).title() if toTitle else translator.translate(value)
    toReturn = value.title() if toTitle else value
    return toReturn
