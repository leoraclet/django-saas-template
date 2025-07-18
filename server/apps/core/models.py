from django.db import models

# ==============================================================================
# COMMON MODELS
# ==============================================================================


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# ==============================================================================
# TEST MODELS
# ==============================================================================


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateField()

    class Meta:
        db_table = "books"
        verbose_name_plural = "books"

    def __str__(self):
        return self.title
