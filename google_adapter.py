# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from googleapiclient import discovery
from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials


class Adapter(object):
    scope = ['https://www.googleapis.com/auth/drive']

    def __init__(self, credentials_json, sheet_id):
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            credentials_json, self.scope
        )

        http_auth = credentials.authorize(Http())
        self.service = discovery.build('sheets', 'v4', http=http_auth)
        self.sheet_id = sheet_id

    def write_data(self, data, sheet_name):
        range_properties = '{sheet_name}!A2:F{data_len}'.format(
            sheet_name=sheet_name, data_len=str(1 + len(data))
        )

        values = data
        body = {'values': values}
        self.service.spreadsheets().values().update(
           spreadsheetId=self.sheet_id,
           range=range_properties,
           body=body,
           valueInputOption='USER_ENTERED'
        ).execute()

        print('Добавлено {0} задач'.format(len(data)))
