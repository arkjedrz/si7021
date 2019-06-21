import unittest
import si7021

class Si7021SensorTests(unittest.TestCase):

    def setUp(self):
        # TODO: checks for Windows, but should check for embedded platform
        import os
        if os.name == 'Windows':
            raise OSError
        self._sensor = si7021.Si7021Sensor()
    
    def _assert_in_range(self, action, param_name, min, max):
        value = action()
        self.assertGreaterEqual(value, min, f'{param_name} must be greater or equal to {min}.')
        self.assertLessEqual(value, max, f'{param_name} must be less or equal to {max}.')

    def test_read_humidity(self):
        self._assert_in_range(self._sensor.humidity, 'Humidity', 0, 80)

    def test_read_temperature(self):
        self._assert_in_range(self._sensor.temperature, 'Temperature', -10, 85)

if __name__ == '__main__':
    unittest.main()