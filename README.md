# Introduction

This is based off [acheong08/BingImageCreator](https://github.com/acheong08/BingImageCreator), which allows you to use the Bing Image AI from your CLI / in python.

**This** project utilizes that package to read multiple prompts from a txt file and save the images to a folder.

You can also specifiy the number of batches (one batch = 4 images) to generate per prompt.

# Install dependencies

You have to install the requirements listed in `requirements.txt`.

For example, to do this in a virtual environment, run the following commands:

```bash
python3 -m virtualenv venv
pip install -r requirements.txt
```

# Set auth token

Next up, copy `.env.example` to `.env` and set your auth token (+ other settings if you want)

# Running the script

After putting your prompts in the prompts file (`prompts.txt` per default) with one prompt per line, run the following command:

```bash
python main.py
```
