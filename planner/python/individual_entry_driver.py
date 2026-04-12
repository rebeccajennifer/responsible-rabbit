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
#   Copyright 2026, Rebecca Rashkin
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
#   Driver for planner creation.
#_______________________________________________________________________

import argparse
import yaml

from os.path import join


from classes.constants.entries import Entries

from classes.constants.addl_arg_keys import AddlArgKeys as Key

from classes.page_entries.daily_practice_tracker import SevenDayPracticeTracker
from classes.page_entries.day_entry_1 import SimpleDayEntry

from classes.page_entries.project_entry import ProjectEntry

from classes.page_layouts.page_layout import PageLayout
from classes.page_layouts.half_page_divider import HalfPageDivider

from classes.planner_assembler import PlannerAssembler

from utils.planner_parser import PlannerCreationParser

from utils.flux_bunny_utils.file_utils import FileUtils

entry_type_keys: dict =\
  {'seven-day-habit-tracker': Entries.TRACK_7}

#_______________________________________________________________________
def new_line (new_line_count: int = 1) -> None:
  for i in range(new_line_count):
    print()


#_______________________________________________________________________
if __name__ == '__main__':
  new_line(2)

  parser: argparse.ArgumentParser = argparse.ArgumentParser()
  PlannerCreationParser.init_parser(parser)

  args: argparse.Namespace = parser.parse_args()

  # These page layouts are intended to be constructed in landscape
  # orientation
  is_portrait:  bool  = False
  is_dbl_sided: bool  = args.dbl_sided

  # If generating a PDF preview, set to double sided
  if (args.preview):
    is_dbl_sided = True

  project_layout =\
    PageLayout\
    ( is_portrait=is_portrait
    , is_dbl_sided=is_dbl_sided
    , file_name_no_ext='proj-entry'
    , out_dir=args.out_dir
    , entry_0_type=ProjectEntry
    , entry_1_type=ProjectEntry
    )
  project_layout.save_pdf()

  new_line(10)
  print("all done")
  new_line(10)
