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
class NightlyPages:
  """
  Nightly reflection pages.
  """

  LAYOUTS: list =\
  [ {Keys.LEFT: Entries.NIGHTLY, Keys.RGHT: Entries.NIGHTLY}
  , {Keys.LEFT: Entries.NIGHTLY, Keys.RGHT: Entries.NIGHTLY}
  ]


#_______________________________________________________________________
class AceRefrPages:
  """
  ACE reference pages.
  """

  LAYOUTS: list =\
  [ {Keys.LEFT: Entries.ACE_REF, Keys.RGHT: Entries.EMO_REF}
  ]


#_______________________________________________________________________
class AceWkshPages:
  """
  ACE worksheet pages.
  """
  LAYOUTS: list =\
  [ {Keys.LEFT: Entries.ACEWKSH, Keys.RGHT: Entries.SENSEEX}
  , {Keys.LEFT: Entries.SENSEEX, Keys.RGHT: Entries.ACEWKSH}
  ]

#_______________________________________________________________________
class SenseExPages:
  """
  Five Senses grounding exercise pages.
  """
  LAYOUTS: list =\
  [ {Keys.LEFT: Entries.SENSEEX, Keys.RGHT: Entries.SENSEEX}
  , {Keys.LEFT: Entries.SENSEEX, Keys.RGHT: Entries.SENSEEX}
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
  [ {Keys.LEFT: Entries.PREVIEW, Keys.RGHT: Entries.TITLEPG}
  , {Keys.LEFT: Entries.YR_5__0, Keys.RGHT: Entries.YR_5__1}
  , {Keys.LEFT: Entries.YR_1__0, Keys.RGHT: Entries.YR_1__1}
  , {Keys.LEFT: Entries.WEEK_12, Keys.RGHT: Entries.INACTIO}
  , {Keys.LEFT: Entries.COMMITM, Keys.RGHT: Entries.BLANKPG}
  , {Keys.LEFT: Entries.PROJECT, Keys.RGHT: Entries.PROJECT}
  , {Keys.LEFT: Entries.PROJECT, Keys.RGHT: Entries.PROJECT}
  , {Keys.LEFT: Entries.CALENDR, Keys.RGHT: Entries.CALENDR}
  , {Keys.LEFT: Entries.CALENDR, Keys.RGHT: Entries.DATES__}
  ]


  #_____________________________________________________________________
  WEEK_LAYOUTS: list =\
  [ {Keys.LEFT: Entries.WEEK___0 , Keys.RGHT: Entries.WEEK___1}
  , {Keys.LEFT: Entries.DAY__[0] , Keys.RGHT: Entries.QUOTE[0]}
  , {Keys.LEFT: Entries.DAY__[1] , Keys.RGHT: Entries.QUOTE[1]}
  , {Keys.LEFT: Entries.DAY__[2] , Keys.RGHT: Entries.QUOTE[2]}
  , {Keys.LEFT: Entries.DAY__[3] , Keys.RGHT: Entries.QUOTE[3]}
  , {Keys.LEFT: Entries.DAY__[4] , Keys.RGHT: Entries.QUOTE[4]}
  , {Keys.LEFT: Entries.DAY__[5] , Keys.RGHT: Entries.QUOTE[5]}
  , {Keys.LEFT: Entries.DAY__[6] , Keys.RGHT: Entries.QUOTE[6]}
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
  [ {Keys.LEFT: Entries.COMMITM, Keys.RGHT: Entries.PROJECT}
  , {Keys.LEFT: Entries.PROJECT, Keys.RGHT: Entries.INACTIO}
  , {Keys.LEFT: Entries.WEEK_12, Keys.RGHT: Entries.PROJECT}
  , {Keys.LEFT: Entries.PROJECT, Keys.RGHT: Entries.YR_1__1}
  , {Keys.LEFT: Entries.YR_1__0, Keys.RGHT: Entries.CALENDR}
  , {Keys.LEFT: Entries.CALENDR, Keys.RGHT: Entries.YR_5__1}
  , {Keys.LEFT: Entries.YR_5__0, Keys.RGHT: Entries.CALENDR}
  , {Keys.LEFT: Entries.DATES__, Keys.RGHT: Entries.VISION_}
  , {Keys.LEFT: Entries.BLANKPG, Keys.RGHT: Entries.ACTION_ITEMS}
  , {Keys.LEFT: Entries.ACTION_ITEMS, Keys.RGHT: Entries.TITLEPG}
  ]

  #_____________________________________________________________________
  WEEK_LAYOUTS: list =\
  [ {Keys.LEFT: Entries.DAY__[3] ,Keys.RGHT: Entries.QUOTE[3]}
  , {Keys.LEFT: Entries.DAY__[4] ,Keys.RGHT: Entries.QUOTE[2]}
  , {Keys.LEFT: Entries.DAY__[2] ,Keys.RGHT: Entries.QUOTE[4]}
  , {Keys.LEFT: Entries.DAY__[5] ,Keys.RGHT: Entries.QUOTE[1]}
  , {Keys.LEFT: Entries.DAY__[1] ,Keys.RGHT: Entries.QUOTE[5]}
  , {Keys.LEFT: Entries.DAY__[6] ,Keys.RGHT: Entries.QUOTE[0]}
  , {Keys.LEFT: Entries.DAY__[0] ,Keys.RGHT: Entries.QUOTE[6]}
  , {Keys.LEFT: Entries.WEEK___0 ,Keys.RGHT: Entries.WEEK___1}
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
  [ {Keys.LEFT: Entries.TITLEPG, Keys.RGHT: Entries.PROJECT}
  , {Keys.LEFT: Entries.YR_5__0, Keys.RGHT: Entries.PROJECT}
  , {Keys.LEFT: Entries.YR_5__1, Keys.RGHT: Entries.PROJECT}
  , {Keys.LEFT: Entries.YR_1__0, Keys.RGHT: Entries.PROJECT}
  , {Keys.LEFT: Entries.YR_1__1, Keys.RGHT: Entries.CALENDR}
  , {Keys.LEFT: Entries.WEEK_12, Keys.RGHT: Entries.CALENDR}
  , {Keys.LEFT: Entries.INACTIO, Keys.RGHT: Entries.CALENDR}
  , {Keys.LEFT: Entries.COMMITM, Keys.RGHT: Entries.DATES__}
  ]


  #_____________________________________________________________________
  WEEK_LAYOUTS: list =\
  [ {Keys.LEFT: Entries.WEEK___0 , Keys.RGHT: Entries.WEEK___0}
  , {Keys.LEFT: Entries.WEEK___1 , Keys.RGHT: Entries.WEEK___1}
  , {Keys.LEFT: Entries.DAY__[0] , Keys.RGHT: Entries.DAY__[0]}
  , {Keys.LEFT: Entries.QUOTE[0] , Keys.RGHT: Entries.QUOTE[0]}
  , {Keys.LEFT: Entries.DAY__[1] , Keys.RGHT: Entries.DAY__[1]}
  , {Keys.LEFT: Entries.QUOTE[1] , Keys.RGHT: Entries.QUOTE[1]}
  , {Keys.LEFT: Entries.DAY__[2] , Keys.RGHT: Entries.DAY__[2]}
  , {Keys.LEFT: Entries.QUOTE[2] , Keys.RGHT: Entries.QUOTE[2]}
  , {Keys.LEFT: Entries.DAY__[3] , Keys.RGHT: Entries.DAY__[3]}
  , {Keys.LEFT: Entries.QUOTE[3] , Keys.RGHT: Entries.QUOTE[3]}
  , {Keys.LEFT: Entries.DAY__[4] , Keys.RGHT: Entries.DAY__[4]}
  , {Keys.LEFT: Entries.QUOTE[4] , Keys.RGHT: Entries.QUOTE[4]}
  , {Keys.LEFT: Entries.DAY__[5] , Keys.RGHT: Entries.DAY__[5]}
  , {Keys.LEFT: Entries.QUOTE[5] , Keys.RGHT: Entries.QUOTE[5]}
  , {Keys.LEFT: Entries.DAY__[6] , Keys.RGHT: Entries.DAY__[6]}
  , {Keys.LEFT: Entries.QUOTE[6] , Keys.RGHT: Entries.QUOTE[6]}
  ]
