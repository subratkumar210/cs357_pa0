from tkinter import *
en = Tk()
en.title("CSE-357__PA0/19165055")
en.geometry("400x400")

def change(s):
    itable={ 
        'a':'z','b':'y','c':'x','d':'w','e':'v','f':'u','g':'t','h':'s','i':'r','j':'q','k':'p','l':'o','m':'n','n':'m','o':'l','p':'k','q':'j','r':'i','s':'h','t':'g','u':'f','v':'e','w':'d','x':'c','y':'b','z':'a',' ':' ','.':'.','A':'Z','B':'Y','C':'X','D':'W','E':'V','F':'U','G':'T','H':'S','I':'R','J':'Q','K':'P','L':'O','M':'N','N':'M','O':'L','P':'K','Q':'J','R':'I','S':'H','T':'G','U':'F','V':'E','W':'D','X':'C','Y':'B','Z':'A'
    }
    ans=""
    for i in s:
        ans+= itable[i]
    
    return ans	

def for_e():					
	et = change( e1.get())
	e2.insert(0, et)

def for_p():					
	pt = change(e2.get())
	e1.insert(0, pt)
	

l1 = Label(en, text ="Plain text")			
l1.grid(row = 10, column = 1)
l2 = Label(en, text ="Cipher text")
l2.grid(row = 10, column = 12)



e1 = Entry(en)
e1.grid(row = 10, column = 2)
e2 = Entry(en)
e2.grid(row = 10, column = 13)


ent = Button(en, text = "Encrypt", command = for_e)
ent.grid(row = 15, column = 2)


b2 = Button(en, text = "Decrypt", command = for_p)
b2.grid(row = 15, column = 13)



en.mainloop()
