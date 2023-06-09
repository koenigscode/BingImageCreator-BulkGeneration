import os
import re
import time
from colorama.ansi import Fore, Style, AnsiFore, AnsiBack
from BingImageCreator import ImageGen
from dotenv import dotenv_values


class BingImageCreatorBulkGen(ImageGen):
    def __init__(
        self,
        auth_cookie: str,
        prompts_file: str,
        output_dir: str,
        max_dir_length: int,
        batches_per_prompt: int,
        process_prompts: bool = False,
        append_style: bool = False
    ) -> None:
        super().__init__(auth_cookie=auth_cookie, quiet=True)
        self.prompts_file = prompts_file
        self.output_dir = output_dir
        self.max_dir_length = max_dir_length
        self.batches_per_prompt = batches_per_prompt
        self.process_prompts = process_prompts
        self.append_style = append_style

        self.prompts = self.prompts_from_file(prompts_file)

    def prompts_from_file(self, prompts_file: str) -> list:
        with open(prompts_file, 'r') as file:
            if self.process_prompts:
                processed = [re.sub(r'^\s*\d+\.\s*|\.\s*$', '', prompt).strip() for prompt in file if(len(prompt.strip()) > 0)]
                
                if self.append_style is not None:
                    processed = [f"{prompt}, {self.append_style}" for prompt in processed]
                
                return processed

            return [prompt.strip() for prompt in file if len(prompt.strip()) > 0]
        


    def execute(self):
        self.log(
            f'[ Using prompt file "{self.prompts_file}" with {self.batches_per_prompt} {"batches" if self.batches_per_prompt > 1 else "batch"} per prompt ]\n',
                 foreground=Fore.LIGHTBLACK_EX)

        prompt_counter = 0

        for prompt in self.prompts:
            folder_name = self.truncate_filename(self.output_dir + "/" + self.encode_filename(prompt), max_length = int(self.max_dir_length))
            os.makedirs(folder_name, exist_ok=True)
            self.log(f"[{prompt_counter+1}/{len(self.prompts)}] ", foreground=Fore.LIGHTBLACK_EX, end="")
            self.log(prompt.strip(), foreground=Fore.YELLOW)

            for batch in range(self.batches_per_prompt):
                try:
                    self.log(f"  → Batch {batch+1}/{self.batches_per_prompt} ...", end=" ", flush=True)

                    if batch == 0:
                        with open(f"{folder_name}/prompt-used.txt", "w") as file:
                            file.write(prompt.strip())

                    image_urls = self.get_images(prompt)
                    self.save_images(image_urls, folder_name)

                    self.log("Done!", foreground=Fore.GREEN)

                    time.sleep(0.5)
                except Exception as e:
                    self.log(e, foreground=Fore.RED)
                    time.sleep(3)
            
            self.log(f"✓ Prompt completed!", foreground=Fore.GREEN, end=" ")
            self.log(f"[ {folder_name} ]\n", foreground=Fore.LIGHTBLACK_EX)
            prompt_counter += 1


    @staticmethod
    def encode_filename(user_input: str) -> str:
        encoded = user_input.replace(" ", "-")
        encoded = re.sub(r'[<>:"/\\|?*,;]', '', encoded)
        encoded = encoded.lower()
        return encoded

    @staticmethod
    def truncate_filename(filename: str, max_length: int) -> str:
        result = ""
        for name_chunk in filename.split("-"):
            if len(result + name_chunk) + 1 <= max_length:
                result = f"{result}-{name_chunk}"

        if(result == ""):
            result = filename[:max_length]

        return result.removeprefix("-")

    @staticmethod
    def log(msg: str, foreground: AnsiFore = "", background: AnsiBack = "", **kwargs):
        print(f"{foreground}{background}{msg}{Style.RESET_ALL}", **kwargs)