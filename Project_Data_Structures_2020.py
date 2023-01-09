import math
import time


def merge_sort(function_list, limit_left, limit_right):
    # Διαίρεση του πίνακα σε 2 υποπίνακες όσο το μήκος του πίνακα ειναι μεγαλύτερο απο 1,
    # αφου τότε limit_left < light_right
    if limit_right > limit_left:

        # Ορισμός αριστερής διαίρεσης με τα σωστά όρια
        left_division = merge_sort(function_list, limit_left, (limit_left + limit_right) // 2)
        # Ορισμός δεξιάς διαίρεσης με τα σωστά όρια
        right_division = merge_sort(function_list, (limit_left + limit_right) // 2 + 1, limit_right)

    else:
        sorted_list = [function_list[limit_left]]
        return sorted_list  # Επιστροφή του πίνακα με μήκος όταν τελειώσουν οι διαιρέσεις

    sorted_list = []  # Ορισμός πίνακα οπου θα γίνει το merge των δυο υποπινάκων
    l_counter = 0  # Μετρητής αριστερού υποπίνακα
    r_counter = 0  # Μετρητής δεξιού υποπίνακα
    while l_counter < len(left_division) or r_counter < len(right_division):  # Όσο και οι δυο υποπίνακες δεν είναι
        # "άδειοι"

        if r_counter == len(right_division) and l_counter != len(left_division):  # Αν ο δεξιός υποπίνακας είναι
            # άδειος, πρόσθεση του επόμενου στοιχείου του αριστέρου στον ταξινομημένο πίνακα
            sorted_list.append(left_division[l_counter])
            l_counter += 1
        elif l_counter == len(left_division) and r_counter != len(right_division):  # Αν ο αριστερός υποπίνακας είναι
            # άδειος, πρόσθεση του επόμενου στοιχείου του δεξιού στον ταξινομημένο πίνακα
            sorted_list.append(right_division[r_counter])
            r_counter += 1
        elif left_division[l_counter].value > right_division[r_counter].value:  # Αν το επόμενο στοιχείο του αριτερού
            # είναι μεγαλύτερο του δεξίου, πρόσθεση του επόμενου δεξιού στον ταξινομημένο πίνακα
            sorted_list.append(right_division[r_counter])
            r_counter += 1
        else:  # Αν το επόμενο στοιχείο του δεξιού είναι μεγαλύτερο του αριστερού, πρόσθεση του επόμενου αριστερού
            # στον ταξινομημένο πίνακα. Δεν χρειάζεται συνθήκη γιατί είναι η τελευταία δυνατή περίπτωση
            sorted_list.append(left_division[l_counter])
            l_counter += 1

    return sorted_list


def time_merge_sort(function_list, limit_left, limit_right):
    if limit_right > limit_left:  # Διαίρεση του πίνακα σε 2 υποπίνακες όσο το μήκος του πίνακα ειναι μεγαλύτερο απο
        # 1, αφου τότε limit_left < light_right

        left_division = time_merge_sort(function_list, limit_left,
                                        (limit_left + limit_right) // 2)  # Ορισμός αριστερής διαίρεσης με τα σωστά όρια
        right_division = time_merge_sort(function_list, (limit_left + limit_right) // 2 + 1,
                                         limit_right)  # Ορισμός δεξιάς διαίρεσης με τα σωστά όρια

    else:
        sorted_list = [function_list[limit_left]]
        return sorted_list  # Επιστροφή του πίνακα με μήκος όταν τελειώσουν οι διαιρέσεις

    sorted_list = []  # Ορισμός πίνακα οπου θα γίνει το merge των δυο υποπινάκων
    l_counter = 0  # Μετρητής αριστερού υποπίνακα
    r_counter = 0  # Μετρητής δεξιού υποπίνακα
    while l_counter < len(left_division) or r_counter < len(
            right_division):  # Όσο και οι δυο υποπίνακες δεν είναι "άδειοι"

        if r_counter == len(right_division) and l_counter != len(left_division):  # Αν ο δεξιός υποπίνακας είναι
            # άδειος, πρόσθεση του επόμενου στοιχείου του αριστέρου στον ταξινομημένο πίνακα
            sorted_list.append(left_division[l_counter])
            l_counter += 1
        elif l_counter == len(left_division) and r_counter != len(right_division):  # Αν ο αριστερός υποπίνακας είναι
            # άδειος, πρόσθεση του επόμενου στοιχείου του δεξιού στον ταξινομημένο πίνακα
            sorted_list.append(right_division[r_counter])
            r_counter += 1
        elif left_division[l_counter].time > right_division[r_counter].time:  # Αν το επόμενο στοιχείο του αριτερού
            # είναι μεγαλύτερο του δεξίου, πρόσθεση του επόμενου δεξιού στον ταξινομημένο πίνακα
            sorted_list.append(right_division[r_counter])
            r_counter += 1
        else:  # Αν το επόμενο στοιχείο του δεξιού είναι μεγαλύτερο του αριστερού, πρόσθεση του επόμενου αριστερού
            # στον ταξινομημένο πίνακα. Δεν χρειάζεται συνθήκη γιατί είναι η τελευταία δυνατή περίπτωση
            sorted_list.append(left_division[l_counter])
            l_counter += 1
    return sorted_list


def max_heapify(function_list, length, key):  # συνάρτηση με αναδρομή που καλείται στο τέλος, πάνω στο node του
    # υποβιβασμένου πατέρα

    father = key  # πατέρας ενός x υπόδεντρου
    lchild = 2 * key + 1  # αριστερό παιδί εν συναρτήσει του πατέρα σύμφωνα με την τοποθεσία του στην λίστα
    rchild = 2 * key + 2  # δεξί παιδί εν συναρτήσει του πατέρα σύμφωνα με την τοποθεσία του στην λίστα

    if lchild < length and function_list[father].value < function_list[lchild].value:  # αν υπάρχει αριστερό παιδί
        # και η τιμή του είναι μεγαλύτερη αυτής του πατέρα
        father = lchild  # άλλαξε τις μεταξύ τους θέσεις

    if rchild < length and function_list[father].value < function_list[rchild].value:  # αν υπάρχει δεξιό παιδί και η
        # τιμή του είναι μεγαλύτερη αυτής του πατέρα
        father = rchild  # άλλαξε τις μεταξύ τους θέσεις

    if father != key:  # αν στα παραπάνω βήματα άλλαξε η θέση του πατέρα με ένα παιδί
        function_list[key], function_list[father] = function_list[father], function_list[key]  # αντάλλαξε τις τιμές
        # του παιδιού και του πατέρα

        max_heapify(function_list, length, father)  # ξανά-τέσταρε τις συνθήκες για το τροποποιημένο δέντρο


def build_max_heap(list):  # συνάρτηση κατά την οποία φτιάχνεται ένα heap  βάζοντας την μεγαλύτερη τιμή στο τέλος της
    # λίστας(ταξινομημένο μέρος της λίστας)
    n = len(list)

    for i in range(n, -1, -1):  # Βρόχος ο οποίος φέρνει την μέγιστη τιμή στην αρχή της λίστας
        max_heapify(list, n, i)

    for i in range(n - 1, 0,-1):  # Βρόχος ο οποίος ανταλλάζει τις τιμές της 1ης θέσης της λίστας με την i-οστή (
        # τελευταία θέση της μη-ταξινομημένης λίστας)
        list[i], list[0] = list[0], list[i]
        max_heapify(list, i, 0)


# επιτρέπει την προσθήκη λίστας προς επεξεργασία από τον χρήστη
def quick_sort(temperature_list):
    quick_sort2(temperature_list, 0, len(temperature_list) - 1)


# διαχωρισμός της λίστας
def quick_sort2(function_list, left_arrow, right_arrow):
    if left_arrow < right_arrow:  # συνθήκη σύγκρισης αριστερότερου στοιχειου λίστας με το δεξιότερο
        p = partition(function_list, left_arrow, right_arrow)  # ορισμός στοιχείου που χωρίζει τη λίστα
        quick_sort2(function_list, left_arrow, p - 1)
        quick_sort2(function_list, p + 1, right_arrow)


# ορισμός του πίβοτ
def get_pivot(function_list, first, last):
    mid = (first + last) // 2  # μεσαίο στοιχείο της λίστας
    pivot = last
    if function_list[first].value < function_list[mid].value:
        if function_list[mid].value < function_list[last].value:
            pivot = mid
    elif function_list[first].value < function_list[last].value:
        pivot = first
    return pivot


def partition(function_list, first, last):
    pivot_index = get_pivot(function_list, first, last)  # δείκτης πίβοτ
    pivot_value = function_list[pivot_index].value  # τιμή πίβοτ
    function_list[pivot_index], function_list[first] = function_list[first], function_list[
        pivot_index]  # τοποθέτηση του πίβοτ στην αριστερότερη θέση
    barrier = first  # ορισμός στοιχείου ελέγχου από όπου ξεκινάνε οι συγκρίσεις στοιχείων

    for i in range(first, last + 1):  # βρόχος σύγκρισης στοιχείων λίστας με το πίβοτ
        if function_list[i].value < pivot_value:
            barrier += 1  # ορισμός επόμενου στοιχείου ελέγχου από όπου ξεκινάνε οι συγκρίσεις στοιχείων
            function_list[i], function_list[barrier] = function_list[barrier], function_list[
                i]  # τοποθέτηση του στοιχειου λίστας στην θέση του στοιχεόυ ελέγχου
    function_list[first], function_list[barrier] = function_list[barrier], function_list[
        first]  # τοποθέτηση του στοιχείου ελέγχου στην αριστερότερη θέση

    return barrier


def binary_search(l, x):
    left = 0  # Αριστερό άκρο
    right = len(l) - 1  # Δεξιό άκρο
    next = (right + left) // 2  # Κατάλληλο βήμα που πρέπει να γίνει για να εφαρμοστεί σωστά η αναζήτηση. Βασίζεται
    # στα δύο άκρα της λίστας.

    while left < right:  # Βρόχος για την αναζήτηση.
        if x == l[next].time:  # Αν το x είναι ίσο με τη τιμή της λίστας στο σημείο next τότε βγες.
            break

        elif x < l[next].time:  # Αν το x είναι μικρότερο τη τιμή της λίστας στο σημείο next
            right = next - 1  # Αλλαγή του right κατάλληλα ετσι ωστε να μην το δεξί άκρο να γίνει το τωρινό next.

        else:  # Αν το x είναι μεγαλύερο τη τιμή της λίστας στο σημείο next
            left = next + 1  # Αλλαγή του left κατάλληλα ετσι ωστε να μην το αριστερό άκρο να γίνει το τωρινό next.

        next = (right + left) // 2  # Αλλαγή του next ανάλογα τα καινούργια άκρα.

    if x == l[next].time:
        return next
    else:
        return -1


def interpolation_search(f_list, x):
    l = 0  # αριστερό άκρο
    r = len(f_list) - 1  # δεξί άκρο
    while l <= r and f_list[l].time <= x <= f_list[r].time:  # όσο θα υπάρχει λίστα και η τιμή  x θα βρίσκεται μέσα
        # σε αυτή
        next = l + math.ceil(((float(r - l) / (f_list[r].time - f_list[l].time)) * (x - f_list[l].time)))  # υπολογισμός
        # εκτίμησης βάση των άκρων (γνωστή συνάρτηση τροποποιημένη για να δουλεύει στην python)

        if f_list[next].time == x:  # αν η 1η εκτίμηση ήταν επιτυχής επέστρεψε τον δείκτη next (θέση στην λίστα που
            # βρέθηκε το χ)
            return next
        if x > f_list[next].time:  # αν η τιμή χ είναι μεγαλύτερη της τιμής που δείχνει ο δείκτης next ρύθμισε το
            # αριστερό άκρο, διαφορετικά ρύθμισε το δεξί
            l = next + 1
        else:
            r = next - 1
    return -1


def better_binary_interpolation_search(list, x):
    l = 0
    r = len(list) - 1
    next = l + math.ceil(((float(r - l) / (list[r].time - list[l].time)) * (x - list[l].time)))  # Το βήμα που πρέπει να γίνει για να χωρίσουμε τον κώδικα σε κομμάτια για την πιο αποδοτική και γρήγορη αναζήτηση
    while x != list[next].time and l < r:  # Αναζήτηση του στοιχείου
        i = 0
        size = r - l + 1  # Μέγεθος λίστας
        if size <= 3:
            for k in range(0, r):
                if list[next].time == x:
                    return next
        if x > list[next].time:  # Αν το x είναι μεγαλύτερο απο την τιμή της λίστας στο σημείο next τότε
            while x > list[next + i * int(abs(math.sqrt(size))) - 1].time:  # Ψάχνει σε σημεία με διαφορετικό next, χώριντας πάλι τον κωδικο σε κομμάτια, σε αυτη τη περίπτωση σε μεγαλύτερα νούμερα.
                i = 2 * i + 1  # Αντί για i= i + 1 για την βελτίωση του χρόνου της χειρότερης περίπτωησης. Επίσης μας
                # δείχνει το επομενο βήμα.
                # Αλλάζουμε τα άκρα κατάλληλα για να την συνέχιση αναζήτισης στο επόμενο πεδίο.
                r = next + i * int(abs(math.sqrt(size)))
                l = next +(i - 1) * int(abs(math.sqrt(size)))
        if x < list[next].time:  # Αν το x είναι μικρότερο απο την τιμή της λίστας στο σημείο next τότε
            while x < list[next - i * int(abs(math.sqrt(size) + 1))].time:
                i = 2 * i + 1
                # Αλλάζουμε τα άκρα κατάλληλα για να την συνέχιση αναζήτισης στο επόμενο πεδίο.
                r = next - (i - 1) * int(abs(math.sqrt(size)))
                l = next - i * int(abs(math.sqrt(size)))
        next = l + math.ceil(((float(r - l) / (list[r].time - list[l].time)) * (x - list[l].time)))
    if list[next].time == x:  # Αν βρηκαμε το στοιχείο τοτε μας περιστρεφει το σημείο που βρίσκεται.
        return next
    else:
        return -1


def binary_interpolation_search(list, x):
    l = 0
    r = len(list) - 1
    next = l + math.ceil(((float(r - l) / (list[r].time - list[l].time)) * (x - list[l].time)))  # Το βήμα που πρέπει
    # να γίνει για να χωρίσουμε τον κώδικα σε κομμάτια για την πιο αποδοτική και γρήγορη αναζήτηση
    while x != list[next].time and l < r:  # Αναζήτηση του στοιχείου
        i = 0
        size = r - l + 1  # Μέγεθος λίστας
        if size <= 3:
            for k in range(0, r):
                if list[next].time == x:
                    return next
        if x > list[next].time:  # Αν το x είναι μεγαλύτερο απο την τιμή της λίστας στο σημείο next τότε
            while x > list[next + i * int(abs(math.sqrt(size))) - 1].time:  # Ψάχνει σε σημεία με διαφορετικό next,
                # χώριντας πάλι τον κωδικο σε κομμάτια, σε αυτη τη περίπτωση σε μεγαλύτερα νούμερα.
                i += 1
                # Αλλάζουμε τα άκρα κατάλληλα για να την συνέχιση αναζήτισης στο επόμενο πεδίο.
                r = next + i * int(abs(math.sqrt(size)))
                l = next +(i - 1) * int(abs(math.sqrt(size)))
        if x < list[next].time:  # Αν το x είναι μικρότερο απο την τιμή της λίστας στο σημείο next τότε
            while x < list[next - i * int(abs(math.sqrt(size) + 1))].time:
                i +=1
                # Αλλάζουμε τα άκρα κατάλληλα για να την συνέχιση αναζήτισης στο επόμενο πεδίο.
                r = next - (i - 1) * int(abs(math.sqrt(size)))
                l = next - i * int(abs(math.sqrt(size)))
        next = l + math.ceil(((float(r - l) / (list[r].time - list[l].time)) * (x - list[l].time)))
    if list[next].time == x:  # Αν βρηκαμε το στοιχείο τοτε μας περιστρεφει το σημείο που βρίσκεται.
        return next
    else:
        return -1


def find_max(f_list):  # Έρευση μεγίστου
    max = f_list[0].value  # Ορισμός πρώτης τιμής ως μέγιστο
    for i in range(0, len(f_list)):  # Σύγκριση όλων των τιμών της λιστάς, αποθηκεύωντας το τρέχων μέγιστο κάθε φορά
        x = f_list[i].value
        if x > max:
            max = x
    return max  # ΕΠιστροφή μεγίστου


def find_lower(f_list):  # Έρευση ελαχίστου
    lower = f_list[0].value  # Ορισμός πρώτης τιμής ως ελάχιστο
    for i in range(0, len(f_list)):  # Σύγκριση όλων των τιμών της λιστάς, αποθηκεύωντας το τρέχων ελάχιστο κάθε φορά
        x = f_list[i].value
        if x < lower:
            lower = x
    return lower  # Επιστροφή ελάχιστου


def counting_sort(f_list):
    max = find_max(f_list)  # Εύρεση μεγίστου και ελαχίστου για να οριστούν τα όρια του πίνακα count
    lower = find_lower(f_list)
    k = 0  # Διορθωτής σε περίπτωση που ο ελάχιστος είναι και αρνητικός
    count = []
    if lower < 0:  # Διόρθωση, ώστε να μην υπολογίζονται αρνητικοί index για τον πίνακα. Η διόρθωση φαίνεται και όπου
        # υπάρχει +k
        k = 0 - lower
        max += k
    for i in range(0, max + 1):  # Ορισμός θέσεων στον count, τόσες όσοι είναι και οι αριθμοι μεταξύ lower και max
        count.append(0)
    for i in range(0, len(f_list)):  # Μέτρηση εμφάνισης κάθε αριθμόυ
        x = f_list[i].value
        count[x + k] += 1

    for x in range(1, len(count)):  # Πρόσθεση της προηγούμενης θέσης του count στην επόμενη για κάθε θέση,
        # για να δείχνει την θέση στην οποία πρέπει να τοποθετηθεί ο κάθε αριθμός
        count[x] = count[x] + count[x - 1]

    sorted = f_list.copy()  # Αντιγραφή λίστας ώστε να χρησιμοποιηθεί ως ο ταξινομημένος πίνακας

    for x in range(len(f_list) - 1, -1, -1):  # Ταξινόμηση με την χρήση του count. Κάθε φορα που τοποθετούμε εναν
        # αριθμό στην σωστή θέση, αφαιρούμε 1 από την αντίστοιχη θέση του στο count
        sorted[count[f_list[x].value + k] - 1] = f_list[x]
        count[f_list[x].value + k] -= 1
    return sorted


def ch_index(day):  # Υπολογισμός θέσης στο table
    sum = 0
    i = 0
    while i < len(day):  # Άθροισμα των ASCII χαρακτήρα
        sum += ord(day[i])  # Το ord κανει μετατροπή του χαρακτήρα στην τιμή του στο ASCII
        i += 1
    return sum % 7  # Επιστροφή θέσης


def ch_insert(table, date_array, key):
    table[ch_index(date_array[key].day)].append(date_array[key])  # Χρήση της μεθόδου υπολογισμού της θέσης ώστε το
    # επόμενο στοιχείο να τοποθετηθεί στην επόμενη κενή θέση της λίστας της σωστής θέσης


def ch_search(table, day):
    i = 0
    while i < len(table[ch_index(day)]):  # Σειριακή αναζήτηση στην λίστα στην οποία τοποθετήθηκε η συγκεκριμένη μέρα
        if table[ch_index(day)][i].day == day:
            return i  # Αν βρεθεί η μέρα, επιστρέφει την θέση της στην λίστα
        i = i + 1
    print("That day does not exist in the database\n")
    time.sleep(1)
    return None  # Αν δεν βρεθεί η μέρα, επιστρέφει None


def ch_delete(table, day):
    i = ch_search(table, day)  # Αποθηκεύει στο i την θέση της μέρας στην λίστα
    if i is not None:  # Αν βρέθηκε η μέρα
        while i < len(table[ch_index(day)]) - 1:  # Αν δεν είναι το τελευταίο στοιχείο της λίστας, το εναλλάσει με το
            # δεξίο του μέχρι να γίνει το τελευταίο
            table[ch_index(day)][i], table[ch_index(day)][i + 1] = table[ch_index(day)][i + 1], table[ch_index(day)][i]
            i += 1
        del table[ch_index(day)][i]  # Διαγραφή
        print("Deletion successful\n")
        time.sleep(1)


def bst_insert(node, day, average_temp, day_int):
    if node is None:  # Δημιουργία κόμβου όταν φτάσει στην σωστή θέση όπου δεν υπάρχει κόμβος
        return BstDate(day, average_temp, day_int)

    if day_int < node.day_int:  # Αν ο κόμβος που πάμε να κάνουμε insert είναι μικρότερος από τον τρέχων κόμβο,
        # κατεβαίνει προς τα αριστερά
        lchild = bst_insert(node.left, day, average_temp, day_int)
        node.left = lchild  # Ενημέρωση των δεικτών
        lchild.parent = node

    elif day_int > node.day_int:  # Αν ο κόμβος που πάμε να κάνουμε insert είναι μεγαλύτερος από τον τρέχων κόμβο,
        # κατεβαίνει προς τα δεξιά
        rchild = bst_insert(node.right, day, average_temp, day_int)
        node.right = rchild  # Ενημέρωση δεικτών
        rchild.parent = node

    return node  # Επιστροφή τρέχων κόμβου


def bst_insert_temperature(node, day, average_temp, day_int):  # Ομοίως με BST_Insert, απλά για το BST με βάση την
    # μέση θερμοκρασία.

    if node is None:
        return BstDate(day, average_temp, day_int)

    elif average_temp <= node.average_temp:  # Η μόνη αλλαγή είναι η περίπτωση ισότητας, οπού πάλι κατεβαίνει αριστερά
        lchild = bst_insert_temperature(node.left, day, average_temp, day_int)
        node.left = lchild
        lchild.parent = node

    elif average_temp > node.average_temp:
        rchild = bst_insert_temperature(node.right, day, average_temp, day_int)
        node.right = rchild
        rchild.parent = node

    return node


def bst_inorder(node):
    if node is not None:  # Αν ο κόμβος δεν είναι κενός, καλέι την μέθοδο πρώτα στο αριστερο του παιδί, μετά τυπώνει
        # τον εαυτό του, και μετά καλεί την μέθοδο στο δεξί του παιδί.
        bst_inorder(node.left)
        print("Date :", node.day, " | Average Temperature: ", node.average_temp)
        bst_inorder(node.right)
    # Η μέθοδος καλείται και σε παιδία που είναι None, αλλά δεν δημιουργεί πρόβλημα για απλά δεν θα τηρηθεί η συνθήκη.


def bst_search(node, day):
    if day == node.day_int:  # Αν η τιμή του κόμβου που ψάχνουμε είναι ίση με το day.
        return node  # Επιστρόφη του κόμβου.
    elif day < node.day_int:  # Αν το day είναι μικρότερο του κόμβου.
        return bst_search(node.left,
                          day)  # Κάνε αναζήτηση στον αριστερό κόμβο, αφού εκέι θα υπάρχουν οι μικρότεροι αριθμοί.
    elif day > node.day_int:  # Αν το day είναι μεγαλύτερο του κόμβου.
        return bst_search(node.right,
                          day)  # Κάνε αναζήτηση στον δεξιό κόμβο, αφού εκεί θα υπάρχουν οι μεγαλύτεροι αριθμοί.
    else:  # Αν δεν υπάρχει.
        print("Day was not found.\n Try again!")
        time.sleep(1)
        return None  # Επέστρεψε τίποτα.


def bst_new_temperature(node, day, new_temp):
    temp = bst_search(node, day)  # Αναζήτηση του Day στο δέντρο και επιστροφή του σημείου που βρίσκεται.
    if temp is not None:  # Αν το σημείο εχει βρεθεί, δηλαδή δεν είναι το τίποτα.
        temp.average_temp = new_temp  # Εισχώρηση της τιμής που θέλουμε, και αλλαγή της θερμοκρασίας.
        print("Temperature changed successfully")
        time.sleep(1)


def bst_max_value(node):  # Εύρεση του μεγαλύτερης τιμής
    temp = node
    while temp.right is not None:  # Ο βρόχος επαναλαμβάνετε μέχρι ο κόμβος να μην εχει κομβους - παιδιά. Αυτο
        # γίνεται γιατί αν δεν υπαρχουν κόμβοι - παιδία, δεν υπάρχει μεγαλύτερη τιμή

        temp = temp.right  # Κάθε φορά το βάζουμε να αντιστοιχεί με το δεξιό κλάδο γιατί το Binary Search Tree λόγω
        # της κατασκευής του έχει τη μεγαλύτερη τιμή στο δεξιό κλάδο.

    return temp


def bst_min_value(node):  # Εύρεση του μικρότερης τιμής
    temp = node
    while temp.left is not None:  # Ο βρόχος επαναλαμβάνετε μέχρι ο κόμβος να μην εχει κομβους - παιδιά. Αυτο γίνεται
        # γιατί αν δεν υπαρχουν κόμβοι - παιδία, δεν υπάρχει μικρότερη τιμή

        temp = temp.left  # Κάθε φορά το βάζουμε να αντιστοιχεί με το αριστερό κλάδο γιατί το Binary Search Tree λόγω
        # της κατασκευής του έχει τη μικρότερη τιμή στο αριστερό κλάδο.

    return temp


def bst_delete(node, day):
    if node is None:  # Αν ο κόμβος δεν υπάρχει
        return node

    if day < node.day_int:  # Αν το day είναι μικρότερο απο τη τιμή του κόμβου.
        node.left = bst_delete(node.left, day)  # Τότε βρίσκεται στο δεξιό υποδέντρο, άρα πρεπει να ξαναεφαρμοστεί ο
        # κώδικας για το δεξιό υποδέντρο.

    elif day > node.day_int:  # Αν το day είναι μεγαλύτερο απο τη τιμή του κόμβου.
        node.right = bst_delete(node.right, day)  # Τότε βρίσκεται στο αριστερό υποδέντρο, άρα πρεπει να
        # ξαναεφαρμοστεί ο κώδικας για το αριστερό υποδέντρο.

    else:  # Αν το day είναι ίσο με το κόμβο, ο κόμβος αυτός θα διαγραφεί και θα πρέπει να πάρει τη θεση του ένας αλλος.
        # Αν ο κόμβος έχει ένα ή κανένα κόμβους-παιδιά.
        if node.left is None:  # Αν ο αριστέρος κόμβος είναι το τίποτα, ο δεξιός ανεβαίνει.
            temp = node.right
            del node
            return temp
        elif node.right is None:  # Αν ο δεξιός κόμβος είναι το τίποτα, ο αριστερός ανεβαίνει.
            temp = node.left
            del node
            return temp
        temp = bst_min_value(node.right)  # Αν ο κόμβος εχει δύο  κόμβους - παιδιά, τότε πρέπρει ν'ανέβει ο μικρότερος
        # κομβος, δηλαδή απο το δεξιό υποδέντρο.
        node.day = temp.day
        node.right = bst_delete(node.right, temp.day_int)  # Επανάληξη της μέθοδου BST_Delete για την διαγραφη και
        # μετακίνηση των κόμβων.
    return node


with open('tempm.txt', 'r') as f:  # Άνοιγμα αρχείου θερμοκρασιών, το οποίο θα κλείσει μόλις τελειώσει το with

    temp_string = f.read()  # Μετατροπή ολόκληρου του αρχείου σε ενα string
    temp_string = temp_string.replace('{', '')  # Αντικατάσταση των "άχρηστων" χαρακτήρων
    temp_string = temp_string.replace('}', '')
    temp_string = temp_string.replace('\n', ', ')
    temp_string = temp_string.replace('.0', '')
    temp_timestamp_list = temp_string.split(
        ', ')  # Χωρισμός κάθε timestamp (μαζι με την θερμοκρασία του) ως στοιχείο ενός πίνακα

    temperature_list = []  # Δημιουργία πίνακα μόνο για θερμοκρασία
    i = 0
    while i < len(temp_timestamp_list) - 1:  # Διατρέχουμε τον πίνακα για να αποθήκεύσουμε τις μόνο θερμοκράσιες
        if len(temp_timestamp_list[i]) == 27:  # Έλεγχος μεγέθους timestamp για να γνωρίζουμε αν η θερμοκρασία είναι
            # μονοψήφίος ή διψήφιος αριθμός
            temperature_list.append(int(temp_timestamp_list[i][24:26]))
        else:
            temperature_list.append(int(temp_timestamp_list[i][24]))
        i += 1

with open('hum.txt', 'r') as f:  # Ομοίως με αρχείο θερμοκρασίας

    temp_string = f.read()
    temp_string = temp_string.replace('{', '')
    temp_string = temp_string.replace('}', '')
    temp_string = temp_string.replace('\n', ', ')
    temp_string = temp_string.replace('.0', '')
    hum_timestamp_list = temp_string.split(', ')

    humidity_list = []
    i = 0
    while i < len(hum_timestamp_list) - 1:
        if len(hum_timestamp_list[i]) == 27:
            humidity_list.append(int(hum_timestamp_list[i][24:26]))
        elif len(hum_timestamp_list[i]) == 28:
            humidity_list.append(int(hum_timestamp_list[i][24:27]))
        else:
            humidity_list.append(int(hum_timestamp_list[i][24]))
        i += 1


class BstDate:
    """Δημιουργία Class για το BST. Χρησιμοποιεί την ημέρα σε string ως day και την μέση θερμοκρασία ως average_temp
       για τις απαιτήσεις της άσκησης, την ημέρα σε integer ως day_int για την ευκολία εκτέλεσης πράξεων, και τους
       δείκτες right, left και parent για να κρατά τις σχέσεις μεταξύ των αντικειμένων."""

    def __init__(self, day, average_temp=0.0, day_int=0):
        self.day = day
        self.average_temp = average_temp
        self.day_int = day_int
        self.right = None
        self.left = None
        self.parent = None


class Date:
    """Δημιουργία Class για την χρήση στο Hashing. Χρησιμοποιεί την ημέρα σε string ως day και την μέση θερμοκρασία ως
    average_temp για τις απαιτήσεις της άσκησης, την ημέρα σε integer ως day_int για την ευκολία εκτέλεσης πράξεων"""

    def __init__(self, day, average_temp=0.0):
        self.day = day
        self.average_temp = average_temp
        self.day_int = 0


class Timestamp:
    """Δημιουργία Class για χρήση στο part I. Αποθηκεύει το timestamp με την θερμοκρασία/υγρασία σε μορφη string,
       και την θερμοκρασία/υγρασία στο value και τον χρόνο στο time σε μοργη integer για την ευκολία συγκρίσεων."""

    def __init__(self, timestamp, value, time):
        self.timestamp = timestamp
        self.value = value
        self.time = time


temp_class_list = []  # Πίνακες για την αποθήκευση των timestamps στην μορφή του Timestamp Class
hum_class_list = []

i = 0
while i < len(temp_timestamp_list) - 1:  # Αποθήκευση θερμοκρασιών σε μορφη Timestamp Class
    x = temp_timestamp_list[i][1:20]
    x = x.replace("-", "")
    x = x.replace(":", "")
    x = x.replace("T", "")
    temp_class_list.append(Timestamp(temp_timestamp_list[i], temperature_list[i], int(x)))
    i += 1

i = 0

while i < len(hum_timestamp_list) - 1:  # Αποθήκευση υγρασιών σε μορφη Timestamp Class
    x = temp_timestamp_list[i][1:20]
    x = x.replace("-", "")
    x = x.replace(":", "")
    x = x.replace("T", "")
    hum_class_list.append(Timestamp(hum_timestamp_list[i], humidity_list[i], int(x)))
    i += 1

date_array = []  # Πίνακας για αποθήκευση όλων των ημερών σε μορφή του Class Date
index_day = 0
i = 0
j = 0
total_sum = 0
n = 0
first = 1
while i <= len(temp_timestamp_list) - 1:  # Αποθήκευση στο date_array
    if index_day != temp_timestamp_list[i][1:11] and first == 1:  # Εκτελείται στο πρώτο timestamp κάθε μέρας
        date_array.append(Date(temp_timestamp_list[i][1:11]))
        date_array[j].day_int = int(date_array[j].day.replace('-', ''))
        index_day = temp_timestamp_list[i][1:11]  # Αποθήκευση μέρας ώστε να γνωρίζουμε αν άλλαξε
        n = 1
        total_sum = temperature_list[
            i]  # Ξεκινάει το άθροισμα των μετρήσεων της ημέρας για τον υπολογισμό της μέσης θερμοκρασίας
        first = 0
    elif index_day == temp_timestamp_list[i][1:11]:  # Εκτελείται αν δεν άλλαξε η μέρα οσό διατρέχουμε τα timestamps
        total_sum += temperature_list[i]
        n += 1
    else:  # Εκτελείται μόλις αλλάξει η μέρα όσο διατρέχουμε τα timestamps.
        date_array[j].average_temp = round(total_sum / n, 3)  # Υπολογίζει και αποθηκεύει την μέση θερμοκρασία
        j += 1
        first = 1
    i += 1
i = 0
j = 0

# Δημιουργία λίστας ταξινομημένη με βάση τον χρόνο για το 3) και 4) του part I
hum_time_list = time_merge_sort(hum_class_list, 0, len(hum_class_list) - 1)
temp_time_list = time_merge_sort(temp_class_list, 0, len(temp_class_list) - 1)


"""Δημιουργία μενού για εκτέλεση όλων των part του πρότζεκτ. Αποτελείται από μεταβλήτες choice που αποθηκεύουν τις 
επιλογές του χρήστη και από while και ifs που εκτελούν τις επιλογές σε κάθε 'υπο-μενού'. ΕΠίσης υπάρχει αμυντικός 
προγραμματισμός για λανθασμένες επιλογές του χρήστη."""
choice1 = "0"
choice2 = "0"
choice3 = "0"
choice4 = "0"
choice5 = "0"
file_choice = "0"
while choice1 != "3":
    choice1 = input("Choose part 1 or part 2 of the project by typing 1 or 2, or 3 to exit\n")
    if choice1 == "1":
        while choice2 != "exit":
            choice2 = input("Choose which sub-part of part I you want to run from 1 to 4, or type exit to return.\n")
            if choice2 == "1":
                merge_sort_list = temp_class_list.copy()  # Δημιουργία αντιγράφων μη-ταξινομημένης λίστας
                quick_sort_list = temp_class_list.copy()
                n1 = time.time()  # Χρόνος πριν την εκτέλεση
                merge_sort_sorted = merge_sort(merge_sort_list, 0, len(merge_sort_list) - 1)  # Εκτέλεση ταξινόμησης
                n2 = time.time()  # Χρόνος μετά την εκτέλεση
                merge_time = n2 - n1  # Υπολογισμός χρόνου εκτέλεσης
                n1 = time.time()
                quick_sort(quick_sort_list)
                n2 = time.time()
                quick_time = n2 - n1  # Υπολογισμός χρόνου εκτέλεσης
                print("Merge Sort result:")
                i = 0
                while i < len(temp_time_list) - 1:
                    print(merge_sort_sorted[i].timestamp)
                    i += 1
                time.sleep(2)
                print("Quick Sort result:")
                i = 0
                while i < len(temp_time_list) - 1:
                    print(quick_sort_list[i].timestamp)
                    i += 1
                print("Merge Sort runtime: ", merge_time, " | Quick Sort runtime: ", quick_time)
                time.sleep(2)
                del merge_sort_list
                del quick_sort_list
                del merge_sort_sorted
            elif choice2 == "2":
                heap_sort_list = hum_class_list.copy()  # Δημιουργία αντιγράφων μη-ταξινομημένης λίστας
                counting_sort_list = hum_class_list.copy()
                n1 = time.time()  # Χρόνος πριν την εκτέλεση
                build_max_heap(heap_sort_list)  # Εκτέλεση ταξινόμησης
                n2 = time.time()  # Χρόνος μετά την εκτέλεση
                heap_time = n2 - n1  # Υπολογισμός χρόνου εκτέλεσης
                n1 = time.time()
                counting_sort_sorted = counting_sort(counting_sort_list)
                n2 = time.time()
                counting_time = n2 - n1  # Υπολογισμός χρόνου εκτέλεσης
                print("Heap Sort result:")
                i = 0
                while i < len(hum_class_list):
                    print(heap_sort_list[i].timestamp)
                    i += 1
                time.sleep(2)
                print("Counting Sort result:")
                i = 0
                while i < len(hum_class_list):
                    print(counting_sort_sorted[i].timestamp)
                    i += 1
                print("Heap Sort runtime: ", heap_time, " | Counting Sort runtime: ", counting_time)
                del heap_sort_list
                del counting_sort_list
                del counting_sort_sorted
            elif choice2 == "3":
                while file_choice != "3":
                    file_choice = input("Choose to search for temperature by typing 1 or humidity by typing 2\n")
                    if file_choice == "1":
                        x = input("Insert the day you are searching for (using the format Year-Month-DayT00:00:00)\n")
                        x = x.replace("-", "")
                        x = x.replace(":", "")
                        x = x.replace("T", "")
                        n1 = time.time()  # Χρόνος πριν την εκτέλεση
                        r1 = binary_search(temp_time_list, int(x))  # Εκτέλεση αναζήτησης
                        n2 = time.time()  # Χρόνος μετά την εκτέλεση
                        binary_time = n2 - n1  # Υπολογισμός χρόνου εκτέλεσης
                        n1 = time.time()
                        r2 = interpolation_search(temp_time_list, int(x))
                        n2 = time.time()
                        interpolation_time = n2 - n1
                        if r1 != -1:
                            print("Binary Search result: ", temp_time_list[r1].timestamp)
                        else:
                            print("That timestamp doesn't exist in the database")
                        if r2 != -1:
                            print("Interpolation Search Result: ", temp_time_list[r2].timestamp)
                        else:
                            print("That timestamp doesn't exist in the database")
                        print("Binary Search runtime: ", binary_time, " | Interpolation runtime: ", interpolation_time)
                        file_choice = "3"
                    elif file_choice == "2":
                        x = input("Insert the day you are searching for (using the format Year-Month-DayT00:00:00)\n")
                        x = x.replace("-", "")
                        x = x.replace(":", "")
                        x = x.replace("T", "")
                        n1 = time.time()  # Χρόνος πριν την εκτέλεση
                        r1 = binary_search(hum_time_list, int(x))  # Εκτέλεση αναζήτησης
                        n2 = time.time()  # Χρόνος μετά την εκτέλεση
                        binary_time = n2 - n1  # Υπολογισμός χρόνου εκτέλεσης
                        n1 = time.time()
                        r2 = interpolation_search(hum_time_list, int(x))
                        n2 = time.time()
                        interpolation_time = n2 - n1
                        if r1 != -1:
                            print("Binary Search result: ", hum_time_list[r1].timestamp)
                        else:
                            print("That timestamp doesn't exist in the database")
                        if r2 != -1:
                            print("Interpolation Search Result: ", hum_time_list[r2].timestamp)
                        else:
                            print("That timestamp doesn't exist in the database")
                        print("Binary Search runtime: ", binary_time, " | Interpolation runtime: ", interpolation_time)
                        file_choice = "3"
                    else:
                        print("Wrong choice! Try again though.")
                        time.sleep(2)
                file_choice = "0"
            elif choice2 == "4":
                while file_choice != "3":
                    file_choice = input("Choose to search for temperature by typing 1 or humidity by typing 2\n")
                    if file_choice == "1":
                        x = input("Insert the day you are searching for (using the format Year-Month-DayT00:00:00)\n")
                        x = x.replace("-", "")
                        x = x.replace(":", "")
                        x = x.replace("T", "")
                        n1 = time.time()  # Χρόνος πριν την εκτέλεση
                        r1 = binary_interpolation_search(temp_time_list, int(x))  # Εκτέλεση αναζήτησης
                        n2 = time.time()  # Χρόνος μετά την εκτέλεση
                        bis_time = n2 - n1  # Υπολογισμός χρόνου εκτέλεσης
                        n1 = time.time()
                        r2 = better_binary_interpolation_search(temp_time_list, int(x))
                        n2 = time.time()
                        bbis_time = n2 - n1
                        if r1 != -1:
                            print("Binary Interpolation Search result: ", temp_time_list[r1].timestamp)
                        else:
                            print("That timestamp doesn't exist in the database")
                        if r2 != -1:
                            print("Better Binary Interpolation Search Search Result: ", temp_time_list[r2].timestamp)
                        else:
                            print("That timestamp doesn't exist in the database")
                        print("Binary Interpolation Search runtime: ", bis_time,
                              " | Better Binary Interpolation Search runtime: ", bbis_time)
                        file_choice = "3"
                    elif file_choice == "2":
                        x = input("Insert the day you are searching for (using the format Year-Month-DayT00:00:00)\n")
                        x = x.replace("-", "")
                        x = x.replace(":", "")
                        x = x.replace("T", "")
                        n1 = time.time()  # Χρόνος πριν την εκτέλεση
                        r1 = binary_interpolation_search(hum_time_list, int(x))  # Εκτέλεση αναζήτησης
                        n2 = time.time()  # Χρόνος μετά την εκτέλεση
                        bis_time = n2 - n1  # Υπολογισμός χρόνου εκτέλεσης
                        n1 = time.time()
                        r2 = better_binary_interpolation_search(hum_time_list, int(x))
                        n2 = time.time()
                        bbis_time = n2 - n1
                        if r1 != -1:
                            print("Binary Interpolation Search result: ", hum_time_list[r1].timestamp)
                        else:
                            print("That timestamp doesn't exist in the database")
                        if r2 != -1:
                            print("Better Binary Interpolation Search Search Result: ", hum_time_list[r2].timestamp)
                        else:
                            print("That timestamp doesn't exist in the database")
                        print("Binary Interpolation Search runtime: ", bis_time,
                              " | Better Binary Interpolation Search runtime: ", bbis_time)
                        file_choice = "3"
                    else:
                        print("Wrong choice! Try again though.")
                        time.sleep(2)
                file_choice = "0"
            elif choice2 == "exit":
                print("Returning...")
                time.sleep(1)
            else:
                print("Wrong choice! Try again though.")
                time.sleep(2)
        choice2 = "0"
    elif choice1 == "2":
        while choice3 != "exit":
            choice3 = input("Choose whether to load the file into a BST structure by typing 1 or a Chained Hashing "
                            "structure by typing 2, or exit to return.\n")
            if choice3 == "1":
                while choice4 != "exit":
                    choice4 = input("Choose if the Binary Search Tree is sorted based on the date by typing 1, "
                                    "or sorted based on the average temperature by typing 2, or exit to return.\n")
                    if choice4 == "1":
                        left = 0
                        right = len(date_array) - 1
                        middle = (len(date_array) - 1) // 2
                        pointer = 0
                        root = None
                        root = bst_insert(root, date_array[middle].day, date_array[middle].average_temp,
                                          date_array[middle].day_int)
                        """Δημιουργία του BST κινούμενοι από την μέση προς τα άκρα του ταξινομημένου date_array, 
                        αποθηκέυοντας εναλλάξ κάθε φορά την θέση που απέχει +- την τιμή του pointer απο το κέντρο """
                        while middle - pointer >= left or middle + pointer <= right:
                            pointer += 1
                            if middle - pointer >= left:
                                bst_insert(root, date_array[middle - pointer].day,
                                           date_array[middle - pointer].average_temp,
                                           date_array[middle - pointer].day_int)
                            if middle + pointer <= right:
                                bst_insert(root, date_array[middle + pointer].day,
                                           date_array[middle + pointer].average_temp,
                                           date_array[middle + pointer].day_int)
                        while choice5 != "5":
                            choice5 = input("Choose one of the following options by typing it's number:\n1: Show "
                                            "Inorder Tree Traversal\n2: Search for the average temperature of a "
                                            "certain day\n3: Change the average temperature of a certain day\n4: "
                                            "Delete a day\n5: Exit program\n")
                            if choice5 == "1":
                                bst_inorder(root)
                                stall = input("\nPress enter to go back to the menu.\n")
                            elif choice5 == "2":
                                x = input("Insert the day you are searching for (using the format Year-Month-Day)\n")
                                x = int(x.replace('-', ''))
                                found_day = bst_search(root, x)
                                if found_day is not None:
                                    print("The average temperature of the day: ", found_day.day, " is: ",
                                          found_day.average_temp)
                                    stall = input("\nPress enter to go back to the menu.\n")
                            elif choice5 == "3":
                                x = input("Insert the day of which the average temperature you want to change (using "
                                          "the format Year-Month-Day)\n")
                                x = int(x.replace('-', ''))
                                new_temp = input("Insert the new average temperature in float form\n")
                                bst_new_temperature(root, x, new_temp)
                            elif choice5 == "4":
                                x = input("Insert the day which you want to delete (using the format Year-Month-Day)\n")
                                x = int(x.replace('-', ''))
                                bst_delete(root, x)
                            elif choice5 == "5":
                                print("Returning...")
                                time.sleep(1)
                            else:
                                print("Wrong choice! Try again though.")
                                time.sleep(2)
                        choice5 = 0
                        while pointer != middle:
                            pointer -= 1
                            if middle - pointer <= middle:
                                bst_delete(root, date_array[middle - pointer].day_int)
                            if middle + pointer >= middle:
                                bst_delete(root, date_array[middle + pointer].day_int)
                        del left, right, middle, pointer
                    elif choice4 == "2":
                        pointer = 0
                        left = 0
                        right = len(date_array) - 1
                        middle = (len(date_array) - 1) // 2
                        root_temp = None
                        """Δημιουργία του BST κινούμενοι από την μέση προς τα άκρα του ταξινομημένου date_array,
                         αποθηκέυοντας εναλλάξ κάθε φορά την θέση που απέχει +- την τιμή του pointer απο το κέντρο"""
                        root_temp = bst_insert_temperature(root_temp, date_array[middle].day,
                                                           date_array[middle].average_temp, date_array[middle].day_int)
                        while middle - pointer >= left or middle + pointer <= right:
                            pointer += 1
                            if middle - pointer >= left:
                                bst_insert_temperature(root_temp, date_array[middle - pointer].day,
                                                       date_array[middle - pointer].average_temp,
                                                       date_array[middle - pointer].day_int)
                            if middle + pointer <= right:
                                bst_insert_temperature(root_temp, date_array[middle + pointer].day,
                                                       date_array[middle + pointer].average_temp,
                                                       date_array[middle + pointer].day_int)
                        while choice5 != "3":
                            choice5 = input("Choose one of the following options by typing it's number:\n1: Find the "
                                            "day with the lowest average temperature\n2: Find the day with the "
                                            "highest average temperature\n3: Exit program\n")
                            if choice5 == "1":
                                found_day = bst_min_value(root_temp)
                                print("The average temperature of the day: ", found_day.day,
                                      " ,which is the lowest average temperature is: ", found_day.average_temp)
                                stall = input("\nPress enter to go back to the menu.\n")
                            elif choice5 == "2":
                                found_day = bst_max_value(root_temp)
                                print("The average temperature of the day: ", found_day.day,
                                      " ,which is the highest average temperature, is: ", found_day.average_temp)
                                stall = input("\nPress enter to go back to the menu.\n")
                            elif choice5 == "3":
                                print("Returning...")
                                time.sleep(1)
                            else:
                                print("Wrong choice! Try again though.")
                                time.sleep(2)
                        while pointer != middle:
                            pointer -= 1
                            if middle - pointer <= middle:
                                bst_delete(root_temp, date_array[middle - pointer].day_int)
                            if middle + pointer >= middle:
                                bst_delete(root_temp, date_array[middle + pointer].day_int)
                        del left, right, middle, pointer
                        choice5 = "0"
                    elif choice4 == "exit":
                        print("Returning...")
                        time.sleep(1)
                    else:
                        print("Wrong choice! Try again though.")
                        time.sleep(2)
                choice4 = "0"
            elif choice3 == "2":
                hash_table = []
                for i in range(0, 7):
                    hash_table.append([])
                for i in range(0, len(date_array)):
                    ch_insert(hash_table, date_array, i)  # Τοποθετεί ένα ένα τα στοιχεία στο hashing table
                while choice5 != "4":
                    choice5 = input("Choose one of the following options by typing it's number:\n\n1: Search for the "
                                    "average temperature of a certain day\n2: Change the average temperature of a "
                                    "certain day\n3: Delete a day\n4: Return\n")
                    if choice5 == "1":
                        x = input("Insert the day you are searching for (using the format Year-Month-Day)\n")
                        search = ch_search(hash_table, x)
                        if search is not None:
                            found_day = hash_table[ch_index(x)][search]
                            print("The average temperature of the day: ", found_day.day, " is: ",
                                  found_day.average_temp)
                            stall = input("\nPress enter to go back to the menu.\n")
                    elif choice5 == "2":
                        x = input("Insert the day of which the average temperature you want to change (using the "
                                  "format Year-Month-Day)\n")
                        search = ch_search(hash_table, x)
                        if search is not None:
                            found_day = hash_table[ch_index(x)][search]
                            new_temp = input("Insert the new average temperature in float form\n")
                            hash_table[ch_index(x)][search].average_temp = new_temp
                            print("Temperature changed successfully")
                            time.sleep(1)
                    elif choice5 == "3":
                        x = input("Insert the day which you want to delete (using the format Year-Month-Day)\n")
                        ch_delete(hash_table, x)
                    elif choice5 == "4":
                        print("Returning...")
                        time.sleep(1)
                    else:
                        print("Wrong choice! Try again though.")
                        time.sleep(2)
                choice5 = "0"
                del hash_table
            elif choice3 == "exit":
                print("Returning...")
                time.sleep(1)
            else:
                print("Wrong choice! Try again though.")
        choice3 = "0"
    elif choice1 == "3":
        print("Exiting...")
        time.sleep(2)
    else:
        print("Wrong choice! Try again though.")
