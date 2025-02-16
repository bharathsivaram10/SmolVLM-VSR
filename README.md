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
cd SmolVLM-VSR
bash setup.sh
```

Sometimes, the Dropbox link used in the setup.sh file can fail due to too many downloads in that day. In that case go into the visual-spatial-reasoning/data directory
and follow the instructions to download COCO data and run the select_only_revlevant_images.py script. I suggest saving the images locally so you can skip the image download step in future.

If you have already downloaded the images and just want to get dependencies, run with the skip images option:

```bash
bash setup.sh --skip-images
```



You can now follow the along in the notebook!
