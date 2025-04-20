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
#   Standard styles used throughout program.
#_______________________________________________________________________

#_______________________________________________________________________
class PlannerColors:
  """
  Contains colors used in the planner.
  """

  MEDIUM_GREY: str   = '#888888'
  LIGHT_GREY: str    = '#d7d7d7'
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
  NORMAL_TXT: str = FLUX_GRY
  HEADING: str = FLUX_RED

  DEF_PAGE_HEADER_COLOR : str = 'none'

  DEF_TBLE_HEADER_FILL  : str = MEDIUM_GREY
  DEF_TBLE_HEADER_TEXT  : str = WHITE

  BORDER_COLOR          : str = MEDIUM_GREY
  DEF_ROW_COLOR         : str = LIGHT_GREY

  DEBUG0_COLOR          : str = CYAN
  DEBUG1_COLOR          : str = VIOLET


#_______________________________________________________________________
class PlannerFontStyle:
  """
  Contains standard font sizes.
  """

  GOAL_HEADER_SIZE      : int = 32
  DAY_PAGE_HEADER_SIZE  : int = 12
  WEEK_PAGE_HEADER_SIZE : int = 12

  DEF_PAGE_HEADER_SIZE: int = 12

  HEAD_1_SIZE: int = 12
  HEAD_2_SIZE: int = 24
  PROMPT_SIZE: int = 14
  NORMAL_SIZE: int = 10
  LITTLE_SIZE: int = 8

  TEXT_PADDING: int = 5

  FONT_FAMILY_NORMAL: str = 'Ubuntu Mono'
  FONT_FAMILY_HEADER: str = 'Trebuchet MS'
  FONT_FAMILY_PROMPT: str = 'Trebuchet MS'

  STYLE_PROMPT: str = 'italics'

  DEF_LINE_SPC: int =\
    1

  # Empirically determined constants
  WDTH_MULTPLIER: dict =\
  { FONT_FAMILY_NORMAL: 1.75
  , FONT_FAMILY_HEADER: 2.3
  }