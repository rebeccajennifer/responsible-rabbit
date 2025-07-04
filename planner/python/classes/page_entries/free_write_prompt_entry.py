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

from classes.constants.addl_arg_keys import AddlArgKeys as Key
from classes.constants.strings import PlannerStrings as Strings
from classes.elements.row_group import TextRowGroup
from classes.elements.row_group import DualLineRowGroup
from classes.style.std_styles import StdTextBoxStyles
from classes.style.style import PlannerFontStyle as Font

from classes.page_layouts.half_letter_one_page import OnePageHalfLetter


#_______________________________________________________________________
class FreeWritePromptEntry(OnePageHalfLetter):
  """
  Free write layout.
  """

  #_____________________________________________________________________
  def __init__(self
  , total_hght: int = 0
  , total_wdth: int = 0
  , addl_args: dict =\
    {Key.HEADER_TXT: Strings.DEF_PAGE_HEADER_TXT, Key.PROMPT_TXT: ''}
  ):
    """
    Constructor for class. Assumes landscape orientation.
    """

    self.prompt_: str = addl_args[Key.PROMPT_TXT]
    self.header_txt_: str = addl_args[Key.HEADER_TXT]

    super().__init__\
    ( total_hght=total_hght
    , total_wdth=total_wdth
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
          , text=self.prompt_
          , font_family=Font.FONT_FAMILY_NORMAL
          , style=txt_box_test_style)
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
      (header_txt=self.header_txt_)

    return page_header
