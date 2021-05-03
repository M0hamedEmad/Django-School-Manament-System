from django import template

register = template.Library()

@register.filter
def Collect_ist_of_numbers_exam_score(value):
    result = 0
    for element in value:
        result+=element.exam_score
    return result

@register.filter
def Collect_ist_of_numbers_subject_score(value):
    result = 0
    for element in value:
        result+=element.exam_score
    return result
