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

from classes.constants.strings import PlannerStrings as Strings
from classes.page_layouts.free_write_layout import FreeWriteLayout
from classes.page_layouts.day_layout import OneDayLayout
from classes.page_layouts.goal_layout import GoalLayout
from classes.page_layouts.week_layout import WeekLayout
from classes.page_layouts.test_layout import TestLayout
from classes.page_layouts.habit_layout import HabitLayout
from classes.page_layouts.half_letter_divider import DividerPage

from classes.page_entries.test_entry0 import TestEntry0
from classes.page_entries.goal_entry import GoalEntry

from classes.page_layouts.ace_ref_layout import AceRefLayout

from utils.planner_parser import PlannerCreationParser

from classes.page_layouts.half_letter_layout import TwoPageHalfLetterSize

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
  is_dbl_sided: bool  = args.dbl_sided

  #_____________________________________________________________________

  #_____________________________________________________________________
  # Free-write layout generation
  #_____________________________________________________________________

  '''
  free_write_prompts: list =\
  [ Strings.FREE_WRITE_FUTURE
  , Strings.FREE_WRITE_YR
  , Strings.FREE_WRITE_12WK
  , Strings.FREE_WRITE_INACTION
  ]

  free_write_page_headers: list =\
  [ Strings.FUTURE_PAGE_HEADER
  , Strings.FUTURE_YR_PAGE_HEADER
  , Strings.FUTURE_12WK_PAGE_HEADER
  , Strings.INACTION_PAGE_HEADER
  ]

  free_write_file_paths: list =\
  [ Strings.DEF_FUTURE_LAYOUT_PATH
  , Strings.DEF_FUTURE_YR_LAYOUT_PATH
  , Strings.DEF_FUTURE_12WK_LAYOUT_PATH
  , Strings.DEF_INACTION_LAYOUT_PATH
  ]

  for i in range(len(free_write_prompts)-2):
    free_write_layout =\
      FreeWriteLayout\
      ( is_portrait=is_portrait
      , is_dbl_sided=is_dbl_sided
      , file_path=path.join(args.out_dir, free_write_file_paths[i])
      , header_txt_0=free_write_page_headers[i]
      , prompt_0=free_write_prompts[i]
      )
    free_write_layout.save()

  free_write_layout =\
      FreeWriteLayout\
      ( is_portrait=is_portrait
      , is_dbl_sided=is_dbl_sided
      , file_path=path.join(args.out_dir, free_write_file_paths[2])
      , header_txt_0=free_write_page_headers[2]
      , prompt_0=free_write_prompts[2]
      , header_txt_1=free_write_page_headers[3]
      , prompt_1=free_write_prompts[3]
      )
  free_write_layout.save()

  ace_ref_layout =\
    AceRefLayout\
    ( is_portrait=is_portrait
    , is_dbl_sided=is_dbl_sided
    , file_path=path.join(args.out_dir, 'ace-reference.svg')
    )
  ace_ref_layout.save()
  '''
  goal_layout =\
    TwoPageHalfLetterSize\
    ( is_portrait=is_portrait
    , is_dbl_sided=is_dbl_sided
    , file_path=path.join(args.out_dir, Strings.DEF_GOAL_LAYOUT_PATH)
    , entry_0_type=GoalEntry
    , entry_1_type=GoalEntry
    )
  goal_layout.save()

  test_layout =\
    TestLayout\
    ( is_portrait=is_portrait
    , is_dbl_sided=is_dbl_sided
    , file_path=path.join(args.out_dir, Strings.DEF_TEST_LAYOUT_PATH)
    )
  test_layout.save()

  week_layout =\
    WeekLayout\
    ( is_portrait=is_portrait
    , is_dbl_sided=is_dbl_sided
    , file_path=path.join(args.out_dir, Strings.DEF_WEEK_LAYOUT_PATH)
    )
  week_layout.save()

  day_layout =\
    OneDayLayout\
    ( is_portrait=is_portrait
    , is_dbl_sided=True#is_dbl_sided
    , file_path=path.join(args.out_dir, Strings.DEF_DAY_LAYOUT_PATH)
    )
  day_layout.save()

  '''
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

  for i in range(1, 13):
    divider_labels.append(f'Week {i}')


  for i in range(len(divider_labels)):
    DividerPage\
    ( is_portrait=is_portrait
    , divider_pos=i+1
    , divider_str=divider_labels[i]
    , out_dir=args.out_dir
    ).save()
  '''

  new_line(10)
  print("all done")
  new_line(10)
