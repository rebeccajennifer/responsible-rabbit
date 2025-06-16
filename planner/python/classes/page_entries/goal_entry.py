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
#   Entry for goal. Fills content for one half sheet.
#_______________________________________________________________________

import svgwrite.container

from classes.constants.strings import PlannerStrings as Strings

from classes.elements.table import ColumnTable
from classes.elements.table import DualLineTable
from classes.elements.table import SingleLineTable

from classes.page_layouts.half_letter_one_page import OnePageHalfLetter

from classes.style.style import PlannerFontStyle as Font
from classes.style.std_styles import StdTextBoxStyles


#_______________________________________________________________________
class GoalEntry(OnePageHalfLetter):
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
      , addl_args=addl_args
      )

    return

  #_____________________________________________________________________
  def create_content(self) -> None:
    """
    Side Effects:
      Populates self.entries_ class variable.

    Parameters:
      None

    Returns:
      None
    """

    super().create_content()

    self.entries_: list =\
    [ DualLineTable\
      ( total_wdth=self.content_wdth_
      , header_txt=Strings.GOAL_VALUES
      , text_style=StdTextBoxStyles.MED_BACK_HEADER_FONT
      , row_count=3
      , show_outline=False
      )
    , ColumnTable\
      ( total_wdth=self.content_wdth_
      , header_txt_lst=Strings.GOAL_MILESTONES
      , text_style=StdTextBoxStyles.WHT_BACK_HEADER_FONT_NO_OUTLNE
      , row_count=7
      , col_wdths=[275, -1]
      , TableType=DualLineTable
      , show_outline=True
      )

    , DualLineTable\
      ( total_wdth=self.content_wdth_
      , header_txt=Strings.GOAL_MEASUREMENT
      , text_style=StdTextBoxStyles.MED_BACK_HEADER_FONT
      , row_count=1
      , show_outline=False
      )

    , DualLineTable\
      ( total_wdth=self.content_wdth_
      , header_txt=Strings.GOAL_OBSTACLES
      , text_style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE
      , row_count=2
      , show_outline=True
      )

    , DualLineTable\
      ( total_wdth=self.content_wdth_
      , header_txt=Strings.GOAL_LIFE_IMPROVEMENT
      , text_style=StdTextBoxStyles.MED_BACK_HEADER_FONT
      , row_count=2
      , show_outline=False
      )
   ]

    # Calculate remaining height to evenly distribute spanning tables
    fill_hght: int =\
      self.calc_remaining_hght_per_element(2)

    self.entries_ = self.entries_ +\
    [ SingleLineTable\
      ( total_wdth=self.content_wdth_
      , total_hght=fill_hght
      , header_txt=Strings.GOAL_PLAN
      , text_style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE
      , show_outline=True
      )

    , SingleLineTable\
      ( total_wdth=self.content_wdth_
      , total_hght=fill_hght
      , header_txt=Strings.GOAL_REWARD
      , text_style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE
      , show_outline=True
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
      ( header_txt=Strings.GOAL_PAGE_HEADER_TXT
      , font_size=Font.GOAL_HEADER_TXT_SIZE
      )
