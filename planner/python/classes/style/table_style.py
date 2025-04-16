from classes.constants.dims import PlannerDims as Dims
from classes.constants.style import PlannerColors as Colors
from classes.constants.style import PlannerFontStyle as Font


class TextBoxStyle():
  """
  Contains style elements for text box.
  """

  def __init__(self
  , total_wdth: int = 0
  , total_hght: int = 0
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
  ):
    """
    Parameters:
      total_wdth    : Total width of group
      total_hght    : Total height of group
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

    self.total_wdth_   : int   = total_wdth
    self.total_hght_   : int   = total_hght
    self.show_outline_ : bool  = show_outline
    self.outline_color_: str   = outline_color
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

    return

#_______________________________________________________________________
class TableStyle():
  """
  Contains style elements for tables.
  """