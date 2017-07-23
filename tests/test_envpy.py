"""Unit tests for envpy"""

import unittest

import envpy


class TestEnvpy(unittest.TestCase):
    def test_get_basic_strings(self):
        """Should be able to get strings from the environment (no parsing)"""
        config_schema = {
            'SECRET_KEY': envpy.Schema(value_type=str),
        }
        env = {
            'SECRET_KEY': 'my_secret_key',
        }
        config = envpy.get_config(config_schema, env)

        expected_value = 'my_secret_key'
        actual_value = config.get('SECRET_KEY')

        self.assertEqual(expected_value, actual_value)

    def test_throw_missing_error(self):
        """Should throw an error if the key cannot be found in the
        environment and no default is set.
        """
        config_schema = {
            'SECRET_KEY': envpy.Schema(value_type=str),
        }
        env = {}

        with self.assertRaises(envpy.MissingConfigError):
            envpy.get_config(config_schema, env)

    def test_take_default(self):
        """Should return the default value if set and the key cannot be found
        in the environment.
        """
        config_schema = {
            'SECRET_KEY': envpy.Schema(value_type=str, default="base_secret"),
        }
        env = {}
        config = envpy.get_config(config_schema, env)

        expected_value = 'base_secret'
        actual_value = config.get('SECRET_KEY')

        self.assertEqual(expected_value, actual_value)

    def test_unknown_value_type(self):
        """Should throw an error if the value type has no registered parser"""
        with self.assertRaises(envpy.ValueTypeError):
            envpy.Schema(value_type=object())

    def test_parse_error(self):
        """Should throw an error if the value cannot be parsed as the given
        value type.
        """
        config_schema = {
            'SECRET_NUMBER': envpy.Schema(value_type=int),
        }
        env = {
            'SECRET_NUMBER': 'abc'
        }
        with self.assertRaises(envpy.ParsingError):
            config = envpy.get_config(config_schema, env)

    def test_parse_int(self):
        """Should correctly parse integers"""
        config_schema = {
            'SECRET_NUMBER': envpy.Schema(value_type=int),
        }
        env = {
            'SECRET_NUMBER': '12'
        }
        config = envpy.get_config(config_schema, env)

        expected_value = 12
        actual_value = config.get('SECRET_NUMBER')

        self.assertEqual(expected_value, actual_value)

    def test_parse_float(self):
        """Should correctly parse floats"""
        config_schema = {
            'SECRET_NUMBER': envpy.Schema(value_type=float),
        }
        env = {
            'SECRET_NUMBER': '1.2'
        }
        config = envpy.get_config(config_schema, env)

        expected_value = 1.2
        actual_value = config.get('SECRET_NUMBER')

        self.assertEqual(expected_value, actual_value)

    def test_parse_bool(self):
        """Should correctly parse booleans"""
        config_schema = {
            'SECRET_BOOL': envpy.Schema(value_type=bool),
        }
        test_cases = [
            {
                'env': {
                    'SECRET_BOOL': 'true'
                },
                'expected_value': True,
            },
            {
                'env': {
                    'SECRET_BOOL': 'false'
                },
                'expected_value': False,
            },
            {
                'env': {
                    'SECRET_BOOL': 'True'
                },
                'expected_value': True,
            },
            {
                'env': {
                    'SECRET_BOOL': 'False'
                },
                'expected_value': False,
            },
            {
                'env': {
                    'SECRET_BOOL': 'TRUE'
                },
                'expected_value': True,
            },
            {
                'env': {
                    'SECRET_BOOL': 'FALSE'
                },
                'expected_value': False,
            },
            {
                'env': {
                    'SECRET_BOOL': '1'
                },
                'expected_value': True,
            },
            {
                'env': {
                    'SECRET_BOOL': '0'
                },
                'expected_value': False,
            },
        ]

        for test_case in test_cases:
            config = envpy.get_config(config_schema, test_case['env'])

            expected_value = test_case['expected_value']
            actual_value = config.get('SECRET_BOOL')

            self.assertEqual(expected_value, actual_value)
