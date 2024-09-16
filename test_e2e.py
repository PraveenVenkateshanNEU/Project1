import unittest
import subprocess
import time
# import requests
from client import InventoryClient

class TestEndToEnd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Start the Flask server
        cls.server_process = subprocess.Popen(['python', 'server.py'])
        # Give the server a moment to start up
        time.sleep(5)
        cls.client = InventoryClient("http://localhost:5000")

    @classmethod
    def tearDownClass(cls):
        # Stop the Flask server
        cls.server_process.terminate()
        cls.server_process.wait()

    def test_define_and_manage_inventory(self):
        # Define a new item
        response = self.client.define_stuff("widget", "A useful widget")
        self.assertEqual(response, {'message': 'Defined type \'widget\' with description \'A useful widget\'.'})

        # Add items
        response = self.client.add(10, "widget")
        self.assertEqual(response, {'message': 'Added 10 of type \'widget\'.'})

        # Test case 1
        # Check count after adding items
        # Verifies the count after adding items.
        count = self.client.get_count("widget")
        self.assertEqual(count, {'type': 'widget', 'count': 10})

        # Remove items
        response = self.client.remove(5, "widget")
        self.assertEqual(response, {'message': 'Removed 5 of type \'widget\'.'})

        # Test case 2
        # Check count after removing items
        # Verifies the count after removing items.
        count = self.client.get_count("widget")
        self.assertEqual(count, {'type': 'widget', 'count': 5})

        # Undefine the item
        response = self.client.undefine("widget")
        self.assertEqual(response, {'message': 'Undefined type \'widget\'.'})

        # Test case 3
        # Check count for undefined item
        # Checks the count when the quantity is undefined.
        count = self.client.get_count("widget")
        self.assertEqual(count, {'message': "Type 'widget' does not exist."})

if __name__ == '__main__':
    unittest.main()

