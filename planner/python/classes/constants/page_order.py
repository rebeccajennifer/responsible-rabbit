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

from utils.utils import PlannerUtils as Utils

from classes.constants.addl_arg_keys import AddlArgKeys as Key
from classes.constants.strings import PlannerStrings as Strings

from classes.page_entries.day_entry import DayEntry
from classes.page_entries.free_write_entry import FreeWriteEntry
from classes.page_entries.free_write_prompt_entry import FreeWritePromptEntry
from classes.page_entries.goal_entry import GoalEntry
from classes.page_entries.month_entry import MonthEntry
from classes.page_entries.title_page import TitlePage
from classes.page_entries.week_checklist_entry import WeekCheckList
from classes.page_entries.week_entry import WeekEntry0
from classes.page_entries.week_entry import WeekEntry1


#_____________________________________________________________________
#_____________________________________________________________________
class Entries:

  # Blank page
  BLANK: dict =\
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

  WK_12: dict =\
  { Key.ENTRY_TYPE: FreeWritePromptEntry
  , Key.ENTRY_ARGS:
    { Key.HEADER_TXT: Strings.PAGE_HEADER_TXT_FUT_12W
    , Key.PROMPT_TXT: Strings.FREE_WRITE_FUT_12W
    }
  }

  NOACT: dict =\
  { Key.ENTRY_TYPE: FreeWritePromptEntry
  , Key.ENTRY_ARGS:
    { Key.HEADER_TXT: Strings.PAGE_HEADER_TXT_FUT_BAD
    , Key.PROMPT_TXT: Strings.FREE_WRITE_FUT_BAD
    }
  }

  #_____________________________________________________________________
  A_VOW: dict =\
  { Key.ENTRY_TYPE: FreeWritePromptEntry
  , Key.ENTRY_ARGS:
    { Key.HEADER_TXT: Strings.VOW_HEADER_TXT
    , Key.PROMPT_TXT: Strings.A_VOW
    }
  }

  ACTION_ITEMS: dict =\
  { Key.ENTRY_TYPE: FreeWriteEntry
  , Key.ENTRY_ARGS:
    { Key.HEADER_TXT: 'Action Items: '
    }
  }

  #_____________________________________________________________________
  # Populate day and quote pages with variable string
  #_____________________________________________________________________
  DAY : list = []
  QUT : list = []

  for i in range(7):
    DAY.append\
    ( { Key.ENTRY_TYPE: DayEntry
      , Key.ENTRY_ARGS: {Key.CYCLING_PROMPT_IDX: i}
      }
    )

    QUT.append\
    ( { Key.ENTRY_TYPE: FreeWriteEntry
      , Key.ENTRY_ARGS: {Key.HEADER_TXT: Strings.QUOTES[i]}
      }
    )
  #_____________________________________________________________________

  MONTH: dict =\
    { Key.ENTRY_TYPE: MonthEntry
    , Key.ENTRY_ARGS: {}
    }

  #_____________________________________________________________________
  WEEK_0: dict =\
    { Key.ENTRY_TYPE: WeekEntry0
    , Key.ENTRY_ARGS: {}
    }
  WEEK_1: dict =\
    { Key.ENTRY_TYPE: WeekEntry1
    , Key.ENTRY_ARGS: {}
    }

  #_____________________________________________________________________
  GOALS: dict =\
    { Key.ENTRY_TYPE: GoalEntry
    , Key.ENTRY_ARGS: {}
    }


  DATES: dict =\
    { Key.ENTRY_TYPE: FreeWriteEntry
    , Key.ENTRY_ARGS: {Key.HEADER_TXT: 'Important Dates'}
    }


