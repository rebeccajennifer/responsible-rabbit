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
#   Driver for planner creation.
#_______________________________________________________________________

import argparse
from os import path
from os import listdir
from os import remove


from classes.constants.addl_arg_keys import AddlArgKeys as Key
from classes.constants.page_order import DblSidePages
from classes.constants.page_order import OneSidePages

from classes.page_entries.month_entry import MonthEntry
from classes.page_entries.week_habit_entry import HabitTracker
from classes.page_entries.title_page import TitlePage
from classes.page_entries.week_checklist_entry import WeekCheckList
from classes.page_entries.test_entry import TestEntry

from classes.page_layouts.half_letter_divider import DividerPage

from classes.reference_pages.ace_reference import AceReference

from utils.planner_parser import PlannerCreationParser

from classes.page_layouts.half_letter_two_page_layout import TwoPageHalfLetterSize

from utils.utils import PlannerUtils as Utils

#_______________________________________________________________________
def new_line (new_line_count: int = 1) -> None:
  for i in range(new_line_count):
    print()

def generate_pages\
( page_order: list
, is_portrait: bool
, is_dbl_sided: bool
, out_dir: str
) -> None:
  #_____________________________________________________________________
  # Iterate through list containing layout arguments and create
  # for each layout
  #_____________________________________________________________________
  for i in range (len(page_order)):
    layout =\
      TwoPageHalfLetterSize\
      ( is_portrait=is_portrait
      , is_dbl_sided=is_dbl_sided
      , file_name_no_ext=page_order[i][0]
      , out_dir=out_dir
      , entry_0_type=page_order[i][1][Key.ENTRY_TYPE]
      , entry_0_args=page_order[i][1][Key.ENTRY_ARGS]
      , entry_1_type=page_order[i][2][Key.ENTRY_TYPE]
      , entry_1_args=page_order[i][2][Key.ENTRY_ARGS]
      )
    layout.save_pdf()

def generate_dividers\
( is_portrait
, out_dir: str
):
  #_____________________________________________________________________
  # Create dividers
  #_____________________________________________________________________
  divider_labels: list =\
  [ 'Vision'
  , 'Goals'
  , 'Calendar'
  ]

  for i in range(1, 4):
    divider_labels.append(f'Month {i}')

  for i in range(len(divider_labels)):
    DividerPage\
    ( is_portrait=is_portrait
    , divider_pos=i+1
    , divider_str=divider_labels[i]
    , out_dir=out_dir
    , entry_type=TitlePage
    , entry_args={Key.HEADER_TXT: divider_labels[i]}
    ).save()

def generate_habit_tracker\
( is_portrait: bool
, out_dir: str
):
  #_____________________________________________________________________
  # Create weekly habit bookmark
  #_____________________________________________________________________
  weekly_checklist =\
    TwoPageHalfLetterSize\
      ( is_portrait=is_portrait
      , is_dbl_sided=True
      , file_name_no_ext='week-chcklst-back'
      , out_dir=out_dir
      , entry_0_type=TitlePage
      , entry_0_args={}
      , entry_1_type=WeekCheckList
      , entry_1_args={}
      , rgt_bndr_mrgn=True
      )
  weekly_checklist.save()

  habit_tracker =\
    DividerPage\
    ( is_portrait=is_portrait
    , out_dir=args.out_dir
    , divider_pos=0
    , divider_str='Today'
    , file_path=path.join(args.out_dir, 'week-chcklst-frnt.svg')
    , entry_type=HabitTracker
    , entry_args={}
    )
  habit_tracker.save()

#_______________________________________________________________________
def group_pdfs(is_dbl_sided: bool, out_dir: str) -> None:
  """
  Combines pdfs in groups.

  Parameters:
    None

  Side Effects:
    Creates several combined pdfs.

  Returns:
    None
  """

  intr_pdf_group: list = OneSidePages.INTR_FILE_NAMES
  week_pdf_group: list = OneSidePages.WEEK_FILE_NAMES

  if(is_dbl_sided):
    intr_pdf_group: list = DblSidePages.INTR_FILE_NAMES
    week_pdf_group: list = DblSidePages.WEEK_FILE_NAMES

  intr_combo_pdf: list = '__0__intr.pdf '
  week_combo_pdf: list = '__1__week.pdf '

  pdf_paths: list =\
    [path.join(pdf_out_dir, n + '.pdf') for n in intr_pdf_group]
  Utils.combine_pdfs(pdf_paths, path.join(out_dir, intr_combo_pdf))

  pdf_paths: list =\
    [path.join(pdf_out_dir, n + '.pdf') for n in week_pdf_group]
  Utils.combine_pdfs(pdf_paths, path.join(out_dir, week_combo_pdf))


  #_____________________________________________________________________
  # Clean up pdfs
  #_____________________________________________________________________
  # Files to keep (relative names only, not full paths)
  keep_files = {intr_combo_pdf, week_combo_pdf}

  # Loop through all files in the directory
  for filename in listdir(out_dir):
      file_path = path.join(out_dir, filename)

      # Remove if it's a file and not in the keep list
      if path.isfile(file_path) and filename not in keep_files:
          remove(file_path)
  #_____________________________________________________________________

  return

#_______________________________________________________________________
if __name__ == '__main__':
  new_line(2)

  parser: argparse.ArgumentParser = argparse.ArgumentParser()
  PlannerCreationParser.init_parser(parser)

  args: argparse.Namespace = parser.parse_args()

  is_portrait: bool   = False
  is_dbl_sided: bool  = args.dbl_sided

  page_order: list = []

  pdf_out_dir: str =\
    path.join(args.out_dir, TwoPageHalfLetterSize.PDF_SUB_DIR)

  svg_out_dir: str =\
    path.join(args.out_dir, TwoPageHalfLetterSize.SVG_SUB_DIR)


  #_____________________________________________________________________
  # Determine page ordering
  #_____________________________________________________________________
  if (is_dbl_sided):
    page_order = DblSidePages.PAGE_ORDER
  else:
    page_order = OneSidePages.PAGE_ORDER
  #_____________________________________________________________________

  generate_pages(page_order,is_portrait, is_dbl_sided, args.out_dir)
  #generate_dividers(is_portrait, args.out_dir)
  #generate_habit_tracker(is_portrait, args.out_dir)

  test_layout=\
    TwoPageHalfLetterSize\
    ( is_portrait=False
    , is_dbl_sided=is_dbl_sided
    , file_name_no_ext='test'
    , out_dir=args.out_dir
    , entry_0_type=MonthEntry
    , entry_0_args={}
    , entry_1_type=TestEntry
    , entry_1_args={}
    )
  test_layout.save_pdf()


  group_pdfs(is_dbl_sided=is_dbl_sided, out_dir=pdf_out_dir)

  new_line(10)
  print("all done")
  new_line(10)
