# γράφει το κείμενο ανάποδα και βρίσκει τους αντικατοπρικούς χαρακτήρες
file = open("keimeno.txt", "r" ,encoding='utf-8')  # Άνοιγμα του αρχείου.
text = file.read()  # Αποθήκευση του αρχείου σε μια συμβολοσειρά με όλους τους χαρακτήρες.
file.close()        # Κλείσιμο του αρχείου.
print(text)
list_text = list(text)   # Μετατροπή τηε συμβολοσειράς text σε μια λίστα.
list_text.reverse()      # αντιστροφή του κειμένου
print(list_text)         # εμφάνιση της λίστας με αντεστραμένη σειρά των χαρακτήρων του κειμένου
#----------------------------------------------------
i = 0                    # μετρητης για να διατρέξουμε τη λίστα list_text
f = open("demo.txt", "w")   #δημιουργεί ένα αρχείο demo.txt για να γράψει
while i < len(list_text):     #διατρέχει όλους τους χαρακτήρες
     letter=list_text[i]      # παιρνει το χαρακτήρα από τη λίστα
     n=ord(letter)            # τον μετατρέπει σε ASCII
     x=128-n                  # βρίσκει τον κατοπτρικό για 128
     f.write(hex(x))          # τον καταχωρεί στο αρχείο σε 16αδική μορφή
     i = i + 1                # Αυξάνει τη μεταβλητή κατα 1 και επιστρέφει στη while
f.close()                     # κλείνει το αρχείο

f = open("demo.txt", "r")   # Ανοιγμα αρχείου για ανάγνωση-εμφάνιση και έλεγχο
print(f.read())
