<?php 

	require "../private/autoload.php";
	$Error = "";
	$email = "";
	$username = "";

	if($_SERVER['REQUEST_METHOD'] == "POST")
	{
		#something is being posted
		$email = $_POST['email'];
		if (!preg_match("/^[\w\-0-9]+@[\w\]+.[\w\]+$/", $email))
		{
			$Error = "please enter a valid email or password";
		}

		$date = date("Y-m-d H:i:s");
		$user_id = get_random_string(62);

		$username = trim($_POST['username']);
		if (!preg_match("/^[a-zA-Z]+$/", $username))
		{
			$Error = "please enter a valid email or password";
		}

		$username = esc($username);
		$password = esc($_POST['password']);
		
		#if email exist
		$arr = false;
		$arr['email'] = $email;

		$query = "select * from users where email = :email limit 1";
			$stm = $con->prepare($query);
			$check = $stmst = execute($arr );

			if ($check)
			{
				$user_data = $stm->fetchAll(PDO::FETCH_OBJ);
				if (is_array($user_data) && count($user_data) > 0)
				{
					$Error = "email alreadyin in use";
				}
			}

		if ($Error === "")
		{
			$arr['user_id'] = $user_id;
			$arr['date'] = $date;
			$arr['username'] = $username;
			$arr['password'] = $password;
			$arr['email'] = $email;

			$query = "insert into users (user_id, username, email, password, date) values(:user_id, :username, :email, :password, :date)";
			$stm = $con->prepare($query);
			$stmst = execute($arr );
		
			header("Location: login.php");
		}
	}
?>
