const ccxt = require('../../ccxt/ccxt.js');

const exchange = new ccxt.vega({
  apiKey: process.env.WALLET_KEY,
  secret: process.env.WALLET_TOKEN,
});

(async () => {
  try {
    const symbol = 'AAVEDAI.MF21'; // UNIDAI.MF21
    const type = 'LIMIT';
    const side = 'BUY';
    const amount = 2;
    const price = 21;

    // console.log(await exchange.fetchMarkets());
    // console.log(await exchange.fetchCurrencies());
    // console.log(await exchange.fetchTicker(symbol))
    // console.log(await exchange.createOrder(symbol, type, side, amount, price));

    // const orderId = 'V0002108884-0159145573';
    // const orderReference = 'ca22e9c9-1558-420e-ac9e-c2e9bf14da3d';

    // console.log(await exchange.fetchOrders(symbol));
    // console.log(await exchange.cancelOrder(orderId, symbol));
    // console.log(await exchange.fetchOrder(orderReference));
    // console.log(
    //   await exchange.amendOrder(orderId, symbol, {
    //     price: 190,
    //   })
    // );

    console.log(await exchange.fetchPositions(symbol));
  } catch (e) {
    console.error(e);
  }
})();
