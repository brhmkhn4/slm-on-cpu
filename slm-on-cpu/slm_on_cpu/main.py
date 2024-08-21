from llama_cpp import Llama
from ctransformers import AutoModelForCausalLM
from rich.console import Console
import time

# Load the pretrained model
path = r"C:\Users\brhmk\Downloads\Llama-3.1-8b-Uncensored-Dare.Q2_K.gguf"
# llm = Llama(model_path=path, verbose=True)
# start = time.time()

# chars = 0

# args = {
#     "prompts": "what is a large language model?",
#     "stream": True
# }
# for chunk in llm(**args):
#     Console.print(chunk, end="")
#     chars += len(chunk)
# end = time.time()
# Console.print(f"\n{'time taken:': < 12} {end-start: .2f} seconds", style="yellow")
# Console.print(f"{'Chars:' : <12} {chars/(end-start): .2f} / second",style="green")


# High-Level API
from llama_cpp import Llama
llm = Llama(model_path=path)

# Define the prompt for generating a reply
email_content = """
You are an email assistant. Review the following email and generate a formal and polite reply.

Original Email:
Dear Riaz,
Please find booking attached. Cargo will be ready on 31-07-2024.

Regards,
M. Kamran Akhtar
Usman Knitwear

Reply:
"""
output = llm(email_content, max_tokens=150,
    stop=[ "Q:"],
    echo=False,
    temperature=0.7,  # Controls creativity
    top_p=0.9 ) # Controls the diversity of the response echo=True)


{
  "id": "cmpl-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "object": "question_answers",
  "created": 1679561337,
  "model": path,
  "choices": [
    {
      "text": "Email_content: Dear Riaz,\n Please find booking attached. Cargo will be ready on 31-07-2024.\n\nRegards,\nM. Kamran Akhtar\nUsman Knitwear A: Dear Mr. Kamran\nThanks for your mail and for the new booking, we will check with concerns and will revert as soon as we get shipping approval for this shipment.\n\nBest Regards\nM.Ibrahim ",
      "index": 0,
      "logprobs": None,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 14,
    "completion_tokens": 28,
    "total_tokens": 42
  }
} # type: ignore

# Extract the generated text
generated_reply = output["choices"][0]["text"].strip() # type: ignore

# Print the generated reply
print("Generated Reply:\n", generated_reply)