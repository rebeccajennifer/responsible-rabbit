import argparse

from classes.page_layout.half_letter_landscape import HalfLetterSize
from classes.planner_parser import PlannerCreationParser

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