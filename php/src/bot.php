<?php

include './../../ccxt/ccxt.php';

$exchange = new \ccxt\vega (array (
    'enableRateLimit' => true,
    // 'verbose' => true, // uncomment for verbose output
));

// fetch markets
$markets = $exchange->fetch_markets();
var_dump ($markets);

echo "\n";

?>