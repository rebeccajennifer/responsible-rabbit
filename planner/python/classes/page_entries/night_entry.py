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
#   Nightly reflection
#_______________________________________________________________________

import svgwrite.container
from copy import deepcopy

from classes.constants.strings import PlannerStrings as Strings
from classes.elements.table import DualLineTable
from classes.style.std_styles import StdTextBoxStyles

from classes.page_layouts.half_page_layout import HalfPageLayout


#_______________________________________________________________________
class NightEntry(HalfPageLayout):
  """
  Daily entry layout.
  """

  PAGE_HEADER_TXT: str =\
    'Nightly Reflection'

  DAY_HEADER_TXT: str =\
    Strings.DAYS_MONO + 8 * Strings.SPACE + Strings.DATE_STR_MONO

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

    style  = deepcopy(StdTextBoxStyles.LTE_BACK_HEADER_FONT)
    style.line_spc_=1

    style = deepcopy(StdTextBoxStyles.LTE_BACK_NORMAL_FONT)
    style.font_size_ = 8

    fill_hght: int = self.calc_remaining_hght_per_element(7)

    day_reflection = DualLineTable\
      ( total_wdth=self.content_wdth_
      , row_count=3
      , total_hght=fill_hght
      , header_txt=self.DAY_HEADER_TXT
      , text_style=style
      , show_outline=True
      )

    self.entries_: list =\
    [ day_reflection
    , deepcopy(day_reflection)
    , deepcopy(day_reflection)
    , deepcopy(day_reflection)
    , deepcopy(day_reflection)
    , deepcopy(day_reflection)
    , deepcopy(day_reflection)
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

    style = deepcopy(StdTextBoxStyles.DEF_PAGE_HEADER_TXT)
    style.font_size_ = 8

    return super().create_page_header(style=style)
