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
#   Standard styles for text boxes and line row groups.
#_______________________________________________________________________

from classes.style.style import PlannerColors as Colors
from classes.style.style import PlannerFontStyle as Font
from classes.constants.dims import PlannerDims as Dims

from classes.style.table_style import LineRowGroupStyle
from classes.style.table_style import TextBoxStyle


#_______________________________________________________________________
class StdTextBoxStyles():

  DRK_BACK_NORMAL_FONT: TextBoxStyle =\
    TextBoxStyle\
    ( backgnd_color=Colors.FLUX_BLK
    , inner_pad_top=True
    , inner_pad_bot=True
    , inner_pad_lft=True
    , inner_pad_rgt=True
    , font_family=Font.FONT_FAMILY_NORMAL
    , font_color=Colors.WHITE
    )

  DRK_BACK_HEADER_FONT: TextBoxStyle =\
    TextBoxStyle\
    ( backgnd_color=Colors.FLUX_BLK
    , inner_pad_top=True
    , inner_pad_bot=True
    , inner_pad_lft=True
    , inner_pad_rgt=True
    , font_family=Font.FONT_FAMILY_HEADER
    , font_color=Colors.WHITE
    )

  MED_BACK_NORMAL_FONT: TextBoxStyle =\
    TextBoxStyle\
    ( backgnd_color=Colors.MEDIUM_GREY
    , inner_pad_top=True
    , inner_pad_bot=True
    , inner_pad_lft=True
    , inner_pad_rgt=True
    , font_family=Font.FONT_FAMILY_NORMAL
    , font_color=Colors.WHITE
    )

  MED_BACK_HEADER_FONT: TextBoxStyle =\
    TextBoxStyle\
    ( backgnd_color=Colors.MEDIUM_GREY
    , inner_pad_top=True
    , inner_pad_bot=True
    , inner_pad_lft=True
    , inner_pad_rgt=True
    , font_family=Font.FONT_FAMILY_HEADER
    , font_color=Colors.WHITE
    )

  LTE_BACK_NORMAL_FONT: TextBoxStyle =\
    TextBoxStyle\
    ( backgnd_color=Colors.LIGHT_GREY
    , inner_pad_top=True
    , inner_pad_bot=True
    , inner_pad_lft=True
    , inner_pad_rgt=True
    , font_family=Font.FONT_FAMILY_NORMAL
    )

  LTE_BACK_HEADER_FONT: TextBoxStyle =\
    TextBoxStyle\
    ( backgnd_color=Colors.LIGHT_GREY
    , inner_pad_top=True
    , inner_pad_bot=True
    , inner_pad_lft=True
    , inner_pad_rgt=True
    , font_family=Font.FONT_FAMILY_HEADER
    )

  WHT_BACK_NORMAL_FONT_W_OUTLNE: TextBoxStyle =\
    TextBoxStyle\
    ( backgnd_color='none'
    , show_outline=True
    , inner_pad_top=True
    , inner_pad_bot=True
    , inner_pad_lft=True
    , inner_pad_rgt=True
    , font_family=Font.FONT_FAMILY_NORMAL
    )

  WHT_BACK_HEADER_FONT_W_OUTLNE: TextBoxStyle =\
    TextBoxStyle\
    ( backgnd_color='none'
    , show_outline=True
    , inner_pad_top=True
    , inner_pad_bot=True
    , inner_pad_lft=True
    , inner_pad_rgt=True
    , font_family=Font.FONT_FAMILY_HEADER
    )

  WHT_BACK_NORMAL_FONT_NO_OUTLNE: TextBoxStyle =\
    TextBoxStyle\
    ( backgnd_color='none'
    , show_outline=False
    , inner_pad_top=True
    , inner_pad_bot=True
    , inner_pad_lft=True
    , inner_pad_rgt=True
    , font_family=Font.FONT_FAMILY_NORMAL
    )

  WHT_BACK_HEADER_FONT_NO_OUTLNE: TextBoxStyle =\
    TextBoxStyle\
    ( backgnd_color='none'
    , show_outline=False
    , inner_pad_top=True
    , inner_pad_bot=True
    , inner_pad_lft=True
    , inner_pad_rgt=True
    , font_family=Font.FONT_FAMILY_HEADER
    )

  WHT_BACK_TITLE_FONT_NO_OUTLNE: TextBoxStyle =\
    TextBoxStyle\
    ( backgnd_color='none'
    , show_outline=False
    , inner_pad_top=True
    , inner_pad_bot=True
    , inner_pad_lft=True
    , inner_pad_rgt=True
    , font_family=Font.FONT_FAMILY_HEADER
    , font_size=Font.TITLE_SIZE
    )

  DEF_PAGE_HEADER_TXT: TextBoxStyle =\
    TextBoxStyle\
    ( backgnd_color='none'
    , show_outline=True
    , inner_pad_top=True
    , inner_pad_bot=True
    , inner_pad_lft=True
    , inner_pad_rgt=True
    , font_family=Font.FONT_FAMILY_HEADER
    , font_size=Font.DEF_PAGE_HEADER_TXT_SIZE
    )

  REF_SRC: TextBoxStyle =\
    TextBoxStyle\
    ( backgnd_color='none'
    , show_outline=False
    , inner_pad_top=True
    , inner_pad_bot=False
    , inner_pad_lft=False
    , inner_pad_rgt=False
    , font_family=Font.FONT_FAMILY_NORMAL
    , font_size=8
    )

#_______________________________________________________________________
class StdLineRowGroupStyles():

  ONE_THIRD_OFFSET: LineRowGroupStyle =\
    LineRowGroupStyle(y_offset=Dims.DEF_ROW_HGHT/3)

  DOTTED: LineRowGroupStyle =\
    LineRowGroupStyle(dash_array='1,5')

