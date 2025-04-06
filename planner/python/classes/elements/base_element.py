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
import svgwrite.shapes

from classes.constants.style import PlannerFontStyle as Font
from classes.constants.style import PlannerColors as Colors
from classes.constants.dims import PlannerDims as Dims
from classes.constants.error_strings import ErrorStrings as Err


#_______________________________________________________________________
class BaseElement(svgwrite.container.Group):

  #_____________________________________________________________________
  def __init__(self
  , wdth: int = 0
  , hght: int = 0
  , font_color: str = Colors.NORMAL_TXT
  , font_size: int = Font.NORMAL_SIZE
  , font: str = Font.NORMAL_SIZE
  , pad_top: bool = False
  , pad_bot: bool = False
  , pad_rgt: bool = False
  , pad_lft: bool = False
  , show_outline: bool = True
  , outline_color: str = Colors.BORDER_COLOR
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
    """

    super().__init__()

    self.total_wdth_  : int = wdth
    self.total_hght_  : int = hght

    self.font_color_  : str   = font_color
    self.font_size_   : int   = font_size
    self.font_        : str   = font

    self.pad_top_: bool = pad_top
    self.pad_bot_: bool = pad_bot
    self.pad_rgt_: bool = pad_rgt
    self.pad_lft_: bool = pad_lft

    self.show_outline_  : bool  = show_outline
    self.outline_color_ : str = outline_color

    self.content_wdth_: int =\
      self.total_wdth_ - Dims.BRD_MARGIN_PX * (pad_lft + pad_rgt)

    #___________________________________________________________________
    # Calculate heights
    #
    # Some subclasses will calculate the content height from the total
    # height. Other classes will calculate the total height from the
    # content height.
    #
    # If no total height in the constructor is given, then assume that
    # the content height will be calculated by a subclass
    #___________________________________________________________________
    if (self.total_hght_):
      self.content_hght_: int = self.total_hght_\
        - Dims.BRD_MARGIN_PX * (self.pad_top_ + self.pad_bot_)

    self.set_dims()

    if (not hasattr(self, 'content_hght_')):
      raise AttributeError(Err.ABSTRACT_INIT)

    #___________________________________________________________________

    self.insert_y_: int = self.pad_top_ * Dims.BRD_MARGIN_PX
    self.insert_x_: int = self.pad_lft_ * Dims.BRD_MARGIN_PX

    self.create_content()
    self.add_content()
    self.add_outline()

  #_____________________________________________________________________
  def set_dims(self) -> int:
    """
    To be implemented by subclasses. Sets self.content_hght_ and
    self.total_height_ if total height is not provided in constructor.

    Parameters:
      None
    """
    return

  #_____________________________________________________________________
  def create_content(self) -> None:
    """
    To be implemented by subclasses.

    Parameters:
      None
    """
    return

  #_____________________________________________________________________
  def add_content(self) -> None:
    """
    To be implemented by subclasses.

    Parameters:
      None
    """
    return

  #_____________________________________________________________________
  def add_outline(self) -> None:
    """
    Creates rectangular outline around box.

    Parameters:
      None
    """

    if (self.show_outline_):
      self.add(
        svgwrite.shapes.Rect\
        ( size=(self.content_wdth_, self.content_hght_)
        , insert=(self.insert_x_, self.insert_y_)
        , stroke=self.outline_color_
        , fill='none'
        )
      )

    return