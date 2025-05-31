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
from os import path

from classes.constants.addl_arg_keys import AddlArgKeys as Key
from classes.constants.page_order import PageOrder
from classes.constants.strings import PlannerStrings as Strings

from classes.page_layouts.habit_layout import HabitLayout
from classes.page_layouts.half_letter_divider import DividerPage

from classes.page_entries.blank_entry import BlankWrite
from classes.reference_pages.ace_reference import AceReference

from utils.planner_parser import PlannerCreationParser

from classes.page_layouts.half_letter_layout import TwoPageHalfLetterSize

#_______________________________________________________________________
def new_line (new_line_count: int = 1) -> None:
  for i in range(new_line_count):
    print()

#_______________________________________________________________________
if __name__ == '__main__':
  new_line(2)

  parser: argparse.ArgumentParser = argparse.ArgumentParser()
  PlannerCreationParser.init_parser(parser)

  args: argparse.Namespace = parser.parse_args()

  is_portrait: bool   = False
  is_dbl_sided: bool  = args.dbl_sided

  page_order: list = []

  if (is_dbl_sided):
    page_order = PageOrder.DBL_SIDE_PAGE_ORDER
  else:
    page_order = PageOrder.SGL_SIDE_PAGE_ORDER

  for i in range (len(page_order)):
    layout =\
      TwoPageHalfLetterSize\
      ( is_portrait=is_portrait
      , is_dbl_sided=is_dbl_sided
      , file_path=path.join(args.out_dir, page_order[i][0])
      , entry_0_type=page_order[i][1][Key.ENTRY_TYPE]
      , entry_0_args=page_order[i][1][Key.ENTRY_ARGS]
      , entry_1_type=page_order[i][2][Key.ENTRY_TYPE]
      , entry_1_args=page_order[i][2][Key.ENTRY_ARGS]
      )
    layout.save()

  ace_ref_layout =\
    TwoPageHalfLetterSize\
    ( is_portrait=is_portrait
    , is_dbl_sided=is_dbl_sided
    , file_path=path.join(args.out_dir, 'ace-reference.svg')
    , entry_0_type=AceReference
    , entry_0_args={Key.HEADER_TXT: 'test'}
    )
  ace_ref_layout.save()

  test_layout =\
    TwoPageHalfLetterSize\
    ( is_portrait=is_portrait
    , is_dbl_sided=is_dbl_sided
    , file_path=path.join(args.out_dir, Strings.DEF_TEST_LAYOUT_PATH)
    , entry_0_type=BlankWrite
    , entry_0_args={Key.HEADER_TXT: 'page 0'}
    , entry_1_type=BlankWrite
    , entry_1_args={Key.HEADER_TXT: 'page 1'}
    )
  test_layout.save()

  habit_tracker =\
    HabitLayout\
    ( is_portrait=is_portrait
    , is_dbl_sided=is_dbl_sided
    , out_dir=args.out_dir
    , divider_pos=0
    )
  habit_tracker.save()

  #_____________________________________________________________________
  # Create dividers
  #_____________________________________________________________________
  divider_labels: list =\
  [ 'Vision'
  , 'Goals'
  , 'Calendar'
  ]

  for i in range(1, 4):
    divider_labels.append(f'Month {i}')


  for i in range(len(divider_labels)):
    DividerPage\
    ( is_portrait=is_portrait
    , divider_pos=i+1
    , divider_str=divider_labels[i]
    , out_dir=args.out_dir
    ).save()

  new_line(10)
  print("all done")
  new_line(10)
