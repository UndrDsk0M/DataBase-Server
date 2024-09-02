from fastapi import FastAPI
from peewee import *
from datetime import datetime
import threading
import logging

db = SqliteDatabase('data.db')

class Data(Model):
    text = CharField(max_length=1000)
    date = DateField()
    time = TimeField()

    class Meta:
        database = db

db.connect()
db.create_tables([Data, ])

api = FastAPI()

def submit_data(data):
    x = Data.create(text=data, time=datetime.now(), date=datetime.today())
    x.save()
    print(True)

@api.get('/')
def root():
    messages = []
    for msg in Data.select().order_by(Data.date.desc(), Data.time.desc()):
        messages.append({"text":msg.text,
                         "date": msg.date,
                         "time": msg.time})
    return messages

@api.post('/{text}')
def root2(text: str):
    fun = threading.Thread(target=submit_data, args=(text, ))
    fun.start() 
    return 200


if __name__ == "__main__":
    import uvicorn
    try :
        uvicorn.run(api, host="127.0.0.1", port=8000)
    except:
        logging.critical("i think this host and port is not available, you can change it but becareful to replace examples too!")