# μετρά ολες τις τετράδες με 1,ΟΡΙΖΟΝΤΙΑ, ΚΑΘΕΤΑ  και Διαγώνια
from numpy import random
import numpy as np

pl = int(input("Πλευρά Πίνακα : "))  # Δίνω πλευρά.

x = pl * pl # συνολικό πλήθος κελιών πίνακα
print("πλήθος κελιών ", x)

y1 = x//2   # πλήθος μηδενικών (0)
print("πλήθος μηδενικών ", y1)
y2 = x - y1 # πλήθος άσσων (1)

#-----------------------------------------
mo = 0                              # μεταβλητή για το Μέσο Ορο
sum = 0                             # μεταβλητή για πλήθος των τετράδων με 1
while mo < 100:
    sum1=0
    #print("=======================================")
    #print("  Νέος Πίνακας  ")
    #print("=======================================")
    arr1 = []  # λιστα που θα συγκεντρωθουν y1 (0) και y2 (1)
    #-------------------------- # γέμισμα της λίστας πρώτα με 0 και μετα με 1
    for i in range(y1):
        arr1.append(0)          # λιστα με (0)
    #    print(arr1[i])
    for i in range(y1,x):
        arr1.append(1)          # λιστα με (1)
    #   print(arr1[i])
    #--------------------
    arr = np.array(arr1)        # λιστα με μηδενικά και άσσους
    #print(arr)
    random.shuffle(arr)         # ανακάτεμα -> τυχαία θέση τους
    #print(arr)                  # εμφάνιση λίστας με τυχαία τη σειρά 1 και 0
    #------------------------------  εμφάνιση πίνακα
    for i in range(pl):
        print(arr[(i*pl):(i*pl+pl)])    # εμφάνιση σε μορφή πίνακα
    #-------------------------------

    for line in range(pl):
        for i in range(0,pl):
            if i < pl-3:
                tetrada = [arr[line*pl+i],arr[line*pl+i+1], arr[line*pl+i+2], arr[line*pl+i+3]]  # 4 οριζοντιες θεσεις
                #print(tetrada)                                         # εμφανιση για έλεγχο
                z = tetrada.count(1)                                    # μετρημα άσσων
                if z == 4:
                    sum = sum + 1
                    sum1 = sum1 +1
                    #print(z)                                           # εμφάνιση αποτελέσματος 4 άσσοι
    #print(" Ολοκληρώθηκε ο οριζόντιος έλεγχος ")
    # ----------------------------------------------
    for line in range(pl-3):   #Ελεγχος διαγωνίων από πανω Αρ σε κάτω δεξιά
        for i in range(0,pl):
            if i < pl-3:
                tetrada = [arr[line*pl+i],arr[pl+i+1+pl*line], arr[2*pl+i+2+pl*line], arr[3*pl+i+3+pl*line]]      # 4 οριζοντιες θεσεις
                #print(tetrada)                                                   # εμφανιση για έλεγχο
                z = tetrada.count(1)                                             # μετρημα άσσων
                if z == 4:
                    sum = sum + 1
                    sum1 = sum1 +1
                    #print(z)
    #print(" Ολοκληρώθηκε ο Διαγώνιος Π.Α -> Κ.Δ έλεγχος ")
    #----------------------------------
    for line in range(pl):
        if line < pl - 3:
            for i in range(0,pl):
                tetrada = [arr[line*pl+i],arr[line*pl+i+1*pl], arr[line*pl+i+2*pl], arr[line*pl+i+3*pl]]      # 4 οριζοντιες θεσεις
                #print(tetrada)                                                   # εμφανιση για έλεγχο
                z = tetrada.count(1)                                             # μετρημα άσσων
                if z == 4:
                    sum = sum + 1
                    sum1 = sum1 +1
                    #print(z)
    # ολοι οι οριζοντιοι έλεγχοι εγιναν
    #print(" Ολοκληρώθηκε ο ΚΑΘΕΤΟΣ έλεγχος ")
    #------------------------------------
    for line in range(pl-4, pl):   #Ελεγχος διαγωνίων από Κάτω Αρ σε Πάνω δεξιά
        for i in range(0,pl):
            if i < pl-3:
                tetrada = [arr[line*pl+i],arr[pl*line-pl+i+1], arr[pl*line-2*pl+i+2], arr[pl*line-3*pl+i+3]]      # 4 οριζοντιες θεσεις
                #print(tetrada)                                                   # εμφανιση για έλεγχο
                z = tetrada.count(1)                                             # μετρημα άσσων
                if z == 4:
                    sum = sum + 1
                    sum1 = sum1 +1
                    #print(z)
    print("βρέθηκαν ", sum1, " τετράδες με 1")
    #print(" Ολοκληρώθηκε ο Διαγώνιος Κ.Α -> Π.Δ έλεγχος ")
     #------------------------------------

    mo = mo + 1
print("==========================================")
print("βρέθηκαν συνολικά ", sum, " τετράδες με 1")

print("Μέσος όρος τετράδων με 1 για 100 επαναλήψεις = ", sum/100)
