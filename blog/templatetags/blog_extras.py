from django import template

def orientation(image):
    orientation = 'landscape' if image.width > image.height else 'portrait'
    return orientation

register = template.Library()

register.filter('orientation', orientation)
