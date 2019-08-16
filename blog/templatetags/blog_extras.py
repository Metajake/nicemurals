from django import template
from translate import Translator
import random

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
    translator = Translator(to_lang=language, email='jaynoco@gmail.com')
    # toReturn = translator.translate(value).title() if toTitle else translator.translate(value)
    toReturn = value.title() if toTitle else value
    return toReturn

@register.filter
def shuffle(value):
    itemList = []
    for item in value:
        itemList.append(item)
    shuffledList = random.sample(itemList, len(itemList))
    return shuffledList
