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
#   Header used in tables and pages. Creates a group with a rectangle
#   with text inside.
#_______________________________________________________________________

import svgwrite.container
import svgwrite.shapes
import svgwrite.text

from classes.constants.dims import PlannerDims as Dims
from classes.constants.style import PlannerColors as Colors
from classes.constants.style import PlannerFontStyle as Font

from utils.utils import PlannerUtils as Utils


#_______________________________________________________________________
class HeaderBox(svgwrite.container.Group):
  """
  Container for entry table. Header is filled background.
  """

  #_____________________________________________________________________
  def __init__(self
  , wdth: int = 0
  , header_txt: str = ''
  , col_wdths: list = []
  , font_color: str = Colors.NORMAL
  , font_size: int = Font.NORMAL_SIZE
  , font: str = Font.FONT_FAMILY_NORMAL
  , box_fill_color: str = Colors.LIGHT_GREY
  , box_brdr_color: str = Colors.BORDER_COLOR
  , pad_top: bool = False
  , pad_bot: bool = False
  , pad_rgt: bool = False
  , pad_lft: bool = False
  ):

    super().__init__()

    self.total_wdth_: int = wdth
    self.content_wdth_: int = self.total_wdth_

    self.pad_top_: bool = pad_top
    self.pad_bot_: bool = pad_bot
    self.pad_rgt_: bool = pad_rgt
    self.pad_lft_: bool = pad_lft

    self.font_color_: str = font_color
    self.font_size_: int = font_size
    self.font_: str = font

    self.box_hght_: int = self.font_size_ + 2 * Font.TEXT_PADDING
    self.total_hght_: int = self.box_hght_\
      + Dims.BRD_MARGIN_PX * (self.pad_top_ + self.pad_bot_)

    self.box_fill_color_: str = box_fill_color
    self.box_brdr_color_: str = box_brdr_color


    self.content_wdth_ = self.total_wdth_\
      - Dims.BRD_MARGIN_PX * (self.pad_lft_ + self.pad_rgt_)

    #___________________________________________________________________
    # Header can be a string or list
    if (isinstance(header_txt, str)):
      self.header_txt_ = [header_txt]
    else:
      self.header_txt_ = header_txt
    #___________________________________________________________________

    self.col_wdths_: list = Utils.calc_col_wdths\
      ( wdth
      , len(header_txt)
      , col_wdths
      )

    self.create_header()

    return

  #_____________________________________________________________________
  def create_header(self):
    """
    Create boxed header.
    """

    insert_box_x: int = Dims.BRD_MARGIN_PX * self.pad_lft_
    insert_box_y: int = Dims.BRD_MARGIN_PX * self.pad_top_

    header_box: svgwrite.shapes.Rect =\
      svgwrite.shapes.Rect\
      ( size=(self.content_wdth_, self.box_hght_)
      , insert=(insert_box_x, insert_box_y)
      , stroke=self.box_brdr_color_
      , fill=self.box_fill_color_
      )

    self.add(header_box)

    #___________________________________________________________________
    insert_txt_x: int =\
      insert_box_x + Font.TEXT_PADDING
    insert_txt_y: int =\
      insert_box_y + self.box_hght_ - Font.TEXT_PADDING
    #___________________________________________________________________

    for i in range(len(self.header_txt_)):

      header: str = self.header_txt_[i]

      # Note: The SVG to PDF tool rsvg-convert only seems to support
      # 'text-after-edge' for alignment baseline, so this option
      # is selected to accurately render the svg to reflect how the
      # pdf will be created
      header_txt: svgwrite.text.Text =\
        svgwrite.text.Text\
        ( header
        , insert=(insert_txt_x, insert_txt_y)
        , text_anchor='start'
        , alignment_baseline='text-after-edge'
        , fill=self.font_color_
        , font_size=self.font_size_
        , font_family=self.font_
        )

      self.add(header_txt)

      if (i == 0):
        insert_txt_x = insert_txt_x - Font.TEXT_PADDING

      insert_txt_x = insert_txt_x + self.col_wdths_[i]

    return


