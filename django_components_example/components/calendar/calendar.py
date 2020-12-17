from django_components import component


class Calendar(component.Component):
    def context(self, date):
        return {
            "date": date,
        }

    def template(self, context):
        return "django_components_example/components/calendar/calendar.html"

    class Media:
        css = {'all': ['django_components_example/components/calendar/calendar.css']}
        js = ['django_components_example/components/calendar/calendar.js']


component.registry.register(name="calendar", component=Calendar)
