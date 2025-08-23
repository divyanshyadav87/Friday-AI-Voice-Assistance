import google.generativeai as genai

# Paste your API key here
genai.configure(api_key="AIzaSyAFWY3spl5n_k1ASXqmEKXVR82LLr2mWv4")

model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content("capital of india")
print(response.text)
