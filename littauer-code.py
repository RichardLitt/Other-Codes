#Richard Littauer - Simulation Code - Commented Saturday 28-05-2011 for K. Smith.

#Happy to explain anything else, if anyone wants. Also happy to go over this.
#TBH, I'd be surprised if anyone uses or reads this. If you're a real coder - 
#by God, I feel sorry for you. 
#Drop me a line! richard dot littauer [at] gmail [dot] com

from sys import argv

print(argv)

output_file_name = argv[1] + "-" +  argv[2] + "-" +  argv[3] + "-" +  argv[4] + "-" +  argv[5] + "-" +  argv[6] + "-" +  argv[7] + "-" +  argv[8] + "-" + argv[9] + ".csv" 

#Argv is used to run each simulation, so that you don't have to edit it manually each time.
#In essence, we have:
#function-WPT-word.length-possible.syllables-lexicon.size-amount.of.words.in.corpus-initial.lex-random.initial.lex-generations.
#So, for instance, fx1-lexchop-5-4-20-200-sorted-normal-500 is a canonical run.
#That's fx1, lexchop, 20 words 5units long with 5 possible syllables, normal initial lexicon, 500 generations.


#Variables are below. These used to be set by hand - now, they are all done using argv. 

alpha = 0 #Alpha-omega set the amount of syllables. Each syllable is one unit.
omega = int(argv[4]) #4 is therefore 0,1,2,3,4 as possible syllables. 
length = int(argv[3]) #This is the length of a word.
words = int(argv[5]) #This sets the amount of words to have in the lexicon.
amount = int(argv[6]) #The amount of words to use.
total = length*amount #This is the length of the string. Obvious.
iterate = 5 #Not even sure this is used. There is some trash. 

#HARDCODE TIME - these are the initial, non-random lexicons.
#I could have just done them with one word, but this way the code is sure not to break.
#Note that the function randomly selects from here, so it's possible that some words are
#Called more than others in the initial lexicon. 

s1 = ['01234', '01234', '01234', '01234', '01234', '01234', '01234', '01234', '01234', '01234', '01234', '01234', '01234', '01234', '01234', '01234', '01234', '01234', '01234', '01234']
s2 = ['01234', '21043', '01234', '21043', '01234', '21043', '01234', '21043', '01234', '21043', '01234', '21043', '01234', '21043', '01234', '21043', '01234', '21043', '01234', '21043']
s3 = ['01234', '12340', '23401', '34012', '40123', '01234', '12340', '23401', '34012', '40123', '01234', '12340', '23401', '34012', '40123', '01234', '12340', '23401', '34012', '40123']
s4 = ['01234', '43210', '01234', '43210', '01234', '43210', '01234', '43210', '01234', '43210', '01234', '43210', '01234', '43210', '01234', '43210', '01234', '43210', '01234', '43210']

import random, string


def cons(alpha,omega,length): #This creates a word. 
    return [str(random.randint(alpha,omega)) for x in range(length)]

#This creates the initial corpus that is sometimes used - no initial words, just a long string of random.

def randomw(): 
    p = []
    p.append(''.join(cons(alpha,omega,total)))
    return p[0] 

def lex(): #This creates a 'lexicon'.
    p = []
    for i in range(words):
        p.append(''.join(cons(alpha,omega,length)))
    return p

#argv stuff

p = 0
if (argv[7] == "sorted"):
  print("Using sorted for p")
  p = sorted(lex())
elif (argv[7] == "s1"):
  print("Using s1 for p")
  p = s1
elif (argv[7] == "s2"):
  print("Using s2 for p")
  p = s2
elif (argv[7] == "s3"):
  print("Using s3 for p")
  p = s3
elif (argv[7] == "s4"):
  print("Using s4 for p")
  p = s4

e = p

def corp(e,amount): #This takes the number of words, and puts them in a list.
    q = ""
    for i in range(amount):
        q += e[random.randrange(words)]
    return q

w = 0
if (argv[8] == "normal"):
  print("Using corp(p,amount) for w")
  w = corp(p,amount) #This is a [] of words.
elif (argv[8] == "randomw"):
  print("Using randomw for w")
  w = randomw() #This is a [] of words.


#Hamming function. Hams for one list, internally, by measuring each word against each other

def ham(r):
    t = []
    for o in range(len(r)):
        t.append(0)
    for x in range(len(r)):
        for y in range(len(r)):
            for s in range(len(r[0])):
                if r[x][s] == r[y][s]:
                    t[x] += 0
                if r[x][s] != r[y][s]:
                    t[x] += 1
    u = sum(t)/len(r)/((len(r) * len(r[0]))-len(r[0])) * 100
    #u = sum(t)/len(r)/(len(r) * len(r[0])) * 100
    return u

