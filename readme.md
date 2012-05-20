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
This all leads to a table like this.

    ssn,       state, born.date,  died.date,  born.dow, died.dow, born.doy,   died.doy,
    123456789, KY,    1930-02-10, 1978-03-07, mon,      tue,      2000-02-10, 2000-03-07,

"dow" refers to "day of week". "doy" refers to "day of year", but
it's just the date switched to a stardard leap year like so (in R).

    doy <- as.POSIXct(paste('2000', substring('1999-02-28', 5), sep=''))
