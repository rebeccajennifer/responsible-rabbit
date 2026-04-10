#_______________________________________________________________________
#_______________________________________________________________________
#        _   __   _   _ _   _   _   _         _
#   |   |_| | _  | | | V | | | | / |_/ |_| | /
#   |__ | | |__| |_| |   | |_| | \ |   | | | \_
#    _  _         _ ___  _       _ ___   _                    / /
#   /  | | |\ |  \   |  | / | | /   |   \                    (^^)
#   \_ |_| | \| _/   |  | \ |_| \_  |  _/                    (____)o
#_______________________________________________________________________
#_______________________________________________________________________
#
#-----------------------------------------------------------------------
#   Copyright 2025, Rebecca Rashkin
#   -------------------------------
#   This code may be copied, redistributed, transformed, or built
#   upon in any format for educational, non-commercial purposes.
#
#   Please give me appropriate credit should you choose to use this
#   resource. Thank you :)
#-----------------------------------------------------------------------
#
#_______________________________________________________________________
#   //\^.^/\\  //\^.^/\\  //\^.^/\\  //\^.^/\\  //\^.^/\\  //\^.^/\\
#_______________________________________________________________________
#   DESCRIPTION
#   String utility functions.
#_______________________________________________________________________

from .error_utils import ErrorUtils


#_______________________________________________________________________
class StringUtils:

  #_____________________________________________________________________
  def int_to_hex6(n: int) -> str:
    """
    Converts an integer to a 6-digit hex string.

    Parameters
      n : integer to convert

    Returns
      6-digit hex string representation of the input integer.
      e.g.
      255      -> '0000ff'
      16777215 -> 'ffffff'
      0        -> '000000'
      16777216 -> '01000000' (not 6 digits, but 8)
    """
    return f'{n:06x}'

  #_____________________________________________________________________
  def str_hex_to_int(s: str) -> int:
    """
    Parameter
      s : hex integer represented as a string

    Returns
      int represented by the input string
    """

    try:
      if (isinstance(s, str)):
        return int(s, base=16)

    except Exception as error:
      err_msg: str =\
        f'{ErrorUtils.ERROR_TYPE}'\
        f'{type(error).__name__}'\
        f'{ErrorUtils.DESC}'\
        f'{ErrorUtils.CONVERSION_ERROR}'\
        f'{ErrorUtils.LINE}'\

      raise ValueError(err_msg)

  #_____________________________________________________________________
  def bool_to_str(flag: bool, capitalize: bool = False) -> str:
    """
    Prints Boolean string.

    Parameters
      flag        : Boolean to print
      capitalize  : Capitalize first letter
    """

    out_str: str = ''

    if (flag):
      out_str = 'true'
    else:
      out_str = 'false'

    if (capitalize):
      out_str = f'{out_str[0].upper()}{out_str[1:len(out_str)]}'

    return out_str

  #_____________________________________________________________________
  def str_to_bool(s: str) -> bool:
    """
    Returns boolean corresponding with input string. Will return true
    if string is any capitalization of the word 'true'.

    Parameters
      s : any string, assumption s = {'true', 'True', 'false', 'False'}

    Returns
      bool corresponding to input string
    """

    lowercase: str = s.lower()

    return lowercase == 'true' or lowercase == 't'

