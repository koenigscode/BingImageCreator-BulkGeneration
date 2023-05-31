from dotenv import dotenv_values
from BingImageCreatorBulkGen import BingImageCreatorBulkGen

if __name__ == "__main__":
    env = dotenv_values('.env')

    bulk_gen = BingImageCreatorBulkGen(auth_cookie=env["AUTH_COOKIE"], prompts_file=env["PROMPTS_FILE"], output_dir=env["OUTPUT_DIR"], max_dir_length=env["MAX_DIR_LENGTH"], batches_per_prompt=env["BATCHES_PER_PROMPT"])
    bulk_gen.execute()