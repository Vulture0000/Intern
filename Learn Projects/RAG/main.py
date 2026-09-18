import truststore

truststore.inject_into_ssl()

from dotenv import load_dotenv

load_dotenv()

from rag import Rag


rag = Rag("KB/sample_kb_data.json")

rag.load_json()
rag.text_splitter()
rag.vectorizer()

questions = ["What's my discount as a gold tier customer?","What happens if my booking fails?","How far ahead do I need to book?","What's the cancellation policy?","What does 'cutoff window' mean?","Who is uthra unnikrishnan"]
for quest in questions:
    result = rag.ask(
        quest
    )
    print(quest,end = " :")
    print(result,"\n\n\n\n\n")

result = rag.ask("What does 'cutoff window' mean?")
print(result)