#External hamming function - used to compare two lists with each other.
#Each word is compared to each other word in the other list.

def hamex(r,r2):
    t = []
    for o in range(len(r)):
        t.append(0)
    for x in range(len(r)):
        for y in range(len(r2)):
            for s in range(len(r[0])):
                if r[x][s] == r2[y][s]:
                    t[x] += 0
                if r[x][s] != r2[y][s]:
                    t[x] += 1
    u = sum(t)/len(r)/(len(r2) * length) * 100
    return u

#From http://hetland.org/coding/python/levenshtein.py
#Levenshtein distance. Sourced in the source code attached to the thesis. 

def levenshtein(a,b):
    "Calculates the Levenshtein distance between a and b."
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a,b = b,a
        n,m = m,n
        
    current = range(n+1)
    for i in range(1,m+1):
        previous, current = current, [i]+[0]*n
        for j in range(1,n+1):
            add, delete = previous[j]+1, current[j-1]+1
            change = previous[j-1]
            if a[j-1] != b[i-1]:
                change = change + 1
            current[j] = min(add, delete, change)
            
    return current[n]

#More levenshtein distance. 

def lev(r):
    t = []
    for o in range(len(r)):
        t.append(0)
    for x in range(len(r)):
        for y in range(len(r)):
            t[x] += levenshtein(r[x],r[y])
    u = sum(t)/len(r)/((len(r) * len(r[0]))-len(r[0])) * 100
    #u = sum(t)/len(r)/(len(r) * len(r[0])) * 100
    return u

#External levenshtein distance. One list against another. 

def levex(r,r2):
    t = []
    for o in range(len(r)):
        t.append(0)
    for x in range(len(r)):
        for y in range(len(r2)):
            t[x] += levenshtein(r[x],r2[y])
    u = sum(t)/len(r)/(len(r2) * length) * 100
    return u

#Let's just pretend I never didn't know how to redefine a variable or something, and so went with
#dozens of slight variations. That's poor coding. Like, pretty bad. So, yeah...

#Anyway, phist is a way of making histograms out of possible lexicons. I ran this, but the output was odd,
#And I couldn't find a place for it, so I never actually included it in the dissertation. You did say I should
#Do this, though. 

output_fil = output_file_name 

def phist(iterate): #For use in histograms. 
    output = open(output_fil,'a')  
    for e in range(iterate):
        t = sorted(lex())
        h = ham(t)
        output.write(str(h) + '\n')
    return(h)
    output.close()


'''
Transition/Syllable counts per word in p/q.
'''

def silk(t): #Counts which syllables are used where in the words in P (p, of course, being the lexicon).
    global e
    r = []
    for x in range(length):
        r.append([])
        for y in range(len(uniqueli(sorted(unique(e))))):
            r[x].append(0)
    for x in range(len(t)):
        for j in range(length):
            r[j][int(t[x][j])] += 1
    return r
 
def trank(t): #Counts the amount of each syllable transition in total of p.
    global e
    r = []
    for x in range(length-1):
        r.append([])
        for s in range(len(unique(sorted(unique(e))))):
            r[x].append([])
            for y in range(len(unique(sorted(unique(e))))):
                r[x][s].append(0)
    for y in range(length):
        for x in range(len(t)):
            u = y+1
            if u != length:
                r[y][int(t[x][y])][int(t[x][u])] += 1
    return r

#percentage of used transition out of possible transitions for each transition loci in all words in p

def zero(j):
    t = trank(j)
    r = []
    h = [0]
    for x in range(length-1):
        r.append(0)
    for q in range(len(t)):
        for w in range(len(t[q])):
            for e in range(len(t[q][w])):
                    if t[q][w][e] != 0:
                        r[q] += 1
                    h[0] += 1
    for x in range(len(r)):
        r[x] /= (h[0]/len(r))
        r[x] *= 100
    return r

'''
uniqueli() removes multiple instances of discrete strings from a list. 
This may not be advisable - evolving with more instances of the same word
might be more fun / realistic / interesting.

From: http://www.peterbe.com/plog/uniqifiers-benchmark

''' 

def uniqueli(seq, idfun=None):
    if idfun is None:
        def idfun(x): return x
    seen = {}
    result = []
    for item in seq:
        marker = idfun(item)
        if marker in seen: continue
        seen[marker] = 1
        result.append(item)
    return result


#The following finds all instances of each unique syllable in the string.

def unique(inlist, keepstr=True): 
  typ = type(inlist)
  if not typ == list:
    inlist = list(inlist)
  i = 0
  while i < len(inlist):
    try:
      del inlist[inlist.index(inlist[i], i + 1)]
    except:
      i += 1
  else:
    if keepstr:
      inlist = ''.join(inlist)
  return inlist

x = sorted(unique(w))

