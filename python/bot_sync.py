# -*- coding: utf-8 -*-

import os
import sys
from dotenv import load_dotenv
import json

load_dotenv()

root = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root + '/ccxt/python')

import ccxt  # noqa: E402


def test():
    exchange = ccxt.vega({
        'apiKey': os.getenv('WALLET_KEY'),
        'secret': os.getenv('WALLET_TOKEN'),
    })

    symbol = 'AAVEDAI.MF21'  # UNIDAI.MF21
    typ = 'LIMIT'
    side = 'BUY'
    amount = 2
    price = 21

    # print(exchange.fetch_markets())
    # print(exchange.fetch_currencies())
    # print(exchange.fetch_ticker(symbol))
    # print(exchange.create_order(symbol, typ, side, amount, price))

    order_id = 'V0000777744-0023716868'
    # order_reference = 'ca22e9c9-1558-420e-ac9e-c2e9bf14da3d'

    print(json.dumps(exchange.fetch_orders(symbol), sort_keys=True, indent=4))
    # print(exchange.cancel_order(order_id, symbol))
    # print(exchange.fetch_order(order_reference))
    # print(
    #   exchange.amend_order(order_id, symbol, {
    #     price: 190,
    #   })
    # );
    # print(exchange.fetch_positions(symbol))


if __name__ == '__main__':
    test()
