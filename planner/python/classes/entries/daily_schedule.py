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
import svgwrite

from typing import Tuple

import svgwrite.container
import svgwrite.shapes
import svgwrite.text

from classes.constants.error_strings import ErrorStrings as Err
from classes.constants.dims import PlannerDims as Dims
from classes.constants.style import PlannerColors as Colors
from classes.constants.style import PlannerFontStyle as Font
from classes.constants.strings import PlannerStrings as Strings

class DailySchedule(svgwrite.container.Group):
  DEF_STRT_12: str = '05:00'
  DEF_STOP_12: str = '09:00'
  DEF_STRT_24: str = '05:00'
  DEF_STOP_24: str = '21:00'

  HEADER_SIZE: int = Font.NORMAL_SIZE
  HEADER_PADDING: int = HEADER_SIZE / 2
  HEADER_PADDING: int = 0

  #_____________________________________________________________________
  def __init__(self
  , strt_time_str: str = DEF_STRT_24
  , stop_time_str: str = DEF_STOP_24
  , wdth: int = 0
  , hght: int = 0
  , time_inc_min: int = 30
  , use_24: bool = True
  ):
    """
      Parameters:
        strt_time_str: start time of schedule
        stop_time_str: stop time of schedule
        wdth         : width of container
        hght         : height of container
        time_inc_min : incremental  time
        use_24       : use 24 hour time
    """

    super().__init__()

    self.strt_time_str_: str  = strt_time_str
    self.stop_time_str_: str  = stop_time_str
    self.wdth_: int           = wdth
    self.hght_: int           = hght
    self.time_inc_min_: int   = time_inc_min
    self.use_24_: bool        = use_24

    self.create_daily_schedule()

    return

  #_____________________________________________________________________
  def create_daily_schedule(self) -> None:
    """
    Creates schedule with times in increments as indicated. Assumes
    entry is in 24 hour format, though printed strings will reflect
    selection for use_24.

    Parameters:
      None

    Returns:
      None
    """

    fmt: str = '%I:%M'
    if (self.use_24_):
      fmt: str = '%H:%M'

    #___________________________________________________________________
    # Convert to datetime objects
    #___________________________________________________________________
    strt_datetime, stop_datetime =\
      DailySchedule.start_stop_err_check\
      ( self.strt_time_str_
      , self.stop_time_str_
      )

    crnt_datetime: dt.datetime = strt_datetime

    #___________________________________________________________________
    # Convert to strings
    #___________________________________________________________________
    stop_time_str =\
        stop_datetime.strftime(fmt)
    strt_time_str =\
        strt_datetime.strftime(fmt)
    #___________________________________________________________________

    crnt_datetime_str = strt_time_str

    #___________________________________________________________________
    time_block_count: int =\
      1\
      + (stop_datetime - strt_datetime).total_seconds()\
      / 60\
      / self.time_inc_min_

    header_space: int =\
      DailySchedule.HEADER_SIZE + DailySchedule.HEADER_PADDING

    # TODO account for padding
    time_box_wdth: int = self.wdth_
    time_box_hght: int = (self.hght_ - header_space) / time_block_count

    crnt_y: int = header_space + time_box_hght

    self.add(DailySchedule.create_schedule_header())

    #___________________________________________________________________
    # Create boxes with time increments
    while crnt_datetime <= stop_datetime:
      crnt_datetime_str =\
        crnt_datetime.strftime(fmt)

      self.add(
        DailySchedule.create_time_entry\
        ( crnt_datetime_str
        , crnt_y
        , time_box_wdth
        )
      )

      crnt_y = crnt_y + time_box_hght

      crnt_datetime =\
        crnt_datetime\
      + dt.timedelta(minutes=self.time_inc_min_)

    return

  #_____________________________________________________________________
  @staticmethod
  def start_stop_err_check(strt_time_str: str
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

    DEF_STRT: str = DailySchedule.DEF_STRT_24
    DEF_STOP: str = DailySchedule.DEF_STOP_24

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
      strt_datetime: dt.dt = dt.dt.strptime(DailySchedule.DEF_STRT, fmt_24)
      stop_datetime: dt.dt = dt.dt.strptime(DailySchedule.DEF_STOP, fmt_24)

      strt_datetime = dt.dt.combine(dt.dt.today(), strt_datetime.time())
      stop_datetime = dt.dt.combine(dt.dt.today(), stop_datetime.time())

    return strt_datetime, stop_datetime

  #_____________________________________________________________________
  @staticmethod
  def create_time_entry(time_str: str
  , bottom_y
  , wdth: int
  ) -> svgwrite.container.Group:
    """
    Creates text and lines for time entries

    Parameters:
      insert_y: Vertical insert point of entry
      wdth:     Width of container in inches
    """

    line_y: float = bottom_y
    text_y: float = bottom_y - 0.5 * Font.LITTLE_SIZE

    the_time: svgwrite.txt.Text = svgwrite.text.Text\
    ( time_str
    , insert=(0, text_y)
    , text_anchor='start'
    , alignment_baseline='middle'
    , fill=Colors.NORMAL
    , font_size=Font.LITTLE_SIZE
    , font_family=Font.FONT_FAMILY_NORMAL
    )

    line: svgwrite.shapes.Line = svgwrite.shapes.Line\
    ( start=(0, line_y)
    , end=(wdth, line_y)
    , stroke=Colors.DEBUG0_COLOR
    )

    group: svgwrite.container.Group = svgwrite.container.Group()

    if (':00' in time_str):
      group.add(the_time)

    group.add(line)

    return group

  #_____________________________________________________________________
  @staticmethod
  def create_schedule_header() -> svgwrite.text.Text:
    """
    Parameters:
      None

    Returns:
      svgwrite Text object with header
    """

    font_size: int = DailySchedule.HEADER_SIZE
    insert_y: int = font_size / 2

    header: svgwrite.txt.Text = svgwrite.text.Text\
    ( Strings.DAILY_SCHEDULE_HEADER
    , insert=('0in', insert_y)
    , text_anchor='start'
    , alignment_baseline='middle'
    , fill=Colors.HEADING
    , font_size=font_size
    , font_family=Font.FONT_FAMILY_HEADER
    )

    return header
