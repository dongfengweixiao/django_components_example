from django_components import component


class Calendar(component.Component):

    def context(self, date):
        return {
            "date": date,
        }

    def template(self, context):
        return "calendar/calendar.html"

    class Media:
        css = {'all': ['calendar/calendar.css']}
        js = ['calendar/calendar.js']
