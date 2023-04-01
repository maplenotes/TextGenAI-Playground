import datetime
import json
from logging import getLogger
import torch
from transformers import T5Tokenizer, AutoModelForCausalLM

config = None
tokenizer = None
model = None

logger = getLogger("app.inference")


def initialize():
    global tokenizer, model, config
    logger.info("initialize model")
    start_time = datetime.datetime.now()

    with open("appconfig.json") as f:
        config = json.load(f)

    tokenizer = T5Tokenizer.from_pretrained(config.get("tokenizer"))
    model = AutoModelForCausalLM.from_pretrained(config.get("model"))

    if torch.cuda.is_available():
        model = model.to("cuda")
        logger.info("use cuda")
    
    elaplsed_time = (datetime.datetime.now() - start_time).total_seconds()
    logger.info(f"initialize model done, elapsed time: {elaplsed_time:.2f}sec")


def inference(prompt):
    start_time = datetime.datetime.now()
    input_ids = tokenizer.encode(prompt, return_tensors="pt", add_special_tokens=False).to("cuda")
    with torch.no_grad():
        output = model.generate(
            input_ids,
            min_length=20,
            max_length=150,
            do_sample=True,
            top_k=500,
            top_p=0.95,
            pad_token_id=tokenizer.pad_token_id,
            bos_token_id=tokenizer.bos_token_id,
            eos_token_id=tokenizer.eos_token_id,
            num_return_sequences=1
        )
    answer = tokenizer.batch_decode(output, skip_special_tokens=True)[0]

    elapsed_time = (datetime.datetime.now() - start_time).total_seconds()
    logger.info(f"elapsed: {elapsed_time:.2f}sec, input: {prompt}, output: {answer}")
    return answer
