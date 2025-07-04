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
#   Defines classes used to manage and render row-based layout elements.
#   This includes both visual styling properties and row group
#   positioning logic.
#_______________________________________________________________________

import svgwrite
import svgwrite.container
import svgwrite.shapes
import svgwrite.text

from copy import deepcopy

from classes.constants.dims import PlannerDims as Dims
from classes.style.std_styles import StdLineRowGroupStyles
from classes.style.style import PlannerFontStyle as Font
from classes.style.style import PlannerColors as Colors
from classes.style.table_style import LineRowGroupStyle
from classes.style.table_style import TextBoxStyle
from utils.utils import PlannerUtils as Utils


#_______________________________________________________________________
class RowGroup(svgwrite.container.Group):
  """
  Creates a group of objects, positioned in rows.
  """

  def __init__(self
  , total_wdth: int = 0
  , total_hght: int = 0
  , show_outline: bool = True
  , outline_color: str = Colors.BORDER_COLOR
  , backgnd_color: str = 'none'
  , row_hght: int = Dims.DEF_ROW_HGHT
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

    self.total_wdth_    : int  = total_wdth
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
    if (total_hght and (inner_pad_top or inner_pad_bot)):
      self.content_height_ = total_hght -\
        Font.TEXT_PADDING * (inner_pad_top + inner_pad_bot)

    self.content_height_, self.row_hght_ =\
      Utils.get_hght_from_rows(total_hght, row_count, row_hght)

    if ((not inner_pad_top) and (not inner_pad_bot)):
      self.total_hght_ = self.content_height_

    else:
      self.total_hght_ = self.content_height_ + Font.TEXT_PADDING * (inner_pad_bot + inner_pad_top)


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
    # Add outline and background
    #___________________________________________________________________
    if (self.show_outline_ or (not self.show_outline_ and self.backgnd_color_ != 'none')):
      Utils.add_outline\
      ( container=self
      , hght=self.total_hght_
      , wdth=self.total_wdth_
      , outline_color=self.outline_color_
      , backgnd_color=self.backgnd_color_
      )

    #___________________________________________________________________
    # Add rows
    #___________________________________________________________________
    insert_x: int = Font.TEXT_PADDING * self.inner_pad_lft_
    insert_y: int = self.row_hght_\
      - self.y_offset_\
      + Font.TEXT_PADDING * self.inner_pad_top_

    for obj in self.obj_list_:
      obj['transform'] =\
        f'translate({insert_x},{insert_y})'
      self.add(obj)

      insert_y = insert_y  + self.row_hght_


#_______________________________________________________________________
class LineRowGroup(RowGroup):
  """
  Organizes a set of line elements into evenly spaced horizontal rows.
  Ideal for creating multi-line visual groupings.
  """

  #_____________________________________________________________________
  def __init__(self
  , total_wdth: int = 0
  , total_hght: int = 0
  , row_count: int = 0
  , style: LineRowGroupStyle = LineRowGroupStyle()
  ):
    """
    Parameters:
      total_wdth    : Total width of group
      total_hght    : Total height of group
      row_count     : Number of rows
      style         : Style of rows including color, padding, y offset
    """

    self.y_offset_      : int   = style.y_offset_
    self.line_wght_     : str   = style.line_wght_
    self.line_color_    : str   = style.line_color_
    self.outline_color_ : str   = style.outline_color_
    self.show_outline_  : bool  = style.show_outline_
    self.inner_pad_lft_ : bool  = style.inner_pad_lft_
    self.inner_pad_rgt_ : bool  = style.inner_pad_rgt_
    self.inner_pad_top_ : bool  = style.inner_pad_top_
    self.inner_pad_bot_ : bool  = style.inner_pad_bot_
    self.dash_array_    : str   = style.dash_array_

    self.total_wdth_    : int   = total_wdth
    self.total_hght_    : int   = total_hght
    self.row_count_     : int   = row_count

    line_len: int = self.total_wdth_\
      - Font.TEXT_PADDING\
      * (self.inner_pad_lft_ + self.inner_pad_rgt_)

    line: svgwrite.shapes.Line =\
      svgwrite.shapes.Line\
      ( start=(0,0)
      , end=(line_len, 0)
      , stroke=self.line_color_
      , stroke_width=self.line_wght_
      , stroke_dasharray=self.dash_array_
      )

    line_array: list =\
      [deepcopy(line) for _ in range(self.row_count_)]

    return\
      super().__init__\
      ( total_wdth=self.total_wdth_
      , total_hght=self.total_hght_
      , show_outline=self.show_outline_
      , outline_color=self.outline_color_
      , y_offset=self.y_offset_
      , inner_pad_top=self.inner_pad_top_
      , inner_pad_bot=self.inner_pad_bot_
      , inner_pad_lft=self.inner_pad_lft_
      , inner_pad_rgt=self.inner_pad_rgt_
      , obj_list=line_array
      )

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
  , y_offset: int = 0
  , inner_pad_lft: bool = False
  , inner_pad_rgt: bool = False
  , text: str = ''
  , font_size: int = Font.NORMAL_SIZE
  , font_family: int = Font.FONT_FAMILY_NORMAL
  , font_color: str = Colors.NORMAL_TXT
  , line_spc: int = 1
  , style: TextBoxStyle = TextBoxStyle()
  , wrap_txt: bool = True
  ):
    """
    Parameters:
      total_wdth    : Total width of group
      total_hght    : Total height of group
      y_offset      : Offset positioning of objects
      inner_pad_lft : Left padding, impacts length and insertion
      inner_pad_rgt : Right padding, impacts length
    """

    self.show_outline_  = style.show_outline_
    self.outline_color_ = style.outline_color_
    self.backgnd_color_ = style.backgnd_color_
    self.inner_pad_top_ = style.inner_pad_top_
    self.inner_pad_bot_ = style.inner_pad_bot_
    self.inner_pad_lft_ = style.inner_pad_lft_
    self.inner_pad_rgt_ = style.inner_pad_rgt_
    self.font_color_    = style.font_color_
    self.font_family_   = style.font_family_
    self.font_size_     = style.font_size_
    self.line_spc_      = style.line_spc_

    #self.total_hght_    : int  = total_hght
    self.total_wdth_    : int  = total_wdth

    # Error handling for line space
    if (line_spc < 1):
      self.line_spc_ = 1

    self.row_hght_ = self.line_spc_ * self.font_size_

    content_width: int =\
      total_wdth - Font.TEXT_PADDING * (inner_pad_lft + inner_pad_rgt)

    if (wrap_txt):
      split_text: list =\
          Utils.split_txt_by_wdth\
          ( txt=text
          , px_wdth=content_width
          , font_size=font_size
          , font_family=font_family
          )
    else:
      split_text = [text]

    text_array: list = len(split_text) * ['']

    # Create list of text objects
    for i in range(len(split_text)):
      svg_text: svgwrite.text.Text =\
        svgwrite.text.Text\
        ( text=split_text[i]
        , text_anchor='start'
        , alignment_baseline='text-after-edge'
        , fill=self.font_color_
        , font_size=self.font_size_
        , font_family=self.font_family_
        )

      text_array[i] = svg_text

    return\
      super().__init__\
      ( total_wdth=total_wdth
      , total_hght=total_hght
      , show_outline=self.show_outline_
      , outline_color=self.outline_color_
      , backgnd_color=self.backgnd_color_
      , row_hght=self.row_hght_
      , y_offset=y_offset
      , inner_pad_top=self.inner_pad_top_
      , inner_pad_bot=self.inner_pad_bot_
      , inner_pad_lft=self.inner_pad_lft_
      , inner_pad_rgt=self.inner_pad_rgt_
      , obj_list=text_array
      )


