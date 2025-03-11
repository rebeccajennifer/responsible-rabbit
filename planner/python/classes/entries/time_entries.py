import datetime as dt

from classes.constants.error_strings import ErrorStrings as Err

class Day:
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
    # Convert to datetime objects for error handling
    #___________________________________________________________________
    strt_datetime: dt.datetime =\
       dt.datetime.strptime(strt_time_str, fmt_24hr)
    stop_datetime: dt.datetime =\
       dt.datetime.strptime(stop_time_str, fmt_24hr)

    strt_datetime = dt.datetime.combine(dt.datetime.today(), strt_datetime.time())
    stop_datetime = dt.datetime.combine(dt.datetime.today(), stop_datetime.time())

    if (stop_datetime < strt_datetime):
      print(Err.BAD_INPUT)
      return

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

    while crnt_datetime_str != stop_time_str:
      crnt_datetime_str =\
        crnt_datetime.strftime(fmt_24hr)

      print(crnt_datetime_str)

      crnt_datetime = crnt_datetime + dt.timedelta(minutes=time_inc_min)
