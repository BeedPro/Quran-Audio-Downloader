import unittest
from unittest.mock import MagicMock, patch

from requests import Response
from downloader.program import FailedToFetchURLException, get_links


class TestGetLinks(unittest.TestCase):
    def test_get_links_success(self):
        # Arrange
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = """
            <html>
            <body>
            <a href="https://example.com/page1">Link 1</a>
            <a href="https://example.com/page2">Link 2</a>
            </body>
            </html>
        """

        with patch("downloader.program.requests.get") as mock_get:
            mock_get.return_value = mock_response
            expected_links = ["https://example.com/page1", "https://example.com/page2"]

            # Act
            result = get_links("https://www.example_website.com")

            # Assert
            self.assertEqual(result, expected_links)

    def test_get_links_fail(self):
        # Arrange
        mock_response = MagicMock()
        mock_response.status_code = None

        with patch("downloader.program.requests.get") as mock_get:
            mock_get.return_value = mock_response

            # Act/Assert
            with self.assertRaises(FailedToFetchURLException):
                get_links("https://www.example.com")


if __name__ == "__main__":
    unittest.main()
