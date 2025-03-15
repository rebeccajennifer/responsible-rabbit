#_______________________________________________________________________
#_______________________________________________________________________
#       _   __   _   _ _   _   _   _         _
#  |   |_| | _  | | | V | | | | / |_/ |_| | /
#  |__ | | |__| |_| |   | |_| | \ |   | | | \_
#   _  _         _ ___  _       _ ___   _                    / /
#  /  | | |\ |  \   |  | / | | /   |   \                    (^^)
#  \_ |_| | \| _/   |  | \ |_| \_  |  _/                    (____)o
#_______________________________________________________________________
#_______________________________________________________________________
#
#-----------------------------------------------------------------------
#  Copyright 2024, Rebecca Rashkin
#  -------------------------------
#  This code may be copied, redistributed, transformed, or built
#  upon in any format for educational, non-commercial purposes.
#
#  Please give me appropriate credit should you choose to use this
#  resource. Thank you :)
#-----------------------------------------------------------------------
#
#_______________________________________________________________________
#  //\^.^/\\   //\^.^/\\   //\^.^/\\   //\^.^/\\   //\^.^/\\   //\^.^/\\
#_______________________________________________________________________
#  DESCRIPTION
#  Creates hourly entry for daily schedule.
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
from classes.constants.style import PlannerStrokes as Strokes
from classes.constants.style import PlannerFontStyle as Font

class Day:
  DEF_STRT_12: str = '09:00'
  DEF_STOP_12: str = '09:00'
  DEF_STRT_24: str = '09:00'
  DEF_STOP_24: str = '21:00'

  #_____________________________________________________________________
  def create_daily_schedule(strt_time_str: str
  , stop_time_str: str
  , wdth: int
  , hght: int
  , time_inc_min: int = 15
  , use_24: bool = True
  ) -> svgwrite.container.Group:
    """
    Creates schedule with times in increments as indicated. Assumes
    entry is in 24 hour format, though printed strings will reflect
    selection for use_24.

    Parameters:
      strt_time_str: start time of schedule
      stop_time_str: stop time of schedule
      wdth         : width of container
      hght         : height of container
      time_inc_min : incremental  time
      use_24       : use 24 hour time

    Returns:
      svgwrite Group containing all objects making up the time schedule
    """

    fmt: str = '%I:%M'
    if (use_24):
      fmt: str = '%H:%M'

    #___________________________________________________________________
    # Convert to datetime objects
    #___________________________________________________________________
    strt_datetime, stop_datetime =\
      Day.start_stop_err_check(strt_time_str, stop_time_str)

    crnt_datetime: dt.datetime = strt_datetime

    #___________________________________________________________________
    # Convert to strings
    #___________________________________________________________________
    stop_time_str =\
        stop_datetime.strftime(fmt)
    strt_time_str =\
        strt_datetime.strftime(fmt)
    #___________________________________________________________________

    print()
    crnt_datetime_str = strt_time_str

    #___________________________________________________________________
    time_block_count: int =\
    ( stop_datetime - strt_datetime).total_seconds()\
    / 60\
    / time_inc_min

    # Used in the calculation of box height
    # Assumes lines are 1 px
    stroke_wdth_total: int    = Strokes.STD_STROKE * time_block_count
    stroke_wdth_total_in: float = stroke_wdth_total * 1/72

    # TODO account for padding
    time_box_wdth: int = wdth
    time_box_hght: int = hght / time_block_count

    crnt_y: int = 0.5 * Font.NORMAL_SIZE

    group = svgwrite.container.Group()

    #___________________________________________________________________
    # Create boxes with time increments
    while crnt_datetime <= stop_datetime:
      crnt_datetime_str =\
        crnt_datetime.strftime(fmt)

      group.add(
        Day.create_time_entry(crnt_datetime_str, crnt_y, time_box_wdth))

      crnt_y = crnt_y + time_box_hght

      crnt_datetime = crnt_datetime + dt.timedelta(minutes=time_inc_min)

    return group

  #_____________________________________________________________________
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

    DEF_STRT: str = Day.DEF_STRT_24
    DEF_STOP: str = Day.DEF_STOP_24

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
      strt_datetime: dt.dt = dt.dt.strptime(Day.DEF_STRT, fmt_24)
      stop_datetime: dt.dt = dt.dt.strptime(Day.DEF_STOP, fmt_24)

      strt_datetime = dt.dt.combine(dt.dt.today(), strt_datetime.time())
      stop_datetime = dt.dt.combine(dt.dt.today(), stop_datetime.time())

    return strt_datetime, stop_datetime


  #_____________________________________________________________________
  def is_half_hour(t: dt.time) -> bool:
    """
    Verifies that time is in the half hour
    """
    return t.minute in {0, 30}

  #_____________________________________________________________________
  def create_time_entry(time_str: str
  , insert_y
  , wdth: int
  ) -> svgwrite.container.Group:
    """
    Creates text and lines for time entries

    Parameters:
      insert_y: Vertical insert point of entry
      wdth:     Width of container in inches
    """

    line_y: float = insert_y + 0.5 * Font.NORMAL_SIZE
    insert_y_str: str = Dims.to_in_str(insert_y)
    line_y_in_str: str = Dims.to_in_str(line_y)


    the_time: svgwrite.txt.Text = svgwrite.text.Text\
    ( time_str
    , insert=('0in', insert_y_str)
    , text_anchor='start'
    , alignment_baseline='middle'
    , fill=Colors.HEADING
    , font_size=Font.NORMAL_IN
    , font_family=Font.FONT_FAMILY_NORMAL
    )

    line: svgwrite.shapes.Line = svgwrite.shapes.Line\
    ( start=('0in', line_y_in_str)
    , end=(Dims.to_in_str(wdth), line_y_in_str)
    , stroke=Colors.DEBUG0_COLOR
    )

    group: svgwrite.container.Group = svgwrite.container.Group()

    if (':00' in time_str):
      group.add(the_time)

    group.add(line)

    return group
