<html>
  <head>
    <title>Library</title>
    <link rel="stylesheet" href="bootstrap/dist/css/bootstrap.css">
  </head>
  <body>
    <div class="navbar navbar-default navbar-fixed-top">
      <div class="navbar-header">
          <center><h4>Library</h4></center>
      </div>
      <center>
      <ul class="nav nav-pills">
        <li><a href="index.html">Home</a></li>
        <li><a href="login.php">Login</a></li>
        <li class="active"><a href="signup.php">SignUp</a></li>
      </ul>
    </center>
    </div>
    <div style="height:100px"></div>
    <center>
      <form method="POST" role="form" style="width:30%">
        <div class="form-group">
          <label for="username">Username</label>
          <input type="text" class="form-control" name="username"/>
        </div>
        <div class="form-group">
          <label for="contact">Email or Phone Number</label>
          <input type="text" name="contact" class="form-control"/>
        </div>
        <div class="form-group">
          <label for="password">Password</label>
          <input type="password" class="form-control" name="password"/>
        </div>
        <div class="form-group">
          <label for="passwordc">Confirm Password</label>
          <input type="password" class="form-control" name="passwordc"/>
        </div>
        <button type="submit" name="submit" class="btn btn-info">Submit</button>
      </form>
    </center>
    <?php
    if(isset($_POST["submit"])){
      $uname=$_POST["username"];
      $password=$_POST["password"];
      $passwordc=$_POST["passwordc"];
      $contact=$_POST["contact"];
      if(!empty($uname) and !empty($password) and !empty($passwordc) and !empty($contact)){
        $con=mysqli_connect("localhost","root","root","Library");
        $sql="SELECT * FROM users where contact='$contact'";
        $r=mysqli_query($con,$sql);
        if(mysqli_num_rows($r)==0){
          if($password==$passwordc){
            $sql1="INSERT into users(name,contact,password,account) VALUES('$uname','$contact',$password,1000)";
            $r1=mysqli_query($con,$sql1);
            if($r1){
              header("location:login.php");
            }else{
              print "<center><p class='h4' style='color:red'><i>Error while adding user please try again later</i></p></center>";
            }
          }else{
            print "<center><p class='h4' style='color:red'><i>Passwords do not match</i></p></center>";
          }
        }
        else{
          print "<center><p class='h4' style='color:red'><i>The contact is already registered in this site<br/></i></p></center>";
        }
      }else{
        print "<center><p class='h4' style='color:red'><i>Please Fill in all the Fields</i></p></center>";
      }
    }
    ?>
  </body>
</html>
