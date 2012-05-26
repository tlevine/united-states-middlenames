db.runCommand(
 { mapreduce : "person",
   map : function() {emit(
     [this.born_year, this.born_state],
     this.middles.length > 0
   )},
   reduce : function(key, values) {
     // k = Number of people born with middle names
     // n = Number of people born, with or without middle names
     var k = 0;
     values.forEach(k++);
     return {"k": k, n: values.length};
   },
   out: "middle_name_counts",
   jsMode : true,
   verbose : true
 }
);
