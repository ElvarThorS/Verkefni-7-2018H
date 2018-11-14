<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8" />
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>Page Title</title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" type="text/css" media="screen" href="/static/style.css" />
	<script src="main.js"></script>
</head>
<body>
	<h3>Nýskráningarform:</h3>
	<form method="POST" action="/donyskra" accept-charset="ISO-8859-1" id="ny">
		Notendanafn:<br>
		<input type="text" name="user" required><br>
		Lykilorð:<br>
		<input type="text" name="pass" required><br>
		Nafn:<br>
		<input type="text" name="nafn" required><br>
		<input type="submit" value="Nýskrá">
		<input type="reset" value="Hreinsa">
	</form>
	<hr>
	<h3>Innskráningarform:</h3>
	<form method="POST" action="/doinnskra" accept-charset="ISO-8859-1" id="inn">
		Notendanafn:<br>
		<input type="text" name="user" required><br>
		Lykilorð:<br>
		<input type="text" name="pass" required><br>
		<input type="submit" value="Innskrá">
	</form>
</body>
</html>