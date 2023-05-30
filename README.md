# Introduction

This script reads multiple prompts from a txt file and saves the images to a folder. It's useful for bulk-generating images with the Bing Image AI.

This is based off [acheong08/BingImageCreator](https://github.com/acheong08/BingImageCreator), which allows you to use the Bing Image AI from your CLI / in python.

**This** script, on the other hand, utilizies that library to mass-generate images, and you can also specifiy the number of batches (one batch = 4 images) to generate per prompt.

# Setup

## Install dependencies

(_Tested using Python 3.9.6 with venv on macOS_)

You have to install the requirements listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

_If you're not using a virtual environment (recommended), you should maybe use `pip3` instead of `pip`, if `pip3` is your python3 pip._

## Get auth token

Please refer to the [acheong08/BingImageCreator README](https://github.com/acheong08/BingImageCreator) to get your auth token.

## Set auth token

Next up, copy `.env.example` to `.env` and set your auth token (+ other settings if you want)

## Running the script

After putting your prompts in the prompts file (`prompts.txt` per default) with one prompt per line, run the following command:

```bash
python main.py
```

# Example

`prompts.txt`:

```text
A person sitting on a log, oil painting
A cat covered in oil
A dog sitting at the beach
```

I set the number of batches (in the .env) to 3, (4 images per batch), so I get 12 images per prompt.

Terminal output _(with pretty colors)_:
![Terminal Screenshot](readme-images/terminal-screenshot.png)
Generated images (+ folder structure):
![Finder Screenshot](readme-images/finder-screenshot.png)
