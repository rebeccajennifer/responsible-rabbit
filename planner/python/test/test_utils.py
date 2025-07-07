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
#   Copyright 2024, Rebecca Rashkin
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
#   Tests for utility functions.
#_______________________________________________________________________

import pytest

from os.path import exists
from os.path import isdir
from os.path import isfile
from os.path import join
from os import mkdir
from os import makedirs
from os import remove

from shutil import rmtree

import datetime as dt

from utils.utils import PlannerUtils as Utils

class TestConst:
  """
  Constants used in tests.
  """

  TEST_DIR_NAME         : str = 'test_name'
  TEST_DIR_PARENT       : str = join('flux', 'bunny')
  TEST_DIR_FULL_PATH    : str = join(TEST_DIR_PARENT, TEST_DIR_NAME)

#_______________________________________________________________________
class Helper:
  """
  Helper functions for tests.
  """

  #_____________________________________________________________________
  def rm_test_dir(dir_path: str) -> None:
    """
    Removes test directory.

    Parameters:
      dir_path: Path to directory to remove.

    Side Effects:
      Removes test directory

    Returns:
      None
    """

    if isdir(dir_path):
      rmtree(dir_path)
    if isfile(dir_path):
      remove(dir_path)

    return


#_______________________________________________________________________
def test_mkdir_no_parent() -> None:

  parent: str = TestConst.TEST_DIR_PARENT

  # Prep
  Helper.rm_test_dir(parent)

  with pytest.raises(Exception):
    Utils.verify_dir(TestConst.TEST_DIR_FULL_PATH)

#_______________________________________________________________________
def test_mkdir_file_exists() -> None:

  test_path: str = TestConst.TEST_DIR_NAME

  # Prep
  Helper.rm_test_dir(test_path)

  # Create file with same name
  open(test_path, 'a').close()

  with pytest.raises(Exception):
    Utils.verify_dir(test_path)

  # Clean up
  remove(test_path)

#_______________________________________________________________________
def test_mkdir_no_error() -> None:

  test_path: str = TestConst.TEST_DIR_NAME

  # Prep
  Helper.rm_test_dir(test_path)

  assert Utils.verify_dir(TestConst.TEST_DIR_NAME) == True

  # Clean up
  Helper.rm_test_dir(test_path)

#_______________________________________________________________________
def test_mkdir_long_path() -> None:

  test_path : str = TestConst.TEST_DIR_FULL_PATH
  parent    : str = TestConst.TEST_DIR_PARENT

  # Prep
  Helper.rm_test_dir(test_path)
  Helper.rm_test_dir(parent)
  makedirs(parent)

  assert Utils.verify_dir(test_path) == True

  # Clean up
  Helper.rm_test_dir(parent)
