import os

# Jira settings
JIRA_BASIC_AUTH = ('username', 'password')
PROJECTS = ('KEY_ONE', 'KEY_TWO')

# Google settings
SHEET_ID = 'SHEET_KEY'
PWD = os.path.abspath(os.path.dirname(os.path.dirname('__file__')))
CREDENTIALS_JSON = os.path.join(PWD, 'google.json')

# Formats
DATE_FORMAT = '%Y/%m/%d'
