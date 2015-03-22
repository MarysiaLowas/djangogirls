# encoding: utf-8

from django.test import TestCase
from django.core.urlresolvers import reverse

from jobs.models import Job


class JobCreateTests(TestCase):

    def setUp(self):
        self.context = {
            'company': 'My Company',
            'website': 'http://mycompany.com',
            'contact_email': 'jobs@company.com',
            'title': 'Job offer',
            'description': 'description',
            'city': u'Kraków',
            'country': 'PL',
            'save': True,
        }

    def test_job_add_new_company_clean(self):
        """Tests adding a new job with a new company"""
        context = self.context
        context['company'] = 'New Company'
        context['website'] = 'http://newcompany.com'
        response = self.client.post(reverse('jobs:job_new'), context)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Job.objects.get(company="New Company", title="Job offer")
        )


class MainPageTests(TestCase):

    def test_main_page_with_empty_database(self):
        response = self.client.get(reverse('jobs:main'))
        self.assertEqual(response.status_code, 200)
        self.assertIn("No job offers yet", response.content)
        self.assertIn("No meetups yet", response.content)