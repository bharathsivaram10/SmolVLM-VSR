# SmolVLM-VSR
Finetuning SmolVLM for visual reasoning tasks

## Setup
```bash 
git clone https://github.com/bharathsivaram10/SmolVLM-VSR.git
```

This assumes you have an environment setup with common DL libraries such as pytorch, transformers, etc.
I ran this using an A100 on https://lambdalabs.com/. I don't recommend anything lower since the flash attention is optimized for Ampere+ GPUs (as far as I know)

Run the bash file to update some packages and also download the dataset repo + images

```bash
bash setup.sh
```

You can now follow the steps in the notebook!
