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

import datetime as dt
import math

from typing import Tuple

import svgwrite.container
import svgwrite.shapes
import svgwrite.text

from classes.elements.entry_table import EntryTable
from classes.constants.error_strings import ErrorStrings as Err
from classes.constants.style import PlannerColors as Colors
from classes.constants.style import PlannerFontStyle as Font
from classes.constants.strings import PlannerStrings as Strings

class DaySchedule(EntryTable):
  """
  Lists hours in daily schedule.
  """

  DEF_STRT_12: str = '05:00'
  DEF_STOP_12: str = '09:00'
  DEF_STRT_24: str = '05:00'
  DEF_STOP_24: str = '21:00'

  def __init__(self
  , wdth: int = 0
  , hght: int = 0
  , strt_time_str: str = DEF_STRT_24
  , stop_time_str: str = DEF_STOP_24
  , time_inc_min: int = 30
  , use_24: bool = True
  ):
    """
      Parameters:
        wdth         : width of container
        hght         : height of container
        strt_time_str: start time of schedule
        stop_time_str: stop time of schedule
        time_inc_min : incremental  time
        use_24       : use 24 hour time
    """

    self.time_inc_min_: int   = time_inc_min
    self.use_24_: bool        = use_24

    #___________________________________________________________________
    # Convert to datetime objects
    #___________________________________________________________________
    self.strt_datetime_, self.stop_datetime_ =\
      self.start_stop_err_check\
      ( strt_time_str
      , stop_time_str
      )

    entry_row_count: int = self.calc_row_count()

    super().__init__\
      ( wdth=wdth
      , hght=hght
      , text_lst=[Strings.DAILY_SCHEDULE_HEADER]
      , font_color=Colors.NORMAL
      , font_size=Font.NORMAL_SIZE
      , font=Font.FONT_FAMILY_HEADER
      , box_fill_color='none'
      , box_brdr_color='none'
      , entry_row_count=entry_row_count
      , pad_top=True
      , pad_bot=False
      , pad_lft=False
      , pad_rgt=False
      , show_outline=False
      )


    return

  #_____________________________________________________________________
  def calc_row_count(self) -> int:

    time_block_count: float = 1\
      + (self.stop_datetime_ - self.strt_datetime_).total_seconds()\
      / 60\
      / self.time_inc_min_

    return math.floor(time_block_count)

  #_____________________________________________________________________
  def create_rows(self
  , combined_row_hght
  ) -> svgwrite.container.Group:
    """
    Creates schedule with times in increments as indicated. Assumes
    entry is in 24 hour format, though printed strings will reflect
    selection for use_24.

    Parameters:
      None

    Returns:
      Group containing all rows.
    """

    row_group: svgwrite.container.Group = svgwrite.container.Group()

    fmt: str = '%I:%M'
    if (self.use_24_):
      fmt: str = '%H:%M'

    row_height: int = combined_row_hght / self.entry_row_count_

    crnt_datetime: dt.datetime = self.strt_datetime_

    text_x: int = 0
    if (self.show_outline_):
      text_x = Font.TEXT_PADDING

    for i in range(self.entry_row_count_):

      line_y: int = self.header_box_.total_hght_ + row_height + i * row_height
      text_y: int = line_y - 2

      crnt_datetime_str =\
        crnt_datetime.strftime(fmt)

      the_time: svgwrite.txt.Text = svgwrite.text.Text\
      ( crnt_datetime_str
      , insert=(text_x, text_y)
      , text_anchor='start'
      , alignment_baseline='text-after-edge'
      , fill=Colors.NORMAL
      , font_size=Font.LITTLE_SIZE
      , font_family=Font.FONT_FAMILY_NORMAL
      )

      if (':00' in crnt_datetime_str):
        row_group.add(the_time)

      crnt_datetime =\
        crnt_datetime\
      + dt.timedelta(minutes=self.time_inc_min_)

      row_line: svgwrite.shapes.Line =\
        svgwrite.shapes.Line\
        ( start=(0, line_y)
        , end=(self.content_wdth_, line_y)
        , stroke=Colors.DEBUG1_COLOR
        )

      row_group.add(row_line)

    return row_group

  #_____________________________________________________________________
  def start_stop_err_check(self
  , strt_time_str: str
  , stop_time_str: str
  ) -> Tuple:
    """
    Checks if start time is greater than stop time. Converts times to
    datetime objects with dates. Assumes input is in 24 hour format

    Parameters:
      strt_time_str: start time of daily schedule
      stop_time_str: stop time of daily schedule

    Returns:
      (datetime.datetime obj start, datetime.datetime obj stop)
    """

    dt.dt = dt.datetime

    fmt_24: str = '%H:%M'

    DEF_STRT: str = self.DEF_STRT_24
    DEF_STOP: str = self.DEF_STOP_24

    #___________________________________________________________________
    # Convert to datetime objects for error handling
    #___________________________________________________________________
    try:
      strt_datetime: dt.dt = dt.dt.strptime(strt_time_str, fmt_24)
      stop_datetime: dt.dt = dt.dt.strptime(stop_time_str, fmt_24)

      strt_datetime = dt.dt.combine(dt.dt.today(), strt_datetime.time())
      stop_datetime = dt.dt.combine(dt.dt.today(), stop_datetime.time())

    except:
      print(Err.INVALID_TIME)
      strt_datetime: dt.dt = dt.dt.strptime(DEF_STRT, fmt_24)
      stop_datetime: dt.dt = dt.dt.strptime(DEF_STOP, fmt_24)

      strt_datetime = dt.dt.combine(dt.dt.today(), strt_datetime.time())
      stop_datetime = dt.dt.combine(dt.dt.today(), stop_datetime.time())

    if (stop_datetime < strt_datetime):
      strt_datetime: dt.dt = dt.dt.strptime(self.DEF_STRT, fmt_24)
      stop_datetime: dt.dt = dt.dt.strptime(self.DEF_STOP, fmt_24)

      strt_datetime = dt.dt.combine(dt.dt.today(), strt_datetime.time())
      stop_datetime = dt.dt.combine(dt.dt.today(), stop_datetime.time())

    return strt_datetime, stop_datetime

















