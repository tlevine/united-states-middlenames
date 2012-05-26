db.runCommand(
 { mapreduce : "person",
   map : function() {emit(
     [this.born_year, this.born_state],
     this.middles.length > 0
   )},
   reduce : function(key, values) {return {
     // Number of people born with middle names
     k: values.reduce(function(a, b) {return a + b}),
     // Number of people born, with or without middle names
     n: values.length
   };},
   out: "middle_name_counts",
   jsMode : true,
   verbose : true
 }
);
