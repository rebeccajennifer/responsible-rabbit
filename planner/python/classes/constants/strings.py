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

  RIGHT_ARROW: str =\
    '->'

  BULLET_PT: str =\
    '\u2022'

  DATE_STR: str =\
    7 * SPACE\
    + '/'\
    + 7 * SPACE\
    + '/'\
    + SPACE\
    + '20'\
    + 5 * SPACE

  DEF_TABLE_HEADER_TXT: str =\
    'Table Header'

  DEF_PAGE_HEADER_TXT: str =\
    'Page Header'

  DAILY_SCHEDULE_HEADER: str =\
    'Time Well Spent'

  #_____________________________________________________________________
  # Default file names
  #_____________________________________________________________________
  DEF_LAYOUT_PATH: str =\
    'layout'

  DEF_TEST_LAYOUT_PATH: str =\
    'test-layout'

  DEF_GOAL_LAYOUT_PATH: str =\
    'goal-layout'

  DEF_FUTURE_5YR_LAYOUT_PATH: str =\
    'future-5yr-layout'

  DEF_FUTURE_1YR_LAYOUT_PATH: str =\
    'future-1yr-layout'

  DEF_FUTURE_12W_LAYOUT_PATH: str =\
    'future-12w-layout'

  DEF_FUTURE_BAD_LAYOUT_PATH: str =\
    'future-bad-layout'

  DEF_WEEK_LAYOUT_PATH: str =\
    'week-layout'

  DEF_HABIT_LAYOUT_PATH: str =\
    'habit-layout'

  #_____________________________________________________________________
  # Day layout strings
  #_____________________________________________________________________
  QUOTE0: str = (
    'Start where you are. Use what you have. Do what you can. '
    '— Arthur Ashe'
  )

  QUOTE1: str = (
    'It\'s not always that we need to do more, but rather that we need '
    'to focus on less. — Nathan W. Morris'
  )

  QUOTE2: str = str(
    'Your future is created by what you do today, not tomorrow. '
    '— Robert Kiyosaki'
  )

  QUOTE3: str = str(
    'Discipline is the bridge between goals and accomplishment. '
    '— Jim Rohn'
  )

  QUOTE4: str = str(
    'Done is better than perfect. — Sheryl Sandberg'
  )

  QUOTE5: str = str(
    'Don\'t watch the clock; do what it does. Keep going. '
    '— Sam Levenson'
  )

  QUOTE6: str = str(
    'You don\'t have to see the whole staircase, just take the first '
    'step. — Martin Luther King Jr.'
    )

  QUOTE0: str = str(
    'It always seems impossible until it\'s done. — Nelson Mandela'
  )
  QUOTE1: str = str(
    'Owning our story and loving ourselves through that process is the '
    'bravest thing that we\'ll ever do. — Brené Brown'
  )
  QUOTE1: str = str(
    'Be yourself; everyone else is already taken. — Oscar Wilde'
  )
  QUOTE2: str = str(
    'Although the world is full of suffering, it is also full of the '
    'overcoming of it. — Helen Keller'
  )
  QUOTE3: str = str(
    'Every morning we are born again. What we do today is what matters '
    'most. — Buddha'
  )
  QUOTE4: str = str(
    'You cannot escape the responsibility of tomorrow by evading it '
    'today. — Abraham Lincoln'
  )
  QUOTE5: str = str(
    'The most important thing in life is to learn how to give out '
    'love, and to let it come in. — Morrie Schwartz'
  )
  QUOTE6: str = str(
    'Your body hears everything your mind says. — Naomi Judd'
  )

  QUOTES: list =\
  [ QUOTE0
  , QUOTE1
  , QUOTE2
  , QUOTE3
  , QUOTE4
  , QUOTE5
  , QUOTE6
  ]

  #_____________________________________________________________________
  # Goal layout strings
  #_____________________________________________________________________
  GOAL_PAGE_HEADER_TXT: str =\
    'Goal #'

  GOAL_CHECKLIST: str =\
     '[] Specific'    + SPACE\
   + '[] Measureable' + SPACE\
   + '[] Achievable'  + SPACE\
   + '[] Relevant'    + SPACE\
   + '[] Challenging'


  GOAL_ACTIONS: str =\
    'Critical Steps'

  GOAL_MILESTONES: list =\
  [ 'Advancement'
  , 'Date'
  ]

  GOAL_MEASUREMENT: str =\
    'Tangible Results'

  GOAL_OBSTACLES: str =\
    'Obstacles'

  GOAL_LIFE_IMPROVEMENT: str =\
    'Impacts of Success'

  GOAL_PLAN: str =\
    'Commitment Cadence'

  GOAL_REWARD: str =\
    'Celebration Plan'

  GOAL_MONTHS: list =\
  [ 'Month 1:'
  , 'Month 2:'
  , 'Month 3:'
  ]

  GOAL_VALUES: str =\
    'How does this goal support your values?'
  #_____________________________________________________________________
  # Week layout strings
  #_____________________________________________________________________
  WEEK_PAGE_HEADER_TXT_0: str =\
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


  WEEK_PAGE_HEADER_TXT_1: str = 'Week #'\
    + 6 * SPACE + 'Prep'\
    + 4 * SPACE + '|'\
    + 4 * SPACE + 'Start:'\
    + DATE_STR

  WEEK_ACCOMPLISHMENTS: str =\
    'Notable achievements from last week:'

  WEEK_UNFINISHED_BUSINESS: str =\
    'Unfinished Business'

  WEEK_VISUALIZATION_HEADER_TXT: str =\
    'Visualize Your Week'

  WEEK_VISUALIZATION_PROMPT_TXT: str =\
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
    'In the coming week, I\'m eager to experience:'

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

  HABIT_PAGE_HEADER_TXT: str =\
    'Habit Tracking' + 3 * SPACE + 'Month #'

  #_____________________________________________________________________
  # Month layout strings
  #_____________________________________________________________________
  MONTH_PAGE_HEADER_TXT_0: str =\
    'Goal #'

  MONTH_PAGE_HEADER_TXT_1: str =\
    'Goal #'

  MONTH_FOOTER_0: str =\
    "This month's # 1 priority"

  MONTH_FOOTER_1: str =\
    "This month's kaizen"

  #_____________________________________________________________________
  # Free write strings
  #_____________________________________________________________________

  PAGE_HEADER_TXT_FUTURE_5YR: str = 'Imagine a Future...'
  PAGE_HEADER_TXT_FUTURE_1YR: str = 'A Year of Growth'
  PAGE_HEADER_TXT_FUTURE_12W: str = '12 Week Potential'
  PAGE_HEADER_TXT_FUTURE_BAD: str = 'The Consequences of Inaction'

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

  VOW_HEADER_TXT: str =\
    'A Commitment to Growth'

  VOW: str = (
    'I, (your name), vow to be true to my word and to live with '
    'intention. I will no longer treat my time as something to be '
    'taken for granted. From this moment on, I commit to striving for '
    'my fullest potential—for myself, for those I care about, and for '
    'the greater good. I promise to dedicate time to this journal each '
    'day until it is complete, and through this practice, to bring '
    'my dreams, my purpose, and my highest self into being.'
  )