import re
class Bktree:
	def __init__(self,nword):
		self.word=nword
		self.children=[]
		for i in range(30):
			self.children.append(None)

def addword(parent,newword):
	d=lev(parent.word,newword)
	if parent.children[d] is not None:
		addword(parent.children[d],newword)
	else:
		new=Bktree(newword)
		print parent.word+"--"+str(d)+"-->"+newword
		output.writelines(parent.word+"--"+str(d)+"-->"+newword+"\n")
		parent.children[d]=new
def lev(s, t):
    m, n = len(s), len(t)
    d = [range(n+1)]
    d += [[i] for i in range(1,m+1)]
    for i in range(0,m):
        for j in range(0,n):
            cost = 1
            if s[i] == t[j]: cost = 0

            d[i+1].append( min(d[i][j+1]+1, 
                               d[i+1][j]+1, 
                               d[i][j]+cost) 
                           )
    return d[m][n]

def BruteSuggest(word):
	word=word.lower()
	word='^'+word
	while true:
		result=filter(lambda x:re.search(word,x),words)[:10]
		if len(result) > 0:
			return result
		else:
			word=word[:-1]

def search(word,n):
	wordlist=[]
	def process(word,n,node=root):
		d=lev(node.word,word)
		if d <= n : wordlist.append(node.word)
		for i in range (d-n,d+n+1):
			if node.children[i] is not None:
				process(word,n,node.children[i])
	process(word,n)
	return wordlist

def correct(word):
	w=[]
	d=[]
	order=[]
	lis=search(word,3)
	text='^'+word
	text=text[0:2]
	y=filter(lambda x:re.search(text,x),lis)
	for wo in y:
		w.append(wo)
		d.append(lev(wo,word))
	for i  in range(len(word)):
		ind=d.index(min(d))
		order.append(ind)
		d[ind]=999
	for i in order:
		print w[i]

# def CorrectSentence(sentence):
# 	nwords=sentence.split(" ")
# 	w=[]
# 	d=[]
# 	for i in range(len(nwords)):
# 		if nwords[i] not in words:
# 			lis=correct(nwords[i],2)
# 			text="^"+nwords[i]
# 			text=text[0:2]
# 			y=filter(lambda x:re.search(text,x),lis)
# 			for j in y:
# 				w.append(j)
# 				d.append(lev(j,nwords[i]))
# 			ind=d.index(min(d))

# 			nwords[i]=w[ind]
# 	sentence=" ".join(nwords)
# 	return sentence
			
				
				
			
			

	


f=open("allwords.txt","r")
words=f.read()
words=words.split('\n')
root=Bktree(words[0])
output=open("tree","w")
print "BUILDING TREE.........."
for i in range(1,len(words)):
		addword(root,words[i])
output.close()
#lulz

