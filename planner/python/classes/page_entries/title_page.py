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
#   Entry for a blank page with page header.
#_______________________________________________________________________

import svgwrite.container

from classes.constants.addl_arg_keys import AddlArgKeys as Key
from classes.elements.row_group import TextRowGroup
from classes.style.std_styles import StdTextBoxStyles

from classes.page_layouts.half_letter_one_page import OnePageHalfLetter


#_______________________________________________________________________
class TitlePage(OnePageHalfLetter):
  """
  Title page.
  """

  #_____________________________________________________________________
  def __init__(self
  , total_hght: int = 0
  , total_wdth: int = 0
  , addl_args: dict = {Key.HEADER_TXT: ''}
  ):
    """
    Constructor for class. Assumes landscape orientation.
    """

    if (Key.HEADER_TXT not in addl_args.keys()):
      addl_args[Key.HEADER_TXT] = ''

    self.page_header_txt_: str = addl_args[Key.HEADER_TXT]

    super().__init__\
    ( total_hght=total_hght
    , total_wdth=total_wdth
    , pad_bet_elements=False
    , show_page_border=False
    , show_page_header=False
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
        , text=self.page_header_txt_
        , style=StdTextBoxStyles.WHT_BACK_TITLE_FONT_NO_OUTLNE
        )
      ]

    #___________________________________________________________________
    # Vertically center the title by placing it between two empty text
    # boxes. The empty boxes have equal height, calculated as half of
    # the remaining space after subtracting the title’s height from the
    # total height.
    #___________________________________________________________________
    fill_hght: int = self.calc_remaining_hght_per_element(2)
    self.entries_.insert(0, TextRowGroup(total_hght=fill_hght))
    self.entries_.append(TextRowGroup(total_hght=fill_hght))
    #___________________________________________________________________

    return
