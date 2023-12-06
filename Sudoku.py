
#region #! THE INPUT PART
rows, cols = (9,9)
arr = [["   " for i in range(cols)] for j in range(rows)]
def print_array(arr):
    for x in arr:  # outer loop  
        for i in x:  # inner loop  
            print(i, end = "|") # print the elements  
        print() 
#print_array(arr)
def print_value(arr):
    x=0
    y=0
    for x in range (0,9):
        for y in range (0,9):
            print(arr[x][y].value, end="|")
        print()
#[1,2,3,4,5,6,7,8,9]
def print_index(arr):
    x=0
    y=0
    for x in range (0,9):
        for y in range (0,9):
            print(arr[x][y].index, end="|")
        print()

def print_probab(arr):
    x=0
    y=0
    for x in range (0,9):
        for y in range (0,9):
            print(arr[x][y].probab, end="|")
        print()

class placer:
    def __init__(self, index ,value, probable_values) -> None:
        self.index= index
        self.value= value
        self.probab= probable_values

for i in range(0,9):
    for j in range (0,9):
        arr[i][j] = placer(10*(i+1)+(j+1)," ", ["1", "2", "3", "4", "5", "6", "7", "8", "9"])

class Box:
    def __init__(self, id, placers) -> None:
        self.id=id
        self.placers=placers

#region   
B1=[arr[0][0], arr[0][1], arr[0][2], arr[1][0], arr[1][1], arr[1][2], arr[2][0], arr[2][1], arr[2][2]]
B2=[arr[0][3], arr[0][4], arr[0][5], arr[1][3], arr[1][4], arr[1][5], arr[2][3], arr[2][4], arr[2][5]]
B3=[arr[0][6], arr[0][7], arr[0][8], arr[1][6], arr[1][7], arr[1][8], arr[2][6], arr[2][7], arr[2][8]]
B4=[arr[3][0], arr[3][1], arr[3][2], arr[4][0], arr[4][1], arr[4][2], arr[5][0], arr[5][1], arr[5][2]]
B5=[arr[3][3], arr[3][4], arr[3][5], arr[4][3], arr[4][4], arr[4][5], arr[5][3], arr[5][4], arr[5][5]]
B6=[arr[3][6], arr[3][7], arr[3][8], arr[4][6], arr[4][7], arr[4][8], arr[5][6], arr[5][7], arr[5][8]]
B7=[arr[6][0], arr[6][1], arr[6][2], arr[7][0], arr[7][1], arr[7][2], arr[8][0], arr[8][1], arr[8][2]]
B8=[arr[6][3], arr[6][4], arr[6][5], arr[7][3], arr[7][4], arr[7][5], arr[8][3], arr[8][4], arr[8][5]]
B9=[arr[6][6], arr[6][7], arr[6][8], arr[7][6], arr[7][7], arr[7][8], arr[8][6], arr[8][7], arr[8][8]]
Box1=Box(1,B1)
Box2=Box(2,B2)
Box3=Box(3,B3)
Box4=Box(4,B4)
Box5=Box(5,B5)
Box6=Box(6,B6)
Box7=Box(7,B7)
Box8=Box(8,B8)
Box9=Box(9,B9)
Boxes=[Box1, Box2, Box3, Box4, Box5, Box6, Box7, Box8, Box9]
#endregion

def check_col(Array,inp,k,t):
    if inp !="" and inp !=" ":
        h=0
        C=[]
        for h in range (0,9):
            C.append(Array[h][k].value)                       #If t is 1, Check_col is True if there is only 1 number in the column and it is False if there are 2 numbers.
        if C.count(inp)>t: return False                         # If t is 0, check_col is True if there is no number and it is False if it only once
        else: return True
    elif inp=="" or inp==" ": return True
    else: return True

def check_row(Array,inp,h,t):
    if inp !="" and inp !=" ":
        k=0
        R=[]
        for k in range (0,9):
            R.append(Array[h][k].value)
        # print(R)
        # print(inp)
        # print(R.count(inp))
        if R.count(inp)>t: return False
        else: return True
    elif inp=="" or inp==" ": return True
    else: return True

