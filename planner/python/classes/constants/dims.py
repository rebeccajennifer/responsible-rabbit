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
#   Dimensions used in planner
#_______________________________________________________________________

from typing import Tuple

class PlannerDims:
  """
  Dimensions used in planner creation
  """

  DPI: int = 96

  LETTER_SIZE_LNGTH_IN: int = 11
  LETTER_SIZE_WIDTH_IN: int = 8.5

  BND_MARGIN_IN: int = 0.75
  STD_MARGIN_IN: int = 0.25

  LETTER_SIZE_LNGTH_PX: int = DPI * LETTER_SIZE_LNGTH_IN
  LETTER_SIZE_WIDTH_PX: int = DPI * LETTER_SIZE_WIDTH_IN

  BND_MARGIN_PX: int = DPI * BND_MARGIN_IN
  STD_MARGIN_PX: int = DPI * STD_MARGIN_IN

  BRD_MARGIN_PX: int = 8

  #_____________________________________________________________________
  def to_in_str(dim: int) -> str:
    """
    Converts integer value to string appended with 'in'.

    Parameters:
      dim: Dimension to convert

    Returns:
      String indicating value appended with 'in'
    """
    return f'{dim}in'

  #_____________________________________________________________________
  def to_px_str(dim: int) -> str:
    """
    Converts integer value to string appended with 'px'.

    Parameters:
      dim: Dimension to convert

    Returns:
      String indicating value appended with 'px'
    """
    return f'{dim}px'

  #_____________________________________________________________________
  def calc_mid_margin_width(dbl_sided: bool) -> int:
    """
    Calculates the middle margin width. Doubles binder margin for
    double-sided print. Binder + standard margin for single-sided print.

    Parameters:
      dbl_sided: is the layout intended to be printed double-sided

    Returns:
      Width of middle margin
    """

    if (dbl_sided):
      return 2 * PlannerDims.BND_MARGIN_PX

    return PlannerDims.BND_MARGIN_PX + PlannerDims.STD_MARGIN_PX

  #_____________________________________________________________________
  def calc_content_size(is_portrait: bool) -> Tuple:
    """
    Calculates content size based on border size accounting for padding.
    """

    w, h = PlannerDims.calc_border_size(is_portrait)
    w = w - 2 * PlannerDims.BRD_MARGIN_PX
    h = h - 2 * PlannerDims.BRD_MARGIN_PX

    return (w, h)

  #_____________________________________________________________________
  def calc_border_size(is_portrait: bool) -> Tuple:
    """
    Calculates the size of the content border for page orientation.
    Portrait orientation means that each half sheet is of landscape
    orientation.

    Parameters:
      is_portrait:  is the page intended to be printed as a portrait

    Returns:
      width, height of content
    """

    Dims = PlannerDims

    short_side : int = 0.5 * (
      Dims.LETTER_SIZE_LNGTH_PX \
      - 2 * (Dims.STD_MARGIN_PX) \
      - 2 * (Dims.BND_MARGIN_PX)
    )

    long_side: int =\
      Dims.LETTER_SIZE_WIDTH_PX - 2 * Dims.STD_MARGIN_PX

    if (is_portrait):
      content_wdth = long_side
      content_hght = short_side

    else:
      content_wdth = short_side
      content_hght = long_side

    return (content_wdth, content_hght)

  #_____________________________________________________________________
  def inch_to_px(inches: int) -> int:
    """
    Converts inch unit to pixels.

    Parameters:
      inches: Value in inches

    Returns:
      Value in pixels
    """

    return inches * PlannerDims.DPI

