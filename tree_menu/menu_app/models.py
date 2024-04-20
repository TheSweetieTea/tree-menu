from django.db import models


class MenuItem(models.Model):
    name = models.CharField(
        "название",
        help_text="Введите название меню",
        max_length=100
    )
    parent = models.ForeignKey(
        "self",
        related_name="children",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    url = models.CharField(
        max_length=200,
        help_text="Введите ссылку",
        null=True,
        blank=True,
    )
    named_url = models.CharField(
        max_length=200,
        help_text="Введите именованную ссылку",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.name
