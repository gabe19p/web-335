/**
	Title: purselley-assignment-6.2
    Author: Danial Purselley
    Date: 14 Sep 2022
    Description: MongoDB Shell queries.
 */

// query the houses collection for all documents
db.houses.find({});

// query the students collection for all documents
db.students.find({});

// add a student to the collection
db.students.insertOne({
  firstName: "Danial",
  lastName: "Purselley",
  studentId: "s1019",
  houseId: "h1007",
});

// verify student was added
db.students.findOne({ firstName: "Danial" });

// delete the student previously added
db.students.deleteOne({ firstName: "Danial" });

// verify student was deleted
db.students.findOne({ firstName: "Danial" });

// group students by houses
db.houses.aggregate([
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "students",
    },
  },
]);

// match all of the gryffindors (houseId)
db.students.aggregate([{ $match: { houseId: "h1007" } }]);

// find students that belong to eagle mascot (houseId)
db.houses.aggregate([
  { $match: { houseId: "h1009" } },
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "Ravenclaw",
    },
  },
]);
