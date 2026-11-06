<?php
$host = getenv('DB_HOST') ?: 'db';
$user = getenv('DB_USER') ?: 'root';
$pass = getenv('DB_PASS') ?: 'root';
$db   = getenv('DB_NAME') ?: 'empresa';

$conn = new mysqli($host, $user, $pass, $db);

if ($conn->connect_error) {
    die("Erro de conexão com o banco de dados");
}

$result = $conn->query("SELECT nome FROM funcionarios");

echo "<h1>Lista de Funcionários</h1>";

while ($row = $result->fetch_assoc()) {
    echo "<p>" . htmlspecialchars($row['nome']) . "</p>";
}
?>
