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
#   Copyright 2026, Rebecca Rashkin
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


from classes.constants.addl_arg_keys import AddlArgKeys as Key
from classes.constants.strings import PlannerStrings as Strings

from classes.page_entries.day_entry_0 import DayEntry
from classes.page_entries.daily_practice_tracker import SevenDayPracticeTracker
from classes.page_entries.free_write_entry import FreeWriteEntry
from classes.page_entries.free_write_prompt_entry import FreeWritePromptEntry
from classes.page_entries.project_entry import ProjectEntry
from classes.page_entries.month_entry import MonthEntry
from classes.page_entries.night_entry import NightEntry
from classes.page_entries.title_page import TitlePage
from classes.page_entries.week_entry import WeekEntry0
from classes.page_entries.week_entry import WeekEntry1
from classes.reference_pages.ace_reference import AceReference
from classes.reference_pages.emotion_reference import EmotionReference
from classes.page_entries.ace_entry import AceEntry
from classes.page_entries.senses_wksht import SensesWksht


#_____________________________________________________________________
class Entries:

  # Blank page
  BLANKPG: dict =\
    { Key.ENTRY_TYPE: TitlePage
    , Key.ENTRY_ARGS: {Key.HEADER_TXT: ' '}
    }

  PREVIEW: dict =\
  { Key.ENTRY_TYPE: TitlePage
  , Key.ENTRY_ARGS:
    { Key.HEADER_TXT: 'Preview Only - Do Not Print'
    }
  }

  TITLEPG: dict =\
  { Key.ENTRY_TYPE: TitlePage
  , Key.ENTRY_ARGS:
    { Key.HEADER_TXT: 'Book of Plans'
    }
  }

  TRACK_7: dict =\
  { Key.ENTRY_TYPE: SevenDayPracticeTracker
  , Key.ENTRY_ARGS: {}
  }


  VISION_: dict =\
  { Key.ENTRY_TYPE: TitlePage
  , Key.ENTRY_ARGS:
    { Key.HEADER_TXT: 'The Best Version of Me'
    }
  }

  #_____________________________________________________________________
  YR_5__0: dict =\
  { Key.ENTRY_TYPE: FreeWritePromptEntry
  , Key.ENTRY_ARGS:
    { Key.HEADER_TXT: Strings.PAGE_HEADER_TXT_FUT_5YR
    , Key.PROMPT_TXT: Strings.FREE_WRITE_FUT_5YR
    }
  }

  YR_5__1: dict =\
  { Key.ENTRY_TYPE: FreeWriteEntry
  , Key.ENTRY_ARGS:
    { Key.HEADER_TXT: Strings.PAGE_HEADER_TXT_FUT_5YR
    }
  }

  YR_1__0: dict =\
  { Key.ENTRY_TYPE: FreeWritePromptEntry
  , Key.ENTRY_ARGS:
    { Key.HEADER_TXT: Strings.PAGE_HEADER_TXT_FUT_1YR
    , Key.PROMPT_TXT: Strings.FREE_WRITE_FUT_1YR
    }
  }

  YR_1__1: dict =\
  { Key.ENTRY_TYPE: FreeWriteEntry
  , Key.ENTRY_ARGS:
    { Key.HEADER_TXT: Strings.PAGE_HEADER_TXT_FUT_1YR
    }
  }

  WEEK_12: dict =\
  { Key.ENTRY_TYPE: FreeWritePromptEntry
  , Key.ENTRY_ARGS:
    { Key.HEADER_TXT: Strings.PAGE_HEADER_TXT_FUT_12W
    , Key.PROMPT_TXT: Strings.FREE_WRITE_FUT_12W
    }
  }

  INACTIO: dict =\
  { Key.ENTRY_TYPE: FreeWritePromptEntry
  , Key.ENTRY_ARGS:
    { Key.HEADER_TXT: Strings.PAGE_HEADER_TXT_FUT_BAD
    , Key.PROMPT_TXT: Strings.FREE_WRITE_FUT_BAD
    }
  }

  #_____________________________________________________________________
  COMMITM: dict =\
  { Key.ENTRY_TYPE: FreeWritePromptEntry
  , Key.ENTRY_ARGS:
    { Key.HEADER_TXT: Strings.VOW_HEADER_TXT
    , Key.PROMPT_TXT: Strings.COMMITM
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
  DAY__ : list = []
  QUOTE : list = []

  for i in range(7):
    DAY__.append\
    ( { Key.ENTRY_TYPE: DayEntry
      , Key.ENTRY_ARGS: {Key.CYCLING_PROMPT_IDX: i}
      }
    )

    QUOTE.append\
    ( { Key.ENTRY_TYPE: FreeWriteEntry
      , Key.ENTRY_ARGS: {Key.HEADER_TXT: Strings.QUOTES[i]}
      }
    )
  #_____________________________________________________________________

  NIGHTLY: dict =\
    { Key.ENTRY_TYPE: NightEntry
    , Key.ENTRY_ARGS: {Key.HEADER_TXT: 'Daily Reflection'}
    }

  CALENDR: dict =\
    { Key.ENTRY_TYPE: MonthEntry
    , Key.ENTRY_ARGS: {}
    }

  #_____________________________________________________________________
  WEEK___0: dict =\
    { Key.ENTRY_TYPE: WeekEntry0
    , Key.ENTRY_ARGS: {}
    }
  WEEK___1: dict =\
    { Key.ENTRY_TYPE: WeekEntry1
    , Key.ENTRY_ARGS: {}
    }

  #_____________________________________________________________________
  PROJECT: dict =\
    { Key.ENTRY_TYPE: ProjectEntry
    , Key.ENTRY_ARGS: {}
    }

  DATES__: dict =\
    { Key.ENTRY_TYPE: FreeWriteEntry
    , Key.ENTRY_ARGS: {Key.HEADER_TXT: 'Important Dates'}
    }

  ACE_REF: dict =\
    { Key.ENTRY_TYPE: AceReference
    , Key.ENTRY_ARGS: {}
    }

  ACEWKSH: dict =\
    { Key.ENTRY_TYPE: AceEntry
    , Key.ENTRY_ARGS: {}
    }

  SENSEEX: dict =\
    { Key.ENTRY_TYPE: SensesWksht
    , Key.ENTRY_ARGS: {}
    }

  EMO_REF: dict =\
    { Key.ENTRY_TYPE: EmotionReference
    , Key.ENTRY_ARGS: {}
    }
