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
bash setup_training.sh
```

Sometimes, the Dropbox link used in the setup.sh file can fail due to too many downloads in that day. In that case go into the visual-spatial-reasoning/data directory
and follow the instructions to download COCO data and run the select_only_revlevant_images.py script. I suggest saving the images locally so you can skip the image download step in future.

If you have already downloaded the images and just want to get dependencies, run with the skip images option:

```bash
bash setup_training.sh --skip-images
```

You can now follow the along in the notebook!

If you don't want to train and just want to try out the fine-tuned model locally, you can used the following bash and app commands. Note that you do need a GPU to run locally, but most consumer GPUs should work:

```bash
bash setup_app.sh
```

```bash
python app.py
```

# Results

Here's a comparison of outputs form base and fine-tuned model. Although it was trained on True/False queries, the fine-tuned model allows for more descriptive spatial relations:

![Base Model output](assets/images/base_output.png "Base Model output")

![Fine-tuned Model output](assets/images/fine-tuned_output.png "Fine-tuned Model output")

