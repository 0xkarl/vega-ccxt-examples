# -*- coding: utf-8 -*-

import asyncio
import os
import sys

root = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root + '/ccxt/python')

import ccxt.async_support as ccxt  # noqa: E402


async def test():
    exchange = ccxt.vega({
        'enableRateLimit': True,  # as required by the Manual
        # "verbose": True,  # useful for debugging purposes, uncomment if needed
    })
    print(await exchange.fetch_markets())
    await exchange.close()  # don't forget to close it when you're done
    return True

if __name__ == '__main__':
    print('CCXT version:', ccxt.__version__)
    print(asyncio.get_event_loop().run_until_complete(test()))
