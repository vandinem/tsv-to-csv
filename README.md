# tsv-to-csv
Python scripts to help prep a **LibraryThing.com** TSV export file as a **LibIb.com** CSV input file

I am a longtime user of the book and media cataloging site **LibraryThing.com**.  LibraryThing makes it easy to provide your assembled book data as a **TinyCat** repository as well.

But if you want to provide your book data as a **LibIb.com** repository, there is no direct path to do that.  Instead you can export your LibraryThing data to a TSV (tab-separated values) file to use for import elsewhere. (I do this periodically anyway as a backup file). **LibIb.com** will accept a CSV file for a bulk Import of data, and they provide templates to guide how to organize such a file (there are separate templates for books, video, games, and music).  They specify that the CSV file must use the **UTF-8** coding standard.

So the challenge is to convert the **LibraryThing.com**-generated TSV file into a valid CSV input file for **LibIb.com**

I am only interested in books for this example, and **LibIb.com** requires that either the ISBN-10 or ISBN-13 code for the book be provided with each valid record in the CSV file (or the record will be skipped).

I worked with Claude.ai to create two scripts.  The first, **clean_utf8.py**, reads the TSV file and removes any non-UTF8 character codes.  I invoke this script like this:

`cat <tsv file> | python3 clean_utf8.py > clean.tsv`

With the file clean.tsv available, I then use **tsv2csv.py**, where clean.tsv is the hardcoded INPUT_FILE, to create a valid **books.csv** file to import, and **_missing.csv**, to identify any records that are skipped. (This is overkill, because LibIb provides an email of anything it skips during the import process ... my TSV file includes videos and games, so I knew all of these would be skipped.  LibIb will also reject duplicate entries, etc.)
