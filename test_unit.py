import unittest
from unittest.mock import MagicMock
from message_processing import process_message, save_to_mongodb
class TestmessageProcessing(unittest.TestCase)
    def test_process_message_saves_to_mongodb(self):
        sample_message = {"sensor_id": 123, "value": 45.6}
        save_to_mongodb_mock = MagicMock()
        process_message(sample_message)

        save_to_mongodb_mock.assert_called_once_with(sample_message)
    def test_process_message_handle_invalid_message(self):
        invalid_message = {"value": 45.6}

        self.assertRaises(Exception, process_message, invalid_message)


if __name__ == '__main__':
    unittest.main()