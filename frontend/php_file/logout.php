<?php
require "../private/autoload.php";

if(isset($_SESSION['user_id']))
{
	unset($_SESSION['user_id']);

}

if(isset($_SESSION['username']))
{
	unset($_SESSION['username']);

}

header("Location: login.php");
die;