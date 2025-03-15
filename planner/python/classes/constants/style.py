#_______________________________________________________________________
#_______________________________________________________________________
#       _   __   _   _ _   _   _   _         _
#  |   |_| | _  | | | V | | | | / |_/ |_| | /
#  |__ | | |__| |_| |   | |_| | \ |   | | | \_
#   _  _         _ ___  _       _ ___   _                    / /
#  /  | | |\ |  \   |  | / | | /   |   \                    (^^)
#  \_ |_| | \| _/   |  | \ |_| \_  |  _/                    (____)o
#_______________________________________________________________________
#_______________________________________________________________________
#
#-----------------------------------------------------------------------
#  Copyright 2024, Rebecca Rashkin
#  -------------------------------
#  This code may be copied, redistributed, transformed, or built
#  upon in any format for educational, non-commercial purposes.
#
#  Please give me appropriate credit should you choose to use this
#  resource. Thank you :)
#-----------------------------------------------------------------------
#
#_______________________________________________________________________
#  //\^.^/\\   //\^.^/\\   //\^.^/\\   //\^.^/\\   //\^.^/\\   //\^.^/\\
#_______________________________________________________________________
#  DESCRIPTION
#  Standard styles used throughout program.
#_______________________________________________________________________

from classes.constants.dims import PlannerDims as Dims

#_______________________________________________________________________
class PlannerColors:
  """
  Contains colors used in the planner.
  """

  MEDIUM_GREY: str   = '#444444'
  CYAN: str          = '#008080'
  VIOLET: str        = '#800080'
  WHITE: str         = '#ffffff'

  FLUX_RED: str = '#d75f87'
  FLUX_GRN: str = '#87d75f'
  FLUX_YEL: str = '#d7875f'
  FLUX_BLU: str = '#5f5f87'
  FLUX_MAG: str = '#af5fd7'
  FLUX_CYA: str = '#5fafd7'
  FLUX_WHT: str = '#d7d7d7'
  FLUX_BLK: str = '#5f5f5f'
  FLUX_GRY: str = '#444444'

  PROMPT: str = FLUX_MAG
  HEADING: str = FLUX_RED

  BORDER_COLOR: str = MEDIUM_GREY
  DEBUG0_COLOR: str = CYAN
  DEBUG1_COLOR: str = VIOLET


#_______________________________________________________________________
class PlannerStrokes:
  """
  Contains stroke definitions.
  """

  STD_STROKE: int = 1
  DEBUG0_STROKE: int = 5


#_______________________________________________________________________
class PlannerFontStyle:
  """
  Contains standard font sizes.
  """

  HEADER_SIZE: str = 0.3
  PROMPT_SIZE: str = 0.2
  NORMAL_SIZE: str = 0.15

  HEADER_IN: str = Dims.to_in_str(HEADER_SIZE)
  PROMPT_IN: str = Dims.to_in_str(PROMPT_SIZE)
  NORMAL_IN: str = Dims.to_in_str(NORMAL_SIZE)

  FONT_FAMILY_NORMAL: str = 'Trebuchet MS'
  FONT_FAMILY_HEADER: str = 'Monaco'
