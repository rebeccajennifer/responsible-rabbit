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
#   Creates hourly entry for daily schedule.
#_______________________________________________________________________

import svgwrite.container
import svgwrite.shapes
import svgwrite.text

from classes.constants.dims import PlannerDims as Dims
from classes.constants.style import PlannerColors as Colors
from classes.constants.style import PlannerFontStyle as Font
from classes.constants.strings import PlannerStrings as Strings

from classes.elements.header_box import HeaderBox

from utils.utils import PlannerUtils as Utils

class EntryTable(svgwrite.container.Group):

  DEF_ROW_HGHT: int = 20

  #_____________________________________________________________________
  def __init__(self
  , wdth: int = 0
  , hght: int = 0
  , header_txt: str = ''
  , font_color: str = Colors.DEF_TBLE_HEADER_TEXT
  , font_size: int = Font.NORMAL_SIZE
  , font: str = Font.FONT_FAMILY_HEADER
  , box_fill_color: str = Colors.DEF_TBLE_HEADER_FILL
  , box_brdr_color: str = Colors.BORDER_COLOR
  , row_count: int = 1
  , row_hght: int = DEF_ROW_HGHT
  , col_count: int = 1
  , col_wdths: list = []
  , pad_top: bool = False
  , pad_bot: bool = False
  , pad_rgt: bool = False
  , pad_lft: bool = False
  , show_outline: bool = True
  ):
    """
      Parameters:
        wdth            : width of table
        hght            : height of table
        header_txt      : list of headers
        font_color      : color of header text
        font_size       : size of header text
        font            : font of header text
        box_fill_color  : header fill color
        box_brdr_color  : border color
        row_count       : row count of table
        row_hght        : height of row, optional
        col_count       : column count of table
        col_wdths       : width of rows, optional
                          expect that number of elements = col_count
        col_count       : column count of table
        col_wdth        : width of rows, optional
                          expect that number of elements = col_count
        pad_top         : add padding to top
        pad_bot         : add padding to bottom
        pad_rgt         : add padding to right
        pad_lft         : add padding to left
        show_outline    : show table outline
    """

    super().__init__()

    self.total_wdth_  : int = wdth
    self.total_hght_  : int = hght

    self.content_wdth_: int =\
      self.total_wdth_ - Dims.BRD_MARGIN_PX * (pad_lft + pad_rgt)

    # Used to make header box
    self.font_color_      : str   = font_color
    self.font_size_       : int   = font_size
    self.font_            : str   = font
    self.box_fill_color_  : str   = box_fill_color

    if (box_fill_color == 'none'):
      self.font_color_ = Colors.NORMAL


    self.box_brdr_color_  : str   = box_brdr_color
    self.col_count_ : int   = col_count
    self.row_count_ : int   = row_count
    self.show_outline_    : bool  = show_outline

    self.pad_top_: bool = pad_top
    self.pad_bot_: bool = pad_bot
    self.pad_rgt_: bool = pad_rgt
    self.pad_lft_: bool = pad_lft

    self.insert_y_: int = self.pad_top_ * Dims.BRD_MARGIN_PX
    self.insert_x_: int = self.pad_lft_ * Dims.BRD_MARGIN_PX

    self.header_box_: HeaderBox =\
      HeaderBox\
      ( wdth=self.total_wdth_
      , header_txt=header_txt
      , col_wdths=col_wdths
      , font_color=self.font_color_
      , font_size=self.font_size_
      , font=self.font_
      , box_fill_color=self.box_fill_color_
      , box_brdr_color=self.box_brdr_color_
      , pad_top=self.pad_top_
      , pad_lft=self.pad_lft_
      , pad_rgt=self.pad_rgt_
      )

    #___________________________________________________________________
    # Row height calculation
    # Height will take priority in calculation of row height
    #___________________________________________________________________
    if (self.total_hght_):
      self.row_hght_  = (self.total_hght_\
        - self.header_box_.total_hght_) / row_count

    else:
      self.row_hght_ = row_hght
      self.total_hght_ = self.header_box_.total_hght_\
      + row_hght * row_count\
      + self.pad_bot_ * Dims.BRD_MARGIN_PX

    #___________________________________________________________________
    # Column width calculation and error handling
    # If no column widths specified, or number of elements in column
    # width list does not match the number of columns, make all columns
    # equal.
    #___________________________________________________________________
    self.col_wdths_: list = Utils.calc_col_wdths(self.content_wdth_, col_count, col_wdths)
    #___________________________________________________________________

    #___________________________________________________________________
    # Adjust dims for padding
    #___________________________________________________________________
    self.content_hght_ =\
      self.total_hght_ - (pad_top + pad_bot) * Dims.BRD_MARGIN_PX

    self.create_content()
    self.add_content()

    return

  #_____________________________________________________________________
  def create_content(self) -> None:
    """
    Create elements
    """

    # Table outline
    self.outline_: svgwrite.shapes.Rect =\
      svgwrite.shapes.Rect\
      ( size=(self.content_wdth_, self.content_hght_)
      , insert=(self.insert_x_, self.insert_y_)
      , stroke=Colors.DEBUG0_COLOR
      , fill='none'
      )

    self.rows_: svgwrite.container.Group =\
      self.create_rows()

    return

  #_____________________________________________________________________
  def create_rows(self) -> svgwrite.container.Group:
    """
    Creates group containing all rows of content entry.

    Parameters:
      None

    Returns:
      Group containing all rows.
    """

    row_group: svgwrite.container.Group = svgwrite.container.Group()
    row_height: int = self.row_hght_

    for i in range(self.row_count_):

      line_y: int = self.header_box_.total_hght_\
        + row_height\
        + i * row_height\

      start_line_x: int = self.insert_x_

      for i in range(len(self.col_wdths_)):

        wdth: int = self.col_wdths_[i]
        start_padding: int = Font.TEXT_PADDING/2
        end_padding:   int = Font.TEXT_PADDING/2

        # For the first column, don't pad left side
        if (i == 0):
          start_padding = 0

        # For the first column, don't pad right side
        if (i == (len(self.col_wdths_) - 1)):
          end_padding = 0

        line_len = wdth - start_padding - end_padding

        insert_line_x: int = start_line_x + start_padding

        row_line: svgwrite.shapes.Line =\
          svgwrite.shapes.Line\
          ( start=(insert_line_x, line_y)
          , end=(insert_line_x + line_len, line_y)
          , stroke=Colors.DEF_ROW_COLOR
          )

        start_line_x = start_line_x + wdth

        row_group.add(row_line)

    return row_group


  #_____________________________________________________________________
  def add_rows_with_columns(self):

   return

  #_____________________________________________________________________
  def add_content(self):

    self.add(self.header_box_)
    self.add(self.rows_)

    if (self.show_outline_):
      self.add(self.outline_)


