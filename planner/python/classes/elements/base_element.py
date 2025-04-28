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
#   Base class for all table elements.
#_______________________________________________________________________

import svgwrite.container

from classes.constants.dims import PlannerDims as Dims
from classes.style.style import PlannerColors as Colors
from utils.utils import PlannerUtils as Utils


#_______________________________________________________________________
class VerticalStack(svgwrite.container.Group):

  def __init__(self
  , obj_list: list = []
  , add_top_pad: bool = False
  , show_outline: bool = False
  , outline_color: bool = Colors.BORDER_COLOR
  ) -> svgwrite.container.Group:
    """
    Creates a new svgwrite container with all objects stacked
    vertically.

    Parameters:
      obj_list    : List of SVG elements to be stacked. Each
                    element is expected to have a 'total_hght_'
                    attribute defining its height.

      add_top_pad : If True, adds uniform vertical padding
                    between elements. Padding is not added
                    above the first or below the last element.
    """

    super().__init__()
    padding: int = Dims.BRD_MARGIN_PX * add_top_pad
    insert_x: int = 0
    insert_y: int = padding
    self.total_hght_: int = 0
    self.total_wdth_: int = 0


    for i in range(len(obj_list)):

      obj_list[i]['transform'] =\
      f'translate({insert_x},{insert_y})'

      insert_y = insert_y\
        + obj_list[i].total_hght_\
        + padding

      self.total_hght_ += obj_list[i].total_hght_

      if (self.total_wdth_ < obj_list[i].total_wdth_):
        self.total_wdth_ = obj_list[i].total_wdth_

      self.add(obj_list[i])

    self.total_hght_ += padding * (len(obj_list))

    if (show_outline):
      Utils.add_outline\
      ( container=self
      , hght=self.total_hght_
      , wdth=self.total_wdth_
      , outline_color=outline_color
      )

    return

#_______________________________________________________________________
class HorizontalStack(svgwrite.container.Group):

  def __init__(self
  , obj_list: list = []
  , add_inner_pad: bool = False
  , total_hght: int = 0
  ) -> svgwrite.container.Group:
    """
    Creates a new svgwrite container with all objects stacked
    vertically.

    Parameters:
      obj_list    : List of SVG elements to be stacked. Each
                    element is expected to have a 'total_hght_'
                    attribute defining its height.

      add_top_pad : If True, adds uniform vertical padding
                    between elements. Padding is not added
                    above the first or below the last element.
    """

    super().__init__()
    padding: int = Dims.BRD_MARGIN_PX * add_inner_pad
    insert_x: int = 0
    insert_y: int = 0
    self.total_wdth_: int = 0
    self.total_hght_: int = 0

    for i in range(len(obj_list)):

      obj_list[i]['transform'] =\
      f'translate({insert_x},{insert_y})'

      insert_x = insert_x\
        + obj_list[i].total_wdth_\
        + padding

      self.total_wdth_ += obj_list[i].total_wdth_

      if ((obj_list[i].total_hght_) > (self.total_hght_)):
        self.total_hght_ = obj_list[i].total_hght_

      self.add(obj_list[i])

    self.total_wdth_ += padding * (len(obj_list) - 1)

    return