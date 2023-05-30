import os
import re
import time
from colorama import Fore, Style
from BingImageCreator import ImageGen
from dotenv import dotenv_values

def encode_filename(user_input: str) -> str:
    encoded = user_input.replace(" ", "-")
    encoded = re.sub(r'[<>:"/\\|?*,;]', '', encoded)
    encoded = encoded.lower()
    return encoded

def truncate_filename(filename: str, max_length: int) -> str:
    result = ""
    for name_chunk in filename.split("-"):
        if len(result + name_chunk) + 1 <= max_length:
            result = f"{result}-{name_chunk}"

    if(result == ""):
        result = filename[:max_length]

    return result.removeprefix("-")

env = dotenv_values('.env')

output_dir = env["OUTPUT_DIR"]
os.makedirs(output_dir, exist_ok=True)

generator = ImageGen(auth_cookie=env["AUTH_COOKIE"], quiet=True)

prompt_counter = 0

with open(env["PROMPTS_FILENAME"], 'r') as file:
    for prompt in file:
        prompt = prompt.strip()
        if(len(prompt) == 0):
            continue

        folder_name = truncate_filename(output_dir + "/" + encode_filename(prompt), max_length = int(env["MAX_DIR_LENGTH"]))
        os.makedirs(folder_name, exist_ok=True)
        print(f"{Fore.YELLOW}{prompt_counter+1}. {prompt.strip()}{Style.RESET_ALL}")

        for batch in range(int(env["BATCHES_PER_PROMPT"])):
            try:
                print(f"  → Batch #{batch+1} ...", end=" ")

                if batch == 0:
                    with open(f"{folder_name}/prompt-used.txt", "w") as file:
                        file.write(prompt.strip())

                image_urls = generator.get_images(prompt)
                generator.save_images(image_urls, folder_name)

                print(Fore.GREEN + "Done!" + Style.RESET_ALL)

                time.sleep(0.5)
            except Exception as e:
                print(f"{Fore.RED} {e.with_traceback} {Style.RESET_ALL}")
                time.sleep(3)
        
        print(f"{Fore.GREEN}✓ Prompt #{prompt_counter+1} complete! {Fore.LIGHTBLACK_EX}[{folder_name}]{Style.RESET_ALL}\n")
        prompt_counter += 1
        