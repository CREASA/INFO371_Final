import os
from openai import OpenAI
from tqdm import trange

os.environ['OPENAI_API_KEY']='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'
client = OpenAI()


for pad in trange(40):
  with open('original_locations/locations_pad_{}'.format(pad), 'r', encoding='UTF-8') as f:
    content = f.read()

  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "help user recognize the standard english country name of these locations, with each first letter is capitalized. "},
       {"role": "system","content": "If you can find no country match it, you can say 'NaN'. "},
      {"role": "system","content": "The output format is a key-value pair, both the key and the value are enclosed in single quotes. Such as 'leeds':'British', Adjacent key-value pairs are connected by commas, and don't output reference. Here are the locations"},
      {"role": "user", "content": content}
    ]
  )

  response_content = completion.choices[0].message.content
  print(response_content)

  with open('original_locations_json/locations_json_pad_{}.txt'.format(pad),'w', encoding='UTF-8') as f:
    f.write(response_content)