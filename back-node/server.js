// server.js
const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");

const app = express();
const port = 4000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Lista para almacenar los eventos registrados
let eventosRegistrados = [];

// Ruta para registrar un nuevo evento
app.post("/registerEvent", (req, res) => {
  const { nombre, importancia, duracion, descripcion, fecha } = req.body;
  console.log("Importancia recibida:", importancia);

  // Crear un nuevo evento
  const nuevoEvento = {
    nombre,
    importancia,
    duracion,
    descripcion,
    fecha,
  };

  // Agregar el evento a la lista de eventos registrados
  eventosRegistrados.push(nuevoEvento);

  // Responder con el evento registrado
  res.status(201).json(nuevoEvento);
});

// Ruta para obtener todos los eventos registrados
app.get("/events", (req, res) => {
  res.json(eventosRegistrados);
});

// Iniciar el servidor
app.listen(port, () => {
  console.log(`Servidor corriendo en http://localhost:${port}`);
});
