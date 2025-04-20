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
#   Entry for testing. Will not be used in final product.
#_______________________________________________________________________

import svgwrite.container

from classes.constants.dims import PlannerDims as Dims
from classes.constants.strings import PlannerStrings as Strings
from classes.style.std_styles import StdTextBoxStyles
from classes.style.style import PlannerFontStyle as Font

from classes.elements.base_element import VerticalStack
from classes.elements.base_element import HorizontalStack
from classes.elements.rows import TextRowGroup
from classes.elements.table import DualLineTable
from classes.elements.table import SingleLineTable
from classes.elements.table import ColumnTableDualLine

from classes.page_layouts.half_letter_layout import OnePageHalfLetterLayout


#_______________________________________________________________________
class TestEntry(OnePageHalfLetterLayout):
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
    Parameters:
      None

    Side Effects:
      Populates self.entries_ class variable.

    Returns:
      None
    """
    super().create_content()

    test0 = SingleLineTable\
      ( total_wdth=self.content_wdth_/2 - Dims.BRD_MARGIN_PX/2
      , header_txt=Strings.WEEK_ACCOMPLISHMENTS
      , text_style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE
      , show_outline=False
      , row_count=2
      )

    test1 = DualLineTable\
      ( total_wdth=self.content_wdth_/2 - Dims.BRD_MARGIN_PX/2
      , header_txt=Strings.WEEK_LESSONS_LEARNED
      , text_style=StdTextBoxStyles.MED_BACK_HEADER_FONT
      , row_count=3
      , show_outline=True
      )

    horizontal_stack: HorizontalStack =\
      HorizontalStack\
      ( obj_list=[test0, test1]
      , add_inner_pad=True
      )

    self.entries_ =\
    [ ColumnTableDualLine\
      ( total_wdth=self.content_wdth_
      , header_txt_lst=['test0','test1']
      , col_wdths=[50, -1]
      , row_count=3
      , text_style=StdTextBoxStyles.MED_BACK_HEADER_FONT
      , show_outline=True
      , inner_pad_lft=True
      , inner_pad_rgt=True
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
      (header_txt=Strings.DEF_PAGE_HEADER)