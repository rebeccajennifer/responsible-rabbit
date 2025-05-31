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
#   Entry for week. Fills content for one half sheet.
#_______________________________________________________________________

import svgwrite.container

from classes.constants.strings import PlannerStrings as Strings
from classes.elements.table import ColumnTable
from classes.elements.table import DualLineTable
from classes.style.std_styles import StdTextBoxStyles

from classes.page_layouts.half_letter_layout import OnePageHalfLetterLayout

#_______________________________________________________________________
class WeekCheckList(OnePageHalfLetterLayout):
  """
  Daily entry layout.
  """

  PAGE_HEADER_TXT : str = 'Weekly Checklist'
  ACTION_ITEM     : str = 'Action Item'

  WEEKS: list =\
  [ 'Week 1'
  , 'Week 2'
  , 'Week 3'
  , 'Week 4'
  ]

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

    fill_hght: int = self.calc_remaining_hght_per_element(1)

    self.entries_: list =\
    [ ColumnTable\
      ( total_wdth=self.content_wdth_
      , total_hght=fill_hght
      , header_txt_lst=[self.ACTION_ITEM] + self.WEEKS
      , text_style=StdTextBoxStyles.MED_BACK_HEADER_FONT
      , row_count=20
      , col_wdths=[-1] + 4 * [50]
      , inner_pad_lft=True
      , inner_pad_rgt=True
      , show_outline=True
      , TableType=DualLineTable
      )
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
      (header_txt=self.PAGE_HEADER_TXT)