def check_box(Array,inp,h,k,d):
    if inp !="" and inp !=" ":
        B=[]
        #? This loop finds out which box the given placer is in.
        for x in Boxes:
            if Array[h][k] in x.placers:
                box = x
            else:pass
        # box is the box(which is an object of class Box) {i.e. either Box1 or Box2} and id is the id of the box
        for t in box.placers:       # t is of type arr[i][j]
            B.append(t.value)
        if B.count(inp)>d: return False
        else: return True
    elif inp=="" or inp==" ": return True
    else: return True

def isvalid(Array,inp,h,k):
    if check_row(Array, inp, h, 1)==True and check_col(Array, inp, k, 1)==True and check_box(Array, inp, h, k, 1)==True: return True
    else: return False        

def zerotonine(inp):
    if inp in [""," ","1","2","3","4","5","6","7","8","9"]: return True
    else: return False

inp = input("Press Enter to start -->")
record=0
i=0
j=0
#This loop is for storing the given values in the sudoku
while (10*(i+1)+(j+1))!=101 and inp!="done":
    #print_array(arr)
    print_value(arr)
    print_index(arr)
    print("Please type the value to be entered in space numbered ",10*(i+1)+(j+1),"\n")
    print("If there is no given value then press Enter \n")
    inp=str(input("Given value = "))
    print("\n")
    if inp=="": inp=" "
    if zerotonine(inp) == True:
        arr[i][j].value = inp
        #print("inp=",inp)
        if check_col(arr, inp, j, 1)==False: print("Same number in column")
        if check_row(arr, inp, i, 1)==False: print("Same number in row")
        if check_box(arr, inp, i, j, 1)==False: print("Same number in box")
        #print(B)
        if isvalid(arr,inp,i,j)== True:
            if j==8: 
                j=0
                i=i+1
            else: j=j+1 
            if i==9 and j==2: inp="done"
            else: pass
            #print("EVERYTHING IS NORMAL")
        elif isvalid(arr,inp,i,j) == False: 
            print("The move is not valid")
        else: print("Something is wrong")
        record=record+1
    else: print("Value not accepted")
    B=[]
#endregion

print("\n")    #imp           zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz

#region #! THE SOLVING PART

def filled(x):
    if x.value != " ": return True
    else: return False

def removal(arr):
    for i in range (0,9):
        for j in range(0,9):
            if filled(arr[i][j])==True:
                arr[i][j].probab=[]

def clean(arr,i,j):
    val = arr[i][j].value
    #clean column
    for h in range(0,9):
        if val in arr[h][j].probab:
            arr[h][j].probab.remove(val)
    #clean row
    for k in range(0,9):
        if val in arr[i][k].probab:
            arr[i][k].probab.remove(val)
    #clean box
    for x in Boxes:
        if arr[i][j] in x.placers:
            box = x
    for t in box.placers:
        if val in t.probab:
            t.probab.remove(val)

def naked_single(arr):
    for i in range(0,9):  #? This loop removes the inputted value from the probab values
        for j in range (0,9):
            for x in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                if x in arr[i][j].probab:
                    #print("Probab of ",i+1,j+1,"is",arr[i][j].probab)
                    if check_col(arr,x,j,0)==False:
                        arr[i][j].probab.remove(x)             #! remove x from probab of arr[i][j] if it exists in the value of any placer present in the same Col already filled in the input part
                if x in arr[i][j].probab:
                    #print("Probab of ",i+1,j+1,"is",arr[i][j].probab)
                    if check_row(arr,x,i,0)==False:
                        arr[i][j].probab.remove(x)
                if x in arr[i][j].probab:
                    #print("Probab of ",i+1,j+1,"is",arr[i][j].probab)
                    if check_box(arr,x,i,j,0)==False: 
                        arr[i][j].probab.remove(x)
            if len(arr[i][j].probab) == 1:
                arr[i][j].value = arr[i][j].probab[0]

'''
for i in range(0,9):
    for j in range (0,9):
        if arr[i][j].value != " ":
            arr[i][j].probab = [arr[i][j].value]
        else: pass
'''
#~ Should the probab of filled placer be [], or [value]?   FINALLY DECIDED TO GO WITH THE SECOND ONE
#~ todo: The value of the placer is a string. Convert it to integer.
#~ or convert the array in line 43 to ["1", "2", "3", "4", "5", "6", "7", "8", "9"]   DONE THIS

#print_probab(arr)
i=0
j=0

def col(arr,k):
    C=[]
    for h in range(0,9):
        if filled(arr[h][k])==False:
            C.extend(arr[h][k].probab)
    C.sort()
    return C

