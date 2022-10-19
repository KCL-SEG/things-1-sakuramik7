from django.test import TestCase
from things.models import Thing
from django.core.exceptions import ValidationError

class testing_model(TestCase):
    def set_up(self):
        self.thing = Thing(
        name = "Jjj",
        description = "Hi I am JJJ",
        quantity = 100,
        )

    def test_number(self):
        self.quantity= 101
        self.not_working()

    def should_work(self):
        try:
            self.thing.full_clean()
        except(ValidationError):
            self.fail("This should work")

    def not_working(self):
        with self.assertRaises(ValidationError):
            self.thing.full_clean()

# Create your tests here.
