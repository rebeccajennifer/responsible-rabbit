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


from classes.constants.addl_arg_keys import AddlArgKeys as Key

from classes.page_entries.week_habit_entry import HabitTracker
from classes.page_entries.title_page import TitlePage
from classes.page_entries.week_checklist_entry import WeekCheckList
from classes.page_entries.test_entry import TestEntry
from classes.reference_pages.emotion_reference import EmotionReference

from classes.page_layouts.page_layout import PageLayout
from classes.page_layouts.half_page_divider import HalfPageDivider

from classes.planner_assembler import PlannerAssembler

from utils.planner_parser import PlannerCreationParser

from utils.utils import PlannerUtils as Utils

#_______________________________________________________________________
def new_line (new_line_count: int = 1) -> None:
  for i in range(new_line_count):
    print()


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

  test_layout=\
    PageLayout\
    ( is_portrait=False
    , is_dbl_sided=is_dbl_sided
    , file_name_no_ext='test'
    , out_dir='.'
    , entry_0_type=EmotionReference
    )

  test_layout.save_pdf()

  """
  div_dir: str = join(args.out_dir ,'..', 'dividers')
  generate_habit_tracker(is_portrait, div_dir)
  generate_dividers(is_portrait, div_dir)
  """

  PlannerAssembler\
  ( is_portrait=is_portrait
  , is_dbl_sided=is_dbl_sided
  , is_preview=args.preview
  , out_dir=args.out_dir
  )
  """
  """

  new_line(10)
  print("all done")
  new_line(10)