'''
These are the word pair tests. 
'''

def lexrand(): #Two random words
    r = []
    for i in range(2):
        r.append(''.join(cons(alpha,omega,length)))
    #print(r)
    return r

def lexdom(): # 1 real word, 1 completely random, same sounds
    r = []
    r.append(''.join(p[random.randrange(len(p))]))
    for i in range(1):
        r.append(''.join(cons(alpha, omega, length)))
    return r

#Commented this out because it failed with any non-native sounds, as expected.
#Meaning it had longer run times and didn't throw up anything different from
#lexdom()
#def lexdom2(): # 1 real word, completely random, different sounds
#    r = []
#    r.append(''.join(p[random.randrange(len(p))]))
#    for i in range(1):
#        r.append(''.join(cons(0, 9, length)))
#    #print(r)
#    return r

def lexscram(): # 1 real word, random scrambling
    r = []
    r.append(''.join(p[random.randrange(len(p))]))
    for i in range(1):
        t = p[random.randrange(len(p))]
        e = []
        for i in range(len(t)):
            e.append(''.join(t[random.randrange(len(t))]))
        r.append(''.join(e))
    #print(r)
    return r

#I didn't end up using these two, mostly because they just didn't seem that different. Still,
#they're possibilities. 

#def lexscram2(): # 1 real word, no-weight random scrambling
#    #Meaning, can just scramble using any, but not necessarilly all, of the units.
#    r = []
#    r.append(''.join(p[random.randrange(len(p))]))
#    for i in range(1):
#        t = p[random.randrange(len(p))]
#        h = sorted(unique(t))
#        e = []
#        for i in range(len(t)):
#            e.append(''.join(h[random.randrange(len(h))]))
#        r.append(''.join(e))
#    #print(r)
#    return r

#def lexscram3(): # 1 real word, same-weight random scrambling
#    #Only uses the units in the word, in the same amounts.
#    r = []
#    r.append(''.join(p[random.randrange(len(p))]))
#    for i in range(1):
#        t = p[random.randrange(len(p))]
#        e = []
#        for i in range(len(t)):
#            y = random.randrange(len(t))
#            e.append(''.join(t[y]))
#            t = t[:y] + t[y+1:]
#        r.append(''.join(e))
#    #print(r)
#    return r   

def lexchop(): # 1 real word, 1 chopped transitional word
    #Might be nice to mess with this and make the chops variable. 
    r = []
    r.append(''.join(p[random.randrange(len(p))]))
    for o in range(1):
        w = random.randrange(len(p)-1)
        t = p[w:w+2]
        l = []
        l.append(''.join(t[0:2]))
        l = l[0]
        l = l[2:2+length]
        r.append(''.join(l))
    #print(r)
    return r

'''
Fx1: This will create two random words. If it has seen one before, it will output it.
If it has seen both before, it will randomly choose between them. If it has seen neither
it will select neither.

The output is then run through an ILM.

All of the fx_unit()s make the actual pairing. 
'''

def fx1unit(): 
    if (argv[2] == "lexdom"):
      z = lexdom() 
    elif (argv[2] == "lexrand"):
      z = lexrand() 
    elif (argv[2] == "lexscram"):
      z = lexscram() 
    elif (argv[2] == "lexchop"):
      z = lexchop() 
    
    max_str = []
    st = 0
    n = 0
    for x in range(len(w)):
        y = n+x+len(z[st])
        if z[st] == w[n+x:y]:
            max_str.append(z[st])
            break
        n +=1
    st = 0
    for x in range(len(w)):
        y = n+x+len(z[st])
        if z[st+1] == w[n+x:y]:
            max_str.append(z[st+1])
            break
        n +=1
    return max_str

#This decides what to do with the decisions of the two words. If one, it throws it in.
#If two, it randomly chooses one.

def fx1c():
    totstring = ""
    x = []
    while len(totstring) <= (total-length):
        t = fx1unit()
        if len(t) == 0:
            pass #This actually isn't a problem; only happens for defunct lexrand().
        elif len(t) == 1:
            totstring += t[0]
            x.append(t[0])
        elif len(t) == 2:
            e = t[random.randrange(len(t))]
            totstring += e
            x.append(e)
    return totstring, x

#This is the ILM. 



