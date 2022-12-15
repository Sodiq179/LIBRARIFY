<?php 

	require "../private/autoload.php";
	$Error = "";

	if($_SERVER['REQUEST_METHOD'] == "POST")
	{
		#something is being posted
		$email = $_POST['email'];
		if (!preg_match("/^[\w\-]+@[\w\-]+.[\w\-]+$/", $email))
		{
			$Error = "please enter a valid email or password";
		}

		$password = $_POST['password'];

		if ($Error = "")
		{
			
			$arr['password'] = $password;
			$arr['email'] = $email;

			$query = "select * from users where email = :email && password = :password limit 1";
			$stm = $con->prepare($query);
			$check = $stm->execute($arr );

			if ($check)
			{
				$user_data = $stm->fetchAll(PDO::FETCH_OBJ);
				if (is_array($user_data) && count($user_data) > 0)
				{
					$user_data = $user_data[0];
					$_SESSION['user_id'] = $user_data->user_id;
					$_SESSION['username'] = $user_data->username;
					header("Location: userPage.php");
					die;
				}
			}
		}
		$Error = "please enter a valid email or password";
	}
?>
