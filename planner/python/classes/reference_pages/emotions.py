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
#   List of Brene Brown's 87 emotions.
#_______________________________________________________________________

class EmotionStrings:
  """
  List of 87 human emotions and experiences from research by Brene Brown
  """

  PREFIX: str = 'Places we go when...'

  HDR_UNCERTAIN         : str = 'Things are uncertain or too much'
  HDR_COMPARE           : str = 'We compare'
  HDR_UNPLANNED         : str = 'Things don\'t go as planned'
  HDR_BEYOND_US         : str = 'It\'s beyond us'
  HDR_NOT_WHAT_THEY_SEEM: str = 'Things aren\'t what they seem'
  HDR_HURT              : str = 'We\'re hurting'
  HDR_OTHERS            : str = 'With others'
  HDR_FALL_SHORT        : str = 'We fall short'
  HDR_CONNECTION        : str = 'We search for connection'
  HDR_OPEN              : str = 'The heart is open'
  HDR_GOOD              : str = 'Life is good'
  HDR_WRONGED           : str = 'We feel wronged'
  HDR_SELF_ASSESS       : str = 'To self-assess'

  UNCERTAIN: list =\
    [ 'Stress'
    , 'Overwhelm'
    , 'Anxiety'
    , 'Worry'
    , 'Avoidance'
    , 'Excitement'
    , 'Dread'
    , 'Fear'
    , 'Vulnerability'
    ]

  COMPARE: list =\
    [ 'Comparison'
    , 'Admiration'
    , 'Reverence'
    , 'Envy'
    , 'Jealousy'
    , 'Resentment'
    , 'Schadenfreude'
    , 'Freudenfreude'
    ]

  UNPLANNED: list =\
    [ 'Boredom'
    , 'Expectations'
    , 'Regret'
    , 'Resignation'
    , 'Frustration'
    , 'Disappointment'
    , 'Discouragement'
    ]

  BEYOND_US: list =\
    [ 'Awe'
    , 'Wonder'
    , 'Confusion'
    , 'Curiosity'
    , 'Interest'
    , 'Surprise'
    ]

  NOT_WHAT_THEY_SEEM: list =\
    [ 'Amusement'
    , 'Nostalgia'
    , 'Irony'
    , 'Paradox'
    , 'Sarcasm'
    , 'Bittersweetness'
    , 'Cognitive Dissonance'
    ]

  HURT: list =\
    [ 'Anguish'
    , 'Hopelessness'
    , 'Despair'
    , 'Sadness'
    , 'Grief'
    ]

  OTHERS: list =\
    [ 'Compassion'
    , 'Pity'
    , 'Empathy'
    , 'Sympathy'
    , 'Boundaries'
    , 'Comparative Suffering'
    ]

  FALL_SHORT: list =\
    [ 'Shame'
    , 'Perfectionism'
    , 'Guilt'
    , 'Humiliation'
    , 'Embarrassment'
    , 'Self-Compassion'
    ]

  CONNECTION: list =\
    [ 'Belonging'
    , 'Fitting In'
    , 'Connection'
    , 'Disconnection'
    , 'Insecurity'
    , 'Invisibility'
    , 'Loneliness'
    ]

  OPEN: list =\
    [ 'Love'
    , 'Lovelessness'
    , 'Heartbreak'
    , 'Trust'
    , 'Self-Trust'
    , 'Betrayal'
    , 'Defensiveness'
    , 'Flooding'
    , 'Hurt'
    ]

  GOOD: list =\
    [ 'Joy'
    , 'Happiness'
    , 'Calm'
    , 'Contentment'
    , 'Gratitude'
    , 'Relief'
    , 'Tranquility'
    , 'Foreboding Joy'
    ]

  WRONGED: list =\
    [ 'Anger'
    , 'Contempt'
    , 'Disgust'
    , 'Hate'
    , 'Dehumanization'
    , 'Self-Righteousness'
    ]

  SELF_ASSESS: list =\
    [ 'Pride'
    , 'Hubris'
    , 'Humility'
    ]

  UNCERTAIN_DICT          : dict = {'header': HDR_UNCERTAIN         , 'emotions': UNCERTAIN         }
  COMPARE_DICT            : dict = {'header': HDR_COMPARE           , 'emotions': COMPARE           }
  UNPLANNED_DICT          : dict = {'header': HDR_UNPLANNED         , 'emotions': UNPLANNED         }
  BEYOND_US_DICT          : dict = {'header': HDR_BEYOND_US         , 'emotions': BEYOND_US         }
  NOT_WHAT_THEY_SEEM_DICT : dict = {'header': HDR_NOT_WHAT_THEY_SEEM, 'emotions': NOT_WHAT_THEY_SEEM}
  HURT_DICT               : dict = {'header': HDR_HURT              , 'emotions': HURT              }
  OTHERS_DICT             : dict = {'header': HDR_OTHERS            , 'emotions': OTHERS            }
  FALL_SHORT_DICT         : dict = {'header': HDR_FALL_SHORT        , 'emotions': FALL_SHORT        }
  CONNECTION_DICT         : dict = {'header': HDR_CONNECTION        , 'emotions': CONNECTION        }
  OPEN_DICT               : dict = {'header': HDR_OPEN              , 'emotions': OPEN              }
  GOOD_DICT               : dict = {'header': HDR_GOOD              , 'emotions': GOOD              }
  WRONGED_DICT            : dict = {'header': HDR_WRONGED           , 'emotions': WRONGED           }
  SELF_ASSESS_DICT        : dict = {'header': HDR_SELF_ASSESS       , 'emotions': SELF_ASSESS       }