#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test class for access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test access_nested_map function with valid paths.
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test access_nested_map raises KeyError for invalid paths.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), repr(path))


class TestGetJson(unittest.TestCase):
    """
    Test class for get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test that get_json returns expected result from mock.
        """
        mock_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Test class for memoize decorator.
    """

    def test_memoize(self):
        """
        Test memoization behavior.
        """
        class TestClass:
            """
            A simple test class to demonstrate memoization.
            """

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_instance = TestClass()
        with patch.object(test_instance, 'a_method') as mock_method:
            mock_method.return_value = 42
            result_first_call = test_instance.a_property()
            result_second_call = test_instance.a_property()

            self.assertEqual(result_first_call, 42)
            self.assertEqual(result_second_call, 42)
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
