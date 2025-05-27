from classes.constants.addl_arg_keys import AddlArgKeys as Key
from classes.constants.strings import PlannerStrings as Strings

from classes.page_entries.day_entry import DayEntry
from classes.page_entries.week_entry import WeekEntry0
from classes.page_entries.week_entry import WeekEntry1
from classes.page_entries.free_write_entry import FreeWriteEntry
from classes.page_entries.free_write_prompt_entry import FreeWritePromptEntry
from classes.page_entries.goal_entry import GoalEntry

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

  DAY_ENTRY0 : dict =\
    { Key.ENTRY_TYPE: DayEntry
    , Key.ENTRY_ARGS: {Key.CYCLING_PROMPT_IDX: 0}
    }
  DAY_ENTRY1 : dict =\
    { Key.ENTRY_TYPE: DayEntry
    , Key.ENTRY_ARGS: {Key.CYCLING_PROMPT_IDX: 1}
    }
  DAY_ENTRY2 : dict =\
    { Key.ENTRY_TYPE: DayEntry
    , Key.ENTRY_ARGS: {Key.CYCLING_PROMPT_IDX: 2}
    }
  DAY_ENTRY3 : dict =\
    { Key.ENTRY_TYPE: DayEntry
    , Key.ENTRY_ARGS: {Key.CYCLING_PROMPT_IDX: 3}
    }
  DAY_ENTRY4 : dict =\
    { Key.ENTRY_TYPE: DayEntry
    , Key.ENTRY_ARGS: {Key.CYCLING_PROMPT_IDX: 4}
    }
  DAY_ENTRY5 : dict =\
    { Key.ENTRY_TYPE: DayEntry
    , Key.ENTRY_ARGS: {Key.CYCLING_PROMPT_IDX: 5}
    }
  DAY_ENTRY6 : dict =\
    { Key.ENTRY_TYPE: DayEntry
    , Key.ENTRY_ARGS: {Key.CYCLING_PROMPT_IDX: 6}
    }

  WEEK_ENTRY0: dict =\
    { Key.ENTRY_TYPE: WeekEntry0
    , Key.ENTRY_ARGS: {}
    }
  WEEK_ENTRY1: dict =\
    { Key.ENTRY_TYPE: WeekEntry1
    , Key.ENTRY_ARGS: {}
    }

  GOAL_ENTRY: dict =\
    { Key.ENTRY_TYPE: GoalEntry
    , Key.ENTRY_ARGS: {}
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
  , [ Strings.DEF_DAY_LAYOUT_PATH.replace('#', '-0')
    , DAY_ENTRY0
    , DAY_ENTRY0
    ]
  , [ Strings.DEF_DAY_LAYOUT_PATH.replace('#', '-1')
    , DAY_ENTRY1
    , DAY_ENTRY1
    ]
  , [ Strings.DEF_DAY_LAYOUT_PATH.replace('#', '-2')
    , DAY_ENTRY2
    , DAY_ENTRY2
    ]
  , [ Strings.DEF_DAY_LAYOUT_PATH.replace('#', '-3')
    , DAY_ENTRY3
    , DAY_ENTRY3
    ]
  , [ Strings.DEF_DAY_LAYOUT_PATH.replace('#', '-4')
    , DAY_ENTRY4
    , DAY_ENTRY4
    ]
  , [ Strings.DEF_DAY_LAYOUT_PATH.replace('#', '-5')
    , DAY_ENTRY5
    , DAY_ENTRY5
    ]
  , [ Strings.DEF_DAY_LAYOUT_PATH.replace('#', '-6')
    , DAY_ENTRY6
    , DAY_ENTRY6
    ]
  , [ Strings.DEF_WEEK_LAYOUT_PATH
    , WEEK_ENTRY0
    , WEEK_ENTRY1
    ]
  , [ Strings.DEF_GOAL_LAYOUT_PATH
    , GOAL_ENTRY
    , GOAL_ENTRY
    ]
  ]


