<?php

$idx = $_GET['idx'];
$r = $_GET['r'];
$g = $_GET['g'];
$b = $_GET['b'];

shell_exec("sudo /usr/bin/python3 /home/denny0/LED_Project/effects/main.py control $idx $r $g $b");

?>
