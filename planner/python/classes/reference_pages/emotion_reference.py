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
from classes.elements.row_group import TextRowGroup
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
    """
    Parameters:
      emo_grp : Dictionary with 'header' and 'emotions' keys.
      wdth    : Total width of table.
    """

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
      , col_wdths=[-1, -1, -1, 125]
      , header_txt=emo_grp['header']
      , header_style=header_style
      , show_outline=False
      )

#_______________________________________________________________________
class EmotionReference(HalfPageLayout):
  """
  Reference page for ACE method.
  """

  PAGE_HEADER_TXT: str =\
    '87 Emotions and Experiences'

  SOURCE_TXT: str =\
    'Source: "Atlas of the Heart" by Brené Brown'

  #_____________________________________________________________________
  def __init__(self
  , total_hght: int = 0
  , total_wdth: int = 0
  , addl_args: dict = {}
  ):
    """
    Constructor for class. Assumes landscape orientation.
    """
    super().__init__\
      ( total_hght=total_hght
      , total_wdth=total_wdth
      , addl_args=addl_args
      , pad_under_page_header=False
      )

    return

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


    source_style: StdTextBoxStyles =\
      deepcopy(StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE)

    source_style.inner_pad_lft_ = False
    source_style.font_size_ = 8

    self.entries_: list =\
    [ TextRowGroup\
      (total_wdth=self.content_wdth_
      , text=self.SOURCE_TXT
      , style=source_style
      )
    ]

    self.entries_ = self.entries_ +\
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
