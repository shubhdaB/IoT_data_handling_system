import unittest
import threading
import time
from mqtt_rabbitmq_integration import client
from message_processing import process_message
from mongodb_integration import collection
class TestIntegration(unittest.TestCase):
    def test_system_integration(self):
        sample_message = {"sensor_id":123, "value":45.6}
        def simulate_mqtt_message():
            client.on_message(client, None, sample_message)
        mqtt_thread = threading.Thread(target=simulate_mqtt_message)
        mqtt_thread.start()
        time.sleep(1)

        inserted_document = collection.find_one({"sensor_id":123})

        self.assertIsNotNone(inserted_document)
        self.assertEqual(inserted_document["value"], 45.6)
if __name__ = '__main__':
    unittest.main()