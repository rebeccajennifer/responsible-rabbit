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
from copy import deepcopy

from classes.constants.strings import PlannerStrings as Strings
from classes.elements.table import ColumnTable
from classes.elements.table import DualLineTable
from classes.style.std_styles import StdTextBoxStyles

from classes.page_layouts.half_page_layout import HalfPageLayout

#_______________________________________________________________________
class HabitTracker(HalfPageLayout):
  """
  Daily entry layout.
  """

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

    fill_hght: int = self.calc_remaining_hght_per_element(4)

    habit_tracker_table: ColumnTable =\
      ColumnTable\
      ( total_wdth=self.content_wdth_
      , total_hght=fill_hght
      , header_txt_lst=Strings.WEEK_HABIT_TRACKER_HEADINGS
      , text_style=StdTextBoxStyles.LTE_BACK_HEADER_FONT
      , row_count=6
      , col_wdths=[-1, 40] + 7 * [25] + [40]
      , inner_pad_lft=True
      , inner_pad_rgt=True
      , show_outline=True
      , TableType=DualLineTable
      )

    self.entries_: list =\
    [ deepcopy(habit_tracker_table)
    , deepcopy(habit_tracker_table)
    , deepcopy(habit_tracker_table)
    , deepcopy(habit_tracker_table)
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
      (header_txt=Strings.HABIT_PAGE_HEADER_TXT)
