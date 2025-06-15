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

from classes.constants.addl_arg_keys import AddlArgKeys as Key
from classes.constants.strings import PlannerStrings as Strings

from classes.page_entries.day_entry import DayEntry
from classes.page_entries.week_entry import WeekEntry0
from classes.page_entries.week_entry import WeekEntry1
from classes.page_entries.free_write_entry import FreeWriteEntry
from classes.page_entries.title_page import TitlePage
from classes.page_entries.free_write_prompt_entry import FreeWritePromptEntry
from classes.page_entries.goal_entry import GoalEntry
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

  #_____________________________________________________________________
  BLNK_ENTRY: dict =\
    { Key.ENTRY_TYPE: FreeWriteEntry
    , Key.ENTRY_ARGS: {}
    }

  #_____________________________________________________________________
  DBL_SIDE_PAGE_ORDER: list =\
  [ [ 'page-00.svg'
    , FUTURE_1YR_ENTRY0
    , FUTURE_1YR_ENTRY1
    ]
  , [ 'page-01.svg'
    , FUTURE_12W_ENTRY
    , FUTURE_5YR_ENTRY1
    ]
  , [ 'page-02.svg'
    , FUTURE_5YR_ENTRY0
    , FUTURE_BAD_ENTRY
    ]
  , [ 'page-03.svg'
    , VOW_ENTRY
    , TITLE_PAGE
    ]
  , [ Strings.DEF_GOAL_LAYOUT_PATH
    , GOAL_ENTRY
    , GOAL_ENTRY
    ]
  , [ Strings.DEF_GOAL_LAYOUT_PATH
    , GOAL_ENTRY
    , GOAL_ENTRY
    ]
  , [ 'page-04.svg'
    , DAY_ENTRY2
    , DAY_FREE_WRITE_ENTRY[2]
    ]
  , [ 'page-05.svg'
    , DAY_ENTRY3
    , DAY_FREE_WRITE_ENTRY[3]
    ]
  , [ 'page-06.svg'
    , DAY_ENTRY1
    , DAY_FREE_WRITE_ENTRY[1]
    ]
  , [ 'page-07.svg'
    , DAY_ENTRY4
    , DAY_FREE_WRITE_ENTRY[4]
    ]
  , [ 'page-08.svg'
    , DAY_ENTRY0
    , DAY_FREE_WRITE_ENTRY[0]
    ]
  , [ 'page-09.svg'
    , DAY_ENTRY5
    , WEEK_ENTRY1
    ]
  , [ 'page-10.svg'
    , WEEK_ENTRY0
    , BLNK_ENTRY
    ]
  , [ 'page-11.svg'
    , DAY_ENTRY6
    , DAY_FREE_WRITE_ENTRY[6]
    ]
  ]

  #_____________________________________________________________________
  SGL_SIDE_PAGE_ORDER: list =\
  [ [ 'action-items.svg'
    , ACTION_ITEMS_ENTRY
    , ACTION_ITEMS_ENTRY
    ]
  , [ 'page-00.svg'
    , TITLE_PAGE
    , FUTURE_1YR_ENTRY1
    ]
  , [ 'page-01.svg'
    , FUTURE_5YR_ENTRY0
    , FUTURE_12W_ENTRY
    ]
  , [ 'page-02.svg'
    , FUTURE_5YR_ENTRY1
    , FUTURE_BAD_ENTRY
    ]
  , [ 'page-03.svg'
    , FUTURE_1YR_ENTRY0
    , VOW_ENTRY
    ]
  , [ 'page-04.svg'
    , GOAL_ENTRY
    , GOAL_ENTRY
    ]
  , [ 'page-05.svg'
    , GOAL_ENTRY
    , GOAL_ENTRY
    ]
  , [ 'page-06.svg'
    , WEEK_ENTRY0
    , WEEK_ENTRY0
    ]
  , [ 'page-07.svg'
    , WEEK_ENTRY1
    , WEEK_ENTRY1
    ]
  , [ DayEntry.DEF_DAY_LAYOUT_PATH.replace('#', '-0')
    , DAY_ENTRY0
    , DAY_ENTRY0
    ]
  , [ 'day-0-quote.svg'
    , DAY_FREE_WRITE_ENTRY[0]
    , DAY_FREE_WRITE_ENTRY[0]
    ]
  , [ DayEntry.DEF_DAY_LAYOUT_PATH.replace('#', '-1')
    , DAY_ENTRY1
    , DAY_ENTRY1
    ]
  , [ 'day-1-quote.svg'
    , DAY_FREE_WRITE_ENTRY[1]
    , DAY_FREE_WRITE_ENTRY[1]
    ]
  , [ DayEntry.DEF_DAY_LAYOUT_PATH.replace('#', '-2')
    , DAY_ENTRY2
    , DAY_ENTRY2
    ]
  , [ 'day-2-quote.svg'
    , DAY_FREE_WRITE_ENTRY[2]
    , DAY_FREE_WRITE_ENTRY[2]
    ]
  , [ DayEntry.DEF_DAY_LAYOUT_PATH.replace('#', '-3')
    , DAY_ENTRY3
    , DAY_ENTRY3
    ]
  , [ 'day-3-quote.svg'
    , DAY_FREE_WRITE_ENTRY[3]
    , DAY_FREE_WRITE_ENTRY[3]
    ]
  , [ DayEntry.DEF_DAY_LAYOUT_PATH.replace('#', '-4')
    , DAY_ENTRY4
    , DAY_ENTRY4
    ]
  , [ 'day-4-quote.svg'
    , DAY_FREE_WRITE_ENTRY[4]
    , DAY_FREE_WRITE_ENTRY[4]
    ]
  , [ DayEntry.DEF_DAY_LAYOUT_PATH.replace('#', '-5')
    , DAY_ENTRY5
    , DAY_ENTRY5
    ]
  , [ 'day-5-quote.svg'
    , DAY_FREE_WRITE_ENTRY[5]
    , DAY_FREE_WRITE_ENTRY[5]
    ]
  , [ DayEntry.DEF_DAY_LAYOUT_PATH.replace('#', '-6')
    , DAY_ENTRY6
    , DAY_ENTRY6
    ]
  , [ 'day-6-quote.svg'
    , DAY_FREE_WRITE_ENTRY[6]
    , DAY_FREE_WRITE_ENTRY[6]
    ]
  ]