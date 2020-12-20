from django_components import component

from component.calendar.calendar import Calendar

component.registry.register(name="calendar", component=Calendar)
