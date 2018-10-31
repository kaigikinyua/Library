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
      <ul class="nav nav-pills">
        <li><a href="index.html">Home</a></li>
        <li class="active"><a href="login.php">Login</a></li>
        <li><a href="signup.php">SignUp</a></li>
      </ul>
    </div>
    <div style="height:100px"></div>
    <center>
      <form method="POST" role="form" style="width:30%">
        <div class="form-group">
          <label for="contact">Contact</label>
          <input type="text" class="form-control" name="contact"/>
        </div>
        <div class="form-group">
          <label for="password">Password</label>
          <input type="password" class="form-control" name="password"/>
        </div>
        <button type="submit" name="submit" class="btn btn-info">
          Submit
        </button>
      </form>
    </center>
    <?php
      if(isset($_POST["submit"])){
        $contact=$_POST["contact"];
        $password=$_POST["password"];
        if(!empty($contact) and !empty($password)){
          $con=mysqli_connect("localhost","root","root","Library");
          $sql="SELECT name FROM users where contact='$contact' and password='$password'";
          $r=mysqli_query($con,$sql);
          if(mysqli_num_rows($r)==1){
            session_start();
            $n=mysqli_fetch_array($r);
            $user="user";$con="contact";
            setcookie($user,$n["name"],time()+(86400*30),"/");
            setcookie($con,$contact,time()+(86400*30),"/");
            header("location:user.php");
          }else{
            print "<center><p class='h4' style='color:red'><i>Wrong contact or password</i></p></center>";  
          }
        }
        else{
          print "<center><p class='h4' style='color:red'><i>Please Fill in all the Fields</i></p></center>";
        }
      }
    ?>
  </body>
</html>
