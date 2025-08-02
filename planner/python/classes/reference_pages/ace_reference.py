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
#   Entry for a blank page with page header.
#_______________________________________________________________________

import svgwrite.container

from classes.constants.addl_arg_keys import AddlArgKeys as Key
from classes.constants.strings import PlannerStrings as Strings
from classes.elements.base_element import VerticalStack
from classes.elements.row_group import DualLineRowGroup

from classes.page_layouts.half_page_layout import HalfPageLayout
from classes.elements.row_group import TextRowGroup
from classes.style.std_styles import StdTextBoxStyles

class AceStrings:
  """
  Strings used in the ACE Reference page.
  """

  PAGE_HEADER_TXT: str =\
    'Acknowlege ' + Strings.BULLET_PT\
  + ' Connect ' + Strings.BULLET_PT\
  + ' Engage'

  ABOUT_HEADER_TXT: str =\
    'About the ACE Method'

  ABOUT: str = (
    'ACE is a method used as tool to "unhook" oneself when '
    'experiencing unpleasant emotions. These '
    'feelings can cause our nervous system to dysregulate and '
    'can trigger one to engage in behaviors and thought '
    'patterns that moves a person away from their ideal self.'
  )

  USING_HEADER_TXT: str =\
    'How it works'

  USING_DESC: str = (
    'When you experience a triggering thought or feeling, pause and '
    'fill out the worksheet as described below.'
  )

  ACKNOWLEDGE_HEADER_TXT: str =\
    'Acknowlege'
  ACKNOWLEGE_DESC: str = (
    'Reference the list of Brene Brown\'s 87 Emotions and Experiences '
    'and identify the terms that most closely represent your current '
    'state.'
  )

  CONNECT_HEADER_TXT: str =\
    'Connect to Re-Regulate'
  CONNECT_DESC: str = (
    'Connect with your physical body to re-regulate your nervous '
    'system. Engage in one of the exercises described below.'
    '\n'
    '5-4-3-2-1 GROUNDING TECHNIQUE: Identify 5 things you can see, '
    '4 things you can touch, 3 distinct sounds, 2 scents, 1 thing you '
    'can taste.'
    '\n'
    'PROGRESSIVE MUSCLE RELAXATION: Lay on your back and close your '
    'eyes. Systematically tense and release muscles starting from your '
    'toes and ending with the top of your head.'
    '\n'
    'BOX BREATHING: Sit comfortably and close your eyes. Inhale for '
    'four seconds, pause for four seconds, exhale for four seconds, '
    'hold for four seconds. Practice for at least ten breath cycles '
    ' or two to five minutes.'
    '\n'
    'SHAKE: Stand with your feet hip-width apart and gently bounce '
    'your heels while keeping the balls of your feet grounded. Allow '
    'the movement to naturally travel up through your body. Let your '
    'shoulders bounce, your arms and hands shake out, and your head '
    'move gently side to side or in small circles. Keep your body '
    'relaxed and loose. Continue for 1-2 minutes, letting tension '
    'release with each shake.'
  )

  REENGAGE_HEADER_TXT: str =\
    '(Re-)Engage'

  REENGAGE_DESC: str = (
    'After executing the connection exercise, write down what activity '
    'you choose to (re)engage with. This can be what you were doing '
    'before experiencing the trigger, or an intentional act of self '
    'Commonly understood acts of self care include going outside, '
    'physical activity, or journaling. Other acts of self care include '
    'a household chore, creating art, or starting a task you\'ve been '
    'avoiding.'
  )


#_______________________________________________________________________
class AceReference(HalfPageLayout):
  """
  Free write layout.
  """

  #_____________________________________________________________________
  def __init__(self
  , total_hght: int = 0
  , total_wdth: int = 0
  , addl_args: dict = {Key.HEADER_TXT: ''}
  ):
    """
    Constructor for class. Assumes landscape orientation.
    """

    self.page_header_txt_: str = addl_args[Key.HEADER_TXT]

    super().__init__\
    ( total_hght=total_hght
    , total_wdth=total_wdth
    , pad_bet_elements=True
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

    about_stack: list =\
      [ TextRowGroup\
        ( total_wdth=self.content_wdth_
        , style=StdTextBoxStyles.LTE_BACK_HEADER_FONT
        , text=AceStrings.ABOUT_HEADER_TXT
        )
      , TextRowGroup\
        ( total_wdth=self.content_wdth_
        , style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE
        , text=AceStrings.ABOUT
        )
      ]

    using_stack: list =\
      [ TextRowGroup\
        ( total_wdth=self.content_wdth_
        , style=StdTextBoxStyles.LTE_BACK_HEADER_FONT
        , text=AceStrings.USING_HEADER_TXT
        )
      , TextRowGroup\
        ( total_wdth=self.content_wdth_
        , style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE
        , text=AceStrings.USING_DESC
        )
      ]

    acknowlege_stack: list =\
      [ TextRowGroup\
        ( total_wdth=self.content_wdth_
        , style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_W_OUTLNE
        , text=AceStrings.ACKNOWLEDGE_HEADER_TXT
        )
      , TextRowGroup\
        ( total_wdth=self.content_wdth_
        , style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE
        , text=AceStrings.ACKNOWLEGE_DESC
        )
      ]

    connect_stack: list =\
     [ TextRowGroup\
        ( total_wdth=self.content_wdth_
        , style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_W_OUTLNE
        , text=AceStrings.CONNECT_HEADER_TXT
        )
      , TextRowGroup\
        ( total_wdth=self.content_wdth_
        , style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE
        , text=AceStrings.CONNECT_DESC
        )
     ]

    reengage_stack: list =\
      [ TextRowGroup\
        ( total_wdth=self.content_wdth_
        , style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_W_OUTLNE
        , text=AceStrings.REENGAGE_HEADER_TXT
        )
      , TextRowGroup\
        ( total_wdth=self.content_wdth_
        , style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE
        , text=AceStrings.REENGAGE_DESC
        )
      ]

    fill_hght = self.calc_remaining_hght_per_element(5)

    stack_entries: list =\
      [ VerticalStack\
        ( obj_list=about_stack
        , show_outline=True
        )
      , VerticalStack\
        ( obj_list=using_stack
        , show_outline=True
        )
      , VerticalStack\
        ( obj_list=acknowlege_stack
        , show_outline=True
        )
      , VerticalStack\
        ( obj_list=connect_stack
        , show_outline=True
        )
      , VerticalStack\
        ( obj_list=reengage_stack
        , show_outline=True
        )
     ]

    self.entries_: list =\
      [ VerticalStack\
        ( obj_list=stack_entries
        , show_outline=True
        , total_hght=self.content_hght_
        )
      ]
    return


  #_____________________________________________________________________
  def create_page_header(self) -> svgwrite.container.Group:
    """
    Creates page header and saves it to class variable.

    Parameters:
      None

    Returns:

    """

    page_header = super().create_page_header\
      ( header_txt=AceStrings.PAGE_HEADER_TXT
      )

    return page_header
