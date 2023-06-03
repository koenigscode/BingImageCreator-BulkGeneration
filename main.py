from dotenv import dotenv_values
from BingImageCreatorBulkGen import BingImageCreatorBulkGen
import subprocess


if __name__ == "__main__":
    env = dotenv_values('.env')

    bulk_gen = BingImageCreatorBulkGen(
        auth_cookie=env["AUTH_COOKIE"],
        prompts_file=env["PROMPTS_FILE"],
        output_dir=env["OUTPUT_DIR"],
        max_dir_length=env["MAX_DIR_LENGTH"],
        batches_per_prompt=int(env["BATCHES_PER_PROMPT"]),
        process_prompts=env["PROCESS_PROMPTS"].lower() == "true",
        append_style=env["APPEND_STYLE"] if env["APPEND_STYLE"] != "" and env["APPEND_STYLE"].lower() != "false" else None
    ) 
    bulk_gen.execute()

    if env["OPEN_PREVIEW_MACOS"].lower() == "true":
        command = ["open", "-a", "Preview", env["OUTPUT_DIR"]]
        subprocess.run(command)