'''
This coding isn't pretty, so here are the definitions:

w = the total string for each generation.
r = the run through used in each generation, from fx1. 
p = the initial words used to make the first w; also the random word sequence
q = the word list for each generation, used to make the new w.
pg = the previous generations words (the previous q, that is)
pg_ham = the discreteness value for the previous generation, done internally.
uni_q = the unique words found in q, to more accurately reflect storage than multiples.
m = amount of unique words in q, as a proportion with the original amount of words.
aa = this is used in the coding. It's the set of unique words in uni_q
inter = the intersection of the q list and p - the retained words.
ret_p = the amount of retained words as a percentage of the original amount of words.
q_ham = the distinctiveness of q, measured internally.
bb = this is the same as aa, but for comparing words with previous gen.
inter2 = the intersection of the pg list and q - the retained words from each gen.
ret_pg = the amount of retained words as a percentage of the pg's amount of words.
uni_pg = the unique words found in pg, to more accurately reflect storage than multiples.
hamex_q = the hamming of q against the original set
hamex_pg = the hamming of q against the previous generations iterations
'''

output_file = output_file_name

def preg(): #This creates a previous generation lex.
    p = []
    for i in range(words):
        p.append(''.join(cons(0,0,length)))
    return p

pg = preg()
p_lev = lev(p)  #Lev distance of the lexicon. 
p_ham = ham(p)  #hamming distance of the lexicon.
slk_p = silk(p) #list of syllable counts per word location
trank_p = zero(p) #percentage of used transition out of possible transitions for each transition loci in all words in p
    
#again, not pretty. Sorry about that. Let me know if you want me to comment this up. 

#update; not happy with not having explained this, seems pretty lazy of me -so, here, line by line.

def fx1(iterate): #iterate is the amount of generations
    global w, y, p, pg, p_ham, slk_p, trank_p, p_lev #calls
    output = open(output_file,'a') #the excel file
    for i in range(iterate): #the loop
        r = fx1c()  #This calls up the lexicon for each generation, already fully made by concatenating
                    #the WPT results.
        y = fx4p(w) #Figure out the probability of transitions in w. 
        w = r[0]    #redefines w according to the new one. 
        pg_ham = ham(pg) #hamming for the previous generation
        pg_lev = lev(pg) #levving for the previous generation
        q = r[1]    #this sets the current lexicon as the current lexicon, to be used against p
        m = len(sorted(uniqueli(q)))/len(p)*100
                    #amount of unique words in q,
                    #as a proportion with the original amount of words.
        m2 = len(sorted(uniqueli(q)))/len(e)*100
                    #percentage of size of the lexicon in proportion to the original size
        aa = set(sorted(uniqueli(q))) 
        inter = sorted(aa.intersection(e))
        bb = set(sorted(uniqueli(pg)))
        inter2 = sorted(bb.intersection(sorted(uniqueli(q))))
                    #these figure out the amount of similarity between two lists.
        ret_pg = len(inter2)/len(uniqueli(pg))*100
                    #amount of words retained from the previous lexicon
        ret_p = len(inter)/len(e)*100
                    #amount of words retained from the original lexicon
        q_ham = ham(q)
                    #the hamming value of the lexicon to itself
        hamex_q = hamex(q,e)
                    #the hamming value of the lexicon compared to the original
        hamex_pg = hamex(q,pg)
                    #the hamming value of this lexicon compared to the previous one
        q_lev = lev(q)
                    #Same, but lev.
        levex_q = levex(q,e)
                    #"
        levex_pg = levex(q,pg)
                    #"
        pg = r[1]   #Resets the previous generation to be this generation, for next time.
        p = sorted(uniqueli(r[1]))
                    #restes p to be the unique p.
        q_prob = prob(y,q) #On latest w transitions
        q_prob_on_g = prob(g,q) #On original w transition
        slk_q = silk(q) #list of syllable counts per word location in q
        trank_q = zero(q) #percentage of used transition out of possible transitions for each transition loci in all words in q
        #print(m,m2,ret_p,ret_pg,p_ham,q_ham,pg_ham,hamex_q,hamex_pg)
        output.write(str(m) + ',' + str(m2) + ',' + str(ret_p) + ',' + str(ret_pg) + ','
                     + str(p_ham) + ',' + str(q_ham) + ',' + str(pg_ham) + ',' + str(hamex_q) + ','
                     + str(hamex_pg) + ',' + str(p_lev) + ',' + str(q_lev) + ',' + str(pg_lev) + ','
                     + str(levex_q) + ',' + str(levex_pg) + ',' + str(q_prob) + ',' + str(slk_p) + ','
                     + str(slk_q) + ',' + str(trank_p) + ',' + str(trank_q) + '\n')
        output.flush()
    output.close()

'''
Fx2: This chooses the words with the highest count.

There may be an issue, here, and in all of the codes, with hapax legomena.
Essentially, if a word is only used once, it won't output it. This happens every now, then.

'''

