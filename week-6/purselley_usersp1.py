
# Title: purselley_usersp1.py
# Author: Danial Purselley
# Date: 16 Sep 2022
# Description: connecting to mongoDB 
# with python

# mongo import
from pymongo import MongoClient

# connection statement
client = MongoClient("mongodb+srv://web335_user:s3cret@buwebdev-cluster-1.078ar.mongodb.net/web335DBretryWrites=true&w=majority")

# database variable
db = client['web335DB']

# display all documents
#   'for user in' loops through the entire find({}) query
#   firstName, lastName, projections to clean up the return
#   don't forget to print() the user for each iteration
for user in db.users.find({}, {'firstName': 1, 'lastName': 1}):
  print(user)

# display employee 1011 document
print(db.users.find_one({ 'employeeId': '1011' }))

# display employee mozart
print(db.users.find_one({ 'lastName': 'Mozart' }))