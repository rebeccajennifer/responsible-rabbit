#_______________________________________________________________________
#_______________________________________________________________________
#       _   __   _   _ _   _   _   _         _
#  |   |_| | _  | | | V | | | | / |_/ |_| | /
#  |__ | | |__| |_| |   | |_| | \ |   | | | \_
#   _  _         _ ___  _       _ ___   _                    / /
#  /  | | |\ |  \   |  | / | | /   |   \                    (^^)
#  \_ |_| | \| _/   |  | \ |_| \_  |  _/                    (____)o
#_______________________________________________________________________
#_______________________________________________________________________
#
#-----------------------------------------------------------------------
#  Copyright 2024, Rebecca Rashkin
#  -------------------------------
#  This code may be copied, redistributed, transformed, or built
#  upon in any format for educational, non-commercial purposes.
#
#  Please give me appropriate credit should you choose to use this
#  resource. Thank you :)
#-----------------------------------------------------------------------
#
#_______________________________________________________________________
#  //\^.^/\\   //\^.^/\\   //\^.^/\\   //\^.^/\\   //\^.^/\\   //\^.^/\\
#_______________________________________________________________________
#  DESCRIPTION
#  Half-letter sheet layout
#_______________________________________________________________________

import svgwrite
import svgwrite.shapes

from typing import Tuple

from classes.constants.dims import PlannerDims as Dims
from classes.constants.style import PlannerColors as Colors
from classes.constants.style import PlannerStrokes as Strokes


#_______________________________________________________________________
class HalfLetterSize:
  """
  Layout for half letter size prints. Intended to print two pages on
  one sheet and cut in half.
  """

  #_____________________________________________________________________
  def __init__(self
    , is_portrait: bool = False
    , is_dbl_sided: bool = False):
    self.is_portrait_: bool   = is_portrait
    self.is_dbl_sided_: bool  = is_dbl_sided

  #_____________________________________________________________________
  def create_layout(self, file_path: str) -> None:
    """
    Parameters:
    file_path - resulting svg path

    Returns:
    None
    """

    hght: int = Dims.to_in_str(Dims.LETTER_SIZE_WIDTH)
    wdth: int = Dims.to_in_str(Dims.LETTER_SIZE_LNGTH)

    if (self.is_portrait_):
      hght = Dims.to_in_str(Dims.LETTER_SIZE_LNGTH)
      wdth = Dims.to_in_str(Dims.LETTER_SIZE_WIDTH)

    page_layout = svgwrite.Drawing(file_path
      , profile='tiny'
      , size=(wdth, hght)
    )

    content_wdth, content_hght =\
      Dims.calc_content_size(self.is_portrait_)

    if (True):#self.is_portrait_):
      insert_pos00 = Dims.STD_MARGIN
      insert_pos01 = Dims.BINDER_MARGIN

      insert_pos10 = Dims.STD_MARGIN
      insert_pos11 = content_hght\
        + Dims.STD_MARGIN\
        + 2 * Dims.BINDER_MARGIN

      if (self.is_dbl_sided_):
        insert_pos01 = Dims.STD_MARGIN

    insert_pos0: Tuple =\
    ( Dims.to_in_str(insert_pos00)
    , Dims.to_in_str(insert_pos01)
    )

    insert_pos1: Tuple =\
    ( Dims.to_in_str(insert_pos10)
    , Dims.to_in_str(insert_pos11)
    )

    content_box_0: svgwrite.shapes.Rect =\
      self.create_content_box(insert_pos0)

    content_box_1: svgwrite.shapes.Rect =\
      self.create_content_box(insert_pos1)

    page_layout.add(content_box_0)
    page_layout.add(content_box_1)

    page_layout.save()

  #_____________________________________________________________________
  def create_content_box(self
    , insert_position: Tuple) -> svgwrite.shapes.Rect:
    """
    Creates rectangle that will contain content.
    """
    size: Tuple = Dims.calc_content_size(self.is_portrait_)
    w: str = Dims.to_in_str(size[0])
    h: str = Dims.to_in_str(size[1])

    content_box: svgwrite.shapes.Rect =\
      svgwrite.shapes.Rect(size=(w, h)
      , id="flux"
      , insert=insert_position
      , stroke=Colors.DEBUG0_COLOR
      , fill=Colors.DEBUG1_COLOR)

    return content_box