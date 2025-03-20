<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Request Assets</title>
    <link rel="stylesheet" href="../dashboard.css">

</head>
<body>
    <!-- sidebar -->
    <div class="sidebar">
        <div class="logo"></div>
        <ul class="menu">
            <li>
                <a href="" >
                    <i class="fa-solid fa-user"></i><span>Dashboard</span>
                </a>
            </li>
            <li>
                <a href="">
                    <i class="fa-solid fa-bars-progress"></i><span>Requests</span>
                </a>
            </li>
            <li>
                <a href="">
                    <i class="fa-solid fa-list-check"></i><span>Assigned Assets</span>
                </a>
            </li>
            <li class="logout">
                <a href="">
                    <i class="fa-solid fa-arrow-right-from-bracket"></i><span>Log Out</span>
                </a>
            </li>
        </ul>
    </div>

    <section >
        <h1>Asset Request List</h1>
    
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Employee Name</th>
                <th>Asset Type</th>
                <th>Status</th>
                <th>Request Date</th>
            </tr>
        </thead>
        <tbody>
            <?php
            if ($result->num_rows > 0) {
                while ($row = $result->fetch_assoc()) {
                    echo "<tr>
                        <td>{$row['id']}</td>
                        <td>{$row['employee_name']}</td>
                        <td>{$row['asset_type']}</td>
                        <td class='{$row['status']}'>{$row['status']}</td>
                        <td>{$row['request_date']}</td>
                    </tr>";
                }
            } else {
                echo "<tr><td colspan='5'>No requests found</td></tr>";
            }
            ?>
        </tbody>
    </table>

    </section>
</body>
</html>