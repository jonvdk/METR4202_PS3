from enum import Enum

class MicromelonOpCode(Enum):
  READ = 0
  WRITE = 1
  ACK = 2
  NOTIFY = 3
  ERROR_INVALID_OP_CODE = 4
  ERROR_INVALID_PAYLOAD_SIZE = 5
  ERROR_INVALID_CHECKSUM = 6
  ERROR_NOT_IMPLEMENTED = 7

class MicromelonType(Enum):
  # Actuators
  MOTOR_SET = 0
  MOTOR_ENCODERS = 1
  MOTOR_SPEEDS = 2
  RGBS = 3
  SERVO_MOTORS = 4
  BUZZER_TUNE = 5
  BUZZER_FREQ = 6

  # Sensors
  ACCL = 7
  GYRO = 8
  COLOUR_RGBW = 9
  COLOUR_HUE = 10
  COLOUR_ALL = 11
  TIME_OF_FLIGHT = 12
  ULTRASONIC = 13
  ROBOT_NAME = 14
  I2C_HEADER = 15

  # Versions
  HW_VERSION = 16
  FW_VERSION = 17

  # Util
  BUTTON_PRESS = 18
  BATTERY_VOLTAGE = 19
  STATE_OF_CHARGE = 20
  CURRENT_SENSOR = 21
  USB_VOLTAGE = 22

  # Advanced Util
  SENSOR_ERRORS = 23
  ENTER_OTA = 24
  CONFIG = 25
  CONTROL_MODE = 26

  ALL_SENSORS = 27
  MIN_SW_VERSION = 28

  MOTOR_TACHO = 29

  SPAM_MODE = 30
  SPAM_RATE = 31

  BOTID = 32

  RPI_IMAGE = 150
  NETWORK_KEEP_ALIVE = 151

class MicromelonImageResolution(Enum):
  R320x240 = 1
  R640x480 = 2
  R1280x720 = 3
  R1920x1088 = 4

def tupleForResolution(res):
  if not isinstance(res, MicromelonImageResolution):
    res = MicromelonImageResolution(res)
  if res == MicromelonImageResolution.R320x240:
    return (320, 240)
  if res == MicromelonImageResolution.R640x480:
    return (640, 480)
  if res == MicromelonImageResolution.R1280x720:
    return (1280, 720)
  if res == MicromelonImageResolution.R1920x1088:
    return (1920, 1088)
  return (320, 240)
