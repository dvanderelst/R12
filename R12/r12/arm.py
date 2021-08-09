
import glob
import serial
import time
import string
import sys

# Arm controller serial properties.
BAUD_RATE = 19200
PARITY = serial.PARITY_NONE
STOP_BITS = serial.STOPBITS_TWO
BYTE_SIZE = serial.EIGHTBITS

OUTPUT_ENCODING = 'latin_1'

# The read timeout is intentionally long, so that a complete calibration cycle
# can happen before timing out.
READ_TIMEOUT = 30
READ_SLEEP_TIME = 0.1

CMD_SUCCESS = 'OK'
CMD_ERROR = 'ABORTED'
RESPONSE_END_WORDS = [CMD_SUCCESS, CMD_ERROR]

# Assumption: Strings end with a keyword, followed only by ASCII
# whitespace and >, which is to be stripped off.
OUTPUT_STRIP_CHARS = string.whitespace + '>'


class ArmException(Exception):
    ''' Exception raised when things go wrong with the robot arm. '''
    pass


def r12_serial_port(port):
    ''' Create a serial connect to the arm. '''
    return serial.Serial(port, baudrate=BAUD_RATE, parity=PARITY,
                         stopbits=STOP_BITS, bytesize=BYTE_SIZE)




def ending_in(s, li):
    ''' If s ends with an element of the list li, that element will be
    returned. If multiple elements match, the first will be returned. If no
    elements match, returns None. '''
    for ending in li:
        if s.endswith(ending):
            return ending
    return None


class Arm(object):
    ''' Represents an ST Robotics arm. '''

    def __init__(self):
        self.ser = None
        self.port = None

    def connect(self, port):
        self.port = port
        self.ser = r12_serial_port(port)
        
        if not self.ser.isOpen():
            self.ser.open()

        if not self.ser.isOpen():
            raise ArmException('Failed to open serial port. Exiting.')

        return self.port


    def disconnect(self):
        ''' Disconnect from the arm. '''
        self.ser.close()
        self.ser = None
        self.port = None


    def write(self, text):
        ''' Write text out to the arm. '''
        # Output is converted to bytes with Windows-style line endings.
        if sys.version_info[0] == 2:
            text_bytes = str(text.upper() + '\r\n').encode('utf-8')
        else:
            text_bytes = bytes(text.upper() + '\r\n', 'utf-8')
        self.ser.write(text_bytes)


    def read(self, timeout=READ_TIMEOUT, raw=False):
        ''' Read data from the arm. Data is returned as a latin_1 encoded
            string, or raw bytes if 'raw' is True. '''
        time.sleep(READ_SLEEP_TIME)
        raw_out = self.ser.read(self.ser.in_waiting)
        out = raw_out.decode(OUTPUT_ENCODING)

        time_waiting = 0
        while len(out) == 0 or ending_in(out.strip(OUTPUT_STRIP_CHARS), RESPONSE_END_WORDS) is None:
            time.sleep(READ_SLEEP_TIME)
            time_waiting += READ_SLEEP_TIME

            part = self.ser.read(self.ser.in_waiting)
            raw_out = raw_out + part
            #print(part.decode(OUTPUT_ENCODING), end='')
            out = raw_out.decode(OUTPUT_ENCODING)

            # TODO how to handle timeouts, if they're now unexpected?
            if time_waiting >= timeout:
                break
        #print()
        if raw:
            return raw_out
        return out


    def dump(self, raw=False):
        ''' Dump all output currently in the arm's output queue. '''
        raw_out = self.ser.read(self.ser.in_waiting)
        if raw:
            return raw_out
        return raw_out.decode(OUTPUT_ENCODING)


    def is_connected(self):
        ''' True if the serial connection to arm is open. False otherwise. '''
        return self.ser.isOpen() if self.ser else False


    def get_info(self):
        ''' Returns status of the robot arm. '''
        return {
            'Connected': self.is_connected(),
            'Port': self.port,
            'Bytes Waiting': self.ser.in_waiting if self.ser else 0
        }

