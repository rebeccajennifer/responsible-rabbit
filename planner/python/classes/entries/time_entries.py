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
  DEF_STRT: str = '09:00'
  DEF_STOP: str = '21:00'
  #_____________________________________________________________________
  def create_daily_schedule(strt_time_str: str
    , stop_time_str: str
    , wdth: int
    , hght: str
    , time_inc_min: int = 30
    , use_24hr: bool = True
    , use_px:bool = False
  ) -> svgwrite.container.Group:
    """
    Creates schedule table listing time
    """

    fmt_24hr: str = '%H:%M'

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
        stop_datetime.strftime(fmt_24hr)
    strt_time_str =\
        strt_datetime.strftime(fmt_24hr)
    #___________________________________________________________________

    print()
    crnt_datetime_str = strt_time_str

    #___________________________________________________________________
    time_block_count: int =\
    ( stop_datetime - strt_datetime).total_seconds()\
    / 60\
    / time_inc_min

    # Used in the calculation of box height
    stoke_wdth_total: int = Strokes.STD_STROKE * time_block_count

    # TODO account for padding
    time_box_wdth: int = wdth
    time_box_hght: int = hght / time_block_count

    if (use_px):
      time_box_wdth_str: str = Dims.to_in_px(time_box_wdth)
      time_box_hght_str: str = Dims.to_in_px(time_box_hght)
    else:
      time_box_wdth_str: str = Dims.to_in_str(wdth)
      time_box_hght_str: str = Dims.to_in_str(time_box_hght)

    crnt_y: int = 0.5 * Font.NORMAL_SIZE

    group = svgwrite.container.Group()

    #___________________________________________________________________
    # Create boxes with time increments
    while crnt_datetime_str != stop_time_str:
      crnt_datetime_str =\
        crnt_datetime.strftime(fmt_24hr)

      group.add(Day.create_time_box(crnt_datetime_str, crnt_y))
      crnt_y = crnt_y + time_box_hght

      crnt_datetime = crnt_datetime + dt.timedelta(minutes=time_inc_min)

    return group

  #_____________________________________________________________________
  def start_stop_err_check(strt_time_str: str
    , stop_time_str: str
    , use_24=True
  ) -> Tuple:
    """
    Checks if start time is greater than stop time. Converts times to
    datetime objects with dates.

    Parameters:
    strt_time_str -
    stop_time_str -

    Returns:
    (datetime.datetime obj start, datetime.datetime obj stop)

    """

    dt.dt = dt.datetime

    fmt_24hr: str = '%H:%M'

    #___________________________________________________________________
    # Convert to datetime objects for error handling
    #___________________________________________________________________
    strt_datetime: dt.dt = dt.dt.strptime(strt_time_str, fmt_24hr)
    stop_datetime: dt.dt = dt.dt.strptime(stop_time_str, fmt_24hr)

    strt_datetime = dt.dt.combine(dt.dt.today(), strt_datetime.time())
    stop_datetime = dt.dt.combine(dt.dt.today(), stop_datetime.time())

    if (stop_datetime < strt_datetime):
      strt_datetime: dt.dt = dt.dt.strptime(Day.DEF_STRT, fmt_24hr)
      stop_datetime: dt.dt = dt.dt.strptime(Day.DEF_STOP, fmt_24hr)

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
  def create_time_box(time_str: str
    , insert_y) -> svgwrite.container.Group:

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
    , end=('1.5in', line_y_in_str)
    , stroke=Colors.DEBUG0_COLOR
    )

    group: svgwrite.container.Group = svgwrite.container.Group()

    if (':00' in time_str):
      group.add(the_time)

    group.add(line)

    return group