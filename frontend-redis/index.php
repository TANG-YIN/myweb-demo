<?php
require 'vendor/autoload.php'; // 引入composer的自动加载文件

use Predis\Client;

//初始化Redis连接配置
$redisHost = getenv('REDIS_HOST') ?: '127.0.0.1';
$redisPort = getenv('REDIS_PORT') ?: 6379;

$client = new Client([
    'scheme' => 'tcp',
    'host' => $redisHost,
    'port' => $redisPort,
]);

header('Content-Type: application/json');

//处理GET请求
$cmd = $_GET['cmd'] ?? '';

if ($cmd === 'set' && isset($_GET['key'], $_GET['value'])) {
    $client->set($_GET['key'], $_GET['value']);
    echo json_encode(['message' => 'Updated']);
} elseif ($cmd === 'get' && isset($_GET['key'])) {
    $value = $client->get($_GET['key']);
    echo json_encode(['data' => $value]);
} else {
    echo json_encode(['error' => 'Invalid command']);
}