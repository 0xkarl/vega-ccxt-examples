<?php
require './vendor/autoload.php';
include './../../ccxt/ccxt.php';
$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();

$exchange = new \ccxt\vega (array (
    'apiKey' => $_ENV['WALLET_KEY'],
    'secret' => $_ENV['WALLET_TOKEN'],
));

$symbol = 'AAVEDAI.MF21'; // UNIDAI.MF21
$type = 'LIMIT';
$side = 'BUY';
$amount = 2;
$price = 21;

// var_dump(exchange->fetch_markets());
// var_dump(exchange->fetch_currencies());
// var_dump(exchange->fetch_ticker(symbol))
// var_dump(exchange->create_order(symbol, type, side, amount, price));

// $orderId = 'V0002108884-0159145573';
// $orderReference = 'ca22e9c9-1558-420e-ac9e-c2e9bf14da3d';

// var_dump(exchange->fetch_orders(symbol));
// var_dump(exchange->cancel_order(orderId, symbol));
// var_dump(exchange->fetch_order(orderReference));
// console.log(
//   await e.amendOrder($orderId, $symbol, {
//     price: 190,
//   })
// );

var_dump($exchange->fetch_positions($symbol));
echo "\n";

?>