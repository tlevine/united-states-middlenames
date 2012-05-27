db.runCommand(
 { mapreduce : "person",
   map : function() {emit(
     [this.born_year, this.state],
     {'k': this.middles.length > 0, 'n': 1}
   )},
   reduce : function(key, values) {
     // k = Number of people born with middle names
     // n = Number of people born, with or without middle names
     var result={"k": 0, "n": 0};
     values.forEach(function(value){
       result.k+=value.k;
       result.n+=value.n;
     });
     return result;
   },
   out: "middle_name_counts",
   jsMode : true,
   verbose : true
 }
);
