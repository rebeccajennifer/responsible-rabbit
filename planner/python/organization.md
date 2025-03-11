
get_insert_point

- returns top left corner of content_group

class functions
  add_content()
  create_content()

CreateWeek(days, width)

  for days
    create box - width / days
CreateDateBox()

```py


#_______________________________________________________________________
import datetime as dt
import svgwrite

class Day:
  #_____________________________________________________________________
  def create_daily_schedule(strt_time: str
    , stop_time: str
    , width: str
    , height: str
    , time_inc_min: int = 30
    , use_24hr: bool = true
  ) -> svg.group:
    """
    Creates schedule table listing time
    """

    #
    # TODO error handling
    # Bad input format
    #
    # Start > end

    strt_time_str = dt.datetime.strptime(strt_time, '%H:%M')
    stop_time_str = dt.datetime.strptime(stop_time, '%H:%M')

    crnt_time_obj = strt_time_obj

    while crnt_time_obj != stop_time_obj:

      fmt_hr: str = '%H'
      if (not use_24_time):
        hr_fmt = '%I'

      time_fmt: str = f'{hr_fmt}:%M'
      time_str = crnt_time_obj.strftime(time_fmt)




```
