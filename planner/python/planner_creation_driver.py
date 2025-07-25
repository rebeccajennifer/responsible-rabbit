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
from os.path import join
from os.path import isfile
from os import listdir
from os import remove


from classes.constants.addl_arg_keys import AddlArgKeys as Key
from classes.constants.page_order import DblSidePages
from classes.constants.page_order import OneSidePages
from classes.constants.page_order import OptionlPages
from classes.constants.page_order import PageOrder

from classes.page_entries.month_entry import MonthEntry
from classes.page_entries.night_entry import NightEntry
from classes.page_entries.week_habit_entry import HabitTracker
from classes.page_entries.title_page import TitlePage
from classes.page_entries.week_checklist_entry import WeekCheckList
from classes.page_entries.test_entry import TestEntry

from classes.page_layouts.page_layout import PageLayout
from classes.page_layouts.half_page_divider import HalfPageDivider


from utils.planner_parser import PlannerCreationParser


from utils.utils import PlannerUtils as Utils

#_______________________________________________________________________
def new_line (new_line_count: int = 1) -> None:
  for i in range(new_line_count):
    print()


#_______________________________________________________________________
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
      PageLayout\
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


#_______________________________________________________________________
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
    HalfPageDivider\
    ( is_portrait=is_portrait
    , divider_pos=i+1
    , divider_str=divider_labels[i]
    , out_dir=out_dir
    , entry_type=TitlePage
    , entry_args={Key.HEADER_TXT: divider_labels[i]}
    ).save_pdf()

#_______________________________________________________________________
def generate_habit_tracker\
( is_portrait: bool
, out_dir: str
):
  """
  Create weekly habit bookmark.

  Parameters:
    is_portrait : True indicates the half page is in portrait
                  orientation
    out_dir     : Output directory

  Side Effects:
    Creates svgs and pdfs for habit tracker bookmark.

  Returns:
    None
  """

  week_cklst_fname : str = 'week-cklst'
  habt_track_fname : str = 'habt-track'

  week_cklst =\
    PageLayout\
      ( is_portrait=is_portrait
      , is_dbl_sided=True
      , file_name_no_ext=week_cklst_fname
      , out_dir=out_dir
      , entry_0_type=TitlePage
      , entry_0_args={}
      , entry_1_type=WeekCheckList
      , entry_1_args={}
      , rgt_bndr_mrgn=True
      )
  week_cklst.save_pdf()

  habt_track =\
    HalfPageDivider\
    ( is_portrait=is_portrait
    , out_dir=out_dir
    , file_name_no_ext=habt_track_fname
    , divider_pos=0
    , divider_str='Today'
    , entry_type=HabitTracker
    , entry_args={}
    )
  habt_track.save_pdf()

  pdf_out_dir: str = join(out_dir, 'pdf')

  pdf_paths: list =\
    [ join(pdf_out_dir, habt_track.file_name_no_ext_ + '.pdf')
    , join(pdf_out_dir, week_cklst.file_name_no_ext_ + '.pdf')
    ]

  Utils.combine_pdfs(pdf_paths, join(pdf_out_dir, 'dvdr-0-today.pdf'))

  return


#_______________________________________________________________________
def group_pdfs(page_order: PageOrder, is_dbl_sided: bool, out_dir: str) -> None:
  """
  Combines pdfs in groups.

  Parameters:
    None

  Side Effects:
    Creates several combined pdfs.

  Returns:
    None
  """

  intr_pdf_group: list = page_order.intr_file_names
  week_pdf_group: list = page_order.week_file_names
  xtra_pdf_group: list = page_order.xtra_file_names

  intr_combo_pdf: list = '__0__intr.pdf '
  week_combo_pdf: list = '__1__week.pdf '
  xtra_combo_pdf: list = '__2__xtra.pdf '
  habt_combo_pdf: list = '__3__habt.pdf '

  pdf_paths: list =\
    [join(pdf_out_dir, n + '.pdf') for n in intr_pdf_group]
  Utils.combine_pdfs(pdf_paths, join(out_dir, intr_combo_pdf))

  pdf_paths: list =\
    [join(pdf_out_dir, n + '.pdf') for n in week_pdf_group]
  Utils.combine_pdfs(pdf_paths, join(out_dir, week_combo_pdf))

  pdf_paths: list =\
    [join(pdf_out_dir, n + '.pdf') for n in xtra_pdf_group]
  Utils.combine_pdfs(pdf_paths, join(out_dir, xtra_combo_pdf))

  #_____________________________________________________________________
  # Clean up pdfs
  #_____________________________________________________________________
  # Files to keep (relative names only, not full paths)
  keep_files = {intr_combo_pdf, week_combo_pdf, xtra_combo_pdf}

  # Loop through all files in the directory
  for filename in listdir(out_dir):
      file_path = join(out_dir, filename)

      # Remove if it's a file and not in the keep list
      if isfile(file_path) and filename not in keep_files:
          remove(file_path)
  #_____________________________________________________________________

  return

#_______________________________________________________________________
if __name__ == '__main__':
  new_line(2)

  parser: argparse.ArgumentParser = argparse.ArgumentParser()
  PlannerCreationParser.init_parser(parser)

  args: argparse.Namespace = parser.parse_args()

  is_portrait:  bool  = False
  is_dbl_sided: bool  = args.dbl_sided

  # If generating a PDF preview, set to double sided
  if (args.preview):
    is_dbl_sided = True

  page_order: list =\
    PageOrder\
    ( is_dbl_sided=is_dbl_sided
    , is_preview=args.preview
    )

  pdf_out_dir: str =\
    join(args.out_dir, PageLayout.PDF_SUB_DIR)

  svg_out_dir: str =\
    join(args.out_dir, PageLayout.SVG_SUB_DIR)

  generate_pages(page_order, is_portrait, is_dbl_sided, args.out_dir)

  div_dir: str = join(args.out_dir ,'..', 'dividers')
  generate_habit_tracker(is_portrait, div_dir)
  generate_dividers(is_portrait, div_dir)

  test_layout=\
    PageLayout\
    ( is_portrait=False
    , is_dbl_sided=is_dbl_sided
    , file_name_no_ext='test'
    #, out_dir='.'
    , entry_0_type=NightEntry
    , entry_0_args={Key.HEADER_TXT: 'Nighty Night'}
    , entry_1_type=NightEntry
    , entry_1_args={}
    )
  #test_layout.save_pdf()


  group_pdfs(page_order=page_order, is_dbl_sided=is_dbl_sided, out_dir=pdf_out_dir)

  new_line(10)
  print("all done")
  new_line(10)
