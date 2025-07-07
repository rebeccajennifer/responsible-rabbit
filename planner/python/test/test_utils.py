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
  def make_test_dir(dir_path: str) -> None:
    """
    Removes test directory.

    Parameters:
      None

    Side Effects:
      Makes test directory

    Returns:
      None
    """
    makedirs(dir_path)
    return

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
    rmtree(dir_path)
    return


#_______________________________________________________________________
def test_mkdir_no_parent() -> None:
  with pytest.raises(Exception):
    Utils.verify_dir(TestConst.TEST_DIR_FULL_PATH)

def test_mkdir_file_exists() -> None:
  open(TestConst.TEST_DIR_NAME, 'a').close()

  with pytest.raises(Exception):
    Utils.verify_dir(TestConst.TEST_DIR_NAME)

def test_mkdir_file_exist() -> None:
  remove(TestConst.TEST_DIR_NAME)
  assert Utils.verify_dir(TestConst.TEST_DIR_NAME) == True