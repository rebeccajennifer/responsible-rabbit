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

from classes.constants.dims import PlannerDims as Dims
from classes.style.style import PlannerColors as Colors
from classes.style.style import PlannerFontStyle as Font

#_______________________________________________________________________
class LineRowGroupStyle:
  """
  Encapsulates styling properties for row groups in a table.
  Includes attributes such as stroke width, color, dash array,
  and other visual characteristics used to render table elements
  consistently.
  """

  #_____________________________________________________________________
  def __init__(self
  , total_wdth: int = 0
  , total_hght: int = 0
  , row_hght: int = Dims.DEF_ROW_HGHT
  , line_wght: int = 1
  , line_color: str = Colors.DEF_ROW_COLOR
  , show_outline: bool = False
  , outline_color: str = Colors.BORDER_COLOR
  , y_offset: int = 0
  , inner_pad_top: bool = False
  , inner_pad_bot: bool = False
  , inner_pad_lft: bool = False
  , inner_pad_rgt: bool = False
  , dash_array: str = '1,0'
  ):
    """
    Parameters:
      total_wdth    : Total width of group
      total_hght    : Total height of group
      row_hght      : Height of rows
      line_wght     : Line weight
      line_color    : Row color
      show_outline  : Show outline bool
      outline_color : Outline color
      y_offset      : Offset positioning of objects
      inner_pad_top : Top padding, impacts height and text position
      inner_pad_bot : Right padding, impacts height and text position
      inner_pad_lft : Left padding, impacts length and insertion
      inner_pad_rgt : Right padding, impacts length
      dash_array    : Dash style in form 'dash length, space length'
    """
    self.total_wdth_    : int   = total_wdth
    self.total_hght_    : int   = total_hght
    self.row_hght_      : int   = row_hght
    self.line_wght_     : int   = line_wght
    self.line_color_    : str   = line_color
    self.show_outline_  : bool  = show_outline
    self.outline_color_ : bool  = outline_color
    self.y_offset_      : int   = y_offset
    self.inner_pad_top_ : bool  = inner_pad_top
    self.inner_pad_bot_ : bool  = inner_pad_bot
    self.inner_pad_lft_ : bool  = inner_pad_lft
    self.inner_pad_rgt_ : bool  = inner_pad_rgt
    self.dash_array_    : str   = dash_array

    return


#_______________________________________________________________________
class TextBoxStyle():
  """
  Contains style elements for text box.
  """

  LEFT_ALIGN: str = 'start'
  RGHT_ALIGN: str = 'end'
  CNTR_ALIGN: str = 'middle'

  #_____________________________________________________________________
  def __init__(self
  , show_outline: bool = False
  , outline_color: str = Colors.BORDER_COLOR
  , backgnd_color: str = 'none'
  , y_offset: int = 0
  , inner_pad_top: bool = False
  , inner_pad_bot: bool = False
  , inner_pad_lft: bool = False
  , inner_pad_rgt: bool = False
  , font_size: int = Font.NORMAL_SIZE
  , font_family: int = Font.FONT_FAMILY_NORMAL
  , font_color: str = Colors.NORMAL_TXT
  , line_spc: int = Font.DEF_LINE_SPC
  , alignment: str = LEFT_ALIGN
  ):
    """
    Parameters:
      show_outline  : Show outline bool
      outline_color : Outline color
      backgnd_color : Background of box
      y_offset      : Offset positioning of objects
      inner_pad_top : Top padding, impacts height and text position
      inner_pad_bot : Right padding, impacts height and text position
      inner_pad_lft : Left padding, impacts length and insertion
      inner_pad_rgt : Right padding, impacts length
      font_size     : Size of font
      font_family   : Font
      font_color    : Text color
      line_spc      : Line spacing for multiline text
    """

    self.show_outline_ : bool  = show_outline

    if (self.show_outline_):
      self.outline_color_: str   = outline_color

    else:
      self.outline_color_: str   = backgnd_color

    self.backgnd_color_: str   = backgnd_color
    self.y_offset_     : int   = y_offset
    self.inner_pad_top_: bool  = inner_pad_top
    self.inner_pad_bot_: bool  = inner_pad_bot
    self.inner_pad_lft_: bool  = inner_pad_lft
    self.inner_pad_rgt_: bool  = inner_pad_rgt
    self.font_size_    : int   = font_size
    self.font_family_  : str   = font_family
    self.font_color_   : str   = font_color
    self.line_spc_     : int   = line_spc
    self.alignment_    : str   = alignment

    return

  def set_font_color(self, x: str):
    self.font_color_ = x
    return

  def set_font_size(self, x: int):
    self.font_size_= x
    return

  def set_font_family(self, x: str):
    self.font_family_= x
    return
