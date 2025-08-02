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
from classes.constants.addl_arg_keys import AddlArgKeys as Keys


#_______________________________________________________________________
class PdfPrefix:
  """
  File prefixes for grouped PDFs.
  """

  INTR: str = '0__intr__'
  WEEK: str = '1__week__'
  XTRA: str = '2__xtra__'
  NITE: str = '3__nite__'
  ACE_: str = '3__ace___'

#_______________________________________________________________________
class OptionlPages:
  """
  Defines and organizes configuration data for additional optional
  pages that can be inserted.
  """

  XTRA_LAYOUTS: list =\
  [ [Entries.ACEPG, Entries.ACEPG]
  , [Entries.ACEPG, Entries.ACEPG]
  , [Entries.NIGHT, Entries.NIGHT]
  , [Entries.ACERF, Entries.ACERF]
  , [Entries.ACEPG, Entries.ACEPG]
  ]

  XTRA_LAYOUTS_DICT: list =\
  [ {Keys.LEFT: Entries.ACEPG, Keys.RGHT: Entries.ACEPG}
  , {Keys.LEFT: Entries.ACEPG, Keys.RGHT: Entries.ACEPG}
  , {Keys.LEFT: Entries.NIGHT, Keys.RGHT: Entries.NIGHT}
  , {Keys.LEFT: Entries.ACERF, Keys.RGHT: Entries.ACERF}
  , {Keys.LEFT: Entries.ACEPG, Keys.RGHT: Entries.ACEPG}
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

  INTR_LAYOUTS_DICT: list =\
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

  WEEK_LAYOUTS_DICT: list =\
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

  INTR_LAYOUTS_DICT: list =\
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
  [ [Entries.DAY[3] , Entries.QUT[3]]
  , [Entries.DAY[4] , Entries.QUT[2]]
  , [Entries.DAY[2] , Entries.QUT[4]]
  , [Entries.DAY[5] , Entries.QUT[1]]
  , [Entries.DAY[1] , Entries.QUT[5]]
  , [Entries.DAY[6] , Entries.QUT[0]]
  , [Entries.DAY[0] , Entries.QUT[6]]
  , [Entries.WEEK_0 , Entries.WEEK_1]
  ]

  WEEK_LAYOUTS_DICT: list =\
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

  #_____________________________________________________________________

#_______________________________________________________________________
class PageOrder(list):
  """
  List of files names and associated layouts. Takes the following form:

    [ [ 'group_0_pdf_0'
      , {'entry_type': LeftEntry, 'entry_args: {}'}
      , {'entry_type': RghtEntry, 'entry_args: {}'}
      ]
    , [ 'group_0_pdf_1'
      , {'entry_type': LeftEntry, 'entry_args: {}'}
      , {'entry_type': RghtEntry, 'entry_args: {}'}
      ]
    , [ 'group_1_pdf_0'
      , {'entry_type': LeftEntry, 'entry_args: {}'}
      , {'entry_type': RghtEntry, 'entry_args: {}'}
      ]
    , [ 'group_1_pdf_1'
      , {'entry_type': LeftEntry, 'entry_args: {}'}
      , {'entry_type': RghtEntry, 'entry_args: {}'}
      ]
    , [ 'group_2_pdf_0'
      , {'entry_type': LeftEntry, 'entry_args: {}'}
      , {'entry_type': RghtEntry, 'entry_args: {}'}
      ]
    , [ 'group_2_pdf_1'
      , {'entry_type': LeftEntry, 'entry_args: {}'}
      , {'entry_type': RghtEntry, 'entry_args: {}'}
      ]
    ]
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
    xtra_layouts   : list = OptionlPages.XTRA_LAYOUTS
    intr_layouts   : list = OneSidePages.INTR_LAYOUTS
    week_layouts   : list = OneSidePages.WEEK_LAYOUTS

    if (is_preview):
      intr_layouts : list = PreviewPages.INTR_LAYOUTS
      week_layouts : list = PreviewPages.WEEK_LAYOUTS

    elif (is_dbl_sided):
      intr_layouts    = DblSidePages.INTR_LAYOUTS
      week_layouts    = DblSidePages.WEEK_LAYOUTS

    #___________________________________________________________________
    # Generate file names and add page groups

    self.intr_file_names: list =\
      self.add_page_group(intr_layouts, PdfPrefix.INTR)

    self.week_file_names: list =\
      self.add_page_group(week_layouts, PdfPrefix.WEEK)

    self.xtra_file_names: list =\
      self.add_page_group(xtra_layouts, PdfPrefix.XTRA)

    return

  #_____________________________________________________________________
  def add_page_group(self, layouts: list, name_prefix: str) -> list:
    """
    Adds groups of pdfs to page order. Each element in self takes
    the following format:

      [ 'group_0_pdf_0'
      , {'entry_type': LeftEntry, 'entry_args: {}'}
      , {'entry_type': RghtEntry, 'entry_args: {}'}
      ]

    Parameters:
      layouts     : List of layouts in the following form:
                    [ [ {'entry_type': LeftEntry, 'entry_args: {}'}
                      , {'entry_type': RghtEntry, 'entry_args: {}'}
                      ]
                    , [ {'entry_type': LeftEntry, 'entry_args: {}'}
                      , {'entry_type': RghtEntry, 'entry_args: {}'}
                      ]
                    ]

      name_prefix : Prefix given to all pdf file names in the group

    Returns:
      list of file names for group
    """

    file_name_list: list = []

    counter = Utils.inc()

    # Extra entry files
    for i in range(len(layouts)):
      file_name: str = name_prefix + str(next(counter))
      file_name_list.append(file_name)

      page: list = [file_name] + layouts[i]
      self.append(page)

    return file_name_list

