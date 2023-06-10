from django.template import Library

register = Library()


@register.filter
def get_workout_for_day(day, workout_dict):
    return workout_dict[day]