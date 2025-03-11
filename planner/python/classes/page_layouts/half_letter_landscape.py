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

class HalfLetterSize:

  #_____________________________________________________________________
  def print_something() -> None:
    """
    Test print function.

    Parameters:
    None

    Returns:
    None
    """
    print('hi there')
    return

  #_____________________________________________________________________
  def create_svg(file_path:str) -> None:
    """
    Test function to create an svg. This function was taken directly
    from ChatGPT

    Parameters:
    filename - resulting svg path

    Returns:
    None
    """

    page_layout = svgwrite.Drawing(file_path
      , profile='tiny'
      , size=(Dims.to_in_str(Dims.LETTER_SIZE_LNGTH)
        , Dims.to_in_str(Dims.LETTER_SIZE_WIDTH)
        )
      )

    insert_pos: Tuple =\
      Dims.to_in_str(Dims.STD_MARGIN), Dims.to_in_str(Dims.STD_MARGIN)

    content_box_0: svgwrite.shapes.Rect =\
      HalfLetterSize.create_content_box(True, insert_pos)

    content_box_1: svgwrite.shapes.Rect =\
      HalfLetterSize.create_content_box(True, insert_pos)

    page_layout.add(content_box_0)

    page_layout.save()

  #_____________________________________________________________________
  def create_content_box(is_portrait: bool
    , insert_position) -> svgwrite.shapes.Rect:
    """
    Creates rectangle that will contain content.
    """
    size: Tuple = Dims.calc_content_size(is_portrait)
    w: str = Dims.to_in_str(size[0])
    h: str = Dims.to_in_str(size[1])

    content_box: svgwrite.shapes.Rect =\
      svgwrite.shapes.Rect(size=(w, h)
      , id="flux"
      , insert=insert_position
      , stroke=Colors.DEBUG0_COLOR
      , fill=Colors.DEBUG1_COLOR)

    return content_box