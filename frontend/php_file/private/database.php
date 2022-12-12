<?php

define (DB_HOST, 'localhost');
define (DB_USER, 'root');
define (DB_PASS,  '');
define (DB_NAME, 'login_db');

$string = "mysql:host= localhost; dbname = login_db";
if(!$con = new PDO($string, DB_USER, DB_PASS))
{
	die("failed to connect!");
}
