from flask_testing import TestCase
import json
from app import create_app
from config import Config



class BaseTestCase(TestCase):
    """ Base Tests """
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

        with self.app.app_context():
          

    # def tearDown(self):
    #     pass
