import copy
import svgwrite
import svgwrite.container
import svgwrite.shapes
import svgwrite.text

from classes.constants.dims import PlannerDims as Dims
from classes.constants.error_strings import ErrorStrings as Err
from classes.constants.style import PlannerFontStyle as Font
from classes.constants.style import PlannerColors as Colors
from utils.utils import PlannerUtils as Utils

from classes.elements.base_element import BaseElement


#_______________________________________________________________________
class Rows(BaseElement):
  """
  Group of objects that are rendered in rows.
  """

  DEF_ROW_HGHT: int = 30

  #_____________________________________________________________________
  def __init__(self
  , wdth: int = 0
  , hght: int = 0
  , font_color: str = Colors.NORMAL_TXT
  , font_size: int = Font.NORMAL_SIZE
  , font: str = Font.FONT_FAMILY_HEADER
  , pad_top: bool = False
  , pad_bot: bool = False
  , pad_rgt: bool = False
  , pad_lft: bool = False
  , show_outline: bool = True
  , outline_color: str = Colors.BORDER_COLOR
  , row_color: str = Colors.BORDER_COLOR
  , row_count: int = 1
  , row_hght: int = DEF_ROW_HGHT
  , col_count: int = 1
  , col_wdths: list = []
  , inner_pad_lft: bool = False
  , inner_pad_rgt: bool = False
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

      row_count       : Row count of table
      row_hght        : Height of row, optional
      col_count       : Column count of table
      col_wdths       : Width of columns, optional
                        expect that # of elements = col_count
      inner_pad_lft   : Pad left side of row inside border
      inner_pad_rgt   : Pad right side of row inside border
    """

    self.row_count_ : int   = row_count
    self.row_hght_  : int   = row_hght
    self.row_color_ : str   = row_color

    self.col_count_ : int   = col_count
    self.col_wdths_ : int   = col_wdths

    self.inner_pad_lft_ : bool = inner_pad_lft
    self.inner_pad_rgt_ : bool = inner_pad_rgt

    return super().__init__\
      ( wdth=wdth
      , hght=hght
      , font_color=font_color
      , font_size=font_size
      , font=font
      , pad_top=pad_top
      , pad_bot=pad_bot
      , pad_rgt=pad_rgt
      , pad_lft=pad_lft
      , show_outline=show_outline
      , outline_color=outline_color
      )

  #_____________________________________________________________________
  def set_dims(self) -> int:
    """
    Calculates total_hght_, content_hght_, and/or row height depending
    on what is provided. Calculates column widths if necessary.

    Parameters:
      None
    """

    #___________________________________________________________________
    # Error handling
    #___________________________________________________________________
    if ( (not self.row_count_) or
         (not self.total_hght_ and not self.row_hght_)
    ):
      raise ValueError(Err.INSUFFICIENT_ARGS)

    if (self.total_hght_ and not self.content_hght_):
      raise RuntimeError(Err.INVALID_CONDITION)
    #___________________________________________________________________

    #___________________________________________________________________
    # Row height calculation
    #
    # Provided height will take priority in calculation of row height
    #___________________________________________________________________
    if (self.total_hght_):
      self.row_hght_ = self.content_hght_ / self.row_count_

    else:
      self.content_hght_: int = self.row_hght_ * self.row_count_

      self.total_hght_: int = self.content_hght_\
        + Dims.BRD_MARGIN_PX * (self.pad_top_ + self.pad_bot_)

    #___________________________________________________________________
    # Column width calculation and error handling
    #
    # If no column widths specified, or number of elements in column
    # width list does not match the number of columns, make all columns
    # equal.
    #___________________________________________________________________
    self.col_wdths_: list = Utils.calc_col_wdths\
      (self.content_wdth_, self.col_count_, self.col_wdths_)
    #___________________________________________________________________

    return

  #_____________________________________________________________________
  def create_content(self):
    """
    Parameters:
      None

    Side Effects:
      Populates class variables for entries.
    """

    self.y_coord_: list = self.get_y_of_rows()

    return

  #_____________________________________________________________________
  def get_y_of_rows(self) -> svgwrite.container.Group:
    """
    Returns list of y coordinates of rows.

    Parameters:
      None

    Returns:
      List of y coordinates where row objects will be inserted.
    """

    y_coord: list = []

    for i in range(self.row_count_):
      y: int = self.row_hght_ + i * self.row_hght_

      y_coord = y_coord + [y]

    return y_coord

#_______________________________________________________________________
class RowGroup(svgwrite.container.Group):
  """
  Creates a group of objects, positioned in rows.
  """

  DEF_ROW_HGHT: int = 30

  def __init__(self
  , wdth: int = 0
  , total_hght: int = 0
  , show_outline: bool = True
  , outline_color: str = Colors.BORDER_COLOR
  , backgnd_color: str = 'none'
  , row_hght: int = DEF_ROW_HGHT
  , y_offset: int = 0
  , inner_pad_top: bool = False
  , inner_pad_bot: bool = False
  , inner_pad_lft: bool = False
  , inner_pad_rgt: bool = False
  , obj_list: list = []
  ):
    """
    Parameters:
      wdth            : Width of table
      total_hght      : Height of table
      show_outline    : Show table outline
      outline_color   : Color of outline
      backgnd_color   : Background color of group
      row_hght        : Height of row, optional
      y_offset        : Offset positioning of objects
      inner_pad_lft   : Pad left side of row inside border
      inner_pad_rgt   : Pad right side of row inside border
    """

    super().__init__()

    self.wdth_          : int  = wdth
    self.inner_pad_top_ : bool = inner_pad_top
    self.inner_pad_bot_ : bool = inner_pad_bot
    self.inner_pad_lft_ : bool = inner_pad_lft
    self.inner_pad_rgt_ : bool = inner_pad_rgt
    self.obj_list_      : list = obj_list
    self.show_outline_  : bool = show_outline
    self.outline_color_ : bool = outline_color
    self.backgnd_color_ : bool = backgnd_color
    self.y_offset_      : int  = y_offset

    row_count     : int  = len(obj_list)


    #___________________________________________________________________
    # Determine heights based on given information
    #___________________________________________________________________
    self.total_hght_ = total_hght
    #___________________________________________________________________
    if (total_hght and (inner_pad_top or inner_pad_top)):
      self.content_height_ = total_hght -\
        Dims.BRD_MARGIN_PX * (inner_pad_top + inner_pad_bot)

    self.content_height_, self.row_hght_ =\
      Utils.get_hght_from_rows(total_hght, row_count, row_hght)

    if ((not inner_pad_top) and (not inner_pad_bot)):
      self.total_hght_ = self.content_height_

    else:
      self.total_hght_ = self.content_height_ + Dims.BRD_MARGIN_PX * (inner_pad_bot + inner_pad_top)


    self.add_content()

    return

  #_____________________________________________________________________
  def add_content(self):
    """
    Adds row objects and outline to group.

    Parameters:
      None

    Side Effects:
      Adds objects in rows to self.

    Returns:
      None
    """
    #___________________________________________________________________
    # Add rows
    #___________________________________________________________________
    insert_x: int = Dims.BRD_MARGIN_PX * self.inner_pad_lft_
    insert_y: int = self.row_hght_ - self.y_offset_ + Dims.BRD_MARGIN_PX * self.inner_pad_top_

    for obj in self.obj_list_:
      obj['transform'] =\
        f'translate({insert_x},{insert_y})'
      self.add(obj)

      insert_y = insert_y  + self.row_hght_

    #___________________________________________________________________
    # Add outline
    #___________________________________________________________________
    if (self.show_outline_):
      Utils.add_outline\
      ( container=self
      , hght=self.total_hght_
      , wdth=self.wdth_
      , outline_color=self.outline_color_
      , backgnd_color=self.backgnd_color_
      )


#_______________________________________________________________________
class LineRowGroup():
  """
  Organizes a set of line elements into evenly spaced horizontal rows.
  Ideal for creating multi-line visual groupings.
  """

  #_____________________________________________________________________
  def __init__(self
  , total_wdth: int = 0
  , total_hght: int = 0
  , row_count: int = 0
  , row_hght: int = RowGroup.DEF_ROW_HGHT
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
      line_wght     : Line weight
      line_color    : Row color
      show_outline  : Show outline bool
      outline_color : Outline color
      y_offset      : Offset positioning of objects
      inner_pad_lft : Left padding, impacts length and insertion
      inner_pad_rgt : Right padding, impacts length
      dash_array    : Dash style in form 'dash length, space length'
    """

    self.total_wdth_    : int = total_wdth
    self.total_hght_    : int = total_hght
    self.inner_pad_lft_ : bool = inner_pad_lft
    self.inner_pad_rgt_ : bool = inner_pad_rgt

    line_len: int =\
      total_wdth - Dims.BRD_MARGIN_PX * (inner_pad_lft + inner_pad_rgt)

    line: svgwrite.shapes.Line =\
      svgwrite.shapes.Line\
      ( start=(0,0)
      , end=(line_len, 0)
      , stroke=line_color
      , stroke_width=line_wght
      , stroke_dasharray=dash_array
      )

    line_array: list =\
      [copy.deepcopy(line) for _ in range(row_count)]

    self.line_row_group_: RowGroup =\
      RowGroup\
      ( wdth=total_wdth
      , total_hght=total_hght
      , show_outline=show_outline
      , outline_color=outline_color
      , y_offset=y_offset
      , inner_pad_top=inner_pad_top
      , inner_pad_bot=inner_pad_bot
      , inner_pad_lft=inner_pad_lft
      , inner_pad_rgt=inner_pad_rgt
      , obj_list=line_array
      )

    return

#_______________________________________________________________________
class TextRowGroup(RowGroup):
  """
  Breaks a string into multiple lines and arranges them as rows of text
  elements. Designed for displaying paragraph-like content within an SVG
  layout.
  """

  #_____________________________________________________________________
  def __init__(self
  , total_wdth: int = 0
  , total_hght: int = 0
  , show_outline: bool = False
  , outline_color: str = Colors.BORDER_COLOR
  , y_offset: int = 0
  , inner_pad_top: bool = False
  , inner_pad_bot: bool = False
  , inner_pad_lft: bool = False
  , inner_pad_rgt: bool = False
  , text: str = ''
  , font_size: int = Font.NORMAL_SIZE
  , font_family: int = Font.FONT_FAMILY_NORMAL
  , font_color: str = Colors.NORMAL_TXT
  , line_spc: int = 1
  ):
    """
    Parameters:
      total_wdth    : Total width of group
      total_hght    : Total height of group
      line_wght     : Line weight
      line_color    : Row color
      show_outline  : Show outline bool
      outline_color : Outline color
      y_offset      : Offset positioning of objects
      inner_pad_top : Top padding, impacts height and text position
      inner_pad_bot : Right padding, impacts height and text position
      inner_pad_lft : Left padding, impacts length and insertion
      inner_pad_rgt : Right padding, impacts length
    """

    self.total_wdth_    : int  = total_wdth
    self.inner_pad_top_ : bool = inner_pad_top
    self.inner_pad_bot_ : bool = inner_pad_bot
    self.inner_pad_lft_ : bool = inner_pad_lft
    self.inner_pad_rgt_ : bool = inner_pad_rgt
    self.font_size_     : int  = font_size
    self.font_family_   : int  = font_family
    self.line_spc_      : int  = line_spc

    # Error handling for line space
    if (line_spc < 1):
      self.line_spc_ = 1

    self.row_hght_ = self.line_spc_ * self.font_size_

    content_width: int =\
      total_wdth - Dims.BRD_MARGIN_PX * (inner_pad_lft + inner_pad_rgt)

    split_text: list =\
        Utils.split_txt_by_wdth\
        ( txt=text
        , px_wdth=content_width
        , font_size=font_size
        , font_family=font_family
        )


    text_array: list = len(split_text) * ['']

    for i in range(len(split_text)):
      svg_text: svgwrite.text.Text =\
        svgwrite.text.Text\
        ( text=split_text[i]
        , text_anchor='start'
        , alignment_baseline='text-after-edge'
        , fill=font_color
        , font_size=font_size
        , font_family=font_family
        )

      text_array[i] = svg_text

    self.text_row_group_: RowGroup =\
      RowGroup\
      ( wdth=total_wdth
      , total_hght=total_hght
      , show_outline=show_outline
      , outline_color=outline_color
      , row_hght=self.row_hght_
      , y_offset=y_offset
      , inner_pad_top=inner_pad_top
      , inner_pad_bot=inner_pad_bot
      , inner_pad_lft=inner_pad_lft
      , inner_pad_rgt=inner_pad_rgt
      , obj_list=text_array
      )

    return
