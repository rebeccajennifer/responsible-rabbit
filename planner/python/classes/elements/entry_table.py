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

from classes.elements.header_box import HeaderBox

from classes.constants.error_strings import ErrorStrings as Err
from classes.constants.dims import PlannerDims as Dims
from classes.constants.style import PlannerColors as Colors
from classes.constants.style import PlannerFontStyle as Font
from classes.constants.strings import PlannerStrings as Strings

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
  , entry_col_count: int = 1
  , entry_row_count: int = 1
  , entry_row_hght: int = DEF_ROW_HGHT
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
        entry_col_count : column count of table
        entry_row_count : row count of table
        entry_row_hght  : height of row, optional
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

    self.box_brdr_color_  : str   = box_brdr_color
    self.entry_col_count_ : int   = entry_col_count
    self.entry_row_count_ : int   = entry_row_count
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
      , font_color=self.font_color_
      , font_size=self.font_size_
      , font=self.font_
      , box_fill_color=self.box_fill_color_
      , box_brdr_color=self.box_brdr_color_
      , pad_top=self.pad_top_
      , pad_lft=self.pad_lft_
      , pad_rgt=self.pad_rgt_
      )

    # Height will take priority in calculation of row height
    if (self.total_hght_):
      self.row_hght_  = (self.total_hght_\
        - self.header_box_.total_hght_) / entry_row_count

    else:
      self.row_hght_ = entry_row_hght

      self.total_hght_ = self.header_box_.total_hght_\
      + entry_row_hght * entry_row_count\
      + self.pad_bot_ * Dims.BRD_MARGIN_PX

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

    for i in range(self.entry_row_count_):

      line_y: int = self.header_box_.total_hght_\
        + row_height\
        + i * row_height\

      row_line: svgwrite.shapes.Line =\
        svgwrite.shapes.Line\
        ( start=(self.insert_x_, line_y)
        , end=(self.insert_x_ + self.content_wdth_, line_y)
        , stroke=Colors.DEF_ROW_COLOR
        )

      row_group.add(row_line)

    return row_group

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
  , entry_col_count: int = 1
  , entry_row_count: int = 1
  , pad_top: bool = False
  , pad_bot: bool = False
  , pad_rgt: bool = False
  , pad_lft: bool = False
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
    , entry_col_count=entry_col_count
    , entry_row_count=entry_row_count
    , pad_top=pad_top
    , pad_bot=pad_bot
    , pad_rgt=pad_rgt
    , pad_lft=pad_lft
    , show_outline=True
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
  , entry_col_count: int = 1
  , entry_row_count: int = 1
  , entry_row_hght: int = EntryTable.DEF_ROW_HGHT
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
        prepend_txt        : list of text to include in rows
        font_color      : color of header text
        font_size       : size of header text
        font            : font of header text
        box_fill_color  : header fill color
        box_brdr_color  : border color
        entry_col_count : column count of table
        entry_row_count : row count of table
        entry_row_hght  : height of row, optional
        pad_top         : add padding to top
        pad_bot         : add padding to bottom
        pad_rgt         : add padding to right
        pad_lft         : add padding to left
        show_outline    : show table outline
    """

    self.prepend_txt_ = [''] * entry_row_count
    #___________________________________________________________________
    # If prepend_txt is not provided, default to numbered.
    #___________________________________________________________________
    if (not prepend_txt):
      for i in range(entry_row_count):
        self.prepend_txt_ = self.prepend_txt_ + [i+1]
    #___________________________________________________________________
    # If prepend_txt is a string, prepend it to each row.
    #___________________________________________________________________
    elif (isinstance(prepend_txt, str)):
      self.prepend_txt_ = [prepend_txt] * entry_row_count
    #___________________________________________________________________
    # Otherwise, assign prepend_txt to class variable
    #___________________________________________________________________
    else:
      for i in range(entry_row_count):
        try:
          self.prepend_txt_[i] = prepend_txt[i]

        except IndexError:
          self.prepend_txt_[i] = ''
    #___________________________________________________________________


    super().__init__\
    ( wdth           =wdth
    , hght           =hght
    , header_txt     =header_txt
    , font_color     =font_color
    , font_size      =font_size
    , font           =font
    , box_fill_color =box_fill_color
    , box_brdr_color =box_brdr_color
    , entry_col_count=entry_col_count
    , entry_row_count=entry_row_count
    , entry_row_hght =entry_row_hght
    , pad_top        =pad_top
    , pad_bot        =pad_bot
    , pad_rgt        =pad_rgt
    , pad_lft        =pad_lft
    , show_outline   =show_outline
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

    row_group: svgwrite.container.Group = svgwrite.container.Group()

    row_height: int = self.row_hght_

    text_x: int = 0

    if (self.show_outline_):
      text_x = Font.TEXT_PADDING + self.insert_x_


    for i in range(self.entry_row_count_):

      line_y: int = self.header_box_.total_hght_\
        + row_height\
        + i * row_height\

      text_y: int = line_y - 6

      row_line: svgwrite.shapes.Line =\
        svgwrite.shapes.Line\
        ( start=(self.insert_x_, line_y)
        , end=(self.insert_x_ + self.content_wdth_, line_y)
        , stroke=Colors.DEF_ROW_COLOR
        )

      txt: svgwrite.txt.Text = svgwrite.text.Text\
      ( self.prepend_txt_[i]
      , insert=(text_x, text_y)
      , text_anchor='start'
      , alignment_baseline='text-after-edge'
      , fill=Colors.NORMAL
      , font_size=Font.LITTLE_SIZE
      , font_family=Font.FONT_FAMILY_NORMAL
      )

      row_group.add(row_line)
      row_group.add(txt)

    return row_group


