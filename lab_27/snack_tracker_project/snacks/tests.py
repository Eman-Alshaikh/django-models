import imp
from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class TestSnack(TestCase):
    # 1- test the status response code 
    def test_status_code(self):
        url=reverse('snacks_list')

        response=self.client.get(url)

        self.assertEqual(response.status_code,200)


    # 2- test the template if they inherit from the right base 

    def test_template(self):

        url=reverse('snacks_list')

        response=self.client.get(url)

        self.assertTemplateUsed(response,'snacks_list.html')
        self.assertTemplateUsed(response,'_base.html')


    def test_detail_view(self):

        url=reverse('snack_detail',args='(1,)')

        response=self.client.get(url)

        self.assertTemplateUsed(response,'snack_detail.html')
        self.assertTemplateUsed(response,'_base.html')



