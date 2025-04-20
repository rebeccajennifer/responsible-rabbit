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
from classes.style.style import PlannerColors as Colors
from classes.style.style import PlannerFontStyle as Font

from classes.elements.rows import LineRowGroup
from classes.elements.rows import TextRowGroup
from classes.elements.rows import DualLineRowGroup
from classes.elements.table import DualLineTable
from classes.style.std_styles import StdTextBoxStyles
from classes.style.std_styles import StdLineRowGroupStyles

from classes.page_layouts.half_letter_layout import OnePageHalfLetterLayout


#_______________________________________________________________________
class FutureEntry(OnePageHalfLetterLayout):
  """
  Free write layout.
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
    , pad_bet_elements=False
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

    txt_box_test_style = StdTextBoxStyles.WHT_BACK_NORMAL_FONT_W_OUTLNE
    txt_box_test_style.line_spc_ = 1.2

    self.entries_: list =\
      [ TextRowGroup\
          ( total_wdth=self.content_wdth_
          , text=Strings.FREE_WRITE_FUTURE
          , font_family=Font.FONT_FAMILY_NORMAL
          , style=txt_box_test_style).text_row_group_
      ]

    fill_hght: int = self.calc_remaining_hght_per_element()

    self.entries_.insert(1,
      DualLineRowGroup\
        ( total_wdth=self.content_wdth_
        , total_hght=fill_hght
        , row_count=20
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

    page_header = super().create_page_header\
      ( header_txt=Strings.FUTURE_PAGE_HEADER
      )

    return page_header
