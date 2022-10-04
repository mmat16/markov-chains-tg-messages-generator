import markovify

text_di = open('messages_di.txt', encoding='utf8').read()
text_me = open('messages_me.txt', encoding='utf8').read()
text = open('messages.txt', encoding='utf8').read()

text_model_di = markovify.Text(text_di)
text_model_me = markovify.Text(text_me)
text_model_mix = markovify.Text(text)
