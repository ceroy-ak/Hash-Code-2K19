from tqdm import tqdm
from multiprocessing import Pool

class Test :
    def __init__(self,val,id):#,no_of_tags,tags):
        self.val=val
        self.id=id
        self.oren=val[0]
        self.no_of_tags=int(val[2])
        self.tags=val[4:-1]
        self.tagsList=self.tags.split(' ')


file = open('e.txt','r')

no_of_lines = int(file.readline())

file = open('e.txt','r')

n=no_of_lines

my_object = []

d=file.readline()
flag = False
tmpobj = []
vFlag=False
for f in range(no_of_lines):
    tmp =file.readline()
    if tmp[0] == 'V' and vFlag==True:
        n=n-1
        vFlag=False
    else:
        vFlag=True
    obj = Test(tmp,str(f))
    my_object.append(obj)

N = len(my_object)


max = 0
for i in tqdm(range(N)):
    for j in range(i+1,N):
        common=list(set(my_object[i].tagsList).intersection(my_object[j].tagsList))
        if len(common)>0:
            if len(common)>max:
                my_object[i+1],my_object[j]=my_object[j],my_object[i+1]
            else:
                max = len(common)
                if i > (N-max):
                    my_object[i + 1], my_object[j] = my_object[j], my_object[i + 1]
                else:
                    my_object[max+len(common)], my_object[j] = my_object[j], my_object[max+len(common)]


#######################################################################################################
#Write the final file

flag=False
p = 0

newfile = open('e_sol.txt', 'w')
newfile.write(str(n))
newfile.write('\n')

for i in range(len(my_object)):
    if my_object[i].oren == 'V':
        if flag is False:
            p=my_object[i].id
            flag=True
        else:
            newfile.write(str(p) +" " + str(my_object[i].id))
            newfile.write('\n')
            flag=False
    else:
        newfile.write(str(my_object[i].id))
        newfile.write('\n')
