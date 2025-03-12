import datetime as dt

from typing import Tuple

from classes.constants.error_strings import ErrorStrings as Err

class Day:
  DEF_STRT: str = '09:00'
  DEF_STOP: str = '21:00'
  #_____________________________________________________________________
  def create_daily_schedule(strt_time_str: str
    , stop_time_str: str
    #, width: str
    #, height: str
    , time_inc_min: int = 30
    , use_24hr: bool = True
  ) -> None:#svg.group:
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

    # Create boxes with time increments
    while crnt_datetime_str != stop_time_str:
      crnt_datetime_str =\
        crnt_datetime.strftime(fmt_24hr)

      print(crnt_datetime_str)

      crnt_datetime = crnt_datetime + dt.timedelta(minutes=time_inc_min)

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
