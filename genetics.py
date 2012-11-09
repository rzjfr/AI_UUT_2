
cofnt=[]
powr=[]
ab=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w']

def load_data(file,cofnt=[],powr=[]):
    '''
    dsc: loads Coefficient and Power into seperate lists 
    from .txt file
    example:
    >>>load_data("input.txt",cofnt,powr)
    [('8', '2'), ('3', '3'), ('2', '4'), ('5', '2'), ('1', '5')]
    '''
    f = open(file)
    cofnt+= f.readline().split()
    powr+= f.readline().split()
    f.close()
    return zip(cofnt,powr)
print load_data("input.txt",cofnt,powr)
def make_eq(powr,cofnt,i=0,result=""):
    '''
    (list,list)->str
    dsc: returns an equation of imported data
    example:
    >>>make_eq(powr,cofnt)
    (1a^2)+(-1b^2)+(1c^2)+(1d^2)+(1e^2)+0= 0
    '''
    for x in powr:
        for y in cofnt:
            result+= "(%i%s^%s)+" %(int(y),ab[i],int(x))
            i+=1
        break
    return result+"0= 0"
def len_eq(file,result="",i=0):
    '''
    (filestr)->int
    '''
    f = open(file)
    y= f.readline().split()
    for ch in y:
        i+=1                        #result+=ch
    f.close()
    return i                        #len(result)/2
    
print len_eq("input.txt")

def summs(powr,cofnt,result=0):
    '''
    (list,list,list)->int
    '''
    for x in powr:
        for y in cofnt:
            #result+= int(y)*(int(z)^int(x))
            result+= int(y)+int(x)
            #print x,y
        break
    return result

print summs(powr,cofnt)
 
