
from app import app
from flask import request
import unittest
import json

from models import content


class BasicTestCase(unittest.TestCase):
    def setUp(self):
        content.clear()
    def test_get_all(self):
        tester = app.test_client(self)
        response = tester.get('/api/v1/entries', content_type='application/json')
        self.assertEqual(response.status_code, 200)
    def test_post(self):
        tester = app.test_client(self)
        data = json.dumps({
			"title":" Article one",
			"description":"This represents the body of the first article",
			"date":"04-25-2018"})
        response = tester.post(
            '/api/v1/entries', data=data,
            content_type='application/json'
            )
        self.assertIn(json.loads(response.data)['message'], "successful")
    def test_get_one(self):
        tester = app.test_client(self)
        data = json.dumps({
			"title":" Article one",
			"description":"This represents the body of the first article",
			"date":"04-25-2018"})
        res1 = tester.post(
            '/api/v1/entries', data=data,
            content_type='application/json'
            )

        response = tester.get('/api/v1/entries/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)
    def test_update(self):
        tester = app.test_client(self)
        data = json.dumps({
			"title":" Article one",
			"description":"This represents the body of the first article",
			"date":"04-25-2018"})
        res1 = tester.post(
            '/api/v1/entries', data=data,
            content_type='application/json'
            )
        id =  json.loads(res1.data)['entry']['id']
        put_data = json.dumps({"title":"football", "description":"FINAL FRANCE WON"})
        response = tester.put("/api/v1/entries/" + str(id),  data=put_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
    def test_del(self):
        tester = app.test_client(self)
        data = json.dumps({
			"title":" Article one",
			"description":"This represents the body of the first article",
			"date":"04-25-2018"})
        res1 = tester.post(
            '/api/v1/entries', data=data,
            content_type='application/json'
            )
        response = tester.delete('/api/v1/entries/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        


if __name__ == '__main__':
    unittest.main()