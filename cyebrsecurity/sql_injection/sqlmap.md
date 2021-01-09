Sqlmap is arguably the most popular automated SQL injection tool out there. It checks for various types of injections, and has plenty of customization options.
How do you specify which url to check?

-u
What about which google dork to use?

-g
How do you select(lol) which parameter to use?(Example: in the url http://ex.com?test=1 the parameter would be test.)

-p
What flag sets which database is in the target host's backend?(Example: If the flag is set to mysql then sqlmap will only test mysql injections).
--dbms
How do you select the level of depth sqlmap should use(Higher = more accurate and more tests in general).

--level
How do you dump the table entries of the database?

--dump
Which flag sets which db to enumerate?

(Case sensitive)

-D
Which flag sets which table to enumerate?

(Case sensitive)

-T
Which flag sets which column to enumerate?

(Case sensitive)

-C
How do you ask sqlmap to try to get an interactive os-shell?
--os-shell
What flag dumps all data from every table

--dump-all
