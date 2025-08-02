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
#   This module specifies the types of planner entries and how
#   they are arranged in single- and double-sided printing formats.
#
#   Each entry is represented by a dictionary containing the entry
#   type and any additional arguments it requires. These configurations
#   enable automated generation of printable journal pages with
#   consistent formatting and content.
#_______________________________________________________________________

from classes.constants.entries import Entries
from classes.constants.addl_arg_keys import AddlArgKeys as Keys


#_______________________________________________________________________
class OptionlPages:
  """
  Defines and organizes configuration data for additional optional
  pages that can be inserted.
  """

  XTRA_LAYOUTS: list =\
  [ {Keys.LEFT: Entries.ACEPG, Keys.RGHT: Entries.ACEPG}
  , {Keys.LEFT: Entries.ACEPG, Keys.RGHT: Entries.ACEPG}
  , {Keys.LEFT: Entries.NIGHT, Keys.RGHT: Entries.NIGHT}
  , {Keys.LEFT: Entries.NIGHT, Keys.RGHT: Entries.NIGHT}
  #, {Keys.LEFT: Entries.ACERF, Keys.RGHT: Entries.ACERF}
  ]

#_______________________________________________________________________
class PreviewPages:
  """
  Defines and organizes configuration data for preview of pages.
  """

  #_____________________________________________________________________
  # List of layouts
  #_____________________________________________________________________
  INTR_LAYOUTS: list =\
  [ {Keys.LEFT: Entries.PREVW, Keys.RGHT: Entries.TITLE}
  , {Keys.LEFT: Entries.YR5_0, Keys.RGHT: Entries.YR5_1}
  , {Keys.LEFT: Entries.YR1_0, Keys.RGHT: Entries.YR1_1}
  , {Keys.LEFT: Entries.WK_12, Keys.RGHT: Entries.NOACT}
  , {Keys.LEFT: Entries.A_VOW, Keys.RGHT: Entries.BLANK}
  , {Keys.LEFT: Entries.GOALS, Keys.RGHT: Entries.GOALS}
  , {Keys.LEFT: Entries.GOALS, Keys.RGHT: Entries.GOALS}
  , {Keys.LEFT: Entries.MONTH, Keys.RGHT: Entries.MONTH}
  , {Keys.LEFT: Entries.MONTH, Keys.RGHT: Entries.DATES}
  ]


  #_____________________________________________________________________
  WEEK_LAYOUTS: list =\
  [ {Keys.LEFT: Entries.WEEK_0 , Keys.RGHT: Entries.WEEK_0}
  , {Keys.LEFT: Entries.WEEK_1 , Keys.RGHT: Entries.WEEK_1}
  , {Keys.LEFT: Entries.DAY[0] , Keys.RGHT: Entries.QUT[0]}
  , {Keys.LEFT: Entries.DAY[1] , Keys.RGHT: Entries.QUT[1]}
  , {Keys.LEFT: Entries.DAY[2] , Keys.RGHT: Entries.QUT[2]}
  , {Keys.LEFT: Entries.DAY[3] , Keys.RGHT: Entries.QUT[3]}
  , {Keys.LEFT: Entries.DAY[4] , Keys.RGHT: Entries.QUT[4]}
  , {Keys.LEFT: Entries.DAY[5] , Keys.RGHT: Entries.QUT[5]}
  , {Keys.LEFT: Entries.DAY[6] , Keys.RGHT: Entries.QUT[6]}
  ]


