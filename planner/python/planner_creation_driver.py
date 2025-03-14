import argparse

from classes.page_layouts.half_letter_layout import HalfLetterSize
from classes.planner_parser import PlannerCreationParser
from classes.entries.time_entries import Day

#_______________________________________________________________________
def new_line (new_line_count: int = 1) -> None:
  for i in range(new_line_count):
    print()

if __name__ == '__main__':
  new_line(2)

  parser: argparse.ArgumentParser = argparse.ArgumentParser()
  PlannerCreationParser.init_parser(parser)

  args: argparse.Namespace = parser.parse_args()

  layout_landscpe_no_dbl_sided: HalfLetterSize =\
    HalfLetterSize\
    ( is_portrait=False
    , is_dbl_sided=False
    )

  layout_landscpe_dbl_sided: HalfLetterSize =\
    HalfLetterSize\
    ( is_portrait=False
    , is_dbl_sided=True
    )

  layout_portrait_no_dbl_sided: HalfLetterSize =\
    HalfLetterSize\
    ( is_portrait=True
    , is_dbl_sided=False
    )

  layout_portrait_dbl_sided: HalfLetterSize =\
    HalfLetterSize\
    ( is_portrait=True
    , is_dbl_sided=True
    )


  # Generate the SVG file
  layout_landscpe_no_dbl_sided.create_layout('landscpe.svg')
  layout_landscpe_dbl_sided.create_layout('landscpe_dbl.svg')
  layout_portrait_no_dbl_sided.create_layout('portrait.svg')
  layout_portrait_dbl_sided.create_layout('portrait_dbl.svg')

  txt = Day.create_daily_schedule\
  ( strt_time_str='19:00'
  , stop_time_str='11:00'
  , wdth=2
  , hght=7.9
  )

  layout_test: HalfLetterSize =\
    HalfLetterSize\
    ( is_portrait=False
    , is_dbl_sided=False
    )

  layout_test.create_layout('test-layout.svg', txt)

