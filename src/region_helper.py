#!/usr/bin/env python
# -*-coding:utf-8-*-

import logging
import requests

def _found_region(cookies):
    try:
        for cookie in cookies:
            if cookie['name'] == 'JSESSIONID':
                _region = cookie['domain'].split('.')[0]
                # 4th region - chinese uses different endpoints, not covered by current plugin
                if _region.lower() in ['eu', 'us', 'kr']:
                    return _region
                else:
                    raise ValueError(f'Unknown region {_region}')
        else:  # for
            raise ValueError('JSESSIONID cookie not found')
    except Exception:
        return 'eu'


def guess_region(local_client):
    """
    1. read the consts.py
    2. try read the battlenet db OR config get the region info.
    3. try query https://www.blizzard.com/en-us/user
    4. failed return ""
    """
    from consts import REGION
    if REGION:
        return REGION

    try:
        if local_client._load_local_files():
            if local_client.config_parser.region:
                return local_client.config_parser.region.lower()

            if local_client.database_parser.region:
                return local_client.database_parser.region.lower()

        response = requests.get('https://www.blizzard.com/en-us/user', timeout=10)
        assert response.status_code == 200
        return response.json()['region'].lower()
    except Exception as e:
        logging.error(f'{e}')
        return ""
