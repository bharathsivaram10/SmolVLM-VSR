#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Download checkpoint file and unzip
gdown https://drive.google.com/uc?id=1Q5tRkklwLLkqPGH_80VQwACBOUAKvWK1 -o checkpoint-480.zip

# Unzip file
unzip checkpoint-480.zip