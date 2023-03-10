from django.db import models
from django.core.exceptions import ValidationError
from django.utils.crypto import get_random_string

# Create your models here.
class Chart(models.Model):
    chart_name = models.CharField(
        max_length=200,
        unique=True,
        default=get_random_string(
            length=10, allowed_chars="abcdefghijklmnopqrstuvwxyz"
        ),
    )

    def __str__(self):
        return f"{self.id}, {self.chart_name}"


class Persona(models.Model):
    chart = models.ForeignKey(Chart, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    is_ego = models.BooleanField(default=False)
    step = models.IntegerField(default=0)
    bio_father = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children_bio_father",
    )
    bio_mother = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children_bio_mother",
    )
    non_bio_fathers = models.ManyToManyField(
        "self", blank=True, related_name="children_non_bio_father"
    )
    non_bio_mothers = models.ManyToManyField(
        "self", blank=True, related_name="children_non_bio_mother"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["chart"],
                condition=models.Q(is_ego=True),
                name="unique_ego_per_chart",
            )
        ]

    """def clean(self):
        if (
            self.is_ego
            and Persona.objects.filter(chart=self.chart, is_ego=True)
            .exclude(id=self.id)
            .exists()
        ):
            raise ValidationError("There can only be one Ego per Chart.")
    """

    def __str__(self):
        return f"id:{self.id}, {self.name}, {self.surname}, Ego: {self.is_ego}, Chart: {self.chart.chart_name}"
