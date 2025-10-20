from ollama import chat

while True:
    inp = input("\n> ")
    
    stream = chat(
        model='gemma3:270m',
        messages=[{'role': 'user', 'content': inp}],
        stream=True,
    )

    for chunk in stream:
         print(chunk['message']['content'], end='', flush=True)
    
