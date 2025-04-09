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
#   Box of text.
#_______________________________________________________________________

import svgwrite
import svgwrite.container

from classes.constants.dims import PlannerDims as Dims
from classes.constants.error_strings import ErrorStrings as Err
from classes.constants.style import PlannerFontStyle as Font
from classes.constants.style import PlannerColors as Colors
from utils.utils import PlannerUtils as Utils

from classes.elements.rows import Rows
#_______________________________________________________________________
class TextBox(Rows):

  #_____________________________________________________________________
  def __init__(self
  , wdth: int = 0
  , hght: int = 0
  , font_color: str = Colors.NORMAL_TXT
  , font_size: int = Font.NORMAL_SIZE
  , font: str = Font.FONT_FAMILY_NORMAL
  , pad_top: bool = False
  , pad_bot: bool = False
  , pad_rgt: bool = False
  , pad_lft: bool = False
  , show_outline: bool = True
  , outline_color: str = Colors.BORDER_COLOR
  , row_hght: int = 0
  , inner_pad_lft: bool = True
  , txt = ''
  , line_spc: int = Font.DEF_LINE_SPC
  ):
    """
    Parameters:
      wdth            : Width of table
      hght            : Height of table
      font_color      : Color of header text
      font_size       : Size of header text
      font            : Font of header text
      pad_top         : Add padding to top
      pad_bot         : Add padding to bottom
      pad_rgt         : Add padding to right
      pad_lft         : Add padding to left
      show_outline    : Show table outline
      outline_color   : Color of outline

      txt             : String or list of strings for text
      line_spc        : Line spacing
    """

    self.txt_: str = txt
    self.line_spc_: int = line_spc

    if (not row_hght):
      row_hght = line_spc * font_size

    return super().__init__\
      ( wdth=wdth
      , font_color=font_color
      , font_size=font_size
      , font=font
      , pad_top=pad_top
      , pad_bot=pad_bot
      , pad_rgt=pad_rgt
      , pad_lft=pad_lft
      , show_outline=show_outline
      , outline_color=outline_color
      , row_hght=row_hght
      , inner_pad_lft=inner_pad_lft
      )


  #_____________________________________________________________________
  def create_content(self):
    """
    Parameters:
      None

    Side Effects:
      Populates class variables for entries.
    """

    txt_wdth: int =\
      self.content_wdth_ -\
      Dims.BRD_MARGIN_PX * (2 * self.inner_pad_lft_)

    self.txt_rows_: list =\
      Utils.split_txt_by_wdth\
      ( txt=self.txt_
      , px_wdth=txt_wdth
      , font_size=self.font_size_
      , font_family=self.font_
      )

    self.row_count_ = len(self.txt_rows_)
    self.y_coord_: list = self.get_y_of_rows()

    self.txt_row_group_: svgwrite.container.Group =\
      self.create_row_txt\
      ( pad_lft=self.inner_pad_lft_
      , y_coord=self.y_coord_
      )

    return

  #_____________________________________________________________________
  def add_content(self):
    """
    Adds svgwrite objects to class.

    Parameters:
      None

    Returns:
      None
    """
    self.add(self.txt_row_group_)
    return

  #_____________________________________________________________________
  def create_row_txt(self
    , pad_lft: bool = False
    , y_coord: list = []
    , y_offset: int = 0
    ) -> svgwrite.container.Group:
    """
    Creates group of lines.

    Parameters:
      pad_lft   : Add padding to left, modifies length of drawn line
      pad_rgt   : Add padding to right, modifies length of drawn line
      y_coord   : List of y coordinates for object insertion
      y_offset  : Offset from y_coord to insert object
    """

    start_padding: int = Font.TEXT_PADDING * pad_lft
    insert_x:      int = start_padding + self.insert_x_

    row_group: svgwrite.container.Group = svgwrite.container.Group()

    for i in range(len(y_coord)):

      insert_y: int = y_coord[i] - y_offset

      row_txt: svgwrite.txt.Text = svgwrite.text.Text\
      ( self.txt_rows_[i]
      , insert=(insert_x, insert_y)
      , text_anchor='start'
      , alignment_baseline='text-after-edge'
      , fill=self.font_color_
      , font_size=self.font_size_
      , font_family=self.font_
      )

      row_group.add(row_txt)

    return row_group