def fx2unit(): #makes the WPT
    new_str = [] 
    counts = []

    while (len(new_str) == 0):
      if (argv[2] == "lexdom"):
        u = lexdom() 
      elif (argv[2] == "lexrand"):
        u = lexrand() 
      elif (argv[2] == "lexscram"):
        u = lexscram() 
      elif (argv[2] == "lexchop"):
        u = lexchop() 

      first_n = w.count(u[0])
      second_n = w.count(u[1])
      if (first_n > 0):
        new_str.append(u[0])
        counts.append(first_n)
      if (second_n > 0):
        new_str.append(u[1])
        counts.append(second_n)
      if (len(new_str) == 1):
        new_str.append(new_str[0])
        counts.append(0)

      # If new_str's length is still 0 (ie, we didn't find either word in the list,
      # then the while loop will ensure we generate a new pair and check that instead.

    return new_str, counts


def fx2c(): 
    totstring = ""
    x = []
    while len(totstring) <= total:
        t = fx2unit()
        if t[1][0] == t[1][1]:
            r = t[0][random.randrange(len(t[0]))]
            totstring += r
            x.append(r)
        elif t[1][0] >= t[1][1]:
            totstring += t[0][0]
            x.append(t[0][0])
        elif t[1][0] <= t[1][1]:
            totstring += t[0][1]
            x.append(t[0][1])
    return totstring, x

#This is the ILM.

output_fi = output_file_name 

def fx2(iterate): 
    global w, p, p_ham, pg, slk_p, trank_p, p_lev
    output = open(output_fi,'a')  
    for i in range(iterate):
        r = fx2c()
        y = fx4p(w)
        w = r[0]
        pg_ham = ham(pg)
        pg_lev = lev(pg)
        q = r[1] 
        m = len(sorted(uniqueli(q)))/len(p)*100
        m2 = len(sorted(uniqueli(q)))/len(e)*100 
        aa = set(sorted(uniqueli(q))) 
        inter = sorted(aa.intersection(e))
        bb = set(sorted(uniqueli(pg)))
        inter2 = sorted(bb.intersection(sorted(uniqueli(q))))
        ret_pg = len(inter2)/len(uniqueli(pg))*100
        ret_p = len(inter)/len(e)*100 
        q_ham = ham(q)
        hamex_q = hamex(q,e)
        hamex_pg = hamex(q,pg)
        q_lev = lev(q)
        levex_q = levex(q,e)
        levex_pg = levex(q,pg)
        pg = r[1]
        p = sorted(uniqueli(r[1]))
        q_prob = prob(y,q) #On latest w transitions
        q_prob_on_g = prob(g,q) #On original w transition
        slk_q = silk(q) #list of syllable counts per word location in q
        trank_q = zero(q) #percentage of used transition out of possible transitions for each transition loci in all words in q
        #print(m,ret_p,ret_pg,p_ham,q_ham,pg_ham,hamex_q,hamex_pg)
        output.write(str(m) + ',' + str(m2) + ',' + str(ret_p) + ',' + str(ret_pg) + ',' + str(p_ham) + ',' + str(q_ham) + ',' + str(pg_ham) + ',' + str(hamex_q) + ',' + str(hamex_pg) + ',' + str(p_lev) + ',' + str(q_lev) + ',' + str(pg_lev) + ',' + str(levex_q) + ',' + str(levex_pg) + ',' + str(q_prob) + ',' + str(slk_p) + ',' + str(slk_q) + ',' + str(trank_p) + ',' + str(trank_q) + '\n')
        output.flush()
    output.close()

'''
Fx3: This takes the two words made by the lex procresses, and judges them based on syllable
transitions. It checks to see if pairs are repeated throughout the string - it then judges
based on the amount of repetitions of pairs. Per word, it judges how many pairs are repea-
ted based on counts of each transition. The word with the highest count - not always the
real word - gets chosen. 
'''

def fx3unit():
    if (argv[2] == "lexdom"):
      fx = lexdom() 
    elif (argv[2] == "lexrand"):
      fx = lexrand() 
    elif (argv[2] == "lexscram"):
      fx = lexscram() 
    elif (argv[2] == "lexchop"):
      fx = lexchop() 

    f = fx[0]
    g = fx[1]
    mx = [0,0]
    y = 0
    for x in range(len(f)):
        for x in range(len(w)):
            if f[y:y+2] == w[x:x+2]:
                mx[0] += 1
                #print(f,f[y:y+2],mx,y,x)
        y += 1
    y = 0
    for x in range(len(g)):
        for x in range(len(w)):
            if g[y:y+2] == w[x:x+2]:
                mx[1] += 1
                #print(g,g[y:y+2],mx,y,x)
        y += 1
    return(fx, mx)

def fx3c():
    totstring = ""
    x = []
    while len(totstring) <= total:
        t = fx3unit()
        if t[1][0] == t[1][1]:
            i = t[0][random.randrange(len(t[0]))]
            totstring += i
            x.append(i)
        elif t[1][0] >= t[1][1]:
            totstring += t[0][0]
            x.append(t[0][0])
        elif t[1][0] <= t[1][1]:
            totstring += t[0][1]
            x.append(t[0][1])
    return totstring, x

