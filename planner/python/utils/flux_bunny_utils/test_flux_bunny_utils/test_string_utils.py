#______________________________________________________________________
#______________________________________________________________________
#        _   __   _   _ _   _   _   _         _
#   |   |_| | _  | | | V | | | | / |_/ |_| | /
#   |__ | | |__| |_| |   | |_| | \ |   | | | \_
#    _  _         _ ___  _       _ ___   _                    / /
#   /  | | |\ |  \   |  | / | | /   |   \                    (^^)
#   \_ |_| | \| _/   |  | \ |_| \_  |  _/                    (____)o
#______________________________________________________________________
#______________________________________________________________________
#
#----------------------------------------------------------------------
#   Copyright 2025, Rebecca Rashkin
#   -------------------------------
#   This code may be copied, redistributed, transformed, or built
#   upon in any format for educational, non-commercial purposes.
#
#   Please give me appropriate credit should you choose to use this
#   resource. Thank you :)
#----------------------------------------------------------------------
#
#______________________________________________________________________
#   //\^.^/\\  //\^.^/\\  //\^.^/\\  //\^.^/\\  //\^.^/\\  //\^.^/\\
#______________________________________________________________________
#   DESCRIPTION
#   Tests for string utility functions.
#______________________________________________________________________

import pytest

from utils.flux_bunny_utils.string_utils import StringUtils


#_______________________________________________________________________
class TestConst:
  """
  Contains constants used in tests.
  """

  ALL_CAPS_2_CHAR_WITH_0X: str = '0XFF'
  MIX_CAPS_2_CHAR_WITH_0X: str = '0xFf'
  ALL_CAPS_6_CHAR_WITH_0X: str = '0XFFFFFF'
  MIX_CAPS_6_CHAR_WITH_0X: str = '0xFfFFff'

  ALL_CAPS_2_CHAR_NO_PRFX: str = 'FF'
  MIX_CAPS_2_CHAR_NO_PRFX: str = 'fF'
  ALL_CAPS_6_CHAR_NO_PRFX: str = 'FFFFFF'
  MIX_CAPS_6_CHAR_NO_PRFX: str = 'fFfFFf'

  ERR_VAL_WITH_0X: str = '0x5g'

  INT_2_CHAR: int = 255
  INT_6_CHAR: int = 16777215

  ERR_VAL: int = -1

#_______________________________________________________________________
def test_str_hex2int_all_caps_with_0x():
  assert(
    StringUtils.str_hex_to_int(TestConst.ALL_CAPS_2_CHAR_WITH_0X) ==\
    TestConst.INT_2_CHAR
  )
  assert(
    StringUtils.str_hex_to_int(TestConst.ALL_CAPS_6_CHAR_WITH_0X) ==\
    TestConst.INT_6_CHAR
  )

def test_str_hex2int_mix_caps_with_0x():
  assert(
    StringUtils.str_hex_to_int(TestConst.MIX_CAPS_2_CHAR_WITH_0X) ==\
    TestConst.INT_2_CHAR
  )
  assert(
    StringUtils.str_hex_to_int(TestConst.MIX_CAPS_6_CHAR_WITH_0X) ==\
    TestConst.INT_6_CHAR
  )

def test_str_hex2int_all_caps_no_prfx():
  assert(
    StringUtils.str_hex_to_int(TestConst.ALL_CAPS_2_CHAR_NO_PRFX) ==\
    TestConst.INT_2_CHAR
  )
  assert(
    StringUtils.str_hex_to_int(TestConst.ALL_CAPS_6_CHAR_NO_PRFX) ==\
    TestConst.INT_6_CHAR
  )

def test_str_hex2int_mix_caps_no_prfx():
  assert(
    StringUtils.str_hex_to_int(TestConst.MIX_CAPS_2_CHAR_NO_PRFX) ==\
    TestConst.INT_2_CHAR
  )
  assert(
    StringUtils.str_hex_to_int(TestConst.MIX_CAPS_6_CHAR_NO_PRFX) ==\
    TestConst.INT_6_CHAR
  )

#_______________________________________________________________________
def test_str_hex2int_err():
  with pytest.raises(Exception):
    StringUtils.str_hex_to_int(TestConst.ERR_VAL_WITH_0X)

#_______________________________________________________________________
def test_bool_to_str():
  assert(StringUtils.bool_to_str(True) == 'true')
  assert(StringUtils.bool_to_str(False) == 'false')
  assert(StringUtils.bool_to_str(True, capitalize=True) == 'True')
  assert(StringUtils.bool_to_str(False, capitalize=True) == 'False')

  assert(StringUtils.bool_to_str(1) == 'true')
  assert(StringUtils.bool_to_str(0) == 'false')
  assert(StringUtils.bool_to_str(1, capitalize=True) == 'True')
  assert(StringUtils.bool_to_str(0, capitalize=True) == 'False')

  assert(StringUtils.bool_to_str(-1) == 'true')
  assert(StringUtils.bool_to_str(42) == 'true')
  assert(StringUtils.bool_to_str('foo', capitalize=True) == 'True')

#_______________________________________________________________________
def test_str_to_bool():
  assert(StringUtils.str_to_bool('true') == True)
  assert(StringUtils.str_to_bool('True') == True)
  assert(StringUtils.str_to_bool('false') == False)
  assert(StringUtils.str_to_bool('False') == False)
  assert(StringUtils.str_to_bool('TRUE') == True)
  assert(StringUtils.str_to_bool('FALSE') == False)
  assert(StringUtils.str_to_bool('TrUe') == True)
  assert(StringUtils.str_to_bool('fAlSe') == False)
  assert(StringUtils.str_to_bool('fAlSe') == False)
  assert(StringUtils.str_to_bool('foo') == False)