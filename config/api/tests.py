from django.test import TestCase
from django.urls import resolve
import requests
from .views import SuperMarketViewSet
from api.models import SuperMarket
# Create your tests here.



class ApiTests(TestCase):
    fixtures = ["fixtures.json"]

    def test_get_api(self):
        response = self.client.get('/api/market/')
        view = resolve('/api/market/')
        print(response.content)
        self.assertEquals(response.status_code, 200)
        market = SuperMarket.objects.get(name="Simran")
        self.assertEqual(market.name, "Simran")

    def test_post_api(self):
        url = '/api/market/'
        data = {
            "id": 2,
            "name": "SimranThakur",
            "product": "Craft Maerial",
            "price": 2140
        }
        response = self.client.post(url, data=data)
        print(response.content)
        market = SuperMarket.objects.get(id=2)
        self.assertEquals(response.status_code, 201)
        self.assertEqual(market.name, "SimranThakur")

    def test_put_api(self):
        market = SuperMarket.objects.get(id=1)
        url = '/api/market/' + str(market.id) + '/'
        d = {
            "name": "Sim",
            "product": "Craft Material",
            "price": 2140
        }
        response = self.client.put(url, data=d, content_type='application/json')
        print(response.content)
        self.assertEquals(response.status_code, 200)

    def test_delete_api(self):
        market = SuperMarket.objects.get(id=1)  
        url = '/api/market/' + str(market.id) + '/'
        d = {
            "name": "Simran",
            "product": "Craft",
            "price": 500
        }
        response = self.client.delete(url, data=d)
        print(response.content) 
        self.assertEquals(response.status_code, 204)

    def test_patch_api(self):
        market = SuperMarket.objects.get(id=1)  
        url = '/api/market/' + str(market.id) + '/'
        d = {
            "name": "Simran S",
            "product": "Craft",
            "price": 500
        }
        response = self.client.patch(url, data=d, content_type='application/json')
        print(response.content) 
        self.assertEquals(response.status_code, 200)


