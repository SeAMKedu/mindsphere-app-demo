# Standard Library
import json
# Additional Modules
import requests

class IoTTimeSeries(object):
    """ MindSphere IoT Time Series Service """
    def __init__(self):
        self.base_url = 'https://gateway.eu1.mindsphere.io/api/iottimeseries/v3'

    def read(self, token, asset_id, aspect, _from=None, to=None, limit=2000, select=None, sort='asc'):
        """
        Read time series data for a single asset and aspect.
        Return the latest value if no time range is provided.

        Params:
            token (str): A valid token.
            asset_id (str): The unique ID of the asset.
            aspect (str): The name of the aspect.
            _from (str): Start date of the time range to read.
            to (str): End date of the time range to read.
            limit (int:2000): Max number of entries to read.
            select (str): Select variables to return.
            sort (str): Sort order by time. asc (default) or desc.
        Returns:
            HTTP response. If success, the status code is 200,
            and the body is a list of dicts.
        """
        url = self.base_url + '/timeseries/' + asset_id + '/' + aspect
        query_params = {
            'limit': limit,
            'sort': sort
        }
        if _from:
            query_params['from'] = _from
        if to:
            query_params['to'] = to
        if select:
            query_params['select'] = select
        headers = {'Authorization': token}
        response = requests.get(url, params=query_params, headers=headers)
        return response

    def write(self, token, asset_id, aspect, time_series):
        """
        Write or update time series data.

        If new time series data has the same timestamp than the
        previous data, existing data is overwritten. Data for
        all variables needs to be provided together.

        Params:
            token (str): A valid token.
            asset_id: (str): The unique ID of the asset.
            aspect (str: The name of the aspect.
            time_series (list): Time series data as a list of dicts.
        
        Returns:
            HTTP response: If success, the status code is 204.
        """
        url = self.base_url + '/timeseries/' + asset_id + '/' + aspect
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        response = requests.put(url, json=time_series, headers=headers)
        return response

    def delete(self, token, asset_id, aspect, _from, to):
        """
        Delete time series data.

        Delete time series data for a single asset and aspect
        within a given time range. Data for all variables within
        the aspect is deleted.

        Params:
            token (str): A valid token.
            asset_id: (str): The unique ID of the asset.
            aspect (str): The name of the aspect.
            _from (str): Start date of the time range.
            to (str): End date of the time range.
        
        Returns:
            HTTP response: If the request was successfull,
            status code is 200 with no response body.
        """
        url = self.base_url + '/timeseries/' + asset_id + '/' + aspect
        headers = {'Authorization': token}
        query_params = {'from': _from, 'to': to}
        response = requests.delete(url, params=query_params, headers=headers)
        return response
