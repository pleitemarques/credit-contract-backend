from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created at"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated at"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Is active?"
    )

    class Meta:
        abstract = True
        ordering = ["-created_at"]

    def __str__(self):
        return str(self.pk)