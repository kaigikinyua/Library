<html>
  <head>
    <title>username</title>
    <link rel="stylesheet" href="bootstrap/dist/css/bootstrap.css">
  </head>
  <body>
  	<div class="navbar navbar-default navbar-fixed-top">
  		<div class="navbar-header">
  			<!--username or userprofile-->
  			Library
  		</div>
  		<center>
  		<ul class="nav nav-pills">
  			<li><a href="index.html">Home</a></li>
  			<li class="active"><a href="user.php">Userpage</a></li>
  		</ul>
  	</center>
  	</div>
  	<div style="height:15%"></div>
  	<div class="row">
  		<div class="col-sm-4">
  			<!--history col-->
  			<h4>Your History</h4>
  		</div>
  		<div class="col-sm-6">
  			<!--Books col-->
  			<h4>Available Books</h4>
  			<table class="table-striped table-hover">
  				<tr style="color:blue"><td>Book Name</td><td>Author</td><td>Category</td></tr>
  				<?php
  				$con=mysqli_connect("localhost","root","root","Library");
  				if($con){
  					$sql="SELECT * FROM Inventory where CopiesAvailable>1";
  					$r=mysqli_query($con,$sql);
  					while($r1=mysqli_fetch_array($r))
  					{
  						echo"<tr><td>".$r1[1]."</td><td>".$r1[2]."</td><td>".$r1[3]."</td></tr>";
  					}
  				}
  				?>
  			</table>
  		</div>
  	</div>
  </body>
</html>
