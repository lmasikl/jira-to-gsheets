# -*- coding:utf-8 -*-
from __future__ import unicode_literals

import datetime
import re

from google_adapter import Adapter as Google
from jira_adapter import Adapter as Jira
from settings import (CREDENTIALS_JSON, DATE_FORMAT, JIRA_BASIC_AUTH, PROJECTS,
                      SHEET_ID)

DATE_INPUT_PATTERN = re.compile('\d{4}/\d{2}/\d{2}')

on_date = input('На какую дату "YYYY/MM/DD" составить отчет? '.encode('utf-8'))
if not DATE_INPUT_PATTERN.match(on_date):
    on_date = datetime.date.today().strftime(DATE_FORMAT)

jira = Jira(JIRA_BASIC_AUTH, PROJECTS, on_date)
google = Google(CREDENTIALS_JSON, SHEET_ID)

jira_data = jira.get_data()
sheet_name = '.'.join([on_date[-2:], on_date[5:7], on_date[:4]])
google.write_data(jira_data, sheet_name)
