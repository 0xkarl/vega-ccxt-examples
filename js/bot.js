const ccxt = require('../../ccxt/ccxt.js');

const e = new ccxt.vega({
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

    // console.log(await e.fetchMarkets());
    // console.log(await e.fetchCurrencies());
    // console.log(await e.fetchTicker(symbol))
    console.log(await e.createOrder(symbol, type, side, amount, price));

    // const orderId = 'V0002108884-0159145573';
    // const orderReference = 'ca22e9c9-1558-420e-ac9e-c2e9bf14da3d';

    // console.log(await e.fetchOrders(symbol));
    // console.log(await e.cancelOrder(orderId, symbol));
    // console.log(await e.fetchOrder(orderReference));
    // console.log(
    //   await e.amendOrder(orderId, symbol, {
    //     price: 190,
    //   })
    // );

    console.log(await e.fetchPositions(symbol));
  } catch (e) {
    console.error(e);
  }
})();
