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
#   Copyright 2026, Rebecca Rashkin
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
#   Entry for one week of daily practices.
#_______________________________________________________________________

# Enables forward references in type hints, allowing us to use the
# class name 'FluxSvgObject' within the class definition itself.
from __future__ import annotations
from enum import IntEnum, auto

import svgwrite

#_______________________________________________________________________
class AnchorPt(IntEnum):
  """
  Enum for anchor points used in positioning elements.
  """
  TOP_LEFT  = auto()
  TOP_CNTR  = auto()
  TOP_RGHT  = auto()
  MID_LEFT  = auto()
  MID_CNTR  = auto()
  MID_RGHT  = auto()
  BOT_LEFT  = auto()
  BOT_CNTR  = auto()
  BOT_RGHT  = auto()

#_______________________________________________________________________
class FluxSvgObject(svgwrite.container.Group):
  """
  Base object for svg elements.
  """

  #_____________________________________________________________________
  def __init__(self
  , hght: int = 0
  , wdth: int = 0
  ):
    """
    Constructor for class. Assumes landscape orientation.
    """

    super().__init__()

    self.hght_ = hght
    self.wdth_ = wdth

    return

  #_____________________________________________________________________
  def overlay_element(self
  , obj: FluxSvgObject = None
  , anchor_pt: AnchorPt = AnchorPt.TOP_LEFT
  , padding: int = 0
  ) -> None:
    """
    Overlays the given object on top of this one. Assumes anchor point
    for geometry is top left and bottom left for text.

    Parameters:
      obj (FluxSvgObject): The object to overlay on top of this one.
    """


    insert_x: int = 0
    insert_y: int = 0

    if (anchor_pt == AnchorPt.TOP_LEFT or
        anchor_pt == AnchorPt.MID_LEFT or
        anchor_pt == AnchorPt.BOT_LEFT):

        if (padding):
          insert_x: int = padding

    if (anchor_pt == AnchorPt.TOP_LEFT or
        anchor_pt == AnchorPt.TOP_CNTR or
        anchor_pt == AnchorPt.TOP_RGHT):

        if (padding):
          insert_y: int = padding

    if (anchor_pt == AnchorPt.TOP_RGHT or
        anchor_pt == AnchorPt.MID_RGHT or
        anchor_pt == AnchorPt.BOT_RGHT):

        insert_x: int = self.wdth_ - obj.wdth_

        if (padding):
          insert_x -= padding

    if (anchor_pt == AnchorPt.BOT_RGHT or
        anchor_pt == AnchorPt.BOT_RGHT or
        anchor_pt == AnchorPt.BOT_RGHT):

        insert_y: int = self.hght_ - obj.hght_

        if (padding):
          insert_y -= padding

    if (anchor_pt == AnchorPt.MID_CNTR):

        insert_x: int = (self.wdth_ - obj.wdth_) // 2
        insert_y: int = (self.hght_ - obj.hght_) // 2

    obj['transform'] =\
      f'translate({insert_x},{insert_y})'

    self.add(obj)

    return