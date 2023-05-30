# Introduction

This is based off [acheong08/BingImageCreator](https://github.com/acheong08/BingImageCreator), which allows you to use the Bing Image AI from your CLI / in python.

**This** project utilizes that package to read multiple prompts from a txt file and save the images to a folder.

You can also specifiy the number of batches (one batch = 4 images) to generate per prompt.

# Setup

## Install dependencies

(_Tested using Python 3.9.6_)

You have to install the requirements listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

_If you're not using a virtual environment (recommended), you should maybe use `pip3` instead of `pip`, if `pip3` is your python3 pip._

## Get auth token

Please refer to [acheong08/BingImageCreator](https://github.com/acheong08/BingImageCreator) to get your auth token.

## Set auth token

Next up, copy `.env.example` to `.env` and set your auth token (+ other settings if you want)

## Running the script

After putting your prompts in the prompts file (`prompts.txt` per default) with one prompt per line, run the following command:

```bash
python main.py
```
