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
#   This module contains the entry objects used to generate layouts.
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
from classes.page_entries.night_entry import NightEntry
from classes.page_entries.title_page import TitlePage
from classes.page_entries.week_entry import WeekEntry0
from classes.page_entries.week_entry import WeekEntry1
from classes.reference_pages.ace_reference import AceReference
from classes.reference_pages.emotion_reference import EmotionReference
from classes.page_entries.ace_entry import AceEntry


#_____________________________________________________________________
class Entries:

  # Blank page
  BLANK: dict =\
    { Key.ENTRY_TYPE: TitlePage
    , Key.ENTRY_ARGS: {Key.HEADER_TXT: ' '}
    }

  PREVW: dict =\
  { Key.ENTRY_TYPE: TitlePage
  , Key.ENTRY_ARGS:
    { Key.HEADER_TXT: 'Preview Only - Do Not Print'
    }
  }

  TITLE: dict =\
  { Key.ENTRY_TYPE: TitlePage
  , Key.ENTRY_ARGS:
    { Key.HEADER_TXT: 'Book of Plans'
    }
  }

  BEST_: dict =\
  { Key.ENTRY_TYPE: TitlePage
  , Key.ENTRY_ARGS:
    { Key.HEADER_TXT: 'The Best Version of Me'
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

  NIGHT: dict =\
    { Key.ENTRY_TYPE: NightEntry
    , Key.ENTRY_ARGS: {Key.HEADER_TXT: 'Daily Reflection'}
    }

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

  ACERF: dict =\
    { Key.ENTRY_TYPE: AceReference
    , Key.ENTRY_ARGS: {}
    }

  ACEPG: dict =\
    { Key.ENTRY_TYPE: AceEntry
    , Key.ENTRY_ARGS: {}
    }

  EMORF: dict =\
    { Key.ENTRY_TYPE: EmotionReference
    , Key.ENTRY_ARGS: {}
    }