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

from utils.utils import PlannerUtils as Utils

from classes.constants.addl_arg_keys import AddlArgKeys as Key
from classes.constants.strings import PlannerStrings as Strings

from classes.page_entries.day_entry import DayEntry
from classes.page_entries.free_write_entry import FreeWriteEntry
from classes.page_entries.free_write_prompt_entry import FreeWritePromptEntry
from classes.page_entries.goal_entry import GoalEntry
from classes.page_entries.month_entry import MonthEntry
from classes.page_entries.title_page import TitlePage
from classes.page_entries.week_entry import WeekEntry0
from classes.page_entries.week_entry import WeekEntry1


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
  Defines and organizes configuration data for double sided pages.
  """
  #_____________________________________________________________________
  # List of layouts
  #_____________________________________________________________________
  INTR_LAYOUTS: list =\
  [ [Entries.TITLE, Entries.GOALS]
  , [Entries.YR5_0, Entries.GOALS]
  , [Entries.YR5_1, Entries.GOALS]
  , [Entries.YR1_0, Entries.GOALS]
  , [Entries.YR1_1, Entries.MONTH]
  , [Entries.WK_12, Entries.MONTH]
  , [Entries.NOACT, Entries.MONTH]
  , [Entries.A_VOW, Entries.DATES]
  ]

  #_____________________________________________________________________
  WEEK_LAYOUTS: list =\
  [ [Entries.WEEK_0 , Entries.WEEK_0]
  , [Entries.WEEK_1 , Entries.WEEK_1]
  , [Entries.DAY[0] , Entries.DAY[0]]
  , [Entries.QUT[0] , Entries.QUT[0]]
  , [Entries.DAY[1] , Entries.DAY[1]]
  , [Entries.QUT[1] , Entries.QUT[1]]
  , [Entries.DAY[2] , Entries.DAY[2]]
  , [Entries.QUT[2] , Entries.QUT[2]]
  , [Entries.DAY[3] , Entries.DAY[3]]
  , [Entries.QUT[3] , Entries.QUT[3]]
  , [Entries.DAY[4] , Entries.DAY[4]]
  , [Entries.QUT[4] , Entries.QUT[4]]
  , [Entries.DAY[5] , Entries.DAY[5]]
  , [Entries.QUT[5] , Entries.QUT[5]]
  , [Entries.DAY[6] , Entries.DAY[6]]
  , [Entries.QUT[6] , Entries.QUT[6]]
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
