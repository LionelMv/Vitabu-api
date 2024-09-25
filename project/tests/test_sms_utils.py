from unittest import TestCase, mock
from ..utils.sms_utils import send_sms_alert

class SendSmsAlertTestCase(TestCase):

    @mock.patch('project.utils.sms_utils.sms.send')  # Mock the sms.send method
    def test_send_sms_alert_success(self, mock_send):
        """Test that SMS is sent successfully"""
        # Arrange: Set up the mock response to simulate a successful send
        mock_send.return_value = {"status": "success"}

        # Act: Call the function
        response = send_sms_alert("+1234567890", "Test message")

        # Assert: Verify that the send method was called with the correct arguments
        mock_send.assert_called_once_with("Test message", ["+1234567890"])
        self.assertEqual(response, {"status": "success"})

    @mock.patch('project.utils.sms_utils.sms.send')  # Mock the sms.send method
    def test_send_sms_alert_failure(self, mock_send):
        """Test handling of SMS sending failure"""
        # Arrange: Simulate an exception when sending SMS
        mock_send.side_effect = Exception("Network error")

        # Act: Call the function
        response = send_sms_alert("+1234567890", "Test message")

        # Assert: Check that the response is None due to the exception
        mock_send.assert_called_once_with("Test message", ["+1234567890"])
        self.assertIsNone(response)
