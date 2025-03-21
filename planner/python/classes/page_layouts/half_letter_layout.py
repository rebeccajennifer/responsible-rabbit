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

from classes.constants.dims import PlannerDims as Dims
from classes.constants.style import PlannerColors as Colors
from classes.constants.style import PlannerFontStyle as Font
from classes.constants.strings import PlannerStrings as Strings
from classes.elements.header_box import HeaderBox


#_______________________________________________________________________
class HalfLetterSize:
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

    self.is_portrait_: bool   = is_portrait
    self.is_dbl_sided_: bool  = is_dbl_sided
    self.file_path_: str      = file_path


    self.content_wdth_, self.content_hght_ =\
       Dims.calc_content_size(self.is_portrait_)

    # Content insertion points for top left
    self.calc_border_insert_pts()

    self.create_content()


    self.content_hght_ = self.content_hght_ - self.page_header_0_.hght_

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

    self.layout_dwg_: svgwrite.Drawing  = self.create_dwg()
    self.page_header_0_, self.page_header_1_ =\
      self.create_page_headers()

    self.half_page_border_0_, self.half_page_border_1_ =\
      self.create_borders()

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

    x: int = self.insert_pt_content_0_[0]
    y: int = self.insert_pt_content_0_[1]

    self.page_header_0_['transform'] = f'translate({x}, {y})'

    x: int = self.insert_pt_content_1_[0]
    y: int = self.insert_pt_content_1_[1]
    self.page_header_1_['transform'] = f'translate({x}, {y})'

    self.layout_dwg_.add(self.page_header_0_)
    self.layout_dwg_.add(self.page_header_1_)
    self.layout_dwg_.add(self.half_page_border_0_)
    self.layout_dwg_.add(self.half_page_border_1_)

    return

  #_____________________________________________________________________
  def save_svg(self) -> None:
    """
    Saves layout as svg file.

    Parameters:
      None

    Returns:
      None
    """

    self.layout_dwg_.save()

  #_____________________________________________________________________
  def create_dwg(self) -> svgwrite.Drawing:
    """
    Creates Drawing object with height and width of letter size paper.

    Parameters:
      None

    Returns:
      svgwrite.Drawing
    """

    # Leaving these as inches
    hght: int = Dims.to_in_str(Dims.LETTER_SIZE_WIDTH_IN)
    wdth: int = Dims.to_in_str(Dims.LETTER_SIZE_LNGTH_IN)

    if (self.is_portrait_):
      hght = Dims.to_in_str(Dims.LETTER_SIZE_LNGTH_IN)
      wdth = Dims.to_in_str(Dims.LETTER_SIZE_WIDTH_IN)

    return svgwrite.Drawing(self.file_path_
      , profile='tiny'
      , size=(wdth, hght)
    )

 #_____________________________________________________________________
  def create_borders(self) -> Tuple:
    """
    Adds content borders to page.
    Parameters:
      None

    Returns:
      None
    """

    content_box_0: svgwrite.shapes.Rect =\
      self.create_content_box(self.insert_pt_border_0_)

    content_box_1: svgwrite.shapes.Rect =\
      self.create_content_box(self.insert_pt_border_1_)

    return content_box_0, content_box_1

  #_____________________________________________________________________
  def create_content_box(self
  , insert_position: Tuple
  ) -> svgwrite.shapes.Rect:
    """
    Creates rectangle that will contain content.

    Parameters:

    Returns:
      svgwrite rectangle the size of the content
    """

    w,h = Dims.calc_border_size(self.is_portrait_)

    content_box: svgwrite.shapes.Rect =\
      svgwrite.shapes.Rect(size=(w, h)
      , insert=insert_position
      , stroke=Colors.DEBUG0_COLOR
      , fill='none')

    return content_box

  #_____________________________________________________________________
  def calc_border_insert_pts(self) -> None:
    """
    Determines top left insertion points for content boxes and borders.

    Side Effects:
      Adds class variables for insertion points.
    """

    content_wdth, content_hght =\
      Dims.calc_border_size(self.is_portrait_)

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

    # Determine insertion points for content based on border size
    self.insert_pt_content_0_: Tuple =\
    ( self.insert_pt_border_0_[0] + Dims.BRD_MARGIN_PX
    , self.insert_pt_border_0_[1] + Dims.BRD_MARGIN_PX
    )

    self.insert_pt_content_1_: Tuple =\
    ( self.insert_pt_border_1_[0] + Dims.BRD_MARGIN_PX
    , self.insert_pt_border_1_[1] + Dims.BRD_MARGIN_PX
    )

    return

  #_____________________________________________________________________
  def create_page_headers(self) -> Tuple:
    """
    Creates page headers for both half sheets.
    """

    page_header_0: HeaderBox =\
      self.create_page_header(header_txt=f'{Strings.DEF_PAGE_HEADER}_0')

    page_header_1: HeaderBox =\
      self.create_page_header(header_txt=f'{Strings.DEF_PAGE_HEADER}_1')

    return page_header_0, page_header_1

  #_____________________________________________________________________
  def create_page_header(self
  , header_txt = Strings.DEF_PAGE_HEADER
  , font_color: str = Colors.NORMAL
  , font_size: int = Font.HEAD_2_SIZE
  , font: str = Font.FONT_FAMILY_HEADER
  ) -> HeaderBox:
    """
    Creates page header and saves it to class variable.

    Parameters:
      None

    Returns:
      HeaderBox for page header
    """

    box_fill_color: str = Colors.LIGHT_GREY
    box_brdr_color: str = Colors.BORDER_COLOR

    page_header: HeaderBox =\
      HeaderBox\
      ( wdth=self.content_wdth_
      , text_lst=[header_txt]
      , font_color=font_color
      , font_size=font_size
      , font=font
      , box_fill_color=box_fill_color
      , box_brdr_color=box_brdr_color
      )

    return page_header


