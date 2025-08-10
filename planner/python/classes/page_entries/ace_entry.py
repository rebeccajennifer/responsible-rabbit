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

from copy import deepcopy

from classes.constants.strings import PlannerStrings as Strings
from classes.elements.table import DualLineTable
from classes.style.std_styles import StdTextBoxStyles
from classes.elements.row_group import TextRowGroup

from classes.page_layouts.half_page_layout import HalfPageLayout


#_______________________________________________________________________
class AceEntry(HalfPageLayout):
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
    header_style.font_size_ = 16
    prompt_style = StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE

    self.entries_: list =\
    [ DualLineTable\
      ( total_wdth=self.content_wdth_
      , row_count=3
      , header_txt=self.ACKN_PROMPT_MANFST
      , text_style=prompt_style
      , show_outline=False
      )
    , DualLineTable\
      ( total_wdth=self.content_wdth_
      , row_count=3
      , header_txt=self.ACKN_PROMPT_EMOTNS
      , text_style=prompt_style
      , show_outline=False
      )
    , DualLineTable\
      ( total_wdth=self.content_wdth_
      , row_count=3
      , header_txt=self.ACKN_PROMPT_BEFORE
      , text_style=prompt_style
      , show_outline=False
      )
    , DualLineTable\
      ( total_wdth=self.content_wdth_
      , row_count=1
      , header_txt=self.CNCT_PROMPT_TECHNQU
      , text_style=prompt_style
      , show_outline=False
      )
    , DualLineTable\
      ( total_wdth=self.content_wdth_
      , row_count=3
      , header_txt=self.CNCT_PROMPT_REFLECT
      , text_style=prompt_style
      , show_outline=False
      )
    , DualLineTable\
      ( total_wdth=self.content_wdth_
      , row_count=2
      , header_txt=self.ENGA_PROMPT_ACTIVTY
      , text_style=prompt_style
      , show_outline=False
      )
    ]

    fill_hght: int = self.calc_remaining_hght_per_element(3)

    a_header: TextRowGroup =\
      TextRowGroup\
      ( text=self.ACKNOWLEDGE_HEADER
      , total_wdth=self.content_wdth_
      , total_hght=fill_hght
      , style=header_style
      )

    e_header: TextRowGroup =\
      TextRowGroup\
      ( text=self.ENGAGE_HEADER
      , total_wdth=self.content_wdth_
      , total_hght=fill_hght
      , style=header_style
      )

    c_header: TextRowGroup =\
      TextRowGroup\
      ( text=self.CONNECT_HEADER
      , total_wdth=self.content_wdth_
      , style=header_style
      , total_hght=fill_hght
      )

    self.entries_ = [a_header]  +\
      self.entries_[0:3]        +\
      [c_header]                +\
      self.entries_[3:5]        +\
      [e_header]                +\
      [self.entries_[5]]

    return
