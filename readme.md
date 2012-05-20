United States Middle Names
=================

I want to know what proportion of people have middle names
and how this varies by time and location? In considering "time",
I want to consider both raw time and time within cycles.

### Raw data
Get Social Security Death Master File for free

* [Original](http://ssdmf.info/)
* [Torrent](http://thepiratebay.se/torrent/7193029/)

`unpack.sh` unzips them and puts them in the `deathfile` directory.

You can see the format in the `deathfile.head` directory;
this contains the first ten lines of each file.

### Architecture
Data are stored inside a MongoDB, in a collection called `middlenames`.
Jobs are distributed across computers on a local network, and results
are sent back to the MongoDB.

This particular network is composed of cheap computers connected by
100Mbps ethernet. The computer running Mongo has relatively a lot of RAM.

### Import
`load.py` puts the data into a `deathfile` collection in MongoDB,
which is indexed on social security number (SSN).

It doesn't try to be fast because it's loading from the same three
files; once they're in the database, everything will be faster.

### Features
Features for each dead person. Records are distributed across many workers
via ZeroMQ. Results are sent back into the database in a new collection.
The collection is named based on the statistical unit of the features--whether
they are at the person level, year level, &c.; you can also think of this
as the field on which they are uniquely indexed.

#### Personal
Person-level features are extracted and stored them in the `personfeatures`
collection, which is indexed on SSN.

These features are
* Number of middle names/initials
* Age
* Location of registration (based on SSN)

### Simple transformations

#### Name
Surn-middle-forename pairs are collected indexed by each other, so there's a
surname collection that has counts of middle and forenames by surname, a
middlenames collection that has counts of sur and forenames by middlenames field
and a forename collection that has counts of surnames by forename.

#### State


### Resulting table
This all leads to a table like this, proably stored in SQLite.

    ssn,       born.date,  died.date,  born.dow, died.dow, born.doy,   died.doy,   state, forename, surname, middles, middles.count
    123456789, 1930-02-10, 1978-03-07, mon,      tue,      2000-02-10, 2000-03-07, KY,    Mohommad, Lee,     N,       1,

"dow" refers to "day of week". "doy" refers to "day of year", but
it's just the date switched to a stardard leap year like so (in R).

    doy <- as.POSIXct(paste('2000', substring('1999-02-28', 5), sep=''))

"middles" refers to middle initials, and "middles.count" is how many
there are.

#### Missing dates
If the year is missing and the month and day are available, the dates
will be NAs.

    ssn,       born.date, died.date, born.dow, died.dow, born.doy,   died.doy,   state, forename, surname, middles, middles.count
    123456789, NA,        NA,        mon,      tue,      2000-02-10, 2000-03-07, KY,    Mohommad, Lee,     N,       1,

If only the day of the month is missing, the date will use the 15th
day of the month. This is equivalent to the middle day of the month
rounded down, except for February, where it is the day after the middle
day, rounded down. Also, the days of the week will be missing.

    ssn,       born.date,  died.date,  born.dow, died.dow, born.doy,   died.doy,   state, forename, surname, middles, middles.count, funny.name
    123456789, 1930-02-15, 1978-03-15, NA,       NA,       2000-02-15, 2000-03-15, KY,    Mohommad, Lee,     N,       1,             FALSE

"funny.name" is whether the name contains characters other than `[A-Z ',.]`
