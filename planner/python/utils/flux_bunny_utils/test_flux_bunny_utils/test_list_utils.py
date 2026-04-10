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
#   Tests for list utility functions.
#______________________________________________________________________

from utils.flux_bunny_utils.list_utils import ListUtils

#_______________________________________________________________________
def test_split_list_even() -> None:

  test_list: list = [1,2,3,4,5,6]

  list1, list2 = ListUtils.split_list(test_list, 2)

  assert list1 == [1,2,3]
  assert list2 == [4,5,6]

  return

#_______________________________________________________________________
def test_split_list_odd() -> None:

  test_list: list = [1, 2, 3, 4, 5, 6, 7, 8]

  list1, list2, list3 = ListUtils.split_list(test_list, 3)

  assert list1 == [1, 2, 3]
  assert list2 == [4, 5, 6]
  assert list3 == [7, 8]

  return

#_______________________________________________________________________
def test_split_list_n_less_than_elements() -> None:

  test_list: list = [1, 2]

  list1, list2, list3, list4 = ListUtils.split_list(test_list, 4)

  assert list1 == [1]
  assert list2 == [2]
  assert list3 == []
  assert list4 == []

  return