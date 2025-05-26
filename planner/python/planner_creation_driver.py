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
from classes.constants.strings import PlannerStrings as Strings
from classes.page_layouts.free_write_layout import FreeWriteLayout
from classes.page_layouts.day_layout import OneDayLayout
from classes.page_layouts.week_layout import WeekLayout
from classes.page_layouts.test_layout import TestLayout
from classes.page_layouts.habit_layout import HabitLayout
from classes.page_layouts.half_letter_divider import DividerPage

from classes.page_entries.day_entry import DayEntry
from classes.page_entries.week_entry import WeekEntry0
from classes.page_entries.week_entry import WeekEntry1
from classes.page_entries.free_write_entry import FreeWriteEntry
from classes.page_entries.free_write_prompt_entry import FreeWritePromptEntry
from classes.page_entries.goal_entry import GoalEntry
from classes.page_entries.blank_entry import BlankWrite
from classes.reference_pages.ace_reference import AceReference


from classes.page_layouts.ace_ref_layout import AceRefLayout

from utils.planner_parser import PlannerCreationParser

from classes.page_layouts.half_letter_layout import TwoPageHalfLetterSize

#_______________________________________________________________________
def new_line (new_line_count: int = 1) -> None:
  for i in range(new_line_count):
    print()

#_______________________________________________________________________
class PageOrder:
  """
  Defines and organizes configuration data for various journal page
  entries.

  Each page entry specifies a type (e.g., FreeWriteEntry, DayEntry)
  and a corresponding set of arguments specific to that type. Entry
  types may represent unstructured pages (like free writes with optional
  prompts) or structured formats (like daily or weekly tables for
  planning or reflection).

  The class also defines page ordering for both single-sided and
  double-sided journal layouts.

  Attributes:
    SGL_SIDE_PAGE_ORDER: A list of layout configurations for
                         single-sided printing.

    DBL_SIDE_PAGE_ORDER: Same as above, but for double-sided printing
                         layouts.
  """

  FUTURE_5YR_ENTRY0: dict =\
  { Key.ENTRY_TYPE: FreeWritePromptEntry
  , Key.ENTRY_ARGS:
    { Key.HEADER_TXT: Strings.PAGE_HEADER_TXT_FUTURE_5YR
    , Key.PROMPT_TXT: Strings.FREE_WRITE_FUTURE_5YR
    }
  }

  FUTURE_5YR_ENTRY1: dict =\
  { Key.ENTRY_TYPE: FreeWriteEntry
  , Key.ENTRY_ARGS:
    { Key.HEADER_TXT: Strings.PAGE_HEADER_TXT_FUTURE_5YR
    }
  }

  FUTURE_1YR_ENTRY0: dict =\
  { Key.ENTRY_TYPE: FreeWritePromptEntry
  , Key.ENTRY_ARGS:
    { Key.HEADER_TXT: Strings.PAGE_HEADER_TXT_FUTURE_1YR
    , Key.PROMPT_TXT: Strings.FREE_WRITE_FUTURE_1YR
    }
  }

  FUTURE_1YR_ENTRY1: dict =\
  { Key.ENTRY_TYPE: FreeWriteEntry
  , Key.ENTRY_ARGS:
    { Key.HEADER_TXT: Strings.PAGE_HEADER_TXT_FUTURE_1YR
    }
  }

  FUTURE_12W_ENTRY: dict =\
  { Key.ENTRY_TYPE: FreeWritePromptEntry
  , Key.ENTRY_ARGS:
    { Key.HEADER_TXT: Strings.PAGE_HEADER_TXT_FUTURE_12W
    , Key.PROMPT_TXT: Strings.FREE_WRITE_FUTURE_12W
    }
  }

  FUTURE_BAD_ENTRY: dict =\
  { Key.ENTRY_TYPE: FreeWritePromptEntry
  , Key.ENTRY_ARGS:
    { Key.HEADER_TXT: Strings.PAGE_HEADER_TXT_FUTURE_BAD
    , Key.PROMPT_TXT: Strings.FREE_WRITE_FUTURE_BAD
    }
  }

  SGL_SIDE_PAGE_ORDER: list =\
  [ [ Strings.DEF_FUTURE_5YR_LAYOUT_PATH
    , FUTURE_5YR_ENTRY0
    , FUTURE_5YR_ENTRY1
    ]
  , [ Strings.DEF_FUTURE_1YR_LAYOUT_PATH
    , FUTURE_1YR_ENTRY0
    , FUTURE_1YR_ENTRY1
    ]
  , [ Strings.DEF_FUTURE_12W_LAYOUT_PATH
    , FUTURE_12W_ENTRY
    , FUTURE_BAD_ENTRY
    ]
  ]


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

  page_order: list = []

  if (is_dbl_sided):
    page_order = PageOrder.SGL_SIDE_PAGE_ORDER
  else:
    page_order = PageOrder.SGL_SIDE_PAGE_ORDER

  for i in range (len(page_order)):
    free_write_layout =\
      TwoPageHalfLetterSize\
      ( is_portrait=is_portrait
      , is_dbl_sided=is_dbl_sided
      , file_path=path.join(args.out_dir, PageOrder.SGL_SIDE_PAGE_ORDER[i][0])
      , entry_0_type=page_order[i][1][Key.ENTRY_TYPE]
      , entry_0_args=page_order[i][1][Key.ENTRY_ARGS]
      , entry_1_type=page_order[i][2][Key.ENTRY_TYPE]
      , entry_1_args=page_order[i][2][Key.ENTRY_ARGS]
      )
    free_write_layout.save()

  ace_ref_layout =\
    TwoPageHalfLetterSize\
    ( is_portrait=is_portrait
    , is_dbl_sided=is_dbl_sided
    , file_path=path.join(args.out_dir, 'ace-reference.svg')
    , entry_0_type=AceReference
    , entry_0_args={Key.HEADER_TXT: 'test'}
    )
  ace_ref_layout.save()

  day_layout =\
    TwoPageHalfLetterSize\
    ( is_portrait=is_portrait
    , is_dbl_sided=is_dbl_sided
    , file_path=path.join(args.out_dir, Strings.DEF_DAY_LAYOUT_PATH)
    , entry_0_type=DayEntry
    , entry_0_args={Key.CYCLING_PROMPT_IDX: 3}
    , entry_1_type=DayEntry
    , entry_1_args={Key.CYCLING_PROMPT_IDX: 2}
    )

  day_layout.save()

  week_layout =\
    TwoPageHalfLetterSize\
    ( is_portrait=is_portrait
    , is_dbl_sided=is_dbl_sided
    , file_path=path.join(args.out_dir, Strings.DEF_WEEK_LAYOUT_PATH)
    , entry_0_type=WeekEntry0
    , entry_1_type=WeekEntry1
    )
  week_layout.save()

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
