<html>
  <head>
    <?php if(!empty($_COOKIE["user"])){
      echo "<title>".$_COOKIE["user"]."</title>";
    }else{
      header("location:index.html");
    }
    ?>
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
        <table class="table-striped table-hover">
          <tr style="color:blue"><td>Book Name  .</td><td>Borrowed Date  .</td><td>Retured</td></tr>
          <?php
              $con=mysqli_connect("localhost","root","root","Library");
            $name=$_COOKIE["contact"];
            $sql="SELECT * FROM BorrowedBooks WHERE name='$name'";
            $r=mysqli_query($con,$sql);
            while($r1=mysqli_fetch_array($r)){
            #book index,user contact,date,retured state
            $history=array($r1[0],$r1[1],$r1[2],$r1[3]);
            }
            $i=0;
            if(!empty($history)){
              foreach($history as $values){
                if($i%4==0){
                  $bookname="SELECT bookname from Inventory where id='$values'";
                  $r=mysqli_query($con,$bookname);
                  while($ans=mysqli_fetch_array($r)){
                      $bname=$ans[0];
                  }
                }
                else if($i%4==2){
                  $date="SELECT dateborrowed from BorrowedBooks where name='$name'";
                  $d=mysqli_query($con,$date);
                  while($r=mysqli_fetch_array($d)){
                    $da=$r[0];
                  }
                  $dt=strtotime("now");
                  $bd=strtotime($da);
                  $an=($dt-$bd)/86400;
                  
                  if($an>14){
                    echo "<tr bgcolor='#FF407E'><td>".$bname."</td><td>".$da."</td></tr>";
                  }else{
                    echo "<tr bgcolor='#499DFF'><td>".$bname."</td><td>".$da."</td></tr>";
                  }
                }
                else{}
                $i+=1;
              }
            }
          ?>
        </table>
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
