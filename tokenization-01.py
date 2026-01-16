import nltk

nltk.download("punkt_tab")

text = "Machine learning é um campo da inteligência artificial que permite que computadores aprendam padrões a partir de dados. Sem serem programados explicitamente para cada tarefa."

word_tokens = nltk.word_tokenize(text=text)
print(word_tokens)

setence_tokens = nltk.sent_tokenize(text=text, language="portuguese")
print(setence_tokens)


# def preprocess(text):
#     tokens = nltk.word_tokenize(text=text.lower())
#     word_tokenized = []
#     for word in tokens:
#         if word.isalnum():
#             word_tokenized.append(word)
#     return word_tokenized

# List comprehension version
def preprocess(text):
    tokens = nltk.word_tokenize(text=text.lower())
    return [word for word in tokens if word.isalnum()]

documents = [
    "Machine learning é o aprendizado automático de máquinas a partir de dados.",
    "Ele permite que sistemas façam previsões e decisões sem programação explícita.",
    "É usado em áreas como reconhecimento de voz, imagens e recomendação de conteúdo.",
]


# preprocess_docs = []
# for doc in documents:
    # tokens = preprocess(doc)
    # text = " ".join(tokens)
    # preprocess_docs.append(text)

# List comprehension version: 
preprocess_docs = [" ".join(preprocess(doc)) for doc in documents]

print(preprocess_docs)