#_______________________________________________________________________
class DblSidePages:
  """
  Defines and organizes configuration data for double sided pages.
  """
  #_____________________________________________________________________
  # List of layouts
  #_____________________________________________________________________
  INTR_LAYOUTS: list =\
  [ [Entries.TITLE, Entries.BLANK]
  , [Entries.BLANK, Entries.BLANK]
  , [Entries.YR1_0, Entries.YR1_1]
  , [Entries.WK_12, Entries.YR5_1]
  , [Entries.YR5_0, Entries.NOACT]
  , [Entries.A_VOW, Entries.BLANK]
  , [Entries.GOALS, Entries.GOALS]
  , [Entries.GOALS, Entries.GOALS]
  , [Entries.MONTH, Entries.MONTH]
  , [Entries.DATES, Entries.MONTH]
  ]

  #_____________________________________________________________________
  WEEK_LAYOUTS: list =\
  [ [Entries.DAY[3] , Entries.QUT[3]]
  , [Entries.DAY[4] , Entries.QUT[2]]
  , [Entries.DAY[2] , Entries.QUT[4]]
  , [Entries.DAY[5] , Entries.QUT[1]]
  , [Entries.DAY[1] , Entries.QUT[5]]
  , [Entries.DAY[6] , Entries.QUT[0]]
  , [Entries.DAY[0] , Entries.QUT[6]]
  , [Entries.WEEK_0 , Entries.WEEK_1]
  ]

  #_____________________________________________________________________
  # Create list of file names
  #_____________________________________________________________________
  # Intro entry file names
  #---------------------------------------------------------------------
  INTR_FILE_NAMES: list = []
  counter = Utils.inc()

  for i in range(len(INTR_LAYOUTS)):
    INTR_FILE_NAMES.append('0__intr__' + str(next(counter)))

  #---------------------------------------------------------------------
  # Week entry file names
  #---------------------------------------------------------------------
  WEEK_FILE_NAMES: list = []
  counter = Utils.inc()

  for i in range(len(WEEK_LAYOUTS)):
    WEEK_FILE_NAMES.append('1__week__' + str(next(counter)))

  #_____________________________________________________________________
  # Generate list of layouts with file names
  #_____________________________________________________________________
  # Intro entry files
  PAGE_ORDER: list = []
  for i in range(len(INTR_LAYOUTS)):
    page: list = [INTR_FILE_NAMES[i]] + INTR_LAYOUTS[i]
    PAGE_ORDER.append(page)

  # Week entry files
  for i in range(len(WEEK_LAYOUTS)):
    page: list = [WEEK_FILE_NAMES[i]] + WEEK_LAYOUTS[i]
    PAGE_ORDER.append(page)

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
  [ [ '00-action-items'             , Entries.ACTION_ITEMS, Entries.ACTION_ITEMS  ]

  , [ INTR_FILES[IntrPgNo.TTL_F_1YR], Entries.TITLE, Entries.YR1_1 ]
  , [ INTR_FILES[IntrPgNo.F_5YR_12W], Entries.YR5_0, Entries.WK_12 ]
  , [ INTR_FILES[IntrPgNo.F_5YR_BAD], Entries.YR5_1, Entries.NOACT ]
  , [ INTR_FILES[IntrPgNo.F_1YR_VOW], Entries.YR1_0, Entries.A_VOW ]
  , [ INTR_FILES[IntrPgNo.GOALS_0_1], Entries.GOALS, Entries.GOALS ]
  , [ INTR_FILES[IntrPgNo.GOALS_2_3], Entries.GOALS, Entries.GOALS ]
  , [ INTR_FILES[IntrPgNo.MONTH_0_1], Entries.MONTH, Entries.MONTH ]
  , [ INTR_FILES[IntrPgNo.MONTH_2__], Entries.MONTH, Entries.DATES ]

  , [ WEEK_FILES[WeekPgNo.WK_0], Entries.WEEK_0, Entries.WEEK_0 ]
  , [ WEEK_FILES[WeekPgNo.WK_1], Entries.WEEK_1, Entries.WEEK_1 ]
  , [ WEEK_FILES[WeekPgNo.DAY0], Entries.DAY[0], Entries.DAY[0] ]
  , [ WEEK_FILES[WeekPgNo.QUT0], Entries.QUT[0], Entries.QUT[0] ]
  , [ WEEK_FILES[WeekPgNo.DAY1], Entries.DAY[1], Entries.DAY[1] ]
  , [ WEEK_FILES[WeekPgNo.QUT1], Entries.QUT[1], Entries.QUT[1] ]
  , [ WEEK_FILES[WeekPgNo.DAY2], Entries.DAY[2], Entries.DAY[2] ]
  , [ WEEK_FILES[WeekPgNo.QUT2], Entries.QUT[2], Entries.QUT[2] ]
  , [ WEEK_FILES[WeekPgNo.DAY3], Entries.DAY[3], Entries.DAY[3] ]
  , [ WEEK_FILES[WeekPgNo.QUT3], Entries.QUT[3], Entries.QUT[3] ]
  , [ WEEK_FILES[WeekPgNo.DAY4], Entries.DAY[4], Entries.DAY[4] ]
  , [ WEEK_FILES[WeekPgNo.QUT4], Entries.QUT[4], Entries.QUT[4] ]
  , [ WEEK_FILES[WeekPgNo.DAY5], Entries.DAY[5], Entries.DAY[5] ]
  , [ WEEK_FILES[WeekPgNo.QUT5], Entries.QUT[5], Entries.QUT[5] ]
  , [ WEEK_FILES[WeekPgNo.DAY6], Entries.DAY[6], Entries.DAY[6] ]
  , [ WEEK_FILES[WeekPgNo.QUT6], Entries.QUT[6], Entries.QUT[6] ]
  ]