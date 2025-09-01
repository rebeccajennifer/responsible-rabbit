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

from classes.elements.table import TextColumnTable
from classes.style.std_styles import StdTextBoxStyles
from classes.style.style import PlannerColors as Colors

from classes.page_layouts.half_page_layout import HalfPageLayout

from classes.reference_pages.emotions import EmotionStrings as EmoStr


#_______________________________________________________________________
class EmotionTable(TextColumnTable):
  """
  Emotion group table with default styles for header and emotions.
  """

  #_____________________________________________________________________
  def __init__(self, emo_grp: dict, wdth: int) -> None:

    header_style: StdTextBoxStyles =\
      deepcopy(StdTextBoxStyles.LTE_BACK_HEADER_FONT)
    header_style.font_size_ = 10

    emotion_style: StdTextBoxStyles =\
      deepcopy(StdTextBoxStyles.WHT_BACK_NORMAL_FONT_W_OUTLNE)
    emotion_style.show_outline_ = False
    emotion_style.outline_color_ = Colors.FLUX_RED
    emotion_style.font_size_ = 10

    super().__init__(total_wdth=wdth
      , txt_lst=emo_grp['emotions']
      , text_style=emotion_style
      , col_count=4
      , col_wdths=[-1, -1, -1, 130]
      , header_txt=emo_grp['header']
      , header_style=header_style
      , show_outline=True
      )

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


    self.entries_: list =\
    [ EmotionTable(EmoStr.UNCERTAIN_DICT          , self.content_wdth_)
    , EmotionTable(EmoStr.COMPARE_DICT            , self.content_wdth_)
    , EmotionTable(EmoStr.UNPLANNED_DICT          , self.content_wdth_)
    , EmotionTable(EmoStr.BEYOND_US_DICT          , self.content_wdth_)
    , EmotionTable(EmoStr.NOT_WHAT_THEY_SEEM_DICT , self.content_wdth_)
    , EmotionTable(EmoStr.HURT_DICT               , self.content_wdth_)
    , EmotionTable(EmoStr.OTHERS_DICT             , self.content_wdth_)
    , EmotionTable(EmoStr.FALL_SHORT_DICT         , self.content_wdth_)
    , EmotionTable(EmoStr.CONNECTION_DICT         , self.content_wdth_)
    , EmotionTable(EmoStr.OPEN_DICT               , self.content_wdth_)
    , EmotionTable(EmoStr.GOOD_DICT               , self.content_wdth_)
    , EmotionTable(EmoStr.WRONGED_DICT            , self.content_wdth_)
    , EmotionTable(EmoStr.SELF_ASSESS_DICT        , self.content_wdth_)
    ]

    return
