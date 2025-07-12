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
#
#   Configuration file for defining the layout and content of planner
#   pages.
#
#   This module specifies the types of planner entries and how
#   they are arranged in single- and double-sided printing formats.
#
#   Each entry is represented by a dictionary containing the entry
#   type and any additional arguments it requires. These configurations
#   enable automated generation of printable journal pages with
#   consistent formatting and content.
#_______________________________________________________________________

from enum import auto
from enum import IntEnum

from classes.constants.addl_arg_keys import AddlArgKeys as Key
from classes.constants.strings import PlannerStrings as Strings

from classes.page_entries.day_entry import DayEntry
from classes.page_entries.week_entry import WeekEntry0
from classes.page_entries.week_entry import WeekEntry1
from classes.page_entries.month_entry import MonthEntry

from classes.page_entries.goal_entry import GoalEntry

from classes.page_entries.free_write_entry import FreeWriteEntry

from classes.page_entries.title_page import TitlePage
from classes.page_entries.free_write_prompt_entry import FreeWritePromptEntry
from classes.page_entries.week_checklist_entry import WeekCheckList



WEEK_CHECKLIST: dict =\
{ Key.ENTRY_TYPE: WeekCheckList

}

#_____________________________________________________________________
BLNK_ENTRY: dict =\
  { Key.ENTRY_TYPE: TitlePage
  , Key.ENTRY_ARGS: {Key.HEADER_TXT: ' '}
  }

TITLE: dict =\
{ Key.ENTRY_TYPE: TitlePage
, Key.ENTRY_ARGS:
  { Key.HEADER_TXT: 'Book of Plans'
  }
}

#_____________________________________________________________________
YR5_0: dict =\
{ Key.ENTRY_TYPE: FreeWritePromptEntry
, Key.ENTRY_ARGS:
  { Key.HEADER_TXT: Strings.PAGE_HEADER_TXT_FUT_5YR
  , Key.PROMPT_TXT: Strings.FREE_WRITE_FUT_5YR
  }
}

YR5_1: dict =\
{ Key.ENTRY_TYPE: FreeWriteEntry
, Key.ENTRY_ARGS:
  { Key.HEADER_TXT: Strings.PAGE_HEADER_TXT_FUT_5YR
  }
}

YR1_0: dict =\
{ Key.ENTRY_TYPE: FreeWritePromptEntry
, Key.ENTRY_ARGS:
  { Key.HEADER_TXT: Strings.PAGE_HEADER_TXT_FUT_1YR
  , Key.PROMPT_TXT: Strings.FREE_WRITE_FUT_1YR
  }
}

YR1_1: dict =\
{ Key.ENTRY_TYPE: FreeWriteEntry
, Key.ENTRY_ARGS:
  { Key.HEADER_TXT: Strings.PAGE_HEADER_TXT_FUT_1YR
  }
}

FUT_12W_ENTRY: dict =\
{ Key.ENTRY_TYPE: FreeWritePromptEntry
, Key.ENTRY_ARGS:
  { Key.HEADER_TXT: Strings.PAGE_HEADER_TXT_FUT_12W
  , Key.PROMPT_TXT: Strings.FREE_WRITE_FUT_12W
  }
}

FUT_BAD_ENTRY: dict =\
{ Key.ENTRY_TYPE: FreeWritePromptEntry
, Key.ENTRY_ARGS:
  { Key.HEADER_TXT: Strings.PAGE_HEADER_TXT_FUT_BAD
  , Key.PROMPT_TXT: Strings.FREE_WRITE_FUT_BAD
  }
}

#_____________________________________________________________________
VOW: dict =\
{ Key.ENTRY_TYPE: FreeWritePromptEntry
, Key.ENTRY_ARGS:
  { Key.HEADER_TXT: Strings.VOW_HEADER_TXT
  , Key.PROMPT_TXT: Strings.VOW
  }
}

ACTION_ITEMS: dict =\
{ Key.ENTRY_TYPE: FreeWriteEntry
, Key.ENTRY_ARGS:
  { Key.HEADER_TXT: 'Action Items: '
  }
}

#_____________________________________________________________________

DAY: list = []
QUOT: list = []

for i in range(7):
  DAY.append\
  ( { Key.ENTRY_TYPE: DayEntry
    , Key.ENTRY_ARGS: {Key.CYCLING_PROMPT_IDX: i}
    }
  )

  QUOT.append\
  ( { Key.ENTRY_TYPE: FreeWriteEntry
    , Key.ENTRY_ARGS: {Key.HEADER_TXT: Strings.QUOTES[i]}
    }
  )

DAY0 = DAY[0]
DAY1 = DAY[1]
DAY2 = DAY[2]
DAY3 = DAY[3]
DAY4 = DAY[4]
DAY5 = DAY[5]
DAY6 = DAY[6]

MNTH: dict =\
  { Key.ENTRY_TYPE: MonthEntry
  , Key.ENTRY_ARGS: {}
  }

