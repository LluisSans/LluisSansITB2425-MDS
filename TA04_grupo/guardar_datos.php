<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nombre = htmlspecialchars($_POST["name"]);
    $telefono = htmlspecialchars($_POST["tel"]);
    $correo = htmlspecialchars($_POST["mail"]);

    if (!empty($nombre) && !empty($telefono) && !empty($correo)) {
        $archivo = "datos.json";

        // Leer datos existentes en JSON
        $datosExistentes = file_exists($archivo) ? json_decode(file_get_contents($archivo), true) : [];

        // Agregar nuevos datos
        $datosExistentes[] = [
            "nombre" => $nombre,
            "telefono" => $telefono,
            "correo" => $correo
        ];

        // Guardar datos en el archivo JSON
        file_put_contents($archivo, json_encode($datosExistentes, JSON_PRETTY_PRINT));

        echo "Los datos han sido guardados correctamente en JSON.";
    } else {
        echo "Por favor, completa todos los campos.";
    }
} else {
    echo "Método no permitido.";
}
?>
