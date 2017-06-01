'''
module is responsible for synchronising fio account with internal db
'''

import datetime
from dateutil.relativedelta import relativedelta
import fio


def sync(accountId, database):
    account = database.accounts.find_one({'_id': accountId})
    last_sync = account.get('last_sync', default=get_default_import_date()).strftime(
        "%Y-%m-%d")  # might by null or even exception
    now = get_now_datetime()

    fioClient = fio.FioClient(account['token'])


def get_now_datetime():
    return datetime.datetime.now().strftime("%Y-%m-%d")


def get_default_import_date():
    delta = relativedelta(year=1)
    return get_now_datetime() - delta
