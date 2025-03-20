<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php 
        $host = "localhost";
        $dbname = "grp22_assets_mgt_sys";
        $username = "root";
        $password = "";

        $conn = new mysqli($host, $dbname, $username, $password);
        
        if ($conn->connect_error){
            die("Connection failed: " . $conn->connect_error);
        }
    ?>
</body>
</html>