#libraries
from dotenv import find_dotenv,load_dotenv
from transformers import pipeline
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from transformers import AutoProcessor, BarkModel
import scipy


#img_to_text

def img2text(url):
    image_to_text=pipeline("image-to-text",model="Salesforce/blip-image-captioning-base")

    text=image_to_text(url)[0]["generated_text"]
   
    return text

#**********************************************************************************************

#LLM

# Load pre-trained model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Prompt text
prompt_text = img2text("pic.jpg")

# Tokenize the prompt
input_ids = tokenizer.encode(prompt_text, return_tensors="pt")

# Generate text based on the prompt
output = model.generate(input_ids, max_length=200, num_return_sequences=1, temperature=0.7)

# Decode and print the generated text
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)
#**********************************************************************************************




#Text to speech





synthesiser = pipeline("text-to-speech", "suno/bark-small")

speech = synthesiser(generated_text, forward_params={"do_sample": True})

scipy.io.wavfile.write("bark_out.wav", rate=speech["sampling_rate"], data=speech["audio"])










