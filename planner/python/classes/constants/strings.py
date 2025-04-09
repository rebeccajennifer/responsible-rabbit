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
#   Strings used throughout planner.
#_______________________________________________________________________

class PlannerStrings:
  """
  Strings used in planner.
  """
  SPACE: str =\
    '\u00A0\u00A0'

  RIGHT_ARROW: str =\
    '\u2192'

  DATE_STR: str =\
    3 * SPACE\
    + '/'\
    + 3 * SPACE\
    + '/'\
    + SPACE\
    + '20'\
    + 2 * SPACE

  DEF_TABLE_HEADER: str =\
    'Table Header'

  DEF_PAGE_HEADER: str =\
    'Page Header'

  DAILY_SCHEDULE_HEADER: str =\
    'Time Well Spent'



  #_____________________________________________________________________
  # Default file names
  #_____________________________________________________________________
  DEF_LAYOUT_PATH: str =\
    'layout.svg'

  DEF_DAY_LAYOUT_PATH: str =\
    'day-layout.svg'

  DEF_GOAL_LAYOUT_PATH: str =\
    'goal-layout.svg'

  DEF_GOAL_LAYOUT_PATH: str =\
    'goal-layout.svg'

  DEF_WEEK_LAYOUT_PATH: str =\
    'week-layout.svg'

  #_____________________________________________________________________
  # Day layout strings
  #_____________________________________________________________________
  SHORT_QUOTE_0: str =\
    'Start where you are. Use what you have. Do what you can. '
    #'-Arthur Ashe'

  QUOTE0: str =\
    'It’s not always that we need to do more, but rather that we need '\
    'to focus on less.'

  QUOTE1: str =\
    'Your future is created by what you do today, not tomorrow.'

  QUOTES: list =\
  [ {'quote': QUOTE0, 'author': 'Nathan W. Morris'}
  , {'quote': QUOTE1, 'author': 'Robert Kiyosaki'}
  ]

  DAY_PRIMARY_EFFORTS: list =\
    ['Primary Efforts', 'Alignment']

  DAY_TODO: str =\
    'To Do'

  DAY_CHECKLIST: list =\
  ['[] Vision ', '[] Goals', '[] Calendar', '[] Habit']

  DAY_FOCUS: str =\
    'Today I will pay most attention to:'

  DAY_GRATITUDE: str =\
    'Gratitude'

  DAY_PROMPTS: str =\
    [ 'How can I embrace discomfort and grow today?'
    , 'One achievement I take pride in:'
    , 'How can I move towards my ideal self?'
    , 'What am I avoiding and why?'
    , 'What would make today feel meaningful?'
    , 'What can I let go of to move forward?'
    , 'Where can I invite more joy or ease?'
    ]


  #_____________________________________________________________________
  # Goal layout strings
  #_____________________________________________________________________
  GOAL_PAGE_HEADER: str =\
    'Goal #'

  GOAL_CHECKLIST: str =\
     '[] Specific'    + SPACE\
   + '[] Measureable' + SPACE\
   + '[] Achievable'  + SPACE\
   + '[] Relevant'    + SPACE\
   + '[] Challenging'


  GOAL_ACTIONS: str =\
    'Critical Steps'

  GOAL_MEASUREMENT: str =\
    'Evaluation Metrics'

  GOAL_COST: str =\
    'Costs & Challenges'

  GOAL_LIFE_IMPROVEMENT: str =\
    'Impacts of Success'

  GOAL_BENCHMARKS: str =\
    'Monthly Benchmarks'

  GOAL_PLAN: str =\
    'Execution Plan'

  GOAL_REWARD: str =\
    'Celebration Plan'

  GOAL_MONTHS: list =\
  [ 'Month 1:'
  , 'Month 2:'
  , 'Month 3:'
  ]

  #_____________________________________________________________________
  # Week layout strings
  #_____________________________________________________________________
  WEEK_PAGE_HEADER_0: str =\
    'Last week I built momentum:'\
    + SPACE\
    + SPACE + 'disagree'\
    + SPACE + '-2'\
    + SPACE + '-1'\
    + SPACE + ' 0'\
    + SPACE + '+1'\
    + SPACE + '+2'\
    + SPACE + 'agree'


  WEEK_PAGE_HEADER_1: str =\
    'Goals for Week: '\
    + 6 * SPACE\
    + DATE_STR\
    + 3 * SPACE\
    + RIGHT_ARROW\
    + 3 * SPACE\
    + DATE_STR

  WEEK_ACCOMPLISHMENTS: str =\
    'Notable achievements from last week include:'

  WEEK_UNFINISHED_BUSINESS: str =\
    'Unfinished Business'

  WEEK_VISUALIZATION_HEADER: str =\
    'Visualize Your Week'

  WEEK_VISUALIZATION_PROMPT: str =\
    'Sketch a visual of your expectations for the week.'

  WEEK_IMPROVEMENT: str =\
    'What do I need to prioritize for growth?'

  WEEK_GRATITUDE: str =\
    'I appreciate...'

  WEEK_LESSONS_LEARNED: str =\
    'Lessons Learned From Last Week'

  WEEK_FULFILLMENT: str =\
    'How can I find the most fulfillment in these areas?'

  WEEK_FULFILLMENT_AREAS_0 =\
    ['Health', 'Connections']

  WEEK_FULFILLMENT_AREAS_1 =\
    ['Enjoyment', 'Job']

  WEEK_CHECKLIST: list =\
    ['[] Specific', '[] Measurable', '[] Achieveable']

  WEEK_LOOKING_FORWARD: str =\
    "In the coming week, I’m eager to experience:"

  WEEK_HABIT_TRACKER_HEADINGS: list =\
    [ 'Habit'
    , 'Target'
    , 'Mon'
    , 'Tue'
    , 'Wed'
    , 'Thu'
    , 'Fri'
    , 'Sat'
    , 'Sun'
    , 'Tally'
    ]

  #_____________________________________________________________________
  # Month layout strings
  #_____________________________________________________________________
  MONTH_PAGE_HEADER_0: str =\
    'Goal #'

  MONTH_PAGE_HEADER_1: str =\
    'Goal #'

  MONTH_FOOTER_0: str =\
    "This month's # 1 priority"

  MONTH_FOOTER_1: str =\
    "This month's kaizen"

  #_____________________________________________________________________
  # Free write strings
  #_____________________________________________________________________

  FUTURE_PAGE_HEADER: str =\
    'An Imagined Future'

  FREE_WRITE_FUTURE: str =\
    'Write down your ideal future 3-5 years from now—the boldest ' \
    'version you can imagine, even if it feels unrealistic. Ask ' \
    'yourself: What do I want from life? What skills do I want to ' \
    'master? What habits should I break or build? How will my health, ' \
    'social life, and leisure look? What kind of family life do I ' \
    'want? Where will I be financially and in my career? What ' \
    'qualities do I admire and want to develop? What would I do if I ' \
    'weren’t afraid? Who will I become? Start by freewriting a rough ' \
    'draft before writing in your response below.'