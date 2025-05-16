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
#   Half-letter sheet layout
#_______________________________________________________________________

import svgwrite

from os import path

from typing import Tuple

import svgwrite.container
import svgwrite.shapes
import svgwrite.text

from classes.constants.dims import PlannerDims as Dims
from classes.constants.strings import PlannerStrings as Strings
from classes.elements.row_group import TextRowGroup
from classes.elements.base_element import VerticalStack
from classes.style.std_styles import StdTextBoxStyles
from classes.style.style import PlannerColors as Colors
from classes.style.style import PlannerFontStyle as Font
from classes.style.table_style import TextBoxStyle
from classes.page_layouts.half_letter_layout import OnePageHalfLetterLayout


#_______________________________________________________________________
class DividerPage(svgwrite.Drawing):
  """
  Layout for half letter size prints. Intended to print two pages on
  one sheet and cut in half.
  """

  #_____________________________________________________________________
  def __init__(self
  , is_portrait: bool = False
  , is_dbl_sided: bool = False
  , out_dir: str = ''
  , file_name: str = ''
  , file_path: str = ''
  , divider_pos: int = 0
  , divider_str: str = ''
  ):

    if (not file_path):
      if (not file_name):
        file_name: str =\
          'divider-' + divider_str.lower().replace(' ', '-') + '.svg'

    self.file_path_ = path.join(out_dir, file_name)

    self.is_portrait_   : bool  = is_portrait
    self.is_dbl_sided_  : bool  = is_dbl_sided
    self.divider_pos_   : int   = divider_pos
    self.divider_str_   : int   = divider_str

    self.total_hght_: int = Dims.LETTER_SIZE_WIDTH_PX
    self.total_wdth_: int = Dims.LETTER_SIZE_LNGTH_PX

    if (self.is_portrait_):
      self.total_hght_: int = Dims.LETTER_SIZE_LNGTH_PX
      self.total_wdth_: int = Dims.LETTER_SIZE_WIDTH_PX

    super().__init__\
      ( self.file_path_
      , profile='tiny'
      , size=(self.total_wdth_, self.total_hght_)
      )
    #___________________________________________________________________

    self.content_wdth_, self.content_hght_ =\
       Dims.calc_border_size(self.is_portrait_)

    # Content insertion points for top left
    self.calc_border_insert_pts()
    self.create_content()
    self.add_content()

    return

  #_____________________________________________________________________
  def create_content(self) -> None:
    """
    Creates page borders, page header,

    Parameters:
      None

    Returns:
      None
    """

    #___________________________________________________________________
    # Construct divider tab
    #___________________________________________________________________
    tab_y_strt: int = Dims.STD_MARGIN_PX\
    + self.divider_pos_ * Dims.DIVIDER_LGTH

    tab_y_stop: int = tab_y_strt + Dims.DIVIDER_LGTH
    tab_x_strt: int = self.total_wdth_/2 + Dims.DIVIDER_WDTH
    tab_x_stop: int = tab_x_strt + Dims.DIVIDER_WDTH

    self.divider_tab_: svgwrite.container.Group =\
      svgwrite.container.Group()

    self.divider_tab_.add\
    ( svgwrite.shapes.Line\
      ( start=(tab_x_strt, tab_y_strt)
      , end=(tab_x_stop, tab_y_strt)
      , stroke=Colors.DEF_ROW_COLOR
      )
    )
    self.divider_tab_.add\
    ( svgwrite.shapes.Line\
      ( start=(tab_x_stop, tab_y_strt)
      , end=(tab_x_stop, tab_y_stop)
      , stroke=Colors.DEF_ROW_COLOR
      )
    )

    self.divider_tab_.add\
    ( svgwrite.shapes.Line\
      ( start=(tab_x_stop, tab_y_stop)
      , end=(tab_x_strt, tab_y_stop)
      , stroke=Colors.DEF_ROW_COLOR
      )
    )

    #___________________________________________________________________
    # Text for divider tab
    #___________________________________________________________________

    txt_x_insert: int = tab_x_strt + Font.TEXT_PADDING
    txt_y_insert: int = tab_y_strt + Font.TEXT_PADDING

    self.divider_txt_: svgwrite.text.Text =\
      svgwrite.text.Text\
      ( text=self.divider_str_
      , insert=(txt_x_insert, txt_y_insert)
      , text_anchor='start'
      , alignment_baseline='text-after-edge'
      , fill=Colors.NORMAL_TXT
      , font_size=Font.NORMAL_SIZE
      , font_family=Font.FONT_FAMILY_HEADER
      )

    self.divider_txt_.rotate(90, center=(txt_x_insert, txt_y_insert))

    self.cut_line_: svgwrite.shapes.Line =\
      svgwrite.shapes.Line\
      ( start=(tab_x_strt, self.insert_pt_border_0_[1])
      , end=(tab_x_strt, self.content_hght_ + 2 * Dims.BRD_MARGIN_PX)
      , stroke=Colors.DEF_ROW_COLOR
      , stroke_dasharray='2,6'
      )

    #___________________________________________________________________
    self.content_0_: OnePageHalfLetterLayout =\
      OnePageHalfLetterLayout\
      ( total_wdth=self.content_wdth_
      , total_hght=self.content_hght_
      )

    return

  #_____________________________________________________________________
  def add_content(self):
    """
    Adds content as class variables to page.

    Parameters:
      None

    Returns:
      None
    """

    x: int = self.insert_pt_border_0_[0]
    y: int = self.insert_pt_border_0_[1]
    self.content_0_['transform'] = f'translate({x}, {y})'

    self.add(self.content_0_)
    self.add(self.divider_tab_)
    self.add(self.divider_txt_)
    self.add(self.cut_line_)

    return

  #_____________________________________________________________________
  def calc_border_insert_pts(self) -> None:
    """
    Determines top left insertion points for content boxes and borders.

    Side Effects:
      Adds class variables for insertion points.
    """

    content_wdth: int = self.content_wdth_
    content_hght: int = self.content_hght_

    if (self.is_portrait_):
      insert_pos00 = Dims.STD_MARGIN_PX
      insert_pos01 = Dims.BND_MARGIN_PX

      insert_pos10 = Dims.STD_MARGIN_PX
      insert_pos11 = content_hght\
        + Dims.STD_MARGIN_PX\
        + 2 * Dims.BND_MARGIN_PX

      if (self.is_dbl_sided_):
        insert_pos01 = Dims.STD_MARGIN_PX

    else:
      insert_pos00 = Dims.BND_MARGIN_PX
      insert_pos01 = Dims.STD_MARGIN_PX
      insert_pos11 = Dims.STD_MARGIN_PX

      insert_pos10 = content_wdth\
        + Dims.STD_MARGIN_PX\
        + 2 * Dims.BND_MARGIN_PX

      if (self.is_dbl_sided_):
        insert_pos00 = Dims.STD_MARGIN_PX

    insert_pos0: Tuple = (insert_pos00, insert_pos01)
    insert_pos1: Tuple = (insert_pos10, insert_pos11)

    self.insert_pt_border_0_: int =  insert_pos0
    self.insert_pt_border_1_: int =  insert_pos1

    return
