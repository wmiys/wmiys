<?php


$shit = $_SERVER;

ksort($shit);

echo '<pre>';
echo json_encode($shit, JSON_PRETTY_PRINT + JSON_UNESCAPED_SLASHES + JSON_UNESCAPED_UNICODE + JSON_NUMERIC_CHECK + JSON_UNESCAPED_LINE_TERMINATORS);
// echo json_encode($_POST, JSON_PRETTY_PRINT + JSON_UNESCAPED_SLASHES + JSON_UNESCAPED_UNICODE + JSON_NUMERIC_CHECK);
echo '</pre>';
?>