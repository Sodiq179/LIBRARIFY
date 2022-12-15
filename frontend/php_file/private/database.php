<?php

define ('DB_HOST', 'localhost');
define ('DB_USER', 'LIBRARIFY');
define ('DB_PASS',  'root');
define ('DB_NAME', 'LIBRARIFY');

$string = "mysql:host=".DB_HOST.";dbname=".DB_NAME;
if(!$con = new PDO($string, DB_USER, DB_PASS))
{
	die("failed to connect!");
}
