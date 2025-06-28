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
#   Entry for month calendar.
#_______________________________________________________________________

import svgwrite.container
from copy import deepcopy


from classes.constants.strings import PlannerStrings as Strings
from classes.elements.table import SingleLineTable
from classes.style.std_styles import StdTextBoxStyles

from classes.page_layouts.half_letter_one_page import OnePageHalfLetter


#_______________________________________________________________________
class MonthEntry(OnePageHalfLetter):
  """
  Daily entry layout.
  """

  HEADER_TXT: str =\
    'Month #'\
    + Strings.DATE_STR\
    + Strings.RIGHT_ARROW\
    + Strings.DATE_STR

  WEEK_HEADER_TXT: str = 'Week #' + 24 * Strings.SPACE + '/'

  #_____________________________________________________________________
  def __init__(self
  , total_hght: int = 0
  , total_wdth: int = 0
  , addl_args: dict = {}
  ):
    """
    Constructor for class. Assumes landscape orientation.
    """

    super().__init__\
    ( total_hght=total_hght
    , total_wdth=total_wdth
    , addl_args=addl_args
    )

    return

  #_____________________________________________________________________
  def create_content(self) -> None:
    """
    Parameters:
      None

    Side Effects:
      Populates self.entries_ class variable.

    Returns:
      None
    """
    super().create_content()

    style  = deepcopy(StdTextBoxStyles.LTE_BACK_HEADER_FONT)
    style.line_spc_=1

    fill_hght: int = self.calc_remaining_hght_per_element(4)

    week_table = SingleLineTable\
      ( total_wdth=self.content_wdth_
      , row_count=1
      , total_hght=175
      , header_txt=self.WEEK_HEADER_TXT
      , text_style=StdTextBoxStyles.LTE_BACK_NORMAL_FONT
      , show_outline=True
      )

    self.entries_: list =\
    [ week_table
    , deepcopy(week_table)
    , deepcopy(week_table)
    , deepcopy(week_table)
    ]

    return

  #_____________________________________________________________________
  def create_page_header(self) -> svgwrite.container.Group:
    """
    Creates page header and saves it to class variable.

    Parameters:
      None

    Returns:

    """

    return super().create_page_header\
      (header_txt=self.HEADER_TXT)