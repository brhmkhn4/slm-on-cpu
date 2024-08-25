# llama cpp installation
llama.cpp runs quantized LLMs in GGUF format on CPUs. It has many modules, in this project we need a server of llama.cpp to run LLM on our PC.
# Requirements and Installation:
1. clone llama.cpp repo https://github.com/ggerganov/llama.cpp.git
if any error occured during cloning then download the repo in zip format from github, download link https://github.com/ggerganov/llama.cpp/archive/refs/heads/master.zip extract the llama.cpp-master file on your local storage.
2. Download the latest fortran version of w64devkit https://github.com/skeeto/w64devkit/releases. or Download from link https://github.com/skeeto/w64devkit/releases/download/v2.0.0/w64devkit-x64-2.0.0.exe
Extract w64devkit on your pc.
Inside w64devkit folder find w64devkit and run this as administrator, it will open a terminal, in the terminal cd to the llama.cpp folder.
From llama.cpp folder you can run 
```
make llama-server
``` 
and it will build the server under the llama.cpp folder.
Details instructions can be found at https://github.com/ggerganov/llama.cpp/tree/master/examples/server
# Basic usage:
1. Download any LLM model in GGUF format onto your local drive, for now you can download from link https://huggingface.co/yh-yao/Phi-3-mini-4k-instruct-Q4_K_S-GGUF/resolve/main/phi-3-mini-4k-instruct-q4_k_s.gguf?download=true
2. Open terminal / CMD in llama.cpp foloder and run the following command
``` 
llama-server -m path/to/your/model/ -c 1024 
``` 
Change path with path where you have downloaded the model such as 
``` 
llama-server -m C:\Users\brhmk\Downloads\Phi-3-mini-4k-instruct-q4.gguf -c 1024 
``` 
-c flage is for setting tokens, in our case we have set 1024.
The above command will start a server that by default listens on 127.0.0.1:8080 or localhost:8080 until the terminal is open. You can consume the endpoints with Postman or NodeJS with axios library. You can visit the web front end at the same url.

# for llama-cpp-python installation run the following command in CMD
```cmd
pip install llama-cpp-python  --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu
```
You can also download pre built wheel from below url and paste path where the wheel is downloaded
https://abetlen.github.io/llama-cpp-python/whl/cpu/llama-cpp-python
```cmd
pip install llama-cpp-python --wheel-dir=C:\Users\brhmk\Downloads llama_cpp_python-0.2.89-cp312-cp312-win_amd64
```