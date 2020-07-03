from time import sleep as z

def happy_birthday(name):
    p, n, h, b, t, y, x, hp, ho = [
    print, name.capitalize(), 'Happy', 'Birthday', 
    'to', 'you', '\b!', 'Hip', 'Hooray']
    happy = [(h,b,t,y),(h,b,t,y),(h,b,t,n,x),(h,b,t,y)]
    [p(' '.join(s)) or z(1) for s in happy]
    [p(' '.join(s)) for s in [(hp, hp, ho)]*3]
	
happy_birthday('Aditi')