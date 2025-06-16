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
from classes.elements.base_element import VerticalStack
from classes.elements.row_group import TextRowGroup
from classes.elements.table import ColumnTable
from classes.elements.table import DualLineTable
from classes.elements.table import SingleLineTable
from classes.style.std_styles import StdTextBoxStyles
from classes.style.std_styles import StdLineRowGroupStyles

from classes.page_layouts.half_letter_one_page import OnePageHalfLetter

#_______________________________________________________________________
class WeekEntry0(OnePageHalfLetter):
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

    self.entries_: list =\
    [ TextRowGroup\
      ( total_wdth=self.content_wdth_
      , text=Strings.WEEK_MOMENTUM
      , style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE
      )
    , DualLineTable\
      ( total_wdth=self.content_wdth_
      , header_txt=Strings.WEEK_ACCOMPLISHMENTS
      , text_style=StdTextBoxStyles.MED_BACK_HEADER_FONT
      , show_outline=False
      , row_count=2
      )
    , DualLineTable\
      ( total_wdth=self.content_wdth_
      , header_txt=Strings.WEEK_LESSONS_LEARNED
      , text_style=StdTextBoxStyles.WHT_BACK_HEADER_FONT_NO_OUTLNE
      , row_count=2
      , show_outline=True
      )
    , DualLineTable\
      ( total_wdth=self.content_wdth_
      , header_txt=Strings.WEEK_UNFINISHED_BUSINESS
      , text_style=StdTextBoxStyles.MED_BACK_HEADER_FONT
      , row_count=2
      , show_outline=False
      )
    , DualLineTable\
      ( total_wdth=self.content_wdth_
      , header_txt=Strings.WEEK_IMPROVEMENT
      , text_style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE
      , row_count=2
      , show_outline=False
      )
    , DualLineTable\
      ( total_wdth=self.content_wdth_
      , header_txt=Strings.WEEK_THOUGHTS
      , text_style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE
      , row_count=8
      , show_outline=True
      )
    , DualLineTable\
      ( total_wdth=self.content_wdth_
      , header_txt=Strings.WEEK_GRATITUDE
      , text_style=StdTextBoxStyles.MED_BACK_HEADER_FONT
      , row_count=1
      , show_outline=True
      , pri_line_style=StdLineRowGroupStyles.DOTTED
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
      (header_txt=Strings.WEEK_PAGE_HEADER_TXT_0)

#_______________________________________________________________________
class WeekEntry1(OnePageHalfLetter):
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
    Side Effects:
      Populates self.entries_ class variable.

    Parameters:
      None

    Returns:
      None
    """
    super().create_content()

    self.entries_: list =\
    [ ColumnTable\
      ( total_wdth=self.content_wdth_
      , TableType=DualLineTable
      , header_txt_lst=['Goal 1', 'Goal 2']
      , text_style=StdTextBoxStyles.WHT_BACK_HEADER_FONT_NO_OUTLNE
      , row_count=3
      , inner_pad_lft=True
      , inner_pad_rgt=True
      )

    , ColumnTable\
      ( total_wdth=self.content_wdth_
      , TableType=DualLineTable
      , header_txt_lst=['Goal 3', 'Goal 4']
      , text_style=StdTextBoxStyles.WHT_BACK_HEADER_FONT_NO_OUTLNE
      , row_count=3
      , inner_pad_lft=True
      , inner_pad_rgt=True
      )

    , VerticalStack\
      (
        [
           TextRowGroup\
          ( total_wdth=self.content_wdth_
          , text=Strings.WEEK_VISUALIZATION_HEADER_TXT
          , style=StdTextBoxStyles.LTE_BACK_HEADER_FONT
          )

        , SingleLineTable\
          ( total_wdth=self.content_wdth_
          , total_hght=150
          , header_txt=Strings.WEEK_VISUALIZATION_PROMPT_TXT
          , text_style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE
          , show_outline=False
          )
        ]
        , show_outline=True
      )
   ]

    fullfillment: VerticalStack =\
      VerticalStack\
      (
        [ TextRowGroup\
          ( total_wdth=self.content_wdth_
          , text=Strings.WEEK_FULFILLMENT
          , style=StdTextBoxStyles.WHT_BACK_HEADER_FONT_W_OUTLNE
          )

        ,  ColumnTable\
          ( total_wdth=self.content_wdth_
          , total_hght=100
          , header_txt_lst=Strings.WEEK_FULFILLMENT_AREAS_0
          , text_style=StdTextBoxStyles.LTE_BACK_HEADER_FONT
          , row_count=1
          , show_outline=True
          )
        , ColumnTable\
          ( total_wdth=self.content_wdth_
          , total_hght=100
          , header_txt_lst=Strings.WEEK_FULFILLMENT_AREAS_1
          , text_style=StdTextBoxStyles.LTE_BACK_HEADER_FONT
          , row_count=1
          , show_outline=True
          )
        ]
      )

    self.entries_.append(fullfillment)

    fill_hght: int =\
      self.calc_remaining_hght_per_element()

    self.entries_.insert(4,
      DualLineTable\
      ( total_wdth=self.content_wdth_
      , total_hght=fill_hght
      , header_txt=Strings.WEEK_LOOKING_FORWARD
      , text_style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_W_OUTLNE
      , row_count=1
      , show_outline=True
      , pri_line_style=StdLineRowGroupStyles.DOTTED
      )
    )

    return

  #_____________________________________________________________________
  def create_page_header(self) -> svgwrite.container.Group:
    """
    Creates page header and saves it to class variable.

    Parameters:
      None

    Returns:

    """
    return\
      super().create_page_header(header_txt=Strings.WEEK_PAGE_HEADER_TXT_1)