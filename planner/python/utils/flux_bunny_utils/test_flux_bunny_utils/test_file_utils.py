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
#   Tests for file utility functions.
#______________________________________________________________________

import pytest

from os.path import isdir
from os.path import isfile
from os.path import join
from os import makedirs
from os import remove

import cairosvg
import svgwrite

from shutil import rmtree

from utils.flux_bunny_utils.file_utils import FileUtils


#_______________________________________________________________________
class TestConst:
  """
  Constants used in tests.
  """

  TEST_DIR_NAME         : str = 'test_name'
  TEST_DIR_PARENT       : str = join('flux', 'bunny')
  TEST_DIR_GRANDPARENT  : str = 'flux'
  TEST_DIR_FULL_PATH    : str = join(TEST_DIR_PARENT, TEST_DIR_NAME)
  TEST_PDF_NAME         : str = 'test.pdf'
  TEST_SVG_NAME         : str = 'test.svg'

#_______________________________________________________________________
class Helper:
  """
  Helper functions for tests.
  """

  #_____________________________________________________________________
  def rm_test_dir(dir_path: str) -> None:
    """
    Removes test directory.

    Parameters
      dir_path: Path to directory to remove.

    Side Effects
      Removes test directory

    Returns
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
    FileUtils.verify_dir(TestConst.TEST_DIR_FULL_PATH)

  return

#_______________________________________________________________________
def test_mkdir_file_exists() -> None:

  test_path: str = TestConst.TEST_DIR_NAME

  # Prep
  Helper.rm_test_dir(test_path)

  # Create file with same name
  open(test_path, 'a').close()

  with pytest.raises(Exception):
    FileUtils.verify_dir(test_path)

  # Clean up
  remove(test_path)

  return

#_______________________________________________________________________
def test_mkdir_no_error() -> None:

  test_path: str = TestConst.TEST_DIR_NAME

  # Prep
  Helper.rm_test_dir(test_path)

  assert FileUtils.verify_dir(TestConst.TEST_DIR_NAME) == True

  # Clean up
  Helper.rm_test_dir(test_path)

  return

#_______________________________________________________________________
def test_mkdir_long_path() -> None:

  test_path   : str = TestConst.TEST_DIR_FULL_PATH
  parent      : str = TestConst.TEST_DIR_PARENT
  grandparent : str = TestConst.TEST_DIR_GRANDPARENT

  # Prep
  Helper.rm_test_dir(test_path)
  Helper.rm_test_dir(parent)
  Helper.rm_test_dir(grandparent)
  makedirs(parent)

  assert FileUtils.verify_dir(test_path) == True

  # Clean up
  Helper.rm_test_dir(grandparent)

  return

#_______________________________________________________________________
def test_is_pdf() -> None:

  #_____________________________________________________________________
  # Prep
  #_____________________________________________________________________
  test_svg_name: str = TestConst.TEST_SVG_NAME
  test_pdf_name: str = TestConst.TEST_PDF_NAME

  # Create svg
  test_dwg = svgwrite.Drawing\
    ( TestConst.TEST_SVG_NAME
    , profile='tiny'
    , size=(100,100)
    )
  test_dwg.save()

  # Create pdf
  cairosvg.svg2pdf\
    ( url=test_svg_name
    , write_to=test_pdf_name)
  #_____________________________________________________________________

  # Run function under test
  assert FileUtils.is_pdf(test_pdf_name) == True

  # Clean up
  remove(test_pdf_name)
  remove(test_svg_name)

  with pytest.raises(Exception):
    FileUtils.is_pdf(test_pdf_name)

  return
