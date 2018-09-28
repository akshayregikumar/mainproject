<?php 
error_reporting(0);
$db_name = "project2";
$mysql_user = "root";
$mysql_pass = "";
$server_name = "localhost:3307";

$con = mysqli_connect($server_name, $mysql_user, $mysql_pass, $db_name);

if(!$con){
	echo '{"message":"Unable to connect to the database."}';
}
else
{


$date1 = $_POST["name"];


//$password = $_POST["password"];
//$date1='2018-03-22';
/*$sql = "update data2 set block=".$date2."00:00:00 where id=13";
 mysql_query($sql);
*/
$y=00;
$i=1;
$response = array();
while($y<24)
{
//$sql = "SELECT * FROM `data2`  WHERE `date_im`= '".$name."' ; 
//echo "SELECT sum(power) from data2 WHERE date_in BETWEEN '".$date1." ".$y.":00:00' and '".$date1." ".$y.":59:59'";
$sql="SELECT avg(power) from data2 WHERE date_in BETWEEN '".$date1." ".$y.":00:00' and '".$date1." ".$y.":59:59'";
//sql = "SELECT * FROM `data2`  " ; 
$result = mysqli_query($con, $sql);


/*
$response = array();
$i=1;
while($row = mysqli_fetch_array($result)){
echo $row[2]." ";
	$response[$i]=array(status=>$row[2]);
$i++; 
}*/

$y++;

$response[$i]="0";
if(!$result)
{
}
else
{
while($row = mysqli_fetch_array($result))
{
	if($row[0]!=null)
	{
	$response[$i]=$row[0];//device ststus 
	}



}
//$i2=array();
//$i2=array("i"=>$i);
//echo json_encode($response);

}
$i++;
}
$response[$i]=$date1;//device ststus 
$i++;
echo json_encode(array("user_data"=>$response));
}


?>
