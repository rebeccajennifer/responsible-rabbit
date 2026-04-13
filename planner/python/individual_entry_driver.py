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

from classes.constants.entries import Entries
from classes.constants.addl_arg_keys import AddlArgKeys as Keys
from classes.page_layouts.page_layout import PageLayout
from classes.planner_assembler import PageGroup
from utils.planner_parser import PlannerCreationParser


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
  is_portrait   : bool  = False
  is_dbl_sided  : bool  = args.dbl_sided
  out_dir       : str   = args.out_dir

  # If generating a PDF preview, set to double sided
  if (args.preview):
    is_dbl_sided = True

  if (args.entry_cfg):
    with open(args.entry_cfg, 'r') as f:
      entry_cfg_data: dict = yaml.safe_load(f)
      print(entry_cfg_data)

  is_dbl_sided = entry_cfg_data['double-sided']

  page_groups: list = []

  #_____________________________________________________________________
  for pdf_group_name in entry_cfg_data['pdfs']:

    pdf_group: dict = entry_cfg_data['pdfs'][pdf_group_name]

    page_list: list = []
    # Get class type for left and right entries
    # TODO: Add entry arguments to configuration file and use here
    for page_name in pdf_group:
      layout = pdf_group[page_name]
      left_entry_type_str = layout['left_entry']['entry_type']
      left_entry_type     = Entries.ENTRY_NAME_MAP[left_entry_type_str]
      rght_entry_type_str = layout['rght_entry']['entry_type']
      rght_entry_type     = Entries.ENTRY_NAME_MAP[rght_entry_type_str]

      page: dict =\
        { 'file_name' : page_name
        , 'left_entry' : left_entry_type
        , 'rght_entry' : rght_entry_type
        }
      page_list.append(page)

    group: PageGroup = PageGroup\
      ( group_name=pdf_group_name
      , layouts=page_list
      )

    page_groups.append(group)

  #_____________________________________________________________________
  for group in page_groups:

    for pg in group.pages:

      #_________________________________________________________________
      # pg takes the form
      #_________________________________________________________________
      # { 'file_name': 'group_0_pg_0'
      # , 'left_entry': {'entry_type': EntryType, 'entry_args: {}'}
      # , 'rght_entry': {'entry_type': EntryType, 'entry_args: {}'}
      # }
      #_________________________________________________________________
      layout =\
        PageLayout\
        ( is_portrait=is_portrait
        , is_dbl_sided=is_dbl_sided
        , file_name_no_ext=pg[Keys.NAME]
        , out_dir=out_dir
        , entry_0_type=pg[Keys.LEFT][Keys.ENTRY_TYPE]
        , entry_0_args=pg[Keys.LEFT][Keys.ENTRY_ARGS]
        , entry_1_type=pg[Keys.RGHT][Keys.ENTRY_TYPE]
        , entry_1_args=pg[Keys.RGHT][Keys.ENTRY_ARGS]
        )
      layout.save_pdf()

  new_line(10)
  print("all done")
  new_line(10)
