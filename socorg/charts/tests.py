from sqlite3 import IntegrityError
from django.urls import reverse
from django.test import TestCase, Client


from .models import Chart, Persona


def create_chart(chart_name):
    c = Chart(chart_name=chart_name)
    c.save()
    return c


def create_persona(name, surname, chart, is_ego=False, step=0):
    if chart:
        p = Persona(name=name, surname=surname, is_ego=is_ego, step=step, chart=chart)
    else:
        c = Chart()
        c.save()
        p = Persona(
            name=name, surname=surname, is_ego=is_ego, step=step, chart=c.chart_name
        )
    p.save()
    return p


# Create your tests here.
class ChartModelTests(TestCase):
    def test_only_one_ego_per_chart(self):
        """Test if there can only be one ego per Chart."""
        test_chart = create_chart("Testchart")
        ego = create_persona(
            name="Ego", surname="Surego", is_ego=True, step=0, chart=test_chart
        )
        try:
            second_ego = create_persona(
                name="Normalo", surname="Nolo", is_ego=True, step=0, chart=test_chart
            )
        except:
            self.assertRaises(
                IntegrityError,
            )


class CreateEgoTests(TestCase):
    def test_creation_of_chart_when_creating_ego(self):
        """test if the creation of an ego via the create_ego view correctly creates a chart and assigns the ego to it"""
        data = {"name": "Createdego", "surname": "EGON"}
        url = reverse("create_ego")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Persona.objects.count(), 1)
        ego = Persona.objects.filter(name="Createdego").first()
        chart = (
            Chart.objects.all()
            .get()
            .persona_set.filter(is_ego=True)
            .get()
            .chart.chart_name
        )
        self.assertEqual(ego.name, "Createdego")
        self.assertEqual(ego.surname, "EGON")
        self.assertEqual(ego.chart.chart_name, chart)