#This is the ILM. 
    
output_f = output_file_name

def fx3(iterate): 
    global w, p, p_ham, pg, slk_p, trank_p, p_lev
    output = open(output_f,'a')  
    for i in range(iterate):
        r = fx3c()
        y = fx4p(w)
        w = r[0]
        pg_ham = ham(pg)
        pg_lev = lev(pg)
        q = r[1] 
        m = len(sorted(uniqueli(q)))/len(p)*100
        m2 = len(sorted(uniqueli(q)))/len(e)*100 
        aa = set(sorted(uniqueli(q))) 
        inter = sorted(aa.intersection(e))
        bb = set(sorted(uniqueli(pg)))
        inter2 = sorted(bb.intersection(set(sorted(uniqueli(q)))))
        ret_pg = len(inter2)/len(uniqueli(pg))*100
        ret_p = len(inter)/len(e)*100 
        q_ham = ham(q)
        hamex_q = hamex(q,e)
        hamex_pg = hamex(q,pg)
        q_lev = lev(q)
        levex_q = levex(q,e)
        levex_pg = levex(q,pg)
        pg = r[1]
        p = sorted(uniqueli(r[1])) 
        q_prob = prob(y,q) #On latest w transitions
        q_prob_on_g = prob(g,q) #On original w transition
        slk_q = silk(q) #list of syllable counts per word location in q
        trank_q = zero(q) #percentage of used transition out of possible transitions for each transition loci in all words in q
        #print(m,ret_p,ret_pg,p_ham,q_ham,pg_ham,hamex_q,hamex_pg)
        output.write(str(m) + ',' + str(m2) + ',' + str(ret_p) + ',' + str(ret_pg) + ',' + str(p_ham) + ',' + str(q_ham) + ',' + str(pg_ham) + ',' + str(hamex_q) + ',' + str(hamex_pg) + ',' + str(p_lev) + ',' + str(q_lev) + ',' + str(pg_lev) + ',' + str(levex_q) + ',' + str(levex_pg) + ',' + str(q_prob) + ',' + str(slk_p) + ',' + str(slk_q) + ',' + str(trank_p) + ',' + str(trank_q) + '\n')
        output.flush()
    output.close()

'''
Fx4: This takes the two words made by the lex procresses, and judges them based on syllable
transitions. It checks to see if pairs are repeated throughout the string - it then judges
based on the amount of repetitions of pairs. Per word, it judges how many pairs are repea-
ted based on counts of each transition. This one jusges based on probability of a transit-
ion occuring. 
'''

def fx40(l): #This creates an empty [] with zeros for each possible transition.
    mx = []
    for x in range(len(unique(unique(e)))):
        mxx = []
        for y in range(len(unique(unique(e)))):
            mxx.append(0)
        mx.append(mxx)
    return mx

def fx4cx(l): #this fills that list with the counts of types of transitions.
    f = fx40(l)
    for x in range(len(l)-1):
        f[int(l[x])][int(l[x+1])] += 1
    return f

def fx4ct(l): #this counts the total transitions per each number, for use in probability.
    f = fx4cx(l)
    mx = []
    for x in range(len(f)):
        mx.append(sum(f[x]))
    return mx

#`This figures probability, dividing each transition by total of that kind of transition. 

def fx4p(l):
    t = fx4cx(l)
    f = fx4ct(l)
    j = fx40(l)
    for x in range(len(t)):
        for y in range(len(t[0])):
            if (f[x] != 0):
              j[x][y] += t[x][y]/f[x]
    return j

#this cumulatively adds the probabilities of each transition for each word, and puts
#that figure into a list.

rand = randomw()
k = fx4p(rand)
y = fx4p(w)
g = y


def fx4unit():
    if (argv[2] == "lexdom"):
      r = lexdom() 
    elif (argv[2] == "lexrand"):
      r = lexrand() 
    elif (argv[2] == "lexscram"):
      r = lexscram() 
    elif (argv[2] == "lexchop"):
      r = lexchop() 

    t = r[0]
    k = r[1]
    mx = [1,1]
    for x in range(len(t)-1):
        mx[0] *= y[int(t[x])][int(t[x+1])]
    for x in range(len(k)-1):
        if int(k[x]) > (len(y)-1):
            mx[1] *= 0
        if int(k[x+1]) > (len(y)-1):
            mx[1] *= 0
        elif int(k[x]) <= (len(y)-1):
            mx[1] *= y[int(k[x])][int(k[x+1])]
    return(r, mx)

#this outputs the word with the higher probability of existing in w.

