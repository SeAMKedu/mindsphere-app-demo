# Standard Library
from datetime import datetime, timedelta
# Project Files
from iot_time_series import IoTTimeSeries

class DataFetcher(object):
    """ Fetch data from the MindSphere IoT Time Series Service. """
    def __init__(self, auth_token, asset_id, aspect):
        self.auth_token = auth_token
        self.asset_id = asset_id
        self.aspect = aspect
        # Set the time range to 5 days. Note that 2000 is the maximum number of
        # time series data points to be retrieved.
        self.fmt = '%Y-%m-%dT%H:%M:%S.%f'
        self.now = datetime.utcnow()
        # Required time format: 'YYYY-mm-ddTHH:MM:SS.sssZ'.
        self.start = (self.now - timedelta(days=5)).strftime(self.fmt)[:-3] + 'Z'
        self.end = self.now.strftime(self.fmt)[:-3] + 'Z'

    def fetch_data(self, variable):
        """ Read the timeseries data of the variable. """
        timestamps = []
        values = []
        response = IoTTimeSeries().read(
            self.auth_token,
            self.asset_id,
            self.aspect,
            _from=self.start,
            to=self.end,
            select=variable
        )
        if response.status_code == 200:
            data = response.json()
            # Read the latest record if the last 5 days has no data points.
            if not data:
                response = IoTTimeSeries().read(
                    self.auth_token,
                    self.asset_id,
                    self.aspect,
                    select=variable
                )
                if response.status_code == 200:
                    data = response.json()
            # Read timestamps and values.
            for data_point in data:
                timestamps.append(data_point['_time'])
                values.append(data_point[variable])
        return (timestamps, values)
