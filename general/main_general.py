from general_core import IntegerChecker,CountDays,Month1to13,XList


def integerchecker(x):
  return IntegerChecker(x)

def countdays(year,month):
  return CountDays(year,month)

def month1to13(month):
  return Month1to13(month)

def xlist(interval=1):
  return XList(sep=interval)
