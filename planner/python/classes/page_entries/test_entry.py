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

from copy import deepcopy

from classes.constants.dims import PlannerDims as Dims
from classes.constants.strings import PlannerStrings as Strings
from classes.style.std_styles import StdTextBoxStyles
from classes.style.style import PlannerFontStyle as Font
from classes.style.style import PlannerColors as Colors

from classes.elements.base_element import VerticalStack
from classes.elements.base_element import HorizontalStack
from classes.elements.row_group import TextRowGroup
from classes.elements.table import DualLineTable
from classes.elements.table import SingleLineTable
from classes.elements.table import ColumnTable

from classes.page_layouts.half_page_layout import HalfPageLayout

from classes.constants.debug_const import DebugConst

#_______________________________________________________________________
class TestEntry(HalfPageLayout):
  """
  Layout for ACE exercise
  """

  PAGE_HEADER_TXT: str = str(
    'Acknowlege - Connect - Engage : '
    + 2 * Strings.SPACE
    + 'Re-Regulation Practice'
  )

  ACKNOWLEDGE_HEADER  : str = 'Acknowledge'
  CONNECT_HEADER      : str = 'Connect'
  ENGAGE_HEADER       : str = '(Re-)Engage'

  ACKN_PROMPT_MANFST: str = 'How is the dysregulation manifesting?'
  ACKN_PROMPT_EMOTNS: str = 'What emotions are you experiencing?'
  ACKN_PROMPT_BEFORE: str = 'What was happening before the trigger?'

  CNCT_PROMPT_TECHNQU: str = 'Re-regulation technique to practice'
  CNCT_PROMPT_REFLECT: str = 'Reflections after practice'
  ENGA_PROMPT_ACTIVTY: str = 'What activity will you (re-)engage with?'

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

    header_style = deepcopy(StdTextBoxStyles.MED_BACK_HEADER_FONT)
    header_style = deepcopy(StdTextBoxStyles.DRK_BACK_HEADER_FONT)
    header_style.font_size_ = 16
    prompt_style = deepcopy(StdTextBoxStyles.WHT_BACK_NORMAL_FONT_W_OUTLNE)
    prompt_style.show_outline_ = True

    style3 = deepcopy(StdTextBoxStyles.LTE_BACK_NORMAL_FONT)
    style3.outline_color_=Colors.FLUX_BLK
    style3.show_outline_=True
    bleh3 = TextRowGroup(self.content_wdth_
    , text='MM 1M 1M 1M 1M 1 1 3 5 7 9 1 3 5 7 9 1'
    , style=style3
    #, show_outline=True
    , total_hght=30
    )

    self.entries_ = [bleh3]
    #fill_hght: int = self.calc_remaining_hght_per_element(3)


    return

