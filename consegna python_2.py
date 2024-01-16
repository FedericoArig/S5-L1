#!/usr/bin/env python
# coding: utf-8

# In[1]:


nome = input('computer')


# In[2]:


nome[3:7]


# In[3]:


testo = input("inserisci un testo: ")


# In[5]:


testo[0:3] + '...' + testo[-3:]


# In[8]:


nome = input()


# In[9]:


nome[0:3]+'...'+ nome[-3:]


# In[11]:


nome[:3]+'...'+ nome[-3:]


# In[29]:





# In[43]:


#Verificare, per ognuna delle seguenti stringhe, se il numero di caratteri è compreso tra 5 e 8
a = 'Windows'
b = 'Excel'
c = 'Powerpoint'
d = 'Word'

strings = [a,b,c,d]

Lunghezza = len(a)
print(Lunghezza)
Lunghezza = len(b)
print(Lunghezza)
Lunghezza = len(c)
print(Lunghezza)
Lunghezza = len(d)
print(Lunghezza)



# In[46]:


#Inventare un programma che prende in input degli elementi e restituisce in output una loro combinazione (ad esempio prendendo in input due numeri e restituendo la loro somma).
numero1 = int(input("Inserisci il primo numero: "))
numero2 = int(input("inserisci il secondo numero: "))             

Moltiplicazione = (numero1 * numero2)  

print(Moltiplicazione)


# In[51]:


#un utente inserisce tre parole e il programma produce in output la prima in maiuscolo, la seconda in minuscolo e la terza con l'iniziale maiuscola. Poi prende i primi tre caratteri di ognuna e li stampa a video
nome1 = 'Santino'
nome2 = 'Teresa'
nome3 = 'Gaetano'

Maiuscolo = nome1.upper()
print(Maiuscolo)
Minuscolo = nome2.lower()
print(Minuscolo)
Maiuscola_in = nome3.title()
print(Maiuscola_in)


# In[53]:


#Un utente inserisce tre parole e il programma stampa il prodotto delle lunghezze delle parole
nome1=input("Inserisci il primo nome: ")
nome2=input("inserisci il secondo nome: ")

Lunghezza = len(nome1)
print(Lunghezza)
Lunghezza = len(nome2)
print(Lunghezza)


# In[54]:


#scrivi una parola in input e riscrivila al contrario in output
nome = input("inserisci il nome: ")

nome[7],nome[6],nome[5],nome[4],nome[3],nome[2],nome[1],nome[0]


