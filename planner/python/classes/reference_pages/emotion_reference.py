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
#   Reference page for emotions.
#_______________________________________________________________________

from copy import deepcopy

from classes.style.style import PlannerColors as Colors
from classes.constants.strings import PlannerStrings as Strings
from classes.elements.base_element import HorizontalStack
from classes.elements.row_group import DualLineRowGroup

from classes.page_layouts.half_page_layout import HalfPageLayout

from classes.reference_pages.emotions import EmotionStrings

from classes.elements.row_group import TextRowGroup
from classes.style.std_styles import StdTextBoxStyles


#_______________________________________________________________________
class EmotionReference(HalfPageLayout):
  """
  Reference page for ACE method.
  """

  PAGE_HEADER_TXT: str =\
    'List of 87 Emotions and Experiences from Brené Brown'

  #_____________________________________________________________________
  def create_content(self) -> None:
    """
    Parameters:
      None

    Side Effects:
      Populates self.entries_ class variable.

    Returns:
      None
    """
    super().create_content()

    header_style: StdTextBoxStyles =\
      deepcopy(StdTextBoxStyles.LTE_BACK_HEADER_FONT)

    emotion_style: StdTextBoxStyles =\
      deepcopy(StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE)
    emotion_style.show_outline_ = True
    emotion_style.outline_color_ = Colors.FLUX_RED

    col_wdth: int = self.content_wdth_ // 4

    uncertain: list =\
      [ TextRowGroup\
        (total_wdth=col_wdth
        , text=EmotionStrings.UNCERTAIN[0:3]
        , style=emotion_style
        )
      , TextRowGroup\
        (total_wdth=col_wdth
        , text=EmotionStrings.UNCERTAIN[3:6]
        , style=emotion_style
        )
      , TextRowGroup\
        (total_wdth=col_wdth
        , text=EmotionStrings.UNCERTAIN[6:-1]
        , style=emotion_style
        )
      ]

    self.entries_ =\
    [ TextRowGroup
      (total_wdth=self.content_wdth_
      , text=EmotionStrings.HEADER_UNCERTAIN
      , style=header_style
      )
    , HorizontalStack\
      ( obj_list=uncertain
      , add_inner_pad=False
      )
    , TextRowGroup\
      ( total_wdth=self.content_wdth_
      , text=EmotionStrings.HEADER_COMPARE
      , style=header_style
      )
    , TextRowGroup\
      (  total_wdth=self.content_wdth_
      , text=EmotionStrings.HEADER_UNPLANNED
      , style=header_style
      )
    , TextRowGroup\
      (   total_wdth=self.content_wdth_
      , text=EmotionStrings.HEADER_BEYOND_US
      , style=header_style
      )
    , TextRowGroup\
      (    total_wdth=self.content_wdth_
      , text=EmotionStrings.HEADER_NOT_WHAT_THEY_SEEM
      , style=header_style
      )
    , TextRowGroup\
      ( total_wdth=self.content_wdth_
      , text=EmotionStrings.HEADER_HURT
      , style=header_style
      )
    , TextRowGroup\
      ( total_wdth=self.content_wdth_
      , text=EmotionStrings.HEADER_OTHERS
      , style=header_style
      )
    , TextRowGroup\
      ( total_wdth=self.content_wdth_
      , text=EmotionStrings.HEADER_FALL_SHORT
      , style=header_style
      )
    , TextRowGroup\
      ( total_wdth=self.content_wdth_
      , text=EmotionStrings.HEADER_CONNECTION
      , style=header_style
      )
    , TextRowGroup\
      ( total_wdth=self.content_wdth_
      , text=EmotionStrings.HEADER_OPEN
      , style=header_style
      )
    , TextRowGroup\
      (total_wdth=self.content_wdth_
      , text=EmotionStrings.HEADER_GOOD
      , style=header_style
      )
    , TextRowGroup\
      (total_wdth=self.content_wdth_
      , text=EmotionStrings.HEADER_WRONGED
      , style=header_style
      )
    , TextRowGroup\
      ( total_wdth=self.content_wdth_
      , text=EmotionStrings.HEADER_SELF_ASSESS
      , style=header_style
      )
    ]

    return
