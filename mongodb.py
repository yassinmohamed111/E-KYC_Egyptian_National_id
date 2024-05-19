from pymongo import MongoClient


def make_new_link(link):
    username = 'user2'
    password = '1234'
    connection_string = f"mongodb+srv://{username}:{password}@cluster0.ktpjwvv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


    client = MongoClient(connection_string)

    db = client['ERP_Database']
    server_collection = db['server']


    new_link = {
        "link": f"{link}",
        "_class": "com.example.KYCAPP.entity.ServerLink"
    }

    result = server_collection.insert_one(new_link)
    print(f"link updated...")



make_new_link("https://8e46-154-178-73-62.ngrok-free.app/flutter")