#_______________________________________________________________________
class DblSidePages:
  """
  Defines and organizes configuration data for double sided pages.
  """
  #_____________________________________________________________________
  # List of layouts
  #_____________________________________________________________________
  INTR_LAYOUTS: list =\
  [ {Keys.LEFT: Entries.A_VOW, Keys.RGHT: Entries.GOALS}
  , {Keys.LEFT: Entries.GOALS, Keys.RGHT: Entries.NOACT}
  , {Keys.LEFT: Entries.WK_12, Keys.RGHT: Entries.GOALS}
  , {Keys.LEFT: Entries.GOALS, Keys.RGHT: Entries.YR1_1}
  , {Keys.LEFT: Entries.YR1_0, Keys.RGHT: Entries.MONTH}
  , {Keys.LEFT: Entries.MONTH, Keys.RGHT: Entries.YR5_1}
  , {Keys.LEFT: Entries.YR5_0, Keys.RGHT: Entries.MONTH}
  , {Keys.LEFT: Entries.DATES, Keys.RGHT: Entries.BEST_}
  , {Keys.LEFT: Entries.BLANK, Keys.RGHT: Entries.ACTION_ITEMS}
  , {Keys.LEFT: Entries.ACTION_ITEMS, Keys.RGHT: Entries.TITLE}
  ]

  #_____________________________________________________________________
  WEEK_LAYOUTS: list =\
  [ {Keys.LEFT: Entries.DAY[3] ,Keys.RGHT: Entries.QUT[3]}
  , {Keys.LEFT: Entries.DAY[4] ,Keys.RGHT: Entries.QUT[2]}
  , {Keys.LEFT: Entries.DAY[2] ,Keys.RGHT: Entries.QUT[4]}
  , {Keys.LEFT: Entries.DAY[5] ,Keys.RGHT: Entries.QUT[1]}
  , {Keys.LEFT: Entries.DAY[1] ,Keys.RGHT: Entries.QUT[5]}
  , {Keys.LEFT: Entries.DAY[6] ,Keys.RGHT: Entries.QUT[0]}
  , {Keys.LEFT: Entries.DAY[0] ,Keys.RGHT: Entries.QUT[6]}
  , {Keys.LEFT: Entries.WEEK_0 ,Keys.RGHT: Entries.WEEK_1}
  ]


#_______________________________________________________________________
class OneSidePages:
  """
  Defines and organizes configuration data for double sided pages.
  """
  #_____________________________________________________________________
  # List of layouts
  #_____________________________________________________________________
  INTR_LAYOUTS: list =\
  [ {Keys.LEFT: Entries.TITLE, Keys.RGHT: Entries.GOALS}
  , {Keys.LEFT: Entries.YR5_0, Keys.RGHT: Entries.GOALS}
  , {Keys.LEFT: Entries.YR5_1, Keys.RGHT: Entries.GOALS}
  , {Keys.LEFT: Entries.YR1_0, Keys.RGHT: Entries.GOALS}
  , {Keys.LEFT: Entries.YR1_1, Keys.RGHT: Entries.MONTH}
  , {Keys.LEFT: Entries.WK_12, Keys.RGHT: Entries.MONTH}
  , {Keys.LEFT: Entries.NOACT, Keys.RGHT: Entries.MONTH}
  , {Keys.LEFT: Entries.A_VOW, Keys.RGHT: Entries.DATES}
  ]


  #_____________________________________________________________________
  WEEK_LAYOUTS: list =\
  [ {Keys.LEFT: Entries.WEEK_0 , Keys.RGHT: Entries.WEEK_0}
  , {Keys.LEFT: Entries.WEEK_1 , Keys.RGHT: Entries.WEEK_1}
  , {Keys.LEFT: Entries.DAY[0] , Keys.RGHT: Entries.DAY[0]}
  , {Keys.LEFT: Entries.QUT[0] , Keys.RGHT: Entries.QUT[0]}
  , {Keys.LEFT: Entries.DAY[1] , Keys.RGHT: Entries.DAY[1]}
  , {Keys.LEFT: Entries.QUT[1] , Keys.RGHT: Entries.QUT[1]}
  , {Keys.LEFT: Entries.DAY[2] , Keys.RGHT: Entries.DAY[2]}
  , {Keys.LEFT: Entries.QUT[2] , Keys.RGHT: Entries.QUT[2]}
  , {Keys.LEFT: Entries.DAY[3] , Keys.RGHT: Entries.DAY[3]}
  , {Keys.LEFT: Entries.QUT[3] , Keys.RGHT: Entries.QUT[3]}
  , {Keys.LEFT: Entries.DAY[4] , Keys.RGHT: Entries.DAY[4]}
  , {Keys.LEFT: Entries.QUT[4] , Keys.RGHT: Entries.QUT[4]}
  , {Keys.LEFT: Entries.DAY[5] , Keys.RGHT: Entries.DAY[5]}
  , {Keys.LEFT: Entries.QUT[5] , Keys.RGHT: Entries.QUT[5]}
  , {Keys.LEFT: Entries.DAY[6] , Keys.RGHT: Entries.DAY[6]}
  , {Keys.LEFT: Entries.QUT[6] , Keys.RGHT: Entries.QUT[6]}
  ]
  #_____________________________________________________________________