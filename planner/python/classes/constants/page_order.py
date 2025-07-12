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

  WEEK_CHECKLIST: dict =\
  { Key.ENTRY_TYPE: WeekCheckList

  }

  #_____________________________________________________________________
  BLNK_ENTRY: dict =\
    { Key.ENTRY_TYPE: TitlePage
    , Key.ENTRY_ARGS: {Key.HEADER_TXT: ' '}
    }

  TITLE_PAGE: dict =\
  { Key.ENTRY_TYPE: TitlePage
  , Key.ENTRY_ARGS:
    { Key.HEADER_TXT: 'Book of Plans'
    }
  }

  #_____________________________________________________________________
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

  #_____________________________________________________________________
  VOW_ENTRY: dict =\
  { Key.ENTRY_TYPE: FreeWritePromptEntry
  , Key.ENTRY_ARGS:
    { Key.HEADER_TXT: Strings.VOW_HEADER_TXT
    , Key.PROMPT_TXT: Strings.VOW
    }
  }

  ACTION_ITEMS_ENTRY: dict =\
  { Key.ENTRY_TYPE: FreeWriteEntry
  , Key.ENTRY_ARGS:
    { Key.HEADER_TXT: 'Action Items: '
    }
  }

  #_____________________________________________________________________

  DAY_ENTRY: list = []
  DAY_FREE_WRITE_ENTRY: list = []

  for i in range(7):
    DAY_ENTRY.append\
    ( { Key.ENTRY_TYPE: DayEntry
      , Key.ENTRY_ARGS: {Key.CYCLING_PROMPT_IDX: i}
      }
    )

    DAY_FREE_WRITE_ENTRY.append\
    ( { Key.ENTRY_TYPE: FreeWriteEntry
      , Key.ENTRY_ARGS: {Key.HEADER_TXT: Strings.QUOTES[i]}
      }
    )

  DAY_ENTRY0 = DAY_ENTRY[0]
  DAY_ENTRY1 = DAY_ENTRY[1]
  DAY_ENTRY2 = DAY_ENTRY[2]
  DAY_ENTRY3 = DAY_ENTRY[3]
  DAY_ENTRY4 = DAY_ENTRY[4]
  DAY_ENTRY5 = DAY_ENTRY[5]
  DAY_ENTRY6 = DAY_ENTRY[6]

  MONTH_ENTRY: dict =\
    { Key.ENTRY_TYPE: MonthEntry
    , Key.ENTRY_ARGS: {}
    }

  #_____________________________________________________________________
  FREE_WRITE_DAY0: dict =\
    { Key.ENTRY_TYPE: FreeWriteEntry
    , Key.ENTRY_ARGS: {Key.HEADER_TXT: Strings.QUOTES[0]}
    }

  #_____________________________________________________________________
  WEEK_ENTRY0: dict =\
    { Key.ENTRY_TYPE: WeekEntry0
    , Key.ENTRY_ARGS: {}
    }
  WEEK_ENTRY1: dict =\
    { Key.ENTRY_TYPE: WeekEntry1
    , Key.ENTRY_ARGS: {}
    }

  #_____________________________________________________________________
  GOAL_ENTRY: dict =\
    { Key.ENTRY_TYPE: GoalEntry
    , Key.ENTRY_ARGS: {}
    }


  DATES_ENTRY: dict =\
    { Key.ENTRY_TYPE: FreeWriteEntry
    , Key.ENTRY_ARGS: {Key.HEADER_TXT: 'Important Dates'}
    }

  #_____________________________________________________________________
  DBL_SIDE_PAGE_ORDER: list =\
  [ [ '0__title-page'
    , TITLE_PAGE
    , BLNK_ENTRY
    ]
  , [ '1__vision-0'
    , FUTURE_1YR_ENTRY0
    , FUTURE_1YR_ENTRY1
    ]
  , [ '1__vision-1'
    , FUTURE_12W_ENTRY
    , FUTURE_5YR_ENTRY1
    ]
  , [ '1__vision-2'
    , FUTURE_5YR_ENTRY0
    , FUTURE_BAD_ENTRY
    ]
  , [ '1__vision-3'
    , VOW_ENTRY
    , BLNK_ENTRY
    ]
  , [ Strings.DEF_GOAL_LAYOUT_PATH
    , GOAL_ENTRY
    , GOAL_ENTRY
    ]
  , [ Strings.DEF_GOAL_LAYOUT_PATH
    , GOAL_ENTRY
    , GOAL_ENTRY
    ]
  , [ '3__month-0'
    , MONTH_ENTRY
    , MONTH_ENTRY
    ]
  , [ '3__month-1'
    , DATES_ENTRY
    , MONTH_ENTRY
    ]
  , [ '4__week-0'
    , DAY_ENTRY3
    , DAY_FREE_WRITE_ENTRY[3]
    ]
  , [ '4__week-1'
    , DAY_ENTRY4
    , DAY_FREE_WRITE_ENTRY[2]
    ]
  , [ '4__week-2'
    , DAY_ENTRY2
    , DAY_FREE_WRITE_ENTRY[4]
    ]
  , [ '4__week-3'
    , DAY_ENTRY5
    , DAY_FREE_WRITE_ENTRY[1]
    ]
  , [ '4__week-4'
    , DAY_ENTRY1
    , DAY_FREE_WRITE_ENTRY[5]
    ]
  , [ '4__week-5'
    , DAY_ENTRY6
    , DAY_FREE_WRITE_ENTRY[0]
    ]
  , [ '4__week-6'
    , DAY_ENTRY0
    , DAY_FREE_WRITE_ENTRY[6]
    , TITLE_PAGE
    ]
  , [ '4__week-7'
    , WEEK_ENTRY0
    , WEEK_ENTRY1
    ]
  ]

  #_____________________________________________________________________
  # Enums used so page numbers can be automated
  #_____________________________________________________________________
  class SglPagesIntr(IntEnum):
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

  # File names for single sided PDFs
  SGL_SIDE_INTR_FILES: dict =\
  { SglPagesIntr.TTL_F_1YR: f'0-{SglPagesIntr.TTL_F_1YR:02}-ttl_f_1yr'
  , SglPagesIntr.F_5YR_12W: f'0-{SglPagesIntr.F_5YR_12W:02}-f_5yr_12w'
  , SglPagesIntr.F_5YR_BAD: f'0-{SglPagesIntr.F_5YR_BAD:02}-f_5yr_bad'
  , SglPagesIntr.F_1YR_VOW: f'0-{SglPagesIntr.F_1YR_VOW:02}-f_1yr_vow'
  , SglPagesIntr.GOALS_0_1: f'0-{SglPagesIntr.GOALS_0_1:02}-goals_0_1'
  , SglPagesIntr.GOALS_2_3: f'0-{SglPagesIntr.GOALS_2_3:02}-goals_2_3'
  , SglPagesIntr.MONTH_0_1: f'0-{SglPagesIntr.MONTH_0_1:02}-month_0_1'
  , SglPagesIntr.MONTH_2__: f'0-{SglPagesIntr.MONTH_2__:02}-month_3__'
  }

  SGL_SIDE_INTR_FILE_NAMES: list =\
    list(SGL_SIDE_INTR_FILES.values())

  #_____________________________________________________________________
  class SglPagesWeek(IntEnum):
    """
    Page numbers for intro section.
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
  SGL_SIDE_WEEK_FILES: dict =\
  { SglPagesWeek.WK_0: f'0-{SglPagesWeek.WK_0:02}-wk_0'
  , SglPagesWeek.WK_1: f'0-{SglPagesWeek.WK_1:02}-wk_1'
  , SglPagesWeek.DAY0: f'0-{SglPagesWeek.DAY0:02}-day0'
  , SglPagesWeek.QUT0: f'0-{SglPagesWeek.QUT0:02}-qut0'
  , SglPagesWeek.DAY1: f'0-{SglPagesWeek.DAY1:02}-day1'
  , SglPagesWeek.QUT1: f'0-{SglPagesWeek.QUT1:02}-qut1'
  , SglPagesWeek.DAY2: f'0-{SglPagesWeek.DAY2:02}-day2'
  , SglPagesWeek.QUT2: f'0-{SglPagesWeek.QUT2:02}-qut2'
  , SglPagesWeek.DAY3: f'0-{SglPagesWeek.DAY3:02}-day3'
  , SglPagesWeek.QUT3: f'0-{SglPagesWeek.QUT3:02}-qut3'
  , SglPagesWeek.DAY4: f'0-{SglPagesWeek.DAY4:02}-day4'
  , SglPagesWeek.QUT4: f'0-{SglPagesWeek.QUT4:02}-qut4'
  , SglPagesWeek.DAY5: f'0-{SglPagesWeek.DAY5:02}-day5'
  , SglPagesWeek.QUT5: f'0-{SglPagesWeek.QUT5:02}-qut5'
  , SglPagesWeek.DAY6: f'0-{SglPagesWeek.DAY6:02}-day6'
  , SglPagesWeek.QUT6: f'0-{SglPagesWeek.QUT6:02}-qut6'
  }

  SGL_SIDE_WEEK_FILE_NAMES: list =\
    list(SGL_SIDE_WEEK_FILES.values())


  #_____________________________________________________________________
  SGL_SIDE_PAGE_ORDER: list =\
  [ [ '00-action-items'
    , ACTION_ITEMS_ENTRY
    , ACTION_ITEMS_ENTRY
    ]
  , [ SGL_SIDE_INTR_FILES[SglPagesIntr.TTL_F_1YR]
    , TITLE_PAGE
    , FUTURE_1YR_ENTRY1
    ]
  , [ SGL_SIDE_INTR_FILES[SglPagesIntr.F_5YR_12W]
    , FUTURE_5YR_ENTRY0
    , FUTURE_12W_ENTRY
    ]
  , [ SGL_SIDE_INTR_FILES[SglPagesIntr.F_5YR_BAD]
    , FUTURE_5YR_ENTRY1
    , FUTURE_BAD_ENTRY
    ]
  , [ SGL_SIDE_INTR_FILES[SglPagesIntr.F_1YR_VOW]
    , FUTURE_1YR_ENTRY0
    , VOW_ENTRY
    ]
  , [ SGL_SIDE_INTR_FILES[SglPagesIntr.GOALS_0_1]
    , GOAL_ENTRY
    , GOAL_ENTRY
    ]
  , [ SGL_SIDE_INTR_FILES[SglPagesIntr.GOALS_2_3]
    , GOAL_ENTRY
    , GOAL_ENTRY
    ]
  , [ SGL_SIDE_INTR_FILES[SglPagesIntr.MONTH_0_1]
    , MONTH_ENTRY
    , MONTH_ENTRY
    ]
  , [ SGL_SIDE_INTR_FILES[SglPagesIntr.MONTH_2__]
    , MONTH_ENTRY
    , DATES_ENTRY
    ]
  , [ SGL_SIDE_WEEK_FILES[SglPagesWeek.WK_0]
    , WEEK_ENTRY0
    , WEEK_ENTRY0
    ]
  , [ SGL_SIDE_WEEK_FILES[SglPagesWeek.WK_1]
    , WEEK_ENTRY1
    , WEEK_ENTRY1
    ]
  , [ SGL_SIDE_WEEK_FILES[SglPagesWeek.DAY0]
    , DAY_ENTRY0
    , DAY_ENTRY0
    ]
  , [ SGL_SIDE_WEEK_FILES[SglPagesWeek.QUT0]
    , DAY_FREE_WRITE_ENTRY[0]
    , DAY_FREE_WRITE_ENTRY[0]
    ]
  , [ SGL_SIDE_WEEK_FILES[SglPagesWeek.DAY1]
    , DAY_ENTRY1
    , DAY_ENTRY1
    ]
  , [ SGL_SIDE_WEEK_FILES[SglPagesWeek.QUT1]
    , DAY_FREE_WRITE_ENTRY[1]
    , DAY_FREE_WRITE_ENTRY[1]
    ]
  , [ SGL_SIDE_WEEK_FILES[SglPagesWeek.DAY2]
    , DAY_ENTRY2
    , DAY_ENTRY2
    ]
  , [ SGL_SIDE_WEEK_FILES[SglPagesWeek.QUT2]
    , DAY_FREE_WRITE_ENTRY[2]
    , DAY_FREE_WRITE_ENTRY[2]
    ]
  , [ SGL_SIDE_WEEK_FILES[SglPagesWeek.DAY3]
    , DAY_ENTRY3
    , DAY_ENTRY3
    ]
  , [ SGL_SIDE_WEEK_FILES[SglPagesWeek.QUT3]
    , DAY_FREE_WRITE_ENTRY[3]
    , DAY_FREE_WRITE_ENTRY[3]
    ]
  , [ SGL_SIDE_WEEK_FILES[SglPagesWeek.DAY4]
    , DAY_ENTRY4
    , DAY_ENTRY4
    ]
  , [ SGL_SIDE_WEEK_FILES[SglPagesWeek.QUT4]
    , DAY_FREE_WRITE_ENTRY[4]
    , DAY_FREE_WRITE_ENTRY[4]
    ]
  , [ SGL_SIDE_WEEK_FILES[SglPagesWeek.DAY5]
    , DAY_ENTRY5
    , DAY_ENTRY5
    ]
  , [ SGL_SIDE_WEEK_FILES[SglPagesWeek.QUT5]
    , DAY_FREE_WRITE_ENTRY[5]
    , DAY_FREE_WRITE_ENTRY[5]
    ]
  , [ SGL_SIDE_WEEK_FILES[SglPagesWeek.DAY6]
    , DAY_ENTRY6
    , DAY_ENTRY6
    ]
  , [ SGL_SIDE_WEEK_FILES[SglPagesWeek.QUT6]
    , DAY_FREE_WRITE_ENTRY[6]
    , DAY_FREE_WRITE_ENTRY[6]
    ]
  ]