def fx4c():
    totstring = ""
    x = []
    while len(totstring) <= total:
        t = fx4unit()
        if t[1][0] == t[1][1]:
            i = t[0][random.randrange(len(t[0]))]
            totstring += i
            x.append(i)
        elif t[1][0] >= t[1][1]:
            totstring += t[0][0]
            x.append(t[0][0])
        elif t[1][0] <= t[1][1]:
            totstring += t[0][1]
            x.append(t[0][1])
    return totstring, x

#This is the ILM. 

output_fyl = output_file_name

def fx4(iterate): 
    global w, y, p, p_ham, pg, slk_p, trank_p, p_lev
    output = open(output_fyl,'a')  
    for i in range(iterate):
        r = fx4c()
        y = fx4p(w)
        w = r[0]
        pg_ham = ham(pg)
        pg_lev = lev(pg)
        q = r[1] 
        m = len(sorted(uniqueli(q)))/len(p)*100
        m2 = len(sorted(uniqueli(q)))/len(e)*100
        aa = set(sorted(uniqueli(q))) 
        inter = sorted(aa.intersection(e))
        bb = set(sorted(uniqueli(pg)))
        inter2 = sorted(bb.intersection(set(sorted(uniqueli(q)))))
        ret_pg = len(inter2)/len(uniqueli(pg))*100
        ret_p = len(inter)/len(e)*100 
        q_ham = ham(q)
        hamex_q = hamex(q,e)
        hamex_pg = hamex(q,pg)
        q_lev = lev(q)
        levex_q = levex(q,e)
        levex_pg = levex(q,pg)
        pg = r[1]
        p = sorted(uniqueli(r[1]))
        q_prob = prob(y,q) #On latest w transitions
        q_prob_on_g = prob(g,q) #On original w transition
        slk_q = silk(q) #list of syllable counts per word location in q
        trank_q = zero(q) #percentage of used transition out of possible transitions for each transition loci in all words in q
        output.write(str(m) + ',' + str(m2) + ',' + str(ret_p) + ',' + str(ret_pg) + ',' + str(p_ham) + ',' + str(q_ham) + ',' + str(pg_ham) + ',' + str(hamex_q) + ',' + str(hamex_pg) + ',' + str(p_lev) + ',' + str(q_lev) + ',' + str(pg_lev) + ',' + str(levex_q) + ',' + str(levex_pg) + ',' + str(q_prob) + ',' + str(slk_p) + ',' + str(slk_q) + ',' + str(trank_p) + ',' + str(trank_q) + '\n')
        output.flush()
    output.close()

'''
Transition probability for more than one word.
'''

def prob(j,r):
    mx = []
    for x in range(len(uniqueli(sorted(r)))):
        mx.append(1)
    for y in range(len(uniqueli(sorted(r)))):
        for x in range(length-1):
            mx[y] *= j[int(r[y][x])][int(r[y][x+1])]
    h = sum(mx)/len(mx)
    return(h)


'''
I deleted my original code that tried to go from the start. It wasn't very scientific, I think.
In any event, it wasn't in the dissertation, and wasn't relevant to anything. 

'''


'''
These are random functions. They only work with lexrand. They ignore p entirely, and go from an a priori w.
These are only used for the randomw() function, then. 

'''

output_filer1 = output_file_name

def fx1rand(iterate):
    global w, y, pg
    output = open(output_filer1,'a')
    for i in range(iterate):
        r = fx1c()
        y = fx4p(rand)
        w = r[0]
        pg_ham = ham(pg)
        pg_lev = lev(pg)
        q = r[1] 
        m = len(sorted(uniqueli(q)))
        bb = set(sorted(uniqueli(pg)))
        inter2 = sorted(bb.intersection(sorted(uniqueli(q))))
        ret_pg = len(inter2)/len(uniqueli(pg))*100
        q_ham = ham(q)
        hamex_pg = hamex(q,pg)
        q_lev = lev(q)
        levex_pg = levex(q,pg)
        pg = r[1]
        q_prob = prob(y,q) #On latest w transitions
        q_prob_on_g = prob(g,q) #On original w transition
        slk_q = silk(q) #list of syllable counts per word location in q
        trank_q = zero(q) #percentage of used transition out of possible transitions for each transition loci in all words in q
        #print(m,ret_p,ret_pg,p_ham,q_ham,pg_ham,hamex_q,hamex_pg)
        output.write(str(m) + ',' + str(ret_pg) + ',' + str(q_ham) + ',' + str(pg_ham) + ',' + str(hamex_pg) + ',' + str(q_lev) + ',' + str(pg_lev) + ',' + str(levex_pg) + ',' + str(q_prob) + ',' + str(slk_q) + ',' + str(trank_q) + '\n')
    output.close()

output_filer2 = output_file_name

