United States Middle Names
=================

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
`features.py` extracts some features for each dead person. Records
are distributed across many workers via ZeroMQ. Results are sent back
into the database in a collection called `personfeatures`, which is
also indexed on SSN.
