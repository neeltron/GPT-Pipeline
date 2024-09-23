# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 21:48:09 2024

@author: CAR Lab
"""

import openai
import matlab.engine

eng = matlab.engine.connect_matlab()

openai.api_key = 'API_KEY_HERE'
messages = [ {"role": "system", "content": 
              "Just a test."} ]
while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.chat.completions.create(
            model="gpt-4o", messages=messages
        )
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
    eng.workspace['matlab_var'] = reply
    
eng.quit()
    
