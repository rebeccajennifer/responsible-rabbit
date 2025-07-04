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
from os import path, system, chdir

from classes.constants.addl_arg_keys import AddlArgKeys as Key
from classes.constants.page_order import PageOrder

from classes.page_entries.month_entry import MonthEntry
from classes.page_entries.week_habit_entry import HabitTracker
from classes.page_entries.title_page import TitlePage
from classes.page_entries.week_checklist_entry import WeekCheckList
from classes.page_entries.test_entry import TestEntry
from classes.page_entries.test_entry0 import TestEntry0

from classes.page_layouts.half_letter_divider import DividerPage

from classes.reference_pages.ace_reference import AceReference

from utils.planner_parser import PlannerCreationParser

from classes.page_layouts.half_letter_two_page_layout import TwoPageHalfLetterSize

#_______________________________________________________________________
def new_line (new_line_count: int = 1) -> None:
  for i in range(new_line_count):
    print()

def generate_pages\
( page_order: list
, is_portrait: bool
, is_dbl_sided: bool
, out_dir: str
) -> None:
  #_____________________________________________________________________
  # Iterate through list containing layout arguments and create
  # svg for each layout
  #_____________________________________________________________________
  for i in range (len(page_order)):
    layout =\
      TwoPageHalfLetterSize\
      ( is_portrait=is_portrait
      , is_dbl_sided=is_dbl_sided
      , file_path=path.join(out_dir, page_order[i][0])
      , entry_0_type=page_order[i][1][Key.ENTRY_TYPE]
      , entry_0_args=page_order[i][1][Key.ENTRY_ARGS]
      , entry_1_type=page_order[i][2][Key.ENTRY_TYPE]
      , entry_1_args=page_order[i][2][Key.ENTRY_ARGS]
      )
    layout.save()

def generate_dividers\
( is_portrait
, out_dir: str
):
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
    , out_dir=out_dir
    , entry_type=TitlePage
    , entry_args={Key.HEADER_TXT: divider_labels[i]}
    ).save()

def generate_habit_tracker\
( is_portrait: bool
, out_dir: str
):
  #_____________________________________________________________________
  # Create weekly habit bookmark
  #_____________________________________________________________________
  weekly_checklist =\
    TwoPageHalfLetterSize\
      ( is_portrait=is_portrait
      , is_dbl_sided=True
      , file_path=path.join(out_dir, 'week-chcklst-back.svg')
      , entry_0_type=TitlePage
      , entry_0_args={}
      , entry_1_type=WeekCheckList
      , entry_1_args={}
      , rgt_bndr_mrgn=True
      )
  weekly_checklist.save()

  habit_tracker =\
    DividerPage\
    ( is_portrait=is_portrait
    , out_dir=args.out_dir
    , divider_pos=0
    , divider_str='Today'
    , file_path=path.join(args.out_dir, 'week-chcklst-frnt.svg')
    , entry_type=HabitTracker
    , entry_args={}
    )
  habit_tracker.save()


#_______________________________________________________________________
if __name__ == '__main__':
  new_line(2)

  parser: argparse.ArgumentParser = argparse.ArgumentParser()
  PlannerCreationParser.init_parser(parser)

  args: argparse.Namespace = parser.parse_args()

  is_portrait: bool   = False
  is_dbl_sided: bool  = args.dbl_sided

  page_order: list = []

  #_____________________________________________________________________
  # Determine page ordering
  #_____________________________________________________________________
  if (is_dbl_sided):
    page_order = PageOrder.DBL_SIDE_PAGE_ORDER
  else:
    page_order = PageOrder.SGL_SIDE_PAGE_ORDER
  #_____________________________________________________________________

  generate_pages(page_order,is_portrait, is_dbl_sided, args.out_dir)
  generate_dividers(is_portrait, args.out_dir)
  generate_habit_tracker(is_portrait, args.out_dir)

  test_layout=\
    TwoPageHalfLetterSize\
    ( is_portrait=False
    , is_dbl_sided=is_dbl_sided
    , file_path=path.join(args.out_dir, 'test.svg')
    , entry_0_type=MonthEntry
    , entry_0_args={}
    , entry_1_type=TestEntry
    , entry_1_args={}
    )
  test_layout.save()

  chdir(f'{args.out_dir}/..')
  system(f'echo $PWD')
  system('./make-pdfs.sh')

  new_line(10)
  print("all done")
  new_line(10)
