#!/bin/bash

# Detener el script si ocurre algún error
set -e

# Nombre de la carpeta del entorno virtual
ENV_DIR="Environment"

echo "📦 Creando entorno virtual en '$ENV_DIR'..."

# Crear el entorno virtual
python -m venv "$ENV_DIR"

echo "✅ Entorno creado"

# Activar el entorno
echo "⚙️ Activando entorno virtual..."
source "$ENV_DIR/bin/activate"

# Actualizar pip (opcional pero recomendado)
pip install --upgrade pip

# Instalar dependencias
if [ -f Requirements.txt ]; then
    echo "📥 Instalando dependencias..."
    pip install -r Requirements.txt
else
    echo "⚠️ No se encontró Requirements.txt"
fi

echo "🎉 Entorno listo"
echo "👉 Para activarlo manualmente ejecuta:"
echo "   source $ENV_DIR/bin/activate"