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
#   Block of rows for tables.
#_______________________________________________________________________

import svgwrite

from classes.constants.dims import PlannerDims as Dims
from classes.constants.error_strings import ErrorStrings as Err
from classes.constants.style import PlannerFontStyle as Font
from classes.constants.style import PlannerColors as Colors
from utils.utils import PlannerUtils as Utils

from classes.elements.base_element import BaseElement
#_______________________________________________________________________
class TableRows(BaseElement):

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

      row_count       : Row count of table
      row_hght        : Height of row, optional
      col_count       : Column count of table
      col_wdths       : Width of rows, optional
                        expect that number of elements = col_count
      inner_pad_lft   : Pad left side of row inside border
      inner_pad_rgt   : Pad right side of row inside border
    """

    self.row_count_ : int   = row_count
    self.row_hght_  : int   = row_hght

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

    y_coord: list = self.get_y_of_rows()

    self.rows_: svgwrite.container.Group =\
      self.create_row_lines\
      ( total_len=self.content_wdth_
      , pad_lft=self.inner_pad_lft_
      , pad_rgt=self.inner_pad_rgt_
      , y_offset= 0
      , y_coord=y_coord
      )

    return

  #_____________________________________________________________________
  def add_content(self):
    """
    Adds svgwrite objects to class.

    Parameters:
      None

    Returns:
      None
    """
    self.add(self.rows_)
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

  #_____________________________________________________________________
  def create_row_lines(self
    , total_len: int = 0
    , pad_lft: bool = False
    , pad_rgt: bool = False
    , y_offset: int = 0
    , y_coord: list = []
    ) -> svgwrite.container.Group:
    """
    Creates group of lines.

    Parameters:
      total_len : Total length of line / width of column
                  Does not account for padding; padding will reduce
                  the actual drawn length
      pad_lft   : Add padding to left, modifies length of drawn line
      pad_rgt   : Add padding to right, modifies length of drawn line
      y_coord   : List of y coordinates for line insertion
    """

    start_padding: int = Font.TEXT_PADDING/2 * pad_lft
    end_padding:   int = Font.TEXT_PADDING/2 * pad_rgt
    line_len:      int = total_len - start_padding - end_padding
    insert_x:      int = start_padding + self.insert_x_

    row_group: svgwrite.container.Group = svgwrite.container.Group()

    for y in y_coord:

      insert_y: int = y - y_offset

      row_line: svgwrite.shapes.Line =\
        svgwrite.shapes.Line\
        ( start=(insert_x, insert_y)
        , end=(insert_x + line_len, insert_y)
        , stroke=Colors.DEF_ROW_COLOR
        )

      row_group.add(row_line)

    return row_group

#_______________________________________________________________________
class DoubleTableRows(TableRows):
  """
  Double line rows for better spacing to allow for letter descenders,
  i.e. the bottom part of letters g, j, p, q, y
  """
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
  , row_count: int = 1
  , row_hght: int = TableRows.DEF_ROW_HGHT
  , col_count: int = 1
  , col_wdths: list = []
  , inner_pad_lft: bool = False
  , inner_pad_rgt: bool = False
  , y_offset: int = 0
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

      row_count       : Row count of table
      row_hght        : Height of row, optional
      col_count       : Column count of table
      col_wdths       : Width of rows, optional
                        expect that number of elements = col_count
      inner_pad_lft   : Pad left side of row inside border
      inner_pad_rgt   : Pad right side of row inside border
    """

    self.y_offset_: int = y_offset

    super().__init__\
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
    , row_count=row_count
    , row_hght=row_hght
    , col_count=col_count
    , col_wdths=col_wdths
    , inner_pad_lft=inner_pad_lft
    , inner_pad_rgt=inner_pad_rgt
    )

    return


  #_____________________________________________________________________
  def create_content(self):
    """
    Add two lines
    """

    super().create_content()

    y_coord: list = self.get_y_of_rows()

    y_offset: int = 0
    y_offset: int = self.row_hght_ / 3

    self.double_rows_: svgwrite.container.Group =\
      self.create_row_lines\
      ( total_len=self.content_wdth_
      , pad_lft=self.inner_pad_lft_
      , pad_rgt=self.inner_pad_rgt_
      , y_offset=y_offset
      , y_coord=y_coord
      )

    return

  #_____________________________________________________________________
  def add_content(self):

    super().add_content()
    self.add(self.double_rows_)
    return

