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

from typing import Tuple

import svgwrite.container
import svgwrite.drawing
import svgwrite.shapes

from classes.constants.dims import PlannerDims as Dims
from classes.constants.style import PlannerColors as Colors
from classes.constants.style import PlannerFontStyle as Font
from classes.constants.strings import PlannerStrings as Strings
from classes.elements.header_box import HeaderBox


#_______________________________________________________________________
class TwoPageHalfLetterSize_(svgwrite.Drawing):
  """
  Layout for half letter size prints. Intended to print two pages on
  one sheet and cut in half.
  """

  #_____________________________________________________________________
  def __init__(self
  , is_portrait: bool = False
  , is_dbl_sided: bool = False
  , file_path: str = Strings.DEF_LAYOUT_PATH
  ):

    self.is_portrait_   : bool  = is_portrait
    self.is_dbl_sided_  : bool  = is_dbl_sided
    self.file_path_     : str   = file_path

    #___________________________________________________________________
    hght: int = Dims.to_in_str(Dims.LETTER_SIZE_WIDTH_IN)
    wdth: int = Dims.to_in_str(Dims.LETTER_SIZE_LNGTH_IN)

    if (self.is_portrait_):
      hght = Dims.to_in_str(Dims.LETTER_SIZE_LNGTH_IN)
      wdth = Dims.to_in_str(Dims.LETTER_SIZE_WIDTH_IN)

    super().__init__\
      ( self.file_path_
      , profile='tiny'
      , size=(wdth, hght)
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

    self.content_0_: OnePageHalfLetterLayout =\
      OnePageHalfLetterLayout\
      ( total_wdth=self.content_wdth_
      , total_hght=self.content_hght_
      )

    self.content_1_: OnePageHalfLetterLayout =\
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

    x: int = self.insert_pt_border_1_[0]
    y: int = self.insert_pt_border_1_[1]
    self.content_1_['transform'] = f'translate({x}, {y})'

    self.add(self.content_0_)
    self.add(self.content_1_)

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


##_______________________________________________________________________
class OnePageHalfLetterLayout(svgwrite.container.Group):
  """
  """

  #_____________________________________________________________________
  def __init__(self
  , total_hght: int = 0
  , total_wdth: int = 0
  , padding: int = 0
  ):

    super().__init__()

    self.total_hght_: int = total_hght
    self.total_wdth_: int = total_wdth
    self.padding_   : int = padding

    self.page_header_insert_pt_x_ : int = padding
    self.page_header_insert_pt_y_ : int = padding

    self.content_wdth_: int = self.total_wdth_ - 2 * padding

    self.page_header_: HeaderBox = self.create_page_header()

    # Content height is affected by generation of page header
    self.content_hght_: int =\
      self.total_hght_ - 2 * padding - self.page_header_.total_hght_

    self.content_insert_pt_x_ : int = self.page_header_insert_pt_x_
    self.content_insert_pt_y_ : int =\
      self.page_header_insert_pt_y_ + self.page_header_.total_hght_

    self.create_content()
    self.add_content()

    return

  #_____________________________________________________________________
  def create_content(self) -> None:
    """
    Creates content.
    """


    self.border_: svgwrite.shapes.Rect = self.create_border()

    return

  #_____________________________________________________________________
  def add_content(self) -> None:
    """
    Adds content to group.
    """

    x: int = self.page_header_insert_pt_x_
    y: int = self.page_header_insert_pt_y_
    self.page_header_['transform'] = f'translate({x}, {y})'

    self.add(self.border_)
    self.add(self.page_header_)

    return

  #_____________________________________________________________________
  def create_border(self) -> svgwrite.shapes.Rect:
    """
    Parameters:
      None

    Returns:
      svgwrite.shapes.Rect: outline of half page
    """

    border_box: svgwrite.shapes.Rect =\
      svgwrite.shapes.Rect(size=(self.total_wdth_, self.total_hght_)
      , insert=(0,0)
      , stroke=Colors.DEBUG0_COLOR
      , fill='none')

    return border_box

  #_____________________________________________________________________
  def create_page_header(self
  , header_txt = Strings.DEF_PAGE_HEADER
  , font_color: str = Colors.NORMAL
  , font_size: int = Font.HEAD_2_SIZE
  , font: str = Font.FONT_FAMILY_HEADER
  , box_fill_color: str = Colors.DEF_PAGE_HEADER_COLOR
  , box_brdr_color: str = Colors.BORDER_COLOR
  ) -> HeaderBox:
    """
    Creates page header and saves it to class variable.

    Parameters:
      None

    Returns:
      HeaderBox for page header
    """

    page_header: HeaderBox =\
      HeaderBox\
      ( wdth=self.content_wdth_
      , header_txt=[header_txt]
      , font_color=font_color
      , font_size=font_size
      , font=font
      , box_fill_color=box_fill_color
      , box_brdr_color=box_brdr_color
      )

    return page_header
