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

  BULLET_PT: str =\
    '\u2022'

  DATE_STR: str =\
    5 * SPACE\
    + '/'\
    + 5 * SPACE\
    + '/'\
    + SPACE\
    + '20'\
    + 5 * SPACE

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

  DEF_TEST_LAYOUT_PATH: str =\
    'test-layout.svg'

  DEF_DAY_LAYOUT_PATH: str =\
    'day-layout.svg'

  DEF_GOAL_LAYOUT_PATH: str =\
    'goal-layout.svg'

  DEF_FUTURE_LAYOUT_PATH: str =\
    'future-layout.svg'

  DEF_FUTURE_YR_LAYOUT_PATH: str =\
    'future-yr-layout.svg'

  DEF_FUTURE_12WK_LAYOUT_PATH: str =\
    'future-12-wk-layout.svg'

  DEF_INACTION_LAYOUT_PATH: str =\
    'inaction-layout.svg'

  DEF_WEEK_LAYOUT_PATH: str =\
    'week-layout.svg'

  DEF_HABIT_LAYOUT_PATH: str =\
    'habit-layout.svg'

  #_____________________________________________________________________
  # Day layout strings
  #_____________________________________________________________________
  SHORT_QUOTE_0: str =\
    'Start where you are. Use what you have. Do what you can. '
    #'-Arthur Ashe'

  QUOTE0: str =\
    'It’s not always that we need to do more, but rather that we need '\
    'to focus on less. - Nathan W. Morris'

  QUOTE1: str =\
    'Your future is created by what you do today, not tomorrow.'

  QUOTES: list =\
  [ {'quote': QUOTE0, 'author': '- Nathan W. Morris'}
  , {'quote': QUOTE1, 'author': '- Robert Kiyosaki'}
  ]

  DAYS: str =\
    'Mon' + 2 * SPACE +\
    'Tue' + 2 * SPACE +\
    'Wed' + 2 * SPACE +\
    'Thu' + 2 * SPACE +\
    'Fri' + 2 * SPACE +\
    'Sat' + 2 * SPACE +\
    'Sun' + 2 * SPACE + DATE_STR

  DAY_PRIMARY_EFFORTS: list =\
    ['Primary Efforts', 'Alignment']

  DAY_TODO: str =\
    'To Do'

  DAY_CHECKLIST_STR: list =\
    '[] Vision ' + SPACE +\
    '[] Goals'   + SPACE +\
    '[] Calendar'+ SPACE +\
    '[] Habit'

  DAY_FOCUS: str =\
    'Today I will pay most attention to:'

  DAY_GRATITUDE: str =\
    'Gratitude'

  DAY_ACHIEVEMENT: str =\
    'One achievement I take pride in:'

  DAY_PROMPTS: str =\
    [ 'How can I embrace discomfort and grow today?'
    , 'How can I move towards my ideal self?'
    , 'What am I avoiding?'
    , 'What would make today feel meaningful?'
    , 'What can I let go of to move forward?'
    , 'Where can I invite more ease into my life?'
    ]

  DAY_PROMPT_LAST_24: str =\
    'In the last 24 hours...'

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
    'Tangible Results'

  GOAL_OBSTACLES: str =\
    'Obstacles'

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
    'Week #' + 6 * SPACE + 'Reflections and Insights'

  WEEK_MOMENTUM: str =\
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
    'Goals for Week # '\
    + SPACE\
    + DATE_STR\
    + RIGHT_ARROW\
    + DATE_STR

  WEEK_ACCOMPLISHMENTS: str =\
    'Notable achievements from last week:'

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

  WEEK_THOUGHTS: str =\
    'Thoughts and Reflections'

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
    [ 'Habits' + SPACE + 'Week #'
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

  HABIT_PAGE_HEADER: str =\
    'Habit Tracking' + 3 * SPACE + 'Month #'

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

  PAGE_HEADER_FUTURE_5YR: str = 'Imagine a Future...'
  PAGE_HEADER_FUTURE_1YR: str = 'A Year of Growth'
  PAGE_HEADER_FUTURE_12W: str = '12 Week Potential'
  PAGE_HEADER_FUTURE_BAD: str = 'The Consequences of Inaction'

  FREE_WRITE_FUTURE_5YR: str = (
    'Describe your ideal life 3–5 years from now—the boldest vision '
    'you can imagine, even if it feels far off. Ask yourself: What do '
    'I truly want from life? What skills will I master? Which habits '
    'should I drop or build? What will my health and social life look '
    'like? How will I spend leisure time? What kind of family life do '
    'I want? Where will I be in my career and financially? What traits '
    'do I admire and want to grow into? What would I do if I had no '
    'fear? What kind of person will I grow into? Start by freewriting '
    'before refining your answer below.'
  )

  FREE_WRITE_FUTURE_1YR: str = (
    'Imagine your life 12 months from now. Where do you want to be, '
    'and what do you hope to have accomplished? Be specific and aim '
    'for goals that excite you, even if they feel slightly out of '
    'reach. Think about how you want to grow personally, '
    'professionally, and emotionally. What changes do you want to see '
    'in your work, your relationships, and your overall well-being? '
  )

  FREE_WRITE_FUTURE_12W: str = (
    'Imagine how your life will change over the next twelve weeks. '
    'Aim for progress that feels bold but within your reach. What '
    'fears will you face head-on? What talents will you grow? What '
    'knowledge will you seek out? What routines will help—or hold you '
    'back? Who will you spend time with? How will you relax or have '
    'fun? What kind of home life do you want? What will change at work '
    'or with money? How will you evolve as a person? Who are you '
    'choosing to become?'
  )

  FREE_WRITE_FUTURE_BAD: str = (
    'Though it may feel unsettling, envision the genuine consequences '
    'of not honoring your commitments. Picture the most serious yet '
    'believable outcome. What does that scenario look like? Who do you '
    'become, and how are your health, finances, and relationships '
    'affected?'
  )