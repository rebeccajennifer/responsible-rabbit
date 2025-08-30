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
#   Reference page for ACE method.
#_______________________________________________________________________

from copy import deepcopy

from classes.constants.addl_arg_keys import AddlArgKeys as Key
from classes.constants.strings import PlannerStrings as Strings
from classes.elements.base_element import VerticalStack
from classes.elements.row_group import DualLineRowGroup

from classes.page_layouts.half_page_layout import HalfPageLayout
from classes.elements.row_group import TextRowGroup
from classes.style.std_styles import StdTextBoxStyles


#_______________________________________________________________________
class AceReference(HalfPageLayout):
  """
  Strings used in the ACE Reference page.
  """

  PAGE_HEADER_TXT: str = str(
    f'Acknowlege {Strings.BULLET_PT} '
    f'Connect {Strings.BULLET_PT} '
    f'Engage: {2 * Strings.SPACE} Worksheet Instructions'
  )

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

  WKSHT_HEADER_TXT: str =\
    'The Worksheet'

  USING_DESC: str = (
    'When you experience a triggering thought or feeling, pause and '
    'fill out the worksheet as described below.'
  )

  ACKNOWLEDGE_HEADER_TXT: str =\
    'ACKNOWLEGE'
  ACKNOWLEGE_DESC: str = (
    'Reference the list of Brene Brown\'s 87 Emotions and Experiences '
    'and identify the terms that most closely represent your current '
    'state.'
  )

  CONNECT_HEADER_TXT: str =\
    'CONNECT to Re-Regulate'
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
    '(RE-)ENGAGE'

  REENGAGE_DESC: str = (
    'After executing the connection exercise, write down what activity '
    'you choose to (re)engage with. This can be what you were doing '
    'before experiencing the trigger, or an intentional act of self '
    'Commonly understood acts of self care include going outside, '
    'physical activity, or journaling. Other acts of self care include '
    'a household chore, creating art, or starting a task you\'ve been '
    'avoiding.'
  )

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

    # Style for reference section headers
    ref_header_style: StdTextBoxStyles =\
      deepcopy(StdTextBoxStyles.LTE_BACK_HEADER_FONT)
    ref_header_style.font_size = 14

    # Style for worksheet instruction headers
    wksht_header_style: StdTextBoxStyles =\
      deepcopy(StdTextBoxStyles.WHT_BACK_HEADER_FONT_W_OUTLNE)

    # Style for worksheet instructions
    wksht_instructions_style: StdTextBoxStyles =\
      deepcopy(StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE)

    # List of objects for about section
    about_stack: list =\
      [
        TextRowGroup\
        ( total_wdth=self.content_wdth_
        , style=ref_header_style
        , text=self.ABOUT_HEADER_TXT
        )
      , TextRowGroup\
        ( total_wdth=self.content_wdth_
        , style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE
        , text=self.ABOUT
        )
      ]

    # List of objects for "how it works" section
    using_stack: list =\
      [ TextRowGroup\
        ( total_wdth=self.content_wdth_
        , style=ref_header_style
        , text=self.USING_HEADER_TXT
        )
      , TextRowGroup\
        ( total_wdth=self.content_wdth_
        , style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE
        , text=self.USING_DESC
        )
      ]

    # List of objects for acknowledge instruction section
    acknowlege_stack: list =\
      [ TextRowGroup\
        ( total_wdth=self.content_wdth_
        , style=wksht_header_style
        , text=self.ACKNOWLEDGE_HEADER_TXT
        )
      , TextRowGroup\
        ( total_wdth=self.content_wdth_
        , style=wksht_instructions_style
        , text=self.ACKNOWLEGE_DESC
        )
      ]

    # List of objects for connect instruction section
    connect_stack: list =\
     [ TextRowGroup\
        ( total_wdth=self.content_wdth_
        , style=wksht_header_style
        , text=self.CONNECT_HEADER_TXT
        )
      , TextRowGroup\
        ( total_wdth=self.content_wdth_
        , style=wksht_instructions_style
        , text=self.CONNECT_DESC
        )
     ]

    # List of objects for re-engage instruction section
    reengage_stack: list =\
      [ TextRowGroup\
        ( total_wdth=self.content_wdth_
        , style=wksht_header_style
        , text=self.REENGAGE_HEADER_TXT
        )
      , TextRowGroup\
        ( total_wdth=self.content_wdth_
        , style=wksht_instructions_style
        , text=self.REENGAGE_DESC
        )
      ]

    fill_hght = self.calc_remaining_hght_per_element(5)

    worksheet_stack: list =\
      [ TextRowGroup\
        ( total_wdth=self.content_wdth_
        , style=ref_header_style
        , text=self.WKSHT_HEADER_TXT
        )
      , VerticalStack\
        ( obj_list=acknowlege_stack
        , show_outline=False
        )
      , VerticalStack\
        ( obj_list=connect_stack
        , show_outline=False
        )
      , VerticalStack\
        ( obj_list=reengage_stack
        , show_outline=False
        )
      ]

    self.entries_: list =\
      [  VerticalStack\
        ( obj_list=about_stack
        , show_outline=True
        )
      , VerticalStack\
        ( obj_list=using_stack
        , show_outline=True
        )
      , VerticalStack\
        ( obj_list=worksheet_stack
        , show_outline=True
        , pad_bet_elements=True
        )
      ]


    return
