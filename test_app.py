
from app import app

import unittest
import json


class BasicTestCase(unittest.TestCase):

#test for get all entries
    def test_get_all(self):
        tester = app.test_client(self)
        response = tester.get('/api/v1/entries', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        tester = app.test_client(self)
        data = json.dumps({
            "id": 1,
			"title":" Article one",
			"body":"This represents the body of the first article",
			"create_date":"04-25-2018"})
        response = tester.post(
            '/api/v1/entries', data=data,
            content_type='application/json'
            )
        self.assertEqual(response.message, 201)



 #test for deleting an entry
    def test_del(self):

        tester = app.test_client(self)
        data = {"id":0, "title":"football", "description":"FINAL FRANCE WON"}
        response = tester.delete('/api/v1/entries/0', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

#test for get one entry
    def test_get_one(self):
        tester = app.test_client(self)
        response = tester.get('/api/v1/entries/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)
    #
    def test_update(self):
        tester = app.test_client(self)
        data = {"id":0, "title":"football", "description":"FINAL FRANCE WON"}
        response = tester.post("/api/v1/entries",  data=data, content_type="html/text")
        self.assertEqual(response.status_code, 200)

        


if __name__ == '__main__':
    unittest.main()