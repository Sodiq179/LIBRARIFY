<?php

function check_login($con)
{

	if(isset($_SESSION['user_id']))
	{

		$arr['user_id'] = $_SESSION['user_id'];
		$query = "select * from users where user_id = ':user_id' limit 1";

		$stm = $con->prepare($query);
		$check = $stmt->execute($arr);
		if($check)
		{

			$user_data = $stm->fetchAll(PDO::FETCH_OBJ);
			if(is_array($user_data) && count($user_data) > 0)
			{
				$user_data = $user_data[0];
				$_SESSION['username'] = $user_data->username;
				$_SESSION['user_id'] = $user_data->user_id;
				return $user_data[0];
			}
			
		}
	}

	//redirect to login
	header("Location: signin-signup.php");
	die;

}

//function to escape characters
function esc($word)
{
	return addslashes($word);
}

function get_random_string($length)
{

	$array = array(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'N', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z');
	$text = "";
	$len = rand(4, $length);

	for ($i = 0; $i < $len; $i++)
	{
		$random = rand(0, $length);
		$text .= $array[$random];
	}

	return $text;
}
