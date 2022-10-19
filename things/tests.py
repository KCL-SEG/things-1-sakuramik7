from django.test import TestCase
from .models import Thing
from django.core.exceptions import ValidationError

class model(TestCase):
    def test_number(self):
        self.user = Thing.objects.create(
        name = "Jjj",
        description="Hi I am JJJ",
        quantity=101,
        )
        with self.assertRaises(ValidationError):
            self.user.full_clean()

# Create your tests here.
