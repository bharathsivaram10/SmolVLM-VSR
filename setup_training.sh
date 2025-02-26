#!/bin/bash

# Parse command-line arguments
SKIP_IMAGES=false

while [[ "$#" -gt 0 ]]; do
    case $1 in
        --skip-images) SKIP_IMAGES=true ;;
        *) echo "Unknown parameter: $1"; exit 1 ;;
    esac
    shift
done

# Upgrade Jupyter and IPython
pip install --upgrade jupyter
pip install --upgrade jinja2

# Install required Python packages
pip install bitsandbytes tf-keras datasets transformers peft

# Install Flash Attention
pip install flash-attn --no-build-isolation

# Clone the Visual Spatial Reasoning dataset repository
git clone https://github.com/cambridgeltl/visual-spatial-reasoning.git

# Conditionally download and extract images
if [ "$SKIP_IMAGES" = false ]; then
    echo "Downloading dataset..."
    wget -O vsr_images.zip "https://www.dropbox.com/scl/fi/efvlqxp4zhxfp60m1hujd/vsr_images.zip?rlkey=3w3d8dxbt7xgq64pyh7zosnzm&e=1&dl=0"
    unzip vsr_images.zip -d visual-spatial-reasoning/
else
    echo "Skipping dataset download"
fi

unzip checkpoint-480.zip
