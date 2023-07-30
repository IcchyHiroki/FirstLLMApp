import os
import openai

# 一般的には"OPENAI_API_KEY"とコード公開する時には変更する
# 外部流出の恐れを防ぐため
# assigning API KEY to initialize openai environment
openai.api_key = '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'

# function that takes in string argument as parameter
def comp(PROMPT, MaxToken=50, outputs=3):
    # using OpenAI's Completion module that helps execute 
    # any tasks involving text 
    response = openai.Completion.create(
        # model name used here is text-davinci-003
        # there are many other models available under the 
        # umbrella of GPT-3
        model="text-davinci-003",
        # passing the user input 
        prompt=PROMPT,
        # generated output can have "max_tokens" number of tokens 
        max_tokens=MaxToken,
        # number of outputs generated in one call
        n=outputs
    )
    # creating a list to store all the outputs
    output = list()
    for k in response['choices']:
        output.append(k['text'].strip())
    return output

PROMPT = """Write a story to inspire greatness, take the antagonist as a Rabbit and protagnist as turtle. 
Let antagonist and protagnist compete against each other for a common goal. 
Story should atmost have 3 lines."""
output = comp(PROMPT, MaxToken=3000, outputs=3)

print("output:¥n ", output)