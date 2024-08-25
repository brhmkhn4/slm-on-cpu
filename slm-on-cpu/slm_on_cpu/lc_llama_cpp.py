
from langchain_community.llms import LlamaCpp
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from langchain_core.prompts import PromptTemplate

# Load the pretrained model
#homelapto
path= r"C:\Users\brhmk\Downloads\Phi-3-mini-4k-instruct-q4.gguf"
# path = r"C:\Users\brhmk\Downloads\Llama-3.1-8b-Uncensored-Dare.Q2_K.gguf"

# implementing langchain
template = """Question: {question}

Answer: Let's work this out in a step by step way to be sure we have the right answer."""

prompt = PromptTemplate.from_template(template)

# Callbacks support token-wise streaming
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

# Make sure the model path is correct for your system!
llm = LlamaCpp(
    model_path=path,
    temperature=0.75,
    max_tokens=2000,
    top_p=1,
    callback_manager=callback_manager,
    verbose=True,  # Verbose is required to pass to the callback manager
)

question = """
Question: A rap battle between Stephen Colbert and John Oliver
"""
llm.invoke(question)