#_____________________________________________________________________
FREE_WRITE_DAY0: dict =\
  { Key.ENTRY_TYPE: FreeWriteEntry
  , Key.ENTRY_ARGS: {Key.HEADER_TXT: Strings.QUOTES[0]}
  }

#_____________________________________________________________________
WEEK0: dict =\
  { Key.ENTRY_TYPE: WeekEntry0
  , Key.ENTRY_ARGS: {}
  }
WEEK1: dict =\
  { Key.ENTRY_TYPE: WeekEntry1
  , Key.ENTRY_ARGS: {}
  }

#_____________________________________________________________________
GOAL: dict =\
  { Key.ENTRY_TYPE: GoalEntry
  , Key.ENTRY_ARGS: {}
  }


DATES: dict =\
  { Key.ENTRY_TYPE: FreeWriteEntry
  , Key.ENTRY_ARGS: {Key.HEADER_TXT: 'Important Dates'}
  }
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
    PAGE_ORDER: A list of layout configurations for
                         single-sided printing.

    DBL_SIDE_PAGE_ORDER: Same as above, but for double-sided printing
                         layouts.
  """


  #_____________________________________________________________________
  DBL_SIDE_PAGE_ORDER: list =\
  [ [ '0__title-page'
    , TITLE
    , BLNK_ENTRY
    ]
  , [ '1__vision-0'
    , YR1_0
    , YR1_1
    ]
  , [ '1__vision-1'
    , FUT_12W_ENTRY
    , YR5_1
    ]
  , [ '1__vision-2'
    , YR5_0
    , FUT_BAD_ENTRY
    ]
  , [ '1__vision-3'
    , VOW
    , BLNK_ENTRY
    ]
  , [ Strings.DEF_GOAL_LAYOUT_PATH
    , GOAL
    , GOAL
    ]
  , [ Strings.DEF_GOAL_LAYOUT_PATH
    , GOAL
    , GOAL
    ]
  , [ '3__month-0'
    , MNTH
    , MNTH
    ]
  , [ '3__month-1'
    , DATES
    , MNTH
    ]
  , [ '4__week-0'
    , DAY3
    , QUOT[3]
    ]
  , [ '4__week-1'
    , DAY4
    , QUOT[2]
    ]
  , [ '4__week-2'
    , DAY2
    , QUOT[4]
    ]
  , [ '4__week-3'
    , DAY5
    , QUOT[1]
    ]
  , [ '4__week-4'
    , DAY1
    , QUOT[5]
    ]
  , [ '4__week-5'
    , DAY6
    , QUOT[0]
    ]
  , [ '4__week-6'
    , DAY0
    , QUOT[6]
    , TITLE
    ]
  , [ '4__week-7'
    , WEEK0
    , WEEK1
    ]
  ]

#_______________________________________________________________________
class OneSidePages:
  """
  Constants used in single sided pages.
  """
  #_____________________________________________________________________
  # Enums used so page numbers can be automated
  #_____________________________________________________________________
  class IntrPgNo(IntEnum):
    """
    Page numbers for intro section.
    """
    TTL_F_1YR = auto()
    F_5YR_12W = auto()
    F_5YR_BAD = auto()
    F_1YR_VOW = auto()
    GOALS_0_1 = auto()
    GOALS_2_3 = auto()
    MONTH_0_1 = auto()
    MONTH_2__ = auto()

  # File names for intro pages
  INTR_FILES: dict =\
  { IntrPgNo.TTL_F_1YR: f'0-{IntrPgNo.TTL_F_1YR:02}-ttl_f_1yr'
  , IntrPgNo.F_5YR_12W: f'0-{IntrPgNo.F_5YR_12W:02}-f_5yr_12w'
  , IntrPgNo.F_5YR_BAD: f'0-{IntrPgNo.F_5YR_BAD:02}-f_5yr_bad'
  , IntrPgNo.F_1YR_VOW: f'0-{IntrPgNo.F_1YR_VOW:02}-f_1yr_vow'
  , IntrPgNo.GOALS_0_1: f'0-{IntrPgNo.GOALS_0_1:02}-goals_0_1'
  , IntrPgNo.GOALS_2_3: f'0-{IntrPgNo.GOALS_2_3:02}-goals_2_3'
  , IntrPgNo.MONTH_0_1: f'0-{IntrPgNo.MONTH_0_1:02}-month_0_1'
  , IntrPgNo.MONTH_2__: f'0-{IntrPgNo.MONTH_2__:02}-month_3__'
  }

  INTR_FILE_NAMES: list =\
    list(INTR_FILES.values())

  #_____________________________________________________________________
  class WeekPgNo(IntEnum):
    """
    Page numbers for week section.
    """
    WK_0 = auto()
    WK_1 = auto()
    DAY0 = auto()
    QUT0 = auto()
    DAY1 = auto()
    QUT1 = auto()
    DAY2 = auto()
    QUT2 = auto()
    DAY3 = auto()
    QUT3 = auto()
    DAY4 = auto()
    QUT4 = auto()
    DAY5 = auto()
    QUT5 = auto()
    DAY6 = auto()
    QUT6 = auto()

  # File names for single sided PDFs
  WEEK_FILES: dict =\
  { WeekPgNo.WK_0: f'0-{WeekPgNo.WK_0:02}-wk_0'
  , WeekPgNo.WK_1: f'0-{WeekPgNo.WK_1:02}-wk_1'
  , WeekPgNo.DAY0: f'0-{WeekPgNo.DAY0:02}-day0'
  , WeekPgNo.QUT0: f'0-{WeekPgNo.QUT0:02}-qut0'
  , WeekPgNo.DAY1: f'0-{WeekPgNo.DAY1:02}-day1'
  , WeekPgNo.QUT1: f'0-{WeekPgNo.QUT1:02}-qut1'
  , WeekPgNo.DAY2: f'0-{WeekPgNo.DAY2:02}-day2'
  , WeekPgNo.QUT2: f'0-{WeekPgNo.QUT2:02}-qut2'
  , WeekPgNo.DAY3: f'0-{WeekPgNo.DAY3:02}-day3'
  , WeekPgNo.QUT3: f'0-{WeekPgNo.QUT3:02}-qut3'
  , WeekPgNo.DAY4: f'0-{WeekPgNo.DAY4:02}-day4'
  , WeekPgNo.QUT4: f'0-{WeekPgNo.QUT4:02}-qut4'
  , WeekPgNo.DAY5: f'0-{WeekPgNo.DAY5:02}-day5'
  , WeekPgNo.QUT5: f'0-{WeekPgNo.QUT5:02}-qut5'
  , WeekPgNo.DAY6: f'0-{WeekPgNo.DAY6:02}-day6'
  , WeekPgNo.QUT6: f'0-{WeekPgNo.QUT6:02}-qut6'
  }

  WEEK_FILE_NAMES: list =\
    list(WEEK_FILES.values())


  #_____________________________________________________________________
  PAGE_ORDER: list =\
  [ [ '00-action-items'             , ACTION_ITEMS    , ACTION_ITEMS  ]
  , [ INTR_FILES[IntrPgNo.TTL_F_1YR], TITLE           , YR1_1         ]
  , [ INTR_FILES[IntrPgNo.F_5YR_12W], YR5_0           , FUT_12W_ENTRY ]
  , [ INTR_FILES[IntrPgNo.F_5YR_BAD], YR5_1           , FUT_BAD_ENTRY ]
  , [ INTR_FILES[IntrPgNo.F_1YR_VOW], YR1_0           , VOW           ]
  , [ INTR_FILES[IntrPgNo.GOALS_0_1], GOAL            , GOAL          ]
  , [ INTR_FILES[IntrPgNo.GOALS_2_3], GOAL            , GOAL          ]
  , [ INTR_FILES[IntrPgNo.MONTH_0_1], MNTH            , MNTH          ]
  , [ INTR_FILES[IntrPgNo.MONTH_2__], MNTH            , DATES         ]

  , [ WEEK_FILES[WeekPgNo.WK_0], WEEK0    , WEEK0   ]
  , [ WEEK_FILES[WeekPgNo.WK_1], WEEK1    , WEEK1   ]
  , [ WEEK_FILES[WeekPgNo.DAY0], DAY0     , DAY0    ]
  , [ WEEK_FILES[WeekPgNo.QUT0], QUOT[0]  , QUOT[0] ]
  , [ WEEK_FILES[WeekPgNo.DAY1], DAY1     , DAY1    ]
  , [ WEEK_FILES[WeekPgNo.QUT1], QUOT[1]  , QUOT[1] ]
  , [ WEEK_FILES[WeekPgNo.DAY2], DAY2     , DAY2    ]
  , [ WEEK_FILES[WeekPgNo.QUT2], QUOT[2]  , QUOT[2] ]
  , [ WEEK_FILES[WeekPgNo.DAY3], DAY3     , DAY3    ]
  , [ WEEK_FILES[WeekPgNo.QUT3], QUOT[3]  , QUOT[3] ]
  , [ WEEK_FILES[WeekPgNo.DAY4], DAY4     , DAY4    ]
  , [ WEEK_FILES[WeekPgNo.QUT4], QUOT[4]  , QUOT[4] ]
  , [ WEEK_FILES[WeekPgNo.DAY5], DAY5     , DAY5    ]
  , [ WEEK_FILES[WeekPgNo.QUT5], QUOT[5]  , QUOT[5] ]
  , [ WEEK_FILES[WeekPgNo.DAY6], DAY6     , DAY6    ]
  , [ WEEK_FILES[WeekPgNo.QUT6], QUOT[6]  , QUOT[6] ]
  ]