#_______________________________________________________________________
class DualLineRowGroup(svgwrite.container.Group):
  """
  A group of lines arranged in row pairs, typically used for
  tables that are intended to be written in. Each pair includes
  additional space to accommodate descenders in letters like
  'y', 'p', and 'q'.
  """

  #_____________________________________________________________________
  def __init__(self
  , total_wdth: int = 0
  , total_hght: int = 0
  , row_count: int = 0
  , inner_pad_lft: bool = False
  , inner_pad_rgt: bool = False
  , pri_line_style: LineRowGroupStyle =\
      StdLineRowGroupStyles.ONE_THIRD_OFFSET
  , sec_line_style: LineRowGroupStyle =\
      StdLineRowGroupStyles.DOTTED
  ):
    """
    Parameters:
      total_wdth      : Total width of group
      total_hght      : Total height of group
      row_count       : Row count of table
      inner_pad_lft   : Pad line on left
      inner_pad_rgt   : Pad line on right
      pri_line_style  : Line style of primary line
      sec_line_style  : Line style of secondary line
    """

    super().__init__()

    self.sec_line_style_: LineRowGroupStyle =\
      deepcopy(sec_line_style)

    self.sec_line_style_.inner_pad_lft_ = inner_pad_lft
    self.sec_line_style_.inner_pad_rgt_ = inner_pad_rgt

    sec_line = LineRowGroup\
      ( total_wdth=total_wdth
      , total_hght=total_hght
      , row_count=row_count
      , style=self.sec_line_style_
      )

    self.pri_line_style_: LineRowGroupStyle =\
      deepcopy(pri_line_style)

    # Modify the offset based off the row height
    self.pri_line_style_.y_offset_ = sec_line.row_hght_/3
    self.pri_line_style_.inner_pad_lft_ = inner_pad_lft
    self.pri_line_style_.inner_pad_rgt_ = inner_pad_rgt

    pri_line = LineRowGroup\
      ( total_wdth=total_wdth
      , total_hght=total_hght
      , row_count=row_count
      , style=self.pri_line_style_
      )

    self.total_hght_ = pri_line.total_hght_
    self.total_wdth_ = total_wdth

    self.add(sec_line)
    self.add(pri_line)

    return
