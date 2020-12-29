import pytest
from django.test import RequestFactory

from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db