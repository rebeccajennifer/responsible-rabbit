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
from classes.elements.table import SimpleTable
from classes.elements.base_element import BaseElement
from classes.elements.base_element import VerticalStack
from classes.style.table_style import LineRowGroupStyle
from classes.style.table_style import TextBoxStyle

from classes.page_layouts.half_letter_layout import OnePageHalfLetterLayout


#_______________________________________________________________________
class FreeWrite(OnePageHalfLetterLayout):
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
    style =\
      LineRowGroupStyle\
      ( total_wdth=self.content_wdth_
      , row_count=5
      #, row_hght=
      , line_wght=5
      , line_color=Colors.FLUX_GRN
      , show_outline=True
      , outline_color=Colors.DEBUG0_COLOR
      , y_offset=0
      , inner_pad_top= False
      , inner_pad_bot= False
      , inner_pad_lft= False
      , inner_pad_rgt= False
      , dash_array='6, 4'
      )

    row_group=LineRowGroup(style=style)

    line_row_group = LineRowGroup\
      ( total_wdth=self.content_wdth_
       , total_hght=self.content_hght_/2
      , row_count=5
      , show_outline=True
      , outline_color=Colors.FLUX_BLU
      , dash_array='.5,2'
      , inner_pad_top=0
      , inner_pad_bot=0
      )


    g2 = line_row_group.svg_group_
    g3 = BaseElement(hght=self.content_hght_/2, wdth=self.content_wdth_)
    g3.add(g2)

    t = TextRowGroup\
      ( text=50 * 'sf '
      , total_wdth=self.content_wdth_
      , inner_pad_top=True
      , inner_pad_bot=True
      , inner_pad_lft=True
      , inner_pad_rgt=True
      , show_outline=True
      , outline_color=Colors.FLUX_MAG
      , backgnd_color=Colors.CYAN
      ).text_row_group_

    group = VerticalStack(add_inner_pad=True, obj_list=[g2,t])


    text_style = TextBoxStyle(total_wdth=self.content_wdth_)
    table =\
      SimpleTable\
      ( header_txt='this is header text'
      , style=text_style
    )

    self.entries_: list =\
      [table, group, row_group.svg_group_]

    return

  #_____________________________________________________________________
  def create_page_header(self) -> svgwrite.container.Group:
    """
    Creates page header and saves it to class variable.

    Parameters:
      None

    Returns:

    """
    font_size: int = Font.WEEK_PAGE_HEADER_SIZE
    font_family: str = Font.FONT_FAMILY_HEADER

    page_header = super().create_page_header\
      ( header_txt=Strings.FREE_WRITE_FUTURE
      , font_size=font_size
      , font=font_family
      , box_fill_color=Colors.DEF_PAGE_HEADER_COLOR
      )

    return page_header
