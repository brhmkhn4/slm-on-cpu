import os

#loading Phi-3 model
# cmd = os.system('cmd /k "dir cd "C:/Users/brhmk/Downloads/llama.cpp-server/llama-server.exe"')

# print(cmd)

path = "C:/Users/brhmk/Downloads/llama.cpp-server/"
os.chdir(path)
os.system("llama-server.exe -m C:/Users/brhmk/Downloads/Phi-3.5-mini-instruct_Uncensored-IQ3_XS.gguf -c 1024")