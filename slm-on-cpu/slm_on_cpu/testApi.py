import requests

url = f"http://localhost:8080/completion"
prompt = "A virtual assistant answers questions from a user based on the provided text. USER: “I have no medical history worth mentioning except for child asthema” ASSISTANT: I have read this text.</s> USER: What describes medical history in the text? ASSISTANT: "

req_json = {
    "stream": False,
    "n_predict": 400,
    "temperature": 0,
    "stop": [
        "</s>",
    ],
    "repeat_last_n": 256,
    "repeat_penalty": 1,
    "top_k": 20,
    "top_p": 0.75,
    "tfs_z": 1,
    "typical_p": 1,
    "presence_penalty": 0,
    "frequency_penalty": 0,
    "mirostat": 0,
    "mirostat_tau": 5,
    "mirostat_eta": 0.1,
    "grammar": "",
    "n_probs": 0,
    "prompt": prompt
}

res = requests.post(url, json=req_json)
result = res.json()["content"]
print(result)