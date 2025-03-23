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
  SPACE: str ='\u00A0\u00A0'

  DEF_TABLE_HEADER: str =\
    'Table Header'

  DEF_PAGE_HEADER: str =\
    'Page Header'

  DAILY_SCHEDULE_HEADER: str =\
    'Time Well Spent'

  DEF_LAYOUT_PATH: str =\
    'layout.svg'

  DEF_DAY_LAYOUT_PATH: str =\
    'day-layout.svg'

  DEF_GOAL_LAYOUT_PATH: str =\
    'goal-layout.svg'


  #_____________________________________________________________________
  # Day layout strings
  #_____________________________________________________________________
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

  DAY_CHECKLIST: list =\
  ['[] Vision ', '[] Goals', '[] Calendar', '[] Habit']

  DAY_FOCUS: str =\
    'Today I will pay most attention to:'

  DAY_GRATITUDE: str =\
    'Gratitude'

  DAY_PROMPTS: str =\
    [ 'How can I embrace discomfort and grow today?'
    , 'One acheivement I take pride in:'
    , 'How can I move towards my ideal self?'
    ]
  #_____________________________________________________________________

  #_____________________________________________________________________
  # Goal layout strings
  #_____________________________________________________________________
  GOAL_PAGE_HEADER: str =\
    'Goal #'

  GOAL_CHECKLIST: str =\
     '[] Specific'    + SPACE\
   + '[] Actionable'  + SPACE\
   + '[] Measureable' + SPACE\
   + '[] Exciting'    + SPACE\
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