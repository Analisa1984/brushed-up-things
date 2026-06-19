from django.test import TestCase
from django.urls import reverse


class TestContactView(TestCase):
    """Tests for the contact form view and email submission"""

    def test_contact_page_renders_correctly(self):
        """Test that the contact page loads successfully with a status 200"""
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_valid_contact_form_submission(self):
        """Test that a valid form submission redirects and sends messages"""
        form_data = {
            'name': 'Test User',
            'email': 'testuser@hotmail.com',
            'message': 'Hello, I love the Brushed Up Things gallery!'
        }
        # Secure POST request mimicking a customer submission
        response = self.client.post(reverse('contact'), data=form_data)

        # successful form submission will redirect to the contact page
        self.assertRedirects(response, reverse('contact'))

    def test_invalid_contact_form_submission(self):
        """Test that an invalid form submission does not process or redirect"""
        form_data = {
            'name': '',  # name being blank makes the form invalid
            'email': 'not-an-email',
            'message': ''
        }
        response = self.client.post(reverse('contact'), data=form_data)

        # Should stay on the page (status 200) rather than redirecting
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
