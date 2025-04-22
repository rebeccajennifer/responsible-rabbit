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
#   Driver for planner creation.
#_______________________________________________________________________

import argparse

from classes.constants.strings import PlannerStrings as Strings
from classes.page_layouts.free_write_layout import FreeWriteLayout
from classes.page_layouts.day_layout import OneDayLayout
from classes.page_layouts.goal_layout import GoalLayout
from classes.page_layouts.week_layout import WeekLayout
from classes.page_layouts.test_layout import TestLayout
from classes.planner_parser import PlannerCreationParser

#_______________________________________________________________________
def new_line (new_line_count: int = 1) -> None:
  for i in range(new_line_count):
    print()

if __name__ == '__main__':
  new_line(2)

  parser: argparse.ArgumentParser = argparse.ArgumentParser()
  PlannerCreationParser.init_parser(parser)

  args: argparse.Namespace = parser.parse_args()

  is_portrait: bool   = False
  is_dbl_sided: bool  = False

  #_____________________________________________________________________

  free_write_layout =\
    FreeWriteLayout\
    ( is_portrait=is_portrait
    , is_dbl_sided=is_dbl_sided
    )
  free_write_layout.save()

  test_layout =\
    TestLayout\
    ( is_portrait=is_portrait
    , is_dbl_sided=is_dbl_sided
    )
  test_layout.save()

  future_12wk_layout =\
    FreeWriteLayout\
    ( is_portrait=is_portrait
    , is_dbl_sided=is_dbl_sided
    , file_path=Strings.DEF_FUTURE_12WK_LAYOUT_PATH
    , header_txt=Strings.FUTURE_12WK_PAGE_HEADER
    , prompt=Strings.FREE_WRITE_12WK
    )
  future_12wk_layout.save()

  future_layout =\
    FreeWriteLayout\
    ( is_portrait=is_portrait
    , is_dbl_sided=is_dbl_sided
    , file_path=Strings.DEF_FUTURE_LAYOUT_PATH
    , header_txt=Strings.FUTURE_PAGE_HEADER
    , prompt=Strings.FREE_WRITE_FUTURE
    )
  future_layout.save()

  week_layout =\
    WeekLayout\
    ( is_portrait=is_portrait
    , is_dbl_sided=is_dbl_sided
    )
  week_layout.save()

  goal_layout =\
    GoalLayout\
    ( is_portrait=is_portrait
    , is_dbl_sided=is_dbl_sided
    )
  goal_layout.save()

  day_layout =\
    OneDayLayout\
    ( is_portrait=is_portrait
    , is_dbl_sided=is_dbl_sided
    )
  day_layout.save()


  new_line(10)
  print("all done")
  new_line(10)
