# -*- coding: utf-8 -*-

import asyncio
import os
import sys
from dotenv import load_dotenv
import json

load_dotenv()

root = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root + '/ccxt/python')

import ccxt.async_support as ccxt  # noqa: E402


async def test():
    exchange = ccxt.vega({
        'apiKey': os.getenv('WALLET_KEY'),
        'secret': os.getenv('WALLET_TOKEN'),
    })

    symbol = 'AAVEDAI.MF21'  # UNIDAI.MF21
    typ = 'LIMIT'
    side = 'BUY'
    amount = 2
    price = 21

    # print(await exchange.fetch_markets())
    # print(await exchange.fetch_currencies())
    # print(await exchange.fetch_ticker(symbol))
    # print(await exchange.create_order(symbol, typ, side, amount, price))

    orderId = 'V0000778657-0023746594'
    orderReference = 'ca22e9c9-1558-420e-ac9e-c2e9bf14da3d'

    # print(json.dumps(await exchange.fetch_orders(symbol), sort_keys=True, indent=4))
    print(await exchange.cancel_order(orderId, symbol))
    # print(await exchange.fetch_order(orderReference))
    # print(
    #   await exchange.amend_order(order_id, symbol, {
    #     price: 190,
    #   })
    # );
    # print(await exchange.fetch_positions(symbol))

    await exchange.close()  # don't forget to close it when you're done
    return True

if __name__ == '__main__':
    print('CCXT version:', ccxt.__version__)
    print(asyncio.get_event_loop().run_until_complete(test()))
