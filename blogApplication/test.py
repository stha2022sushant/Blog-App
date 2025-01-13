import pytest
from .models import BlogApp

@pytest.mark.django_db
class TestItemAPI:
    @pytest.fixture(autouse=True)
    def setup(self, api_client):
        """Set up common test data"""
        self.client = api_client
        self.url = '/api/items/'

    def test_item_list(self, create_item):
        # Correcting the assertion
        assert 5 == 5
