from datetime import datetime, date
import requests

def coerce_date(value):
    if isinstance(value, date):
        return datetime.combine(value, datetime.min.time())
    else:
        return datetime.strptime(value[:10], '%Y-%m-%d')

class FioClient():
    __url = 'https://www.fio.cz/ib_api/rest/periods/{token}/{from_date}/{to_date}/transactions.json'

    transaction_schema = {
       'column0': ('date', coerce_date),
       'column1': ('amount', float),
       'column2': ('account_number', str),
       'column3': ('bank_code', str),
       'column4': ('constant_symbol', str),
       'column5': ('variable_symbol', str),
       'column6': ('specific_symbol', str),
       'column7': ('user_identification', str),
       'column8': ('type', str),
       'column9': ('executor', str),
       'column10': ('account_name', str),
       'column12': ('bank_name', str),
       'column14': ('currency', str),
       'column16': ('recipient_message', str),
       'column17': ('instruction_id', str),
       'column18': ('specification', str),
       'column22': ('transaction_id', str),
       'column25': ('comment', str),
       'column26': ('bic', str),
    }

    def __init__(self, token):
        self.token = token
   
    def _sanitize_value(self, value, convert=None):
        if isinstance(value, str):
            value = value.strip() or None
        if convert and value is not None:
            return convert(value)
        else:
            return value

    def period(self, from_date, to_date):
        data = self.request(from_date, to_date)
        return self.parse(data)

    def request(self, from_date, to_date):
        url = self.__url.format(token=self.token, from_date=from_date, to_date=to_date)
        response = requests.get(url)
        
        response.raise_for_status()
        if response.content:
            return response.json()
        return None
     
    def parse(self, data):
        schema = self.transaction_schema
        entries = data['accountStatement']['transactionList']['transaction']
        for entry in entries:
            trans = {}
            for column_name, column_data in entry.items():
                if not column_data:
                    continue
                field_name, convert = schema[column_name.lower()]

                value = self._sanitize_value(value=column_data['value'],convert=convert)
                trans[field_name] = value

            for column_data_name, (field_name, convert) in schema.items():
                trans.setdefault(field_name, None)

            yield trans