#_______________________________________________________________________
class PromptTable(EntryTable):

  #_____________________________________________________________________
  def __init__(self
  , wdth: int = 0
  , hght: int = 0
  , header_txt: str = Strings.DEF_TABLE_HEADER
  , row_count: int = 1
  , row_hght: int = EntryTable.DEF_ROW_HGHT
  , col_count: int = 1
  , col_wdths: list = []
  , pad_top: bool = False
  , pad_bot: bool = False
  , pad_rgt: bool = False
  , pad_lft: bool = False
  , show_outline: bool = True
  ):

    super().__init__\
    ( wdth=wdth
    , hght=hght
    , header_txt=header_txt
    , font_color=Colors.NORMAL
    , font_size=Font.NORMAL_SIZE
    , font=Font.FONT_FAMILY_NORMAL
    , box_fill_color='none'
    , box_brdr_color='none'
    , row_count=row_count
    , row_hght=row_hght
    , col_count=col_count
    , col_wdths=col_wdths
    , pad_top=pad_top
    , pad_bot=pad_bot
    , pad_rgt=pad_rgt
    , pad_lft=pad_lft
    , show_outline=show_outline
    )

    return


#_______________________________________________________________________
class NumberedTable(EntryTable):
  """
  EntryTable with numbered rows.
  """

  #_____________________________________________________________________
  def __init__(self
  , wdth: int = 0
  , hght: int = 0
  , header_txt: str = [Strings.DEF_TABLE_HEADER]
  , prepend_txt: str = ''
  , font_color: str = Colors.DEF_TBLE_HEADER_TEXT
  , font_size: int = Font.NORMAL_SIZE
  , font: str = Font.FONT_FAMILY_HEADER
  , box_fill_color: str = Colors.DEF_TBLE_HEADER_FILL
  , box_brdr_color: str = Colors.BORDER_COLOR
  , row_count: int = 1
  , row_hght: int = EntryTable.DEF_ROW_HGHT
  , col_count: int = 1
  , col_wdths: list = []
  , pad_top: bool = False
  , pad_bot: bool = False
  , pad_rgt: bool = False
  , pad_lft: bool = False
  , show_outline: bool = True
  ):
    """
      Parameters:
        wdth            : width of table
        hght            : height of table
        header_txt      : list of headers
        prepend_txt     : list of text to include in rows
        font_color      : color of header text
        font_size       : size of header text
        font            : font of header text
        box_fill_color  : header fill color
        box_brdr_color  : border color
        col_count : column count of table
        row_count : row count of table
        row_hght  : height of row, optional
        pad_top         : add padding to top
        pad_bot         : add padding to bottom
        pad_rgt         : add padding to right
        pad_lft         : add padding to left
        show_outline    : show table outline
    """

    self.prepend_txt_ = [''] * row_count
    #___________________________________________________________________
    # If prepend_txt is not provided, default to numbered.
    #___________________________________________________________________
    if (not prepend_txt):
      for i in range(row_count):
        self.prepend_txt_ = self.prepend_txt_ + [i+1]
    #___________________________________________________________________
    # If prepend_txt is a string, prepend it to each row.
    #___________________________________________________________________
    elif (isinstance(prepend_txt, str)):
      self.prepend_txt_ = [prepend_txt] * row_count
    #___________________________________________________________________
    # Otherwise, assign prepend_txt to class variable
    #___________________________________________________________________
    else:
      for i in range(row_count):
        try:
          self.prepend_txt_[i] = prepend_txt[i]

        except IndexError:
          self.prepend_txt_[i] = ''
    #___________________________________________________________________


    super().__init__\
    ( wdth            =wdth
    , hght            =hght
    , header_txt      =header_txt
    , font_color      =font_color
    , font_size       =font_size
    , font            =font
    , box_fill_color  =box_fill_color
    , box_brdr_color  =box_brdr_color
    , row_count       =row_count
    , row_hght        =row_hght
    , col_count       =col_count
    , col_wdths       =col_wdths
    , pad_top         =pad_top
    , pad_bot         =pad_bot
    , pad_rgt         =pad_rgt
    , pad_lft         =pad_lft
    , show_outline    =show_outline
    )

  #_____________________________________________________________________
  def create_rows(self) -> svgwrite.container.Group:
    """
    Creates group containing all rows of content entry.

    Parameters:
      None

    Returns:
      Group containing all rows.
    """

    row_group: svgwrite.container.Group =\
      super().create_rows()

    row_height: int = self.row_hght_

    text_x: int = 0

    if (self.show_outline_):
      text_x = Font.TEXT_PADDING + self.insert_x_

    for i in range(self.row_count_):

      line_y: int = self.header_box_.total_hght_\
        + row_height\
        + i * row_height\

      text_y: int = line_y - Font.TEXT_PADDING

      txt: svgwrite.txt.Text = svgwrite.text.Text\
      ( self.prepend_txt_[i]
      , insert=(text_x, text_y)
      , text_anchor='start'
      , alignment_baseline='text-after-edge'
      , fill=Colors.NORMAL
      , font_size=Font.LITTLE_SIZE
      , font_family=Font.FONT_FAMILY_NORMAL
      )

      row_group.add(txt)

    return row_group


