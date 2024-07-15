# This code is for v1 of the openai package: pypi.org/project/openai
import os
import openai
from config import apikey

openai.api_key=apikey

response = openai.Completion.create(
  model="gpt-3.5-turbo-instruct",
  prompt="prompt",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)



# Completion(id='cmpl-8UI5psliqxxWsLxDJKpoMVBkHLbRE', choices=[CompletionChoice(finish_reason='length', index=0, logprobs=None, text='\nSubject: Notice of Resignation\n\nDear [Boss’s Name],\n\nI hope this email finds you well. I am writing to inform you that I have decided to resign from my position at [Company Name]. After much consideration and thought, I have come to the difficult decision to move on from [Company Name].\n\nPlease consider this email as an official two weeks’ notice of my resignation. My last day of work will be [Date]. I will do my best to complete all my pending tasks and ensure a smooth transition for my successor during this time.\n\nI am grateful for the opportunities and support that I have received during my time at [Company Name]. I have learned a great deal, both professionally and personally, and I will always be thankful for the experiences and memories I have gained here.\n\nI assure you that I will assist in any way I can to make the transition process as easy as possible for my team and the company. Please let me know if there is anything specific you would like me to focus on during this period.\n\nI am proud to have been a part of [Company Name] and have enjoyed working with such an amazing team. I will miss everyone and wish the company continued success in the future.\n\nThank you again for the support and guidance you have provided')], created=1702230081, model='gpt-3.5-turbo-instruct', object='text_completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=256, prompt_tokens=9, total_tokens=265))  