def fx2rand(iterate): 
    global w, y, pg
    output = open(output_filer2,'a')  
    for i in range(iterate):
        r = fx2c()
        y = fx4p(rand)
        w = r[0]
        pg_ham = ham(pg)
        pg_lev = lev(pg)
        q = r[1] 
        m = len(sorted(uniqueli(q)))
        bb = set(sorted(uniqueli(pg)))
        inter2 = sorted(bb.intersection(sorted(uniqueli(q))))
        ret_pg = len(inter2)/len(uniqueli(pg))*100
        q_ham = ham(q)
        hamex_pg = hamex(q,pg)
        q_lev = lev(q)
        levex_pg = levex(q,pg)
        pg = r[1]
        q_prob = prob(y,q) #On latest w transitions
        q_prob_on_g = prob(g,q) #On original w transition
        slk_q = silk(q) #list of syllable counts per word location in q
        trank_q = zero(q) #percentage of used transition out of possible transitions for each transition loci in all words in q
        #print(m,ret_p,ret_pg,p_ham,q_ham,pg_ham,hamex_q,hamex_pg)
        output.write(str(m) + ',' + str(ret_pg) + ',' + str(q_ham) + ',' + str(pg_ham) + ',' + str(hamex_pg) + ',' + str(q_lev) + ',' + str(pg_lev) + ',' + str(levex_pg) + ',' + str(q_prob) + ',' + str(slk_q) + ',' + str(trank_q) + '\n')
    output.close()

output_filer3 = output_file_name

def fx3rand(iterate): 
    global w, y, pg
    output = open(output_filer3,'a')  
    for i in range(iterate):
        r = fx3c()
        y = fx4p(rand)
        w = r[0]
        pg_ham = ham(pg)
        pg_lev = lev(pg)
        q = r[1] 
        m = len(sorted(uniqueli(q)))
        bb = set(sorted(uniqueli(pg)))
        inter2 = sorted(bb.intersection(sorted(uniqueli(q))))
        ret_pg = len(inter2)/len(uniqueli(pg))*100
        q_ham = ham(q)
        hamex_pg = hamex(q,pg)
        q_lev = lev(q)
        levex_pg = levex(q,pg)
        pg = r[1]
        q_prob = prob(y,q) #On latest w transitions
        q_prob_on_g = prob(g,q) #On original w transition
        slk_q = silk(q) #list of syllable counts per word location in q
        trank_q = zero(q) #percentage of used transition out of possible transitions for each transition loci in all words in q
        #print(m,ret_p,ret_pg,p_ham,q_ham,pg_ham,hamex_q,hamex_pg)
        output.write(str(m) + ',' + str(ret_pg) + ',' + str(q_ham) + ',' + str(pg_ham) + ',' + str(hamex_pg) + ',' + str(q_lev) + ',' + str(pg_lev) + ',' + str(levex_pg) + ',' + str(q_prob) + ',' + str(slk_q) + ',' + str(trank_q) + '\n')
    output.close()

output_filer4 = output_file_name

def fx4rand(iterate): 
    global w, y, pg
    output = open(output_filer4,'a')  
    for i in range(iterate):
        r = fx4c()
        y = fx4p(rand)
        w = r[0]
        pg_ham = ham(pg)
        pg_lev = lev(pg)
        q = r[1] 
        m = len(sorted(uniqueli(q)))
        bb = set(sorted(uniqueli(pg)))
        inter2 = sorted(bb.intersection(sorted(uniqueli(q))))
        ret_pg = len(inter2)/len(uniqueli(pg))*100
        q_ham = ham(q)
        hamex_pg = hamex(q,pg)
        q_lev = lev(q)
        levex_pg = levex(q,pg)
        pg = r[1]
        q_prob = prob(y,q) #On latest w transitions
        q_prob_on_g = prob(g,q) #On original w transition
        slk_q = silk(q) #list of syllable counts per word location in q
        trank_q = zero(q) #percentage of used transition out of possible transitions for each transition loci in all words in q
        #print(m,ret_p,ret_pg,p_ham,q_ham,pg_ham,hamex_q,hamex_pg)
        output.write(str(m) + ',' + str(ret_pg) + ',' + str(q_ham) + ',' + str(pg_ham) + ',' + str(hamex_pg) + ',' + str(q_lev) + ',' + str(pg_lev) + ',' + str(levex_pg) + ',' + str(q_prob) + ',' + str(slk_q) + ',' + str(trank_q) + '\n')
    output.close()

iterations = int(argv[9]) #or generations...

if argv[1] == "fx1":
  print("Using fx1")
  fx1(iterations)
elif argv[1] == "fx2":
  print("Using fx2")
  fx2(iterations)
elif argv[1] == "fx3":
  print("Using fx3")
  fx3(iterations)
elif argv[1] == "fx4":
  print("Using fx4")
  fx4(iterations)