def check_col_probab(arr,var,k):
    if var !="" and var !=" ":
        C=col(arr,k)
        if C.count(var)==1: return False          # If t is 0, check_col is True if there is another number and it is False if it only once
        else: return True
    elif var=="" or var==" ": return True
    else: return True

def row(arr,h):    #row(arr,h) is an array which is the collection of all the probab values in the row
    R=[]
    for k in range(0,9):
        if filled(arr[h][k])==False:
            R.extend(arr[h][k].probab)
    R.sort()
    return R

def check_row_probab(arr,var,h):
    if var !="" and var !=" ":
        R=row(arr,h)
        print("The R for row",h+1,"is",R)
        if R.count(var)==1: return False
        else: return True
    elif var=="" or var==" ": return True
    else: return True

def box(arr,h,k):
    B=[]
    for x in Boxes:
        if arr[h][k] in x.placers:
            box = x
    for p in box.placers:   # p is of type arr[i][j]
        if filled(p) == False:
            B.extend(p.probab)
    B.sort()
    return B

def check_box_probab(arr,var,h,k):
    if var !="" and var !=" ":
        B=box(arr,h,k)
        if B.count(var)==1: return False
        else: return True
    elif var=="" or var==" ": return True
    else: return True

'''
def hidden_single(arr):
    for i in range(0,9):  #? 
        for j in range (0,9):
            for x in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                #print("Probab of ",i+1,j+1,"is",arr[i][j].probab)
                if filled(arr[i][j])==False:
                    if check_col_probab(arr,x,j)==False:
                        if x in arr[i][j].probab:
                            arr[i][j].value = x
                    if check_row_probab(arr,x,i)==False:
                        if x in arr[i][j].probab:
                            arr[i][j].value = x
                    if check_box_probab(arr,x,i,j)==False:
                        if x in arr[i][j].probab:
                            arr[i][j].value = x
                clean(arr,i,j)    
'''
#~ print(x)
#print_probab(arr)
#~ Finds naked single and inputs them (Actally naked_single(arr) finds them)

def hidden_single_col(arr):
    for k in range(0,9):
        co=col(arr,k)
        for i in range(0,9):
            for x in arr[i][k].probab:
                if co.count(x)==1:
                    arr[i][k].value=x

def hidden_single_row(arr):
    for h in range(0,9):
        ro=row(arr,h)
        for j in range(0,9):
            for x in arr[h][j].probab:
                if ro.count(x)==1:
                    arr[h][j].value=x

# def hidden_single_box(arr):


def full_filled(arr):
    F=[]
    for i in range(0,9):
        for j in range(0,9):
            F.append(filled(arr[i][j]))
    if F.count(True) == 81: return True     
    elif F.count(False) == 0: return True
    else: return False

def iterations(arr):
    coun = 1
    while full_filled(arr) != True and coun != 25:
        naked_single(arr)
        coun =coun + 1
    print_value(arr)
    #print_probab(arr)
    print("The program has run ", coun, " iterations")

input2=input("Press enter to solve -->")

removal(arr)
iterations(arr)
print("Test 1 completed")
if full_filled(arr) == True: print("Test 1 successful")

print_probab(arr)

count1=1
while count1<=2: #imp FINAL SOLVING
    if full_filled(arr)==False:
        hidden_single_row(arr)
        hidden_single_col(arr)
        print_probab(arr)
        iterations(arr)
        print_value(arr)
        print("Test", count1,"completed")
        if full_filled(arr) == True: print("Test", count1,"successful")
        #else: print("Test", count1 ,"unsuccessful")
        #print_value(arr)
        removal(arr)
        print_probab(arr)
    count1=count1+1

# hidden_single(arr)
# iterations(arr)
# print("Test 2 completed")
# if full_filled(arr) == True: print("Test 2 successful")
# else: print("Test 2 unsuccessful")
# #print_value(arr)
# removal(arr)
# print_probab(arr)
'''
coun = 1
while full_filled(arr)!=True:
    naked_single(arr)
    change_to_value(arr)
    coun=coun+1
    print(coun)
    print_value(arr)
'''
#~ todo 1 Create a function check_row(arr, t) where t will be 0 for new_check_row 
#todo 2 Create function hidden single and check 
#todo Hidden singles is not complete

#endregion
