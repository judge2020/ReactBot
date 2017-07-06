<?php
if($_GET["key"] !== "KEY")
    die(404);
$newurl = $_GET["url"];
$file = fopen('cards.txt', 'a');
fwrite($file, $newurl."\n")
?>