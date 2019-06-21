"""
API for SI7021 humidity and temperature sensor.
"""

from smbus2 import SMBus
import time

 # TODO: test if sleeps are necessary

class Si7021Sensor:

    def __init__(self):
        self._bus = SMBus(1)
        self._address = 0x40
        
    def __del__(self):
        self._bus.close()

    def _send_command(self, command_code):
        self._bus.write_byte(self._address, command_code)
        time.sleep(0.3)

    def _read_data(self):
        data0 = self._bus.read_byte(self._address)
        data1 = self._bus.read_byte(self._address)
        time.sleep(0.3)
        return data0, data1

    def humidity(self):
        """
        :return: relative humidity in percent.
        """
        self._send_command(0xF5)
        data0, data1 = self._read_data()
        humidity = ((data0 * 256 + data1) * 125 / 65536.0) - 6
        return humidity

    def temperature(self):
        """
        :return: temperature in celsius degrees.
        """
        self._send_command(0xF3)
        data0, data1 = self._read_data()
        cels_temp = ((data0 * 256 + data1) * 175.72 / 65536.0) - 46.85
        return cels_temp
