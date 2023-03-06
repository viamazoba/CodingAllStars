import openai

openai.api_key = 'Put your key here'
translate = openai.Completion.create(engine = "text-davinci-003", prompt = 'Traduce al Hindi: "Google Cloud 日本語版" ', max_tokens = 4000)
print(translate.choices[0].text)

