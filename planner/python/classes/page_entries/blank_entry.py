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
#   Entry for future vision. Fills content for one half sheet.
#_______________________________________________________________________

import svgwrite.container

from classes.constants.strings import PlannerStrings as Strings
from classes.elements.rows import DualLineRowGroup

from classes.page_layouts.half_letter_layout import OnePageHalfLetterLayout


#_______________________________________________________________________
class BlankWrite(OnePageHalfLetterLayout):
  """
  Free write layout.
  """

  #_____________________________________________________________________
  def __init__(self
  , total_hght: int = 0
  , total_wdth: int = 0
  , padding: int = 0
  , page_header: str = ''
  , prompt: str = ''
  ):
    """
    Constructor for class. Assumes landscape orientation.
    """
    super().__init__\
    ( total_hght=total_hght
    , total_wdth=total_wdth
    , padding=padding
    )

    self.page_header_: str = page_header
    self.prompt_: str      = prompt

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
    '''
      ( wdth=self.content_wdth_
      , total_hght=self.content_hght_/2
      , show_outline=True
      , y_offset=20
      , outline_color=Colors.FLUX_BLU
      '''

    self.entries_: list =\
      [ DualLineRowGroup\
        ( total_wdth=self.content_wdth_
        , total_hght=self.content_hght_
        , row_count=30
        )
      ]

    return

  #_____________________________________________________________________
  def add_content(self) -> None:
    """
    Calls parent function, setting pad_bet_elements to True.
    """

    super().add_content(pad_bet_elements=False)

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
