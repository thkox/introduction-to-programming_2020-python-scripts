# Εύρεση στατιστικών ΚΙΝΟ 1ης κλήρωσης για κάθε μέρα του τρέχοντα μήνα
import urllib.request
import json
import datetime
from time import sleep

cur_date=datetime.datetime.now()            # Σημερινη ημερομηνία (Τελικός Έλεγχος 2021-03-02)
print(cur_date)                             # εμφάνιση της μορφής
print(cur_date.year)                        # Ετος 2021
print(cur_date.month)                       # Μήνας 03
print(cur_date.day)                         # Ημέρα 02

cd=cur_date.day             # κρατώ στη μεταβλητή cd τη σημερινή ημέρα
for i in range(cd):         # for για να βρώ για όλες τις ημερομηνίες του τρέχοντα μήνα
    #--------------------------------------------
    #Βρίσκω την τελευταία μερα του προηγούμενου μήνα
    #--------------------------------------------
    cur_date = cur_date - datetime.timedelta(days=cur_date.day-i)
    print(cur_date)                             # την εμφανίζω για έλεγχο

    date_str = cur_date.strftime("%Y-%m-%d")

#---------------------------------------
#χρηση ημνιας date_str ως παραμετρο
#---------------------------------------
    url = 'https://api.opap.gr/draws/v3.0/1100/draw-date/'+"/"+date_str+"/"+date_str
    print(url)                       # εμφάνιση url για έλεγχο ημνιας άντλησης 10 τελ. κληρώσεων

    r=urllib.request.urlopen(url)            #τραβώ τα δεδομενα
    html=r.read()
    html=html.decode()
    data=json.loads(html, strict=False)

    t = []
    for draw in data["content"]:           # από τα content
        t.append(draw["drawId"])           # φέρνει τα 10 τελευταία Id σε λίστα
    print(t[0])                            # το 1ο της λίστας είναι το τελευταίο της ημέρας

    f1=t[0]+1                   # προσθέτω +1 σε αυτό και έχω το drawId για τη 1η κλήρωση επόμενης ημέρας

    f2=str(f1)                  # μετατρέπεω το drawId σε string για να το προσθέσω ως παράμετρο στο url
#--------------------------------------------------------------------
    url2='https://api.opap.gr/draws/v3.0/1100/'+f2 #τοποθετώ το Id σε διαφορετικό api
    print(url2)                 # Εμφανίζω το url

    r2=urllib.request.urlopen(url2)          #Τραβώ από τα δεδομένα την λίστα της κλήρωσης
    html2=r2.read()
    html2=html2.decode()
    data2=json.loads(html2, strict=False)
    print(html2)                            #φέρνει τα στοιχεία για την 1η κληρωση της ημέρας (για έλεγχο)

    protinew = []                           # λίστα που θα μαζεύει όλες τις πρώτες κληρώσεις

    if i == 0:
        proti = protinew
    protinew = data2["winningNumbers"]['list']   # μεταφέρει τα στοιχεία της i ημέρας στη λίστα protinew
#   print(protinew)                         # για έλεγχο
    proti.extend(protinew)                  # προσθέτει στη λίστα proti τη νέα λίστα
    print(proti)
    print("=============================")
    cur_date=datetime.datetime.now()        # σημερινη ημερομηνία
#----------------------------------
print("Τέλος συγκέντρωσης νικητήριων αριθμών")
sum = cd * 20
print("Η λίστα περιέχει ", sum, " αριθμούς")
#-------------------------------------
from collections import Counter
m = Counter(proti)
n = len(sorted(m))
p = dict(sorted(m.items(), key = lambda item: item[1]))
#-----------------------
x = list(p.keys())                      # δημιουργεί λίστα από τα κλειδιά του λεξικού
x.sort()                                # ταξινομεί τη λίστα
#-----------------------
for symbol in x:                        # για κάθε χαρακτήρα της ταξ. λίστας (κλειδί του λεξικού)
     number = p[symbol]                 # τοποθετεί το πλήθος εμφανίσεως του στη μεταβλητή number
     print(symbol, ": ",  end="")       # τυπώνει τον αριθμό που έχει κληρωθεί

     xy = round((number*100/sum),0)     # κάνει στρογγυλοποίηση εμφάνισης

     print("*"*int(xy))                 # τυπώνει το πλήθος των * ανα πλήθος εμφάνισης αριθμών
