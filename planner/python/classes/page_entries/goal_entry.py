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

from classes.constants.dims import PlannerDims as Dims
from classes.constants.strings import PlannerStrings as Strings

from classes.elements.entry_table import EntryTable
from classes.elements.entry_table import NumberedTable
from classes.elements.entry_table import PromptTable
from classes.elements.header_box import HeaderBox

from classes.page_layouts.half_letter_layout import OnePageHalfLetterLayout

from classes.style.style import PlannerColors as Colors
from classes.style.style import PlannerFontStyle as Font



#_______________________________________________________________________
class GoalEntry(OnePageHalfLetterLayout):
  """
  Daily entry layout.
  """

  #_____________________________________________________________________
  def __init__(self
  , total_hght: int = 0
  , total_wdth: int = 0
  , padding: int = 0
  ):
    """
    Constructor for class. Assumes landscape orientation.
    """
    super().__init__\
      ( total_hght=total_hght
      , total_wdth=total_wdth
      , padding=padding
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
    [ HeaderBox\
      ( wdth=self.content_wdth_
      , header_txt=Strings.GOAL_CHECKLIST
      , font_size=9
      , box_brdr_color='none'
      , box_fill_color='none'
      )

    , NumberedTable\
      ( wdth=self.content_wdth_
      , header_txt=Strings.GOAL_ACTIONS
      , prepend_txt='[]'
      , row_count=4
      , show_outline=True
      )

    , EntryTable\
      ( wdth=self.content_wdth_
      , header_txt=Strings.GOAL_MEASUREMENT
      , row_count=2
      , show_outline=False
      )

    , NumberedTable\
      ( wdth=self.content_wdth_
      , header_txt=Strings.GOAL_COST
      , row_count=2
      , font_color=Colors.NORMAL_TXT
      , box_brdr_color='none'
      , box_fill_color='none'
      , show_outline=True
      )

    , NumberedTable\
      ( wdth=self.content_wdth_
      , header_txt=Strings.GOAL_BENCHMARKS
      , prepend_txt=Strings.GOAL_MONTHS
      , row_count=3
      , show_outline=True
      )

    , NumberedTable\
      ( wdth=self.content_wdth_
      , header_txt=Strings.GOAL_LIFE_IMPROVEMENT
      , row_count=2
      , show_outline=False
      )
    ]

    # Calculate remaining height to evenly distribute spanning tables
    fill_hght: int =\
      self.calc_remaining_hght_per_element(2) + Dims.BRD_MARGIN_PX

    self.entries_ = self.entries_ +\
    [ PromptTable\
      ( wdth=self.content_wdth_
      , hght=fill_hght
      , header_txt=Strings.GOAL_PLAN
      )

    , PromptTable\
      ( wdth=self.content_wdth_
      , hght=fill_hght
      , header_txt=Strings.GOAL_REWARD
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
      ( header_txt=Strings.GOAL_PAGE_HEADER
      , font_size=Font.GOAL_HEADER_SIZE
      )
