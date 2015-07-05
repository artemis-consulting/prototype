from mock import patch, MagicMock
from django.test import Client, TestCase


class BasicViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_homepage(self):
        resp = self.client.get('/', follow=True)
        self.assertEquals(resp.status_code, 200)

    @patch("core.api_client.ApiClient")
    def test_browse_events(self, mock_client):
        resp = self.client.get('/browse/events', follow=True)
        self.assertEquals(resp.status_code, 200)

    @patch("core.api_client.ApiClient")
    def test_browse_labels(self, mock_client):
        resp = self.client.get('/browse/labels', follow=True)
        self.assertEquals(resp.status_code, 200)

    @patch("core.api_client.ApiClient")
    def test_browse_enforcements(self, mock_client):
        resp = self.client.get('/browse/enforcements', follow=True)
        self.assertEquals(resp.status_code, 200)

    @patch("core.api_client.ApiClient")
    def test_search_labels(self, mock_client):
        resp = self.client.get('/search/labels?q=test', follow=True)
        self.assertEquals(resp.status_code, 200)

    @patch("core.api_client.ApiClient")
    def test_search_events(self, mock_client):
        resp = self.client.get('/search/events?q=test', follow=True)
        self.assertEquals(resp.status_code, 200)

    @patch("core.api_client.ApiClient")
    def test_search_enforcements(self, mock_client):
        resp = self.client.get('/search/enforcements?q=test', follow=True)
        self.assertEquals(resp.status_code, 200)

    @patch("core.api_client.ApiClient")
    def test_search_manufacturers(self, mock_client):
        resp = self.client.get('/search/manufacturers?q=test', follow=True)
        self.assertEquals(resp.status_code, 200)

    # TODO: get around pickling error for mock objects
    @patch("core.api_client.ApiClient.get_age_sex")
    def xtest_search_detail(self, mock_client_method):
        mock_client_method.return_value = mock_response = MagicMock()
        mock_response.return_value = {}
        self.client.get('/search_detail?q=test&browse_type=events&filter_string=aspirin',
                        follow=True)

    def test_contact(self):
        response = self.client.post('/contact/', {'contact_comment': 'comment',
                                                  'contact_name': 'name',
                                                  'contact_email': 'email@email.com'})
        self.assertEquals(response.status_code, 302)

        response = self.client.get('/contact', follow=True)
        self.assertEquals(response.status_code, 200)

        response = self.client.post('/contact/', {})
        self.assertEquals(response.status_code, 200)
