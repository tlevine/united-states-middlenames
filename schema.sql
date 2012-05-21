CREATE TABLE person_raw (
  ssn character(9) PRIMARY KEY,   -- Social security number
  rawline character(100) NOT NULL -- Raw line of the file
)

CREATE TABLE person (
  -- Social security number
  ssn character(9) references person_raw(ssn) PRIMARY KEY,

  forename varchar(55) NOT NULL,
  surname varchar(55) NOT NULL,
  middles varchar(55) NOT NULL,

  -- Date components
  born_year smallint,
  died_year smallint,
  CHECK (died_year > born_year)

  born_month smallint,
  died_month smallint,
  CHECK (12 >= born_month AND born_month >= 1)
  CHECK (12 >= died_month AND died_month >= 1)

  born_day smallint,
  died_day smallint,
  CHECK (31 >= born_day AND born_day >= 1)
  CHECK (31 >= died_day AND died_day >= 1)

  -- The above date as a proper date
  born_date date,
  died_date date,
  CHECK (died_date > born_date)

  -- Day of the week (0, 1, 2, 3, 4, 5 or 6)
  born_dow smallint,
  died_dow smallint,
  CHECK (6 >= born_dow AND born_dow >= 0)
  CHECK (6 >= died_dow AND died_dow >= 0)

  -- Date in the year 2000, in case the year is not known
  born_doy date,
  died_doy date,

  state character(2) NOT NULL, -- Geographical state of registration
  middles_initials_count smallint NOT NULL -- How many middle initials
)
