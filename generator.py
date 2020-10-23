# sample texts
from random import randrange

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
anditems = ["","& 1 other item ","& 2 other items ","& 8 other items "]

infile = open('TextbookMultiVol.txt','r')
titles = infile.readlines()
infile.close()

outfile = open("generated-samples_short-term-courtesy.txt","w")
outfile.write("SMS samples for 'Courtesy Notice - Short Term - 8 HR or less' notice,\
 with textbook titles and device titles\n-----\n")

for i in range(50):
    title = titles[randrange(len(titles))-1][:-1]
    if len(title) > 57: #max title length is 58 char in this template
        while len(title) > 57:
            titlesplit = title.split()
            titlesplit.pop(-1)
            title = " ".join(titlesplit) + "…"
    anditem = anditems[randrange(len(anditems))-1]
    time = str(randrange(1,13)) + ":" + str(randrange(60))
    month = months[randrange(len(months))-1]
    date = str(randrange(1,28))
    template = 'You checked out "%s" %sfrom the Libraries.\nDue: %spm, %s %s.\ngo.ncsu.edu/see-checkouts'\
               %(title, anditem, time, month, date)
    outfile.write(template + "\n\nText message length: " + str(len(template)) + '\n-----\n')
    print(template + '\n-----\n')

outfile.close()
