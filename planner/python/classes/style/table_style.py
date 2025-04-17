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
  , row_count: int = 0
  , row_hght: int = Dims.DEF_ROW_HGHT
  , line_wght: int = 1
  , line_color: str = Colors.BORDER_COLOR
  , show_outline: bool = False
  , outline_color: bool = False
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
      row_count     : Number of rows
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
    self.row_count_     : int   = row_count
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

  #_____________________________________________________________________
  def set_total_wdth(self, total_wdth: int):
    self.total_wdth = total_wdth
    return

  def set_total_hght(self, total_hght: int):
    self.total_hght = total_hght
    return

  def set_row_count(self, row_count: int):
    self.row_count = row_count
    return

  def set_row_hght(self, row_hght: int):
    self.row_hght = row_hght
    return

  def set_line_wght(self, line_wght: int):
    self.line_wght = line_wght
    return

  def set_line_color(self, line_color: str):
    self.line_color = line_color
    return

  def set_show_outline(self, show_outline: bool):
    self.show_outline = show_outline
    return

  def set_outline_color(self, outline_color: bool):
    self.outline_color = outline_color
    return

  def set_y_offset(self, y_offset: int):
    self.y_offset = y_offset
    return

  def set_inner_pad_top(self, inner_pad_top: bool):
    self.inner_pad_top = inner_pad_top
    return

  def set_inner_pad_bot(self, inner_pad_bot: bool):
    self.inner_pad_bot = inner_pad_bot
    return

  def set_inner_pad_lft(self, inner_pad_lft: bool):
    self.inner_pad_lft = inner_pad_lft
    return

  def set_inner_pad_rgt(self, inner_pad_rgt: bool):
    self.inner_pad_rgt = inner_pad_rgt
    return

  def set_dash_array(self, dash_array: str):
    self.dash_array = dash_array
    return


#_______________________________________________________________________
class TextBoxStyle():
  """
  Contains style elements for text box.
  """

  #
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
class TableRowStyle():
  """
  Contains style elements for tables.
  """