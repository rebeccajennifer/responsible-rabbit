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
from utils.utils import PlannerUtils as Utils


#_______________________________________________________________________
class OptionlPages:
  """
  Defines and organizes configuration data for additional optional
  pages that can be inserted.
  """

  XTRA_LAYOUTS: list =\
  [ [Entries.NIGHT, Entries.NIGHT]
  , [Entries.ACERF, Entries.ACERF]
  ]

  #---------------------------------------------------------------------
  # Extra entry file names
  #---------------------------------------------------------------------
  XTRA_FILE_NAMES: list = []
  counter = Utils.inc()

  for i in range(len(XTRA_LAYOUTS)):
    XTRA_FILE_NAMES.append('2__xtra__' + str(next(counter)))

#_______________________________________________________________________
class PreviewPages:
  """
  Defines and organizes configuration data for preview of pages.
  """

  #_____________________________________________________________________
  # List of layouts
  #_____________________________________________________________________
  INTR_LAYOUTS: list =\
  [ [Entries.PREVW, Entries.TITLE]
  , [Entries.YR5_0, Entries.YR5_1]
  , [Entries.YR1_0, Entries.YR1_1]
  , [Entries.WK_12, Entries.NOACT]
  , [Entries.A_VOW, Entries.BLANK]
  , [Entries.GOALS, Entries.GOALS]
  , [Entries.GOALS, Entries.GOALS]
  , [Entries.MONTH, Entries.MONTH]
  , [Entries.MONTH, Entries.DATES]
  ]

  #_____________________________________________________________________
  WEEK_LAYOUTS: list =\
  [ [Entries.WEEK_0 , Entries.WEEK_0]
  , [Entries.WEEK_1 , Entries.WEEK_1]
  , [Entries.DAY[0] , Entries.QUT[0]]
  , [Entries.DAY[1] , Entries.QUT[1]]
  , [Entries.DAY[2] , Entries.QUT[2]]
  , [Entries.DAY[3] , Entries.QUT[3]]
  , [Entries.DAY[4] , Entries.QUT[4]]
  , [Entries.DAY[5] , Entries.QUT[5]]
  , [Entries.DAY[6] , Entries.QUT[6]]
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



#_______________________________________________________________________
class DblSidePages:
  """
  Defines and organizes configuration data for double sided pages.
  """
  #_____________________________________________________________________
  # List of layouts
  #_____________________________________________________________________
  INTR_LAYOUTS: list =\
  [ [Entries.A_VOW, Entries.GOALS]
  , [Entries.GOALS, Entries.NOACT]
  , [Entries.WK_12, Entries.GOALS]
  , [Entries.GOALS, Entries.YR1_1]
  , [Entries.YR1_0, Entries.MONTH]
  , [Entries.MONTH, Entries.YR5_1]
  , [Entries.YR5_0, Entries.MONTH]
  , [Entries.DATES, Entries.BEST_]
  , [Entries.BLANK, Entries.ACTION_ITEMS]
  , [Entries.ACTION_ITEMS, Entries.TITLE]
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


#_______________________________________________________________________
class PageOrder(list):
  """
  List of files names and associated layouts.
  """

  #_____________________________________________________________________
  def __init__\
  ( self
  , is_dbl_sided: bool = False
  , is_preview: bool = False
  ):
    """
    Parameters:
      is_dbl_sided: True if planner is intended to be printed double-
                    sided. Affects page ordering.
      is_preview:   True if preview pdfs are intended to be generated.
                    Note this page ordering is not intended to be
                    printed.
    """

    xtra_layouts: list = OptionlPages.XTRA_LAYOUTS
    xtra_file_names: list = OptionlPages.XTRA_FILE_NAMES

    intr_layouts: list = OneSidePages.INTR_LAYOUTS
    week_layouts: list = OneSidePages.WEEK_LAYOUTS

    if (is_preview):
      intr_layouts    : list = PreviewPages.INTR_LAYOUTS
      week_layouts    : list = PreviewPages.WEEK_LAYOUTS

    elif (is_dbl_sided):
      intr_layouts    = DblSidePages.INTR_LAYOUTS
      week_layouts    = DblSidePages.WEEK_LAYOUTS

    #_____________________________________________________________________
    # Create list of file names
    #_____________________________________________________________________
    # Intro entry file names
    #---------------------------------------------------------------------
    intr_file_names: list = []
    counter = Utils.inc()

    for i in range(len(intr_layouts)):
      intr_file_names.append('0__intr__' + str(next(counter)))

    #---------------------------------------------------------------------
    # Week entry file names
    #---------------------------------------------------------------------
    week_file_names: list = []
    counter = Utils.inc()

    for i in range(len(week_layouts)):
      week_file_names.append('1__week__' + str(next(counter)))

    #_____________________________________________________________________
    # Generate list of layouts with file names
    #_____________________________________________________________________
    for i in range(len(intr_layouts)):
      page: list = [intr_file_names[i]] + intr_layouts[i]
      self.append(page)

    # Week entry files
    for i in range(len(week_layouts)):
      page: list = [week_file_names[i]] + week_layouts[i]
      self.append(page)

    # Extra entry files
    for i in range(len(xtra_layouts)):
      page: list = [xtra_file_names[i]] + xtra_layouts[i]
      self.append(page)

    return
