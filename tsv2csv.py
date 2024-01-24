import csv

INPUT_FILE = 'clean.tsv'
OUTPUT_FILE = 'books.csv' 
MISSING_FILE = '_missing.csv'

with open(INPUT_FILE, 'r', encoding='utf-8', newline=None) as tsv_in, \
     open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as csv_out, \
     open(MISSING_FILE, 'w', newline='', encoding='utf-8') as missing_out:

    tsv_reader = csv.reader(tsv_in, delimiter='\t')
    csv_writer = csv.writer(csv_out)
    missing_writer = csv.writer(missing_out)

    headers = ['title', 'creators', 'description', 'upc_isbn10', 'ean_isbn13',
               'tags', 'publisher', 'publish_date', 'length_of', 'lcc']
    csv_writer.writerow(headers)
    missing_writer.writerow(headers)

    next(tsv_reader) # skip header
    
    ctr = 0

    for row in tsv_reader:  
        
        isbn = row[33]
        # Remove brackets
        if isbn.startswith('[') and isbn.endswith(']'):
            isbn = isbn[1:-1]
        
        isbns = [x.strip() for x in row[34].split(',')] 

        upc_isbn10 = ''
        ean_isbn13 = ''

        for isbn in isbns:
            if len(isbn) == 10:
                upc_isbn10 = isbn
                break
            elif len(isbn) == 13:
                ean_isbn13 = isbn
                break

        if not upc_isbn10:
            for isbn in isbns:
                if len(isbn) == 10:
                    upc_isbn10 = isbn
                    break
            
        if not ean_isbn13:
            for isbn in isbns:
                if len(isbn) == 13:
                    ean_isbn13 = isbn
                    break
        
        ctr = ctr + 1        
        
        title = row[1] 
        creators = row[3]
        description = row[13]
        
        tags = row[28]
        publisher = row[7]
        publish_date = row[8]
        length_of = row[21]
        lcc = row[32]
        
        if not upc_isbn10 and not ean_isbn13:
            missing_writer.writerow([title, creators, description, '', '', 
                                     tags, publisher, publish_date, length_of, lcc])
        else:
            csv_writer.writerow([title, creators, description, upc_isbn10, ean_isbn13, 
                                 tags, publisher, publish_date, length_of, lcc])