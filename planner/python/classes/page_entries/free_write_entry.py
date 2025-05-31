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
from classes.elements.row_group import DualLineRowGroup

from classes.page_layouts.half_letter_one_page import OnePageHalfLetterLayout


#_______________________________________________________________________
class FreeWriteEntry(OnePageHalfLetterLayout):
  """
  Free write layout.
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
      [ DualLineRowGroup\
        ( total_wdth=self.content_wdth_
        , total_hght=self.content_hght_
        , row_count=24
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

    page_header = super().create_page_header\
      ( header_txt=self.page_header_txt_
      )

    return page_header
