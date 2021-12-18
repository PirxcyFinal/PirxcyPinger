class PingerException(Exception):
  pass

class InvalidPermission(Exception):
  pass

class InvalidPlatform(Exception):
  pass

class AlreadyPinging(PingerException):
  pass

class InvalidURL(PingerException):
  pass
