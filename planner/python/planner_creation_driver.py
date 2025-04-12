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
#
#   NOTES
#   All dimensions in planner are in inches.
#_______________________________________________________________________

import argparse

from classes.page_layouts.day_layout import OneDayLayout
from classes.page_layouts.goal_layout import GoalLayout
from classes.page_layouts.week_layout import WeekLayout

from classes.constants.dims import PlannerDims as Dims
from classes.constants.style import PlannerColors as Colors
from classes.constants.style import PlannerFontStyle as Font
from classes.elements.base_element import BaseElement
from classes.elements.table_rows import TableRows

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
  week_layout =\
    WeekLayout\
    ( is_portrait=is_portrait
    , is_dbl_sided=is_dbl_sided
    )
  week_layout.save()

  day_layout =\
    OneDayLayout\
    ( is_portrait=is_portrait
    , is_dbl_sided=is_dbl_sided
    )
  day_layout.save()

  goal_layout =\
    GoalLayout\
    ( is_portrait=is_portrait
    , is_dbl_sided=is_dbl_sided
    )
  goal_layout.save()


  wdth, hght = Dims.calc_border_size(False)


  print("all done")
