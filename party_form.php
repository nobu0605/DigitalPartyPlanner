<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Party Planner Form</title>
</head>
<body>
    <h1>Party Planner</h1>
    <form action="party_form.php" method="get">
        <div>
            <?php
            $party_items = [
                0 => "Cake",
                1 => "Balloons",
                2 => "Music System",
                3 => "Lights",
                4 => "Catering Service",
                5 => "DJ",
                6 => "Photo Booth",
                7 => "Tables",
                8 => "Chairs",
                9 => "Drinks",
                10 => "Party Hats",
                11 => "Streamers",
                12 => "Invitation Cards",
                13 => "Party Games",
                14 => "Cleaning Service"
            ];

            if ($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_GET['indices'])) {
              $query_string = http_build_query(['indices' => $_GET['indices']]);
              $query_string = urldecode($query_string);
      
              $query_string = preg_replace('/indices\[\d+\]/', 'indices[]', $query_string);
             
              $output = shell_exec("python3 party_planner.py \"$query_string\"");
              if ($output) {
                  echo $output;
              } else {
                  echo "<h1>Error: Failed to execute Python script.</h1>";
              }
              exit;
            }

            foreach ($party_items as $index => $item) {
                echo '<label><input type="checkbox" name="indices[]" value="' . $index . '"> ' . $item . '</label><br>';
            }
            ?>
        </div>
        <br>
        <input type="submit" value="Plan My Party">
    </form>
</body>
</html>
