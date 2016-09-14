# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from jira import JIRA


class Adapter(object):
    hyperlink = '=HYPERLINK("{url}","{name}")'

    def __init__(self, auth_data, projects, on_date, scope=None):
        self.on_date = on_date

        if scope is None:
            scope = 'https://trood-cis.atlassian.net'

        self.jira = JIRA(scope, basic_auth=auth_data)

        JQL = ' AND '.join([
            'project in ("{0}")'.format('", "'.join(projects)),
            'worklogDate = "{0}"'.format(on_date),
        ])
        self.issues = self.jira.search_issues(JQL)

    def prepare_issue(self, issue):
        timespent = issue.fields.timespent
        timespent = timespent if timespent else 0
        timeestimate = issue.fields.timeestimate
        timeestimate = timeestimate if timeestimate else 0
        return [
            '11.00-19.00',
            issue.fields.project.key,
            self.hyperlink.format(
                url=issue.permalink(),
                name=issue.fields.summary
            ),
            str(round(float(timespent) / (60 * 60), 2)),
            str(round(float(timeestimate) / (60 * 60), 2)),
            str(round(float(timeestimate - timespent) / (60 * 60), 2)),
        ]

    def get_data(self):
        return [self.prepare_issue(issue) for issue in self.issues]
