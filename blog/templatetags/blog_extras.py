from django import template

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
