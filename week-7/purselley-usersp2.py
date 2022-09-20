
# Title: purselley_usersp2.py
# Author: Danial Purselley
# Date: 20 Sep 2022
# Description: connecting to mongoDB 
# with python

# mongo import
from datetime import datetime
from pymongo import MongoClient

# connection statement
client = MongoClient("mongodb+srv://web335_user:s3cret@buwebdev-cluster-1.078ar.mongodb.net/web335DBretryWrites=true&w=majority")

# database variable
db = client['web335DB']

# new user document
newUser = {
    'firstName': 'Madison',
    'lastName': 'Purselley',
    'employeeId': '1212',
    'email': 'madison@email',
    'dateCreated': datetime.now()
}

# create new user document
db.users.insert_one(newUser)

# display newly added user
print(db.users.find_one({'firstName': 'Madison'}))

# update the new user email
db.users.update_one({ 'firstName': 'Madison' }, { '$set': { 'email': 'newMadison@email '} })

# display the updated document
print(db.users.find_one({'firstName': 'Madison'}))

# delete the document
db.users.delete_one({'firstName': 'Madison'})

# prove document was deleted
print(db.users.find_one({'firstName': 'Madison'}))