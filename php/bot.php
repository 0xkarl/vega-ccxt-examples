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

// var_dump($exchange->fetch_markets());
// var_dump($exchange->fetch_currencies());
// var_dump($exchange->fetch_ticker($symbol));
// var_dump($exchange->create_order($symbol, $type, $side, $amount, $price));

$order_id = 'V0000778737-0023749213';
$order_reference = '1cafda1b-8ebd-41d8-ab1c-34a2258d00b0';

var_dump($exchange->fetch_orders($symbol));
// var_dump($exchange->cancel_order($order_id, $symbol));
// var_dump($exchange->fetch_order($order_reference));
// var_dump(
//   $exchange->amendOrder($order_id, $symbol, {
//     'price' => 190,
//   })
// );

// var_dump($exchange->fetch_positions($symbol));
echo "\n";

?>