#!/bin/bash

# Detener el script si ocurre algún error
set -e

# Nombre de la carpeta del entorno virtual
ENV_DIR="Environment"

if [ -d "$ENV_DIR" ]; then
    
    echo "🗑️ Deleting virtual Environment..."
    rm -rf "$ENV_DIR"

fi

echo "📦 Crearting virtual Environment in '$ENV_DIR'..."

# Crear el entorno virtual

Python_version=$(python --version 2>&1)

if Python_version == Python 3.13.12; then
    
    echo "✅ Python 3.13.12 found: $(python --version)"

else
    
    echo "❌ Python 3.13.12 not found: $(python --version)"
    echo " ⬇️ Downgrading Now..."

    pyenv install 3.13.12
    pyenv global 3.13.12
    pyenv init - fish | source
    
    echo "✅ Python downgraded succesfully: $(python --version)"
    echo "If you dont have pyenv installed or configured, please install it and run 'pyenv install 3.13.12' and 'pyenv global 3.13.12' to downgrade your Python version to 3.13.12".

fi

python -m venv "$ENV_DIR"

echo "✅ Enviroment created successfully"

# Activar el entorno
echo "⚙️ Activate virtual Environment..."
source "$ENV_DIR/bin/activate"

# Actualizar pip (opcional pero recomendado)
pip install --upgrade pip

# Instalar dependencias
if [ -f Requirements.txt ]; then

    echo "📥 Intalling dependencies from Requirements.txt.."
    pip install -r Requirements.txt

else

    echo "⚠️ Not found Requirements.txt"

fi

echo "🎉 Enviroment Ready"
echo "👉 To active manually:"
echo "   source $ENV_DIR/bin/activate"