#%%
a=5
print(id(a)==id(5))
# %%
a=0
b=1
while id(a+1)==id(b) and a<1000:
    a+=1
    b+=1
print(b)

# %%
a=0
b=1
while id(a+1)==id(b) and a>-1000:
    a-=1
    b-=1
print(b)

# %%
a=456+200
b=656
print(id(a)==id(b))

# %%
a=[]
b=(a,)
a=a+[1]
print(a)
c=(a,)
print(id(b)==id(c))
print(id(b[0])==id(c[0]))
print(b)
print(c)

# %%
a=1
b=a
b+=1
print(a,b)
a=1000
b=a
b+=1
print(a,b)
b-=1
print(a,b)
a=[1]
b=a
b+=[2]
print(a,b)

# %%
a=5
b=a
a+=1
print(id(a)==id(b))

# %%
a=[5]
b=a
a+=[1]
print(id(a)==id(b))
#%%
a=([],)
b=(a[0],)
print(id(a)==id(b))
b[0].append(1)
print(id(a)==id(b))
print(a,b)

#%%
a=1000
b=999+1
print(id(a)==id(b))
print(a is b)
print(a == b)

#%%

def en_liste(elt,L=[]):
    L.append(elt)
    return L

print(en_liste(5))
print(en_liste(6,[3]))
print(en_liste(17))
