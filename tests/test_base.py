from flask_testing import TestCase
from flask import current_app,url_for

from main import app

class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app
    
    def test_app_exist(self):
        self.assertIsNotNone(current_app)
        
    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])
        
    #Probar que la aplicacion redirija a hello
    def test_index_redifects(self):
        response=self.client.get(url_for('index'))
        self.assertRedirects(response,url_for('hello'))

    #probar que la aplicacion responde a hello con un get
    def test_hello_get(self):
        response=self.client.get(url_for('hello'))
        self.assert200(response)
        
    #probar que la aplicacion responde a hello con un post
    def test_hello_post(self):
        response=self.client.post(url_for('hello'),data=dict(username='juan',password='123'))
        self.assertRedirects(response,url_for('index'))