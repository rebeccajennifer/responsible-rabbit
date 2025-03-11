import argparse

from classes.page_layouts.half_letter_landscape import HalfLetterSize
from classes.planner_parser import PlannerCreationParser
from classes.entries.time_entries import Day

#_______________________________________________________________________
def new_line (new_line_count: int = 1) -> None:
  for i in range(new_line_count):
    print()

if __name__ == '__main__':
  new_line(2)
  HalfLetterSize.print_something()

  parser: argparse.ArgumentParser = argparse.ArgumentParser()
  PlannerCreationParser.init_parser(parser)

  args: argparse.Namespace = parser.parse_args()

  # Generate the SVG file
  HalfLetterSize.create_svg('boxy.svg')

  Day.create_daily_schedule('09:00', '21:00')