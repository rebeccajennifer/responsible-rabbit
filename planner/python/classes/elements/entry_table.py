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

from typing import Tuple

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

  #_____________________________________________________________________
  def __init__(self
  , wdth: int = 0
  , hght: int = 0
  , text_lst: str = [Strings.DEF_TABLE_HEADER]
  , font_color: str = Colors.NORMAL
  , font_size: int = Font.NORMAL_SIZE
  , font: str = Font.FONT_FAMILY_NORMAL
  , box_fill_color: str = Colors.LIGHT_GREY
  , box_brdr_color: str = Colors.BORDER_COLOR
  , entry_col_count: int = 1
  , entry_row_count: int = 1
  , pad_top: bool = False
  , pad_bot: bool = False
  , pad_rgt: bool = False
  , pad_lft: bool = False
  ):
    """
      Parameters:
        wdth            : width of table
        hght            : height of table
        text_lst        : list of headers
        font_color      : color of header text
        font_size       : size of header text
        font            : font of header text
        box_fill_color  : header fill color
        box_brdr_color  : border color
        entry_col_count : column count of table
        entry_row_count : row count of table
        pad_top         : add padding to top
        pad_bot         : add padding to bottom
        pad_rgt         : add padding to right
        pad_lft         : add padding to left
    """

    super().__init__()

    self.wdth_: int     = wdth
    self.hght_: int     = hght

    self.pad_top_: bool = pad_top
    self.pad_bot_: bool = pad_bot
    self.pad_rgt_: bool = pad_rgt
    self.pad_lft_: bool = pad_lft

    #___________________________________________________________________
    # Adjust dims for padding
    if (pad_top):
      self.hght_ = self.hght_ - Dims.BRD_MARGIN_PX
    if (pad_bot):
      self.hght_ = self.hght_ - Dims.BRD_MARGIN_PX
    if (pad_rgt):
      self.wdth_ = self.wdth_ - Dims.BRD_MARGIN_PX
    if (pad_lft):
      self.wdth_ = self.wdth_ - Dims.BRD_MARGIN_PX
    #___________________________________________________________________

    self.box_brdr_color_: str   = box_brdr_color
    self.entry_col_count_: int  = entry_col_count
    self.entry_row_count_: int  = entry_row_count


    # Used to make header box
    self.text_lst_: str         = text_lst
    self.font_color_: str       = font_color
    self.font_size_: int        = font_size
    self.font_: str             = font
    self.box_fill_color_: str   = box_fill_color

    self.create_content()

    self.add_content()

    return


  #_____________________________________________________________________
  def create_content(self) -> None:
    """
    Create elements
    """

    self.header_box_: HeaderBox =\
      HeaderBox\
      ( wdth=self.wdth_
      , text_lst=self.text_lst_
      , font_color=self.font_color_
      , font_size=self.font_size_
      , font=self.font_
      , box_fill_color=self.box_fill_color_
      , box_brdr_color=self.box_brdr_color_
      )

    entry_height: int = self.hght_ - self.header_box_.hght_

    # Table outline
    self.outline_: svgwrite.shapes.Rect =\
      svgwrite.shapes.Rect\
      ( size=(self.wdth_, entry_height)
      , insert=(0, self.header_box_.hght_)
      , stroke=self.box_brdr_color_
      , fill='none'
      )

    self.total_row_hght_: int = self.hght_ - self.header_box_.hght_

  #_____________________________________________________________________
  def add_content(self):
    """
    Add content to EntryTable.
    """

    self.add(self.header_box_)
    self.add(self.outline_)


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

    row_height: int = self.total_row_hght_ / self.entry_row_count_

    line_len: int = self.wdth_ - 2 * Dims.BRD_MARGIN_PX

    line_start_x: int = Dims.BRD_MARGIN_PX
    line_end_x: int   = line_start_x + line_len

    for i in range(self.entry_row_count_):

      line_y: int = i * row_height

      row_line: svgwrite.shapes.Line =\
        svgwrite.shapes.Line\
        ( start=(line_start_x, line_y)
        , end=(line_end_x, line_y)
        , stroke=Colors.DEBUG1_COLOR
        )

      row_group.add(row_line)

    return row_group

  #_____________________________________________________________________
  def create_table_outline(self) -> None:
    """
    Creates table from column and row count

    Parameters:
      None

    Returns:
      None
    """


    return outline

  #_____________________________________________________________________
  def add_content(self):

    self.add(self.header_box_)
    self.add(self.outline_)

#    row_height
#
#    #___________________________________________________________________
#    time_block_count: int =\
#      1\
#      + (stop_datetime - strt_datetime).total_seconds()\
#      / 60\
#      / self.time_inc_min_
#
#    header_space: int =\
#      DailySchedule.HEADER_SIZE + DailySchedule.HEADER_PADDING
#
#    time_box_wdth: int = self.wdth_
#    time_box_hght: int = (self.hght_ - header_space) / time_block_count
#
#    crnt_y: int = header_space + time_box_hght
#
#    #___________________________________________________________________
#    # Create boxes with time increments
#    while crnt_datetime <= stop_datetime:
#      crnt_datetime_str =\
#        crnt_datetime.strftime(fmt)
#
#      self.add(
#        DailySchedule.create_time_entry\
#        ( crnt_datetime_str
#        , crnt_y
#        , time_box_wdth
#        )
#      )
#
#      crnt_y = crnt_y + time_box_hght
#
#      crnt_datetime =\
#        crnt_datetime\
#      + dt.timedelta(minutes=self.time_inc_min_)
#
#    return
#
#  #_____________________________________________________________________
#  @staticmethod
#  def create_time_entry(time_str: str
#  , bottom_y
#  , wdth: int
#  ) -> svgwrite.container.Group:
#    """
#    Creates text and lines for time entries
#
#    Parameters:
#      insert_y: Vertical insert point of entry
#      wdth:     Width of container in inches
#    """
#
#    line_y: float = bottom_y
#    text_y: float = bottom_y - 0.5 * Font.LITTLE_SIZE
#
#    the_time: svgwrite.txt.Text = svgwrite.text.Text\
#    ( time_str
#    , insert=(0, text_y)
#    , text_anchor='start'
#    , alignment_baseline='middle'
#    , fill=Colors.NORMAL
#    , font_size=Font.LITTLE_SIZE
#    , font_family=Font.FONT_FAMILY_NORMAL
#    )
#
#    line: svgwrite.shapes.Line = svgwrite.shapes.Line\
#    ( start=(0, line_y)
#    , end=(wdth, line_y)
#    , stroke=Colors.DEBUG0_COLOR
#    )
#
#    group: svgwrite.container.Group = svgwrite.container.Group()
#
#    if (':00' in time_str):
#      group.add(the_time)
#
#    group.add(line)
#
#    return group
#
#  #_____________________________________________________________________
#  @staticmethod
#  def create_schedule_header() -> svgwrite.text.Text:
#    """
#    Parameters:
#      None
#
#    Returns:
#      svgwrite Text object with header
#    """
#
#    font_size: int = DailySchedule.HEADER_SIZE
#    insert_y: int = font_size / 2
#
#    header: svgwrite.txt.Text = svgwrite.text.Text\
#    ( Strings.DAILY_SCHEDULE_HEADER
#    , insert=('0in', insert_y)
#    , text_anchor='start'
#    , alignment_baseline='middle'
#    , fill=Colors.HEADING
#    , font_size=font_size
#    , font_family=Font.FONT_FAMILY_HEADER
#    )
#
#    return header
#