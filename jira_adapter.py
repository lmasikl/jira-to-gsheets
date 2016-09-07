from __future__ import unicode_literals
import csv
import datetime
from jira import JIRA
from settings import JIRA_BASIC_AUTH, PROJECTS

class Adapter(object):
    jira = JIRA('https://trood-cis.atlassian.net', basic_auth=JIRA_BASIC_AUTH)

    TODAY = datetime.date.today().strftime('%Y-%m-%d')
    TODAY = datetime.date(2016, 8, 18).strftime('%Y-%m-%d')

    issues = [jira.search_issues('project="{}"'.format(p)) for p in PROJECTS]

    today_issues = [i for pi in issues for i in pi if TODAY in i.fields.updated]

    hyperlink = '=HYPERLINK("{url}","{name}")'
        
    def get_data(self):
        for issue in self.today_issues:
            timespent = issue.fields.timespent
            timespent = timespent if timespent else 0
            timeestimate = issue.fields.timeestimate
            timeestimate = timeestimate if timeestimate else 0
            return [
                '11.00-19.00',
                self.hyperlink.format(
                    url=issue.fields.project.permalink(),
                    name=issue.fields.project.name
                ),
                self.hyperlink.format(
                    url=issue.permalink(),
                    name=issue.fields.summary
                ),
                str(round(float(timespent) / (60 * 60), 2)),
                str(round(float(timeestimate) / (60 * 60), 2)),
            ]
