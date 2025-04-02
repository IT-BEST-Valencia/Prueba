const express = require('express');
const path = require('path');
const app = express();

 Servir archivos estáticos desde el directorio actual
app.use(express.static(__dirname));

 Ruta para servir index.html
app.get('', (req, res) = {
  res.sendFile(path.join(__dirname, 'index.html'));
});

 Iniciar el servidor en el puerto definido por Azure o 3000
const port = process.env.PORT  3000;
app.listen(port, () = {
  console.log(`Servidor corriendo en el puerto ${port}`);
});
