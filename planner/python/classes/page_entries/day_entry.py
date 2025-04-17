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
#   Layout for daily entry.
#_______________________________________________________________________

import svgwrite.container
import svgwrite.text

from classes.constants.dims import PlannerDims as Dims
from classes.constants.strings import PlannerStrings as Strings
from classes.style.style import PlannerColors as Colors
from classes.style.style import PlannerFontStyle as Font

from classes.elements.daily_schedule import DaySchedule as DaySched
from classes.elements.entry_table import EntryTable
from classes.elements.entry_table import PromptTable
from classes.elements.entry_table import NumberedTable
from classes.elements.header_box import HeaderBox

from classes.page_layouts.half_letter_layout import OnePageHalfLetterLayout


#_______________________________________________________________________
class DayEntry(OnePageHalfLetterLayout):
  """
  Daily entry layout.
  """

  #_____________________________________________________________________
  def __init__(self
  , total_hght: int = 0
  , total_wdth: int = 0
  , padding: int = 0
  ):
    """
    Constructor for class. Assumes landscape orientation.
    """
    super().__init__\
      ( total_hght=total_hght
      , total_wdth=total_wdth
      , padding=padding
      )

    return

  #_____________________________________________________________________
  def add_content(self) -> None:
    """
    Add content to layout.

    Parameters:
      None

    Returns:
      None
    """
    super().add_content()

    #___________________________________________________________________
    sched_insert_x: int = self.content_insert_pt_x_\
      + self.content_wdth_\
      - self.schedule_wdth_\
      + Dims.BRD_MARGIN_PX * self.sched_.pad_lft_

    sched_insert_y: int = self.content_insert_pt_y_

    self.sched_['transform'] =\
      f'translate({sched_insert_x},{sched_insert_y})'

    #___________________________________________________________________
    # Entry insert calculations
    #___________________________________________________________________
    insert_x: int = self.content_insert_pt_x_
    insert_y: int = self.content_insert_pt_y_
    #___________________________________________________________________
    self.pri_efforts_['transform'] =\
      f'translate({insert_x},{insert_y})'

    insert_y: int = insert_y\
      + self.pri_efforts_.total_hght_
    #___________________________________________________________________
    self.checklist_['transform'] =\
      f'translate({insert_x},{insert_y})'

    insert_y: int = insert_y\
      + self.checklist_.total_hght_
    #___________________________________________________________________
    self.focus_['transform'] =\
      f'translate({insert_x},{insert_y})'

    insert_y: int = insert_y\
      + self.focus_.total_hght_
    #___________________________________________________________________
    self.todo_['transform'] =\
      f'translate({insert_x},{insert_y})'

    insert_y: int = insert_y\
      + self.todo_.total_hght_
    #___________________________________________________________________
    self.gratitude_['transform'] =\
      f'translate({insert_x},{insert_y})'

    insert_y: int = insert_y\
      + self.gratitude_.total_hght_
    #___________________________________________________________________
    self.prompt0_['transform'] =\
      f'translate({insert_x},{insert_y})'

    insert_y: int = insert_y\
      + self.prompt0_.total_hght_
    #___________________________________________________________________
    self.prompt1_['transform'] =\
      f'translate({insert_x},{insert_y})'

    insert_y: int = insert_y\
      + self.prompt1_.total_hght_
    #___________________________________________________________________
    self.prompt2_['transform'] =\
      f'translate({insert_x},{insert_y})'

    insert_y: int = insert_y\
      + self.prompt2_.total_hght_
    #___________________________________________________________________


    self.add(self.sched_)
    self.add(self.pri_efforts_)
    self.add(self.checklist_)
    self.add(self.focus_)
    self.add(self.todo_)
    self.add(self.gratitude_)
    self.add(self.prompt0_)
    self.add(self.prompt1_)
    self.add(self.prompt2_)

    return

  #_____________________________________________________________________
  def create_content(self) -> None:
    """

    Side Effects:
      Populates the following class variables.

    Parameters:
      None

    Returns:
      None
    """

    super().create_content()

    # Width of daily schedule content group
    self.schedule_wdth_: int = self.content_wdth_ * 0.25
    self.main_content_wdth_: int =\
      self.content_wdth_ - self.schedule_wdth_

    self.sched_: DaySched =\
      DaySched\
      ( wdth=self.schedule_wdth_
      , hght=self.content_hght_
      , time_inc_min=30
      , use_24=True
      )

    self.pri_efforts_: EntryTable =\
      EntryTable\
      ( wdth=self.main_content_wdth_
      , header_txt=Strings.DAY_PRIMARY_EFFORTS
      , row_count=3
      , pad_top=True
      , pad_rgt=True
      , show_outline=True
      )

    self.checklist_: HeaderBox=\
      HeaderBox\
      ( wdth=self.main_content_wdth_
      , header_txt=Strings.DAY_CHECKLIST
      , box_brdr_color='none'
      , box_fill_color='none'
      , pad_top=True
      , pad_rgt=True
      )

    self.todo_: NumberedTable =\
      NumberedTable\
      ( wdth=self.main_content_wdth_
      , header_txt=Strings.DAY_TODO
      , prepend_txt='[]'
      , row_count=4
      , pad_top=True
      , pad_rgt=True
      , show_outline=True
      )

    self.prompt0_: PromptTable =\
      PromptTable\
      ( wdth=self.main_content_wdth_
      , header_txt=Strings.DAY_PROMPTS[4]
      , row_count=3
      , pad_top=True
      , pad_rgt=True
      )

    self.prompt1_: PromptTable =\
      PromptTable\
      ( wdth=self.main_content_wdth_
      , header_txt=Strings.DAY_PROMPTS[1]
      , row_count=2
      , pad_top=True
      , pad_rgt=True
      )

    self.prompt2_: PromptTable =\
      PromptTable\
      ( wdth=self.main_content_wdth_
      , header_txt=Strings.DAY_PROMPTS[2]
      , row_count=3
      , pad_top=True
      , pad_rgt=True
      )

    # Calculate remaining height to evenly distribute spanning tables
    remaining_hght: int = self.content_hght_\
      - self.pri_efforts_.total_hght_\
      - self.checklist_.total_hght_\
      - self.todo_.total_hght_\
      - self.prompt0_.total_hght_\
      - self.prompt1_.total_hght_\
      - self.prompt2_.total_hght_\

    # Fill half of remaining space
    self.focus_: EntryTable =\
      EntryTable\
      ( wdth=self.main_content_wdth_
      , hght=remaining_hght/2
      , header_txt=[Strings.DAY_FOCUS]
      , row_count=1
      , pad_top=True
      , pad_rgt=True
      , show_outline=True
      )

    # Fill half of remaining space
    self.gratitude_: EntryTable =\
      EntryTable\
      ( wdth=self.main_content_wdth_
      , hght=remaining_hght/2
      , header_txt=[Strings.DAY_GRATITUDE]
      , pad_top=True
      , pad_rgt=True
      , show_outline=True
      )

    return

  #_____________________________________________________________________
  def create_page_header(self) -> svgwrite.container.Group:
    """
    Creates page header and saves it to class variable.

    Parameters:
      None

    Returns:

    """
    font_size: int = Font.DAY_PAGE_HEADER_SIZE
    font_family: str = Font.FONT_FAMILY_NORMAL
    sp: str = Strings.SPACE

    page_header = super().create_page_header\
      ( header_txt=Strings.DAYS
      , font_size=font_size
      , font=font_family
      )

    insert_date_x: int = self.content_wdth_ - 110
    insert_date_y: int = font_size + Font.TEXT_PADDING

    date_txt: svgwrite.text.Text =\
      svgwrite.text.Text\
      ( text=Strings.DATE_STR
      , insert=(insert_date_x, insert_date_y)
      , text_anchor='start'
      , alignment_baseline='text-after-edge'
      , fill=Colors.NORMAL_TXT
      , font_size=font_size
      , font_family=font_family
      )

    #page_header.add(date_txt)

    return page_header
