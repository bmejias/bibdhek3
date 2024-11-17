CREATE SCHEMA IF NOT EXISTS bibdhek;

CREATE TABLE IF NOT EXISTS bibdhek.books (
    id			serial      PRIMARY KEY
  , title		text		NOT NULL
  , author		text		NOT NULL
  , cd			boolean		DEFAULT FALSE
  , collection	text
  , level		text
  , lang		char(2)
  , date		text
  , isbn		text
  , cover		text
  , publisher 	text
  , obs			text
  , acquired	text
);

CREATE TABLE IF NOT EXISTS bibdhek.copies (
    id			serial		PRIMARY KEY
  , book_id		integer		REFERENCES bibdhek.books(id)
  , status		varchar(16)	NOT NULL
  , code		varchar(16)
  , position	varchar(16)
  , type		varchar(16)
);

CREATE TABLE IF NOT EXISTS bibdhek.users (
    id			serial		PRIMARY KEY
  , username	varchar(32)	UNIQUE
  , first_name	text		NOT NULL
  , last_name	text		NOT NULL
  , email		text
  , password 	text
);

CREATE TABLE IF NOT EXISTS bibdhek.groups (
    id		    serial	    PRIMARY KEY
  , name	    text	    UNIQUE
);

CREATE TABLE IF NOT EXISTS bibdhek.group_users (
    id			serial	    PRIMARY KEY -- Maybe remove this key
  , user_id		integer	    REFERENCES bibdhek.users(id)
  , group_id	integer	    REFERENCES bibdhek.groups(id)
);

CREATE TABLE IF NOT EXISTS bibdhek.loans (
    id			serial		PRIMARY KEY
  , copy_id		integer		REFERENCES bibdhek.copies(id)
  , user_id		integer		REFERENCES bibdhek.users(id)
  , status		varchar(16)	NOT NULL
  , date_out	date		NOT NULL
  , date_return	date
  , date_in		date
  , cd			boolean		DEFAULT FALSE
  , deposit		numeric(4, 2)	DEFAULT 0
  , fine		numeric(4, 2)	DEFAULT 0
  , paid		numeric(4, 2)	DEFAULT 0
);

CREATE TABLE IF NOT EXISTS bibdhek.rules (
    id		serial		PRIMARY KEY
  , rule	varchar(32)	NOT NULL
  , amount	integer
  , note	text
);
