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
  NORMAL: str = FLUX_GRY
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

  HEAD_1_SIZE: int = 0.3
  HEAD_2_SIZE: int = 0.25
  PROMPT_SIZE: int = 0.2
  NORMAL_SIZE: int = 0.15
  LITTLE_SIZE: int = 0.1

  HEAD_1_PADDING: int = HEAD_1_SIZE / 2
  HEAD_2_PADDING: int = HEAD_2_SIZE / 2
  PROMPT_PADDING: int = PROMPT_SIZE / 2
  NORMAL_PADDING: int = NORMAL_SIZE / 2
  LITTLE_PADDING: int = LITTLE_SIZE / 2

  HEAD_1_IN: int = Dims.to_in_str(HEAD_1_SIZE)
  HEAD_2_IN: int = Dims.to_in_str(HEAD_2_SIZE)
  PROMPT_IN: int = Dims.to_in_str(PROMPT_SIZE)
  NORMAL_IN: int = Dims.to_in_str(NORMAL_SIZE)
  LITTLE_IN: int = Dims.to_in_str(LITTLE_SIZE)

  FONT_FAMILY_NORMAL: str = 'Ubuntu Mono'
  FONT_FAMILY_HEADER: str = 'Trebuchet MS'
  FONT_FAMILY_PROMPT: str = 'Trebuchet MS'

  STYLE_PROMPT: str = 'italics'
