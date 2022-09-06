/**
	Title: purselley-assignment-4.3
    Author: Danial Purselley
    Date: 6 Sep 2022
    Description: MongoDB Shell queries for the users collection.
 */

// insert document into the collection
db.users.insertOne({
  firstName: "Danial",
  lastName: "Purselley",
  employeeId: "7373",
  email: "dpurselely@me.com",
  dateCreated: new Date(),
});

// updating mozart's email
db.users.updateOne(
  { lastName: "Mozart" },
  { $set: { email: "mozart@me.com" } }
);

// verify if the new email is in the document
db.users.findOne({ email: "mozart@me.com" });

// list all users in the collection, with projections
db.users.find({}, { firstName: 1, lastName: 1, email: 1, _id: 0 });
