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
load_data("input.txt",cofnt,powr)
def make_eq(powr,cofnt,i=0,result=""):
    '''
    (list,list)->str
    dsc: returns an equation of imported data
    example:
    >>>make_eq(powr,cofnt)
    1a^2 + 1b^2 + 1c^2 + 1d^2 + 1e^2 + 0 =0
    '''
    for x in powr:
        for y in cofnt:
            result+= "%s%s^%s + " %(y,ab[i],x)
            i+=1
        break
    return result+"0 =0"
print make_eq(powr,cofnt)
