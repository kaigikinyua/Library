<html>
  <head>
    <?php if(!empty($_COOKIE["user"])){
      echo "<title>".$_COOKIE["user"]."</title>";
    }else{
      header("location:index.html");
    }
    ?>
  <link rel="stylesheet" href="bootstrap/dist/css/bootstrap.css">
  <link rel="stylesheet" href="Css/mycss.css">
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
        <li class="active"><a href="user.php"><?php echo $_COOKIE["user"]?></a></li>
      </ul>
      </center>
    </div>
    <div style="height:15%"></div>
    <div class="row">
      <div class="col-sm-4">
        <!--history col-->
        <h4>Your History</h4>
        <?php
        ?>
        <table class="table table-striped table-hover" colspan="15px">
          <tr style="color:blue"><td>Book Name</td><td>Borrowed Date</td><td>Returned</td></tr>
          <?php
          $con=mysqli_connect("localhost","root","root","Library");
          if($con){
            $contact=$_COOKIE["contact"];
            $sql="SELECT * FROM BorrowedBooks where name='$contact'";
            $r=mysqli_query($con,$sql);
            while($values=mysqli_fetch_array($r)){
              if($values[3]==False){
                $bd=strtotime($values[2]);
                $n=strtotime("now");
                $an=(($n-$bd)/86400);
                echo $an;
                if($ans>0){
                  echo "<tr bgcolor='red'><td>".$values[1]."</td><td>".$values[2]."</td><td>".$values[3]."</td></tr>";
                }else{
                  echo "<tr bgcolor='red'><td>".$values[1]."</td><td>".$values[2]."</td><td>".$values[3]."</td></tr>";
                }
              }else{
                echo "<tr bgcolor='lightblue'><td>".$values[1]."</td><td>".$values[2]."</td><td>".$values[3]."</td></tr>";
              }
            }
          }else{
          #remove this before production
            echo mysqli_error($con);
          }
          ?>
        </table>
      </div>
      <div class="col-sm-6">
        <?php
        $con=mysqli_connect("localhost","root","root","Library");
        $sql="SELECT * FROM BorrowedBooks where state='False'";
        $r=mysqli_query($con,$sql);
        $row=10*mysqli_num_rows($r);
        echo "Books Not Retured : ".($row/10)."<div class='stats' style='width:".$row."'></div>";
        $sql="SELECT * FROM BorrowedBooks where state='True'";
        $r=mysqli_query($con,$sql);
        $row=10*mysqli_num_rows($r);
        echo "Books Returned : ".($row/10)."<div class='stats' style='width:".$row."'></div>";
        ?>
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
