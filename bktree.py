import json
import os
def Bktree(nword):
	node={}
	node["word"]=nword
	for i in range(30):
		node[str(i)]=None
	return node


def addword(parent,newword):
	d=lev(parent["word"],newword)
	if parent[str(d)] is not None:
		addword(parent[str(d)],newword)
	else:
		new=Bktree(newword)
		print parent["word"]+"--"+str(d)+"-->"+newword
		
		parent[str(d)]=new

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



def search(word,n):
	wordlist=[]
	def process(word,n,node=root):
		d=lev(node["word"],word)
		if d <= n : wordlist.append(node["word"])
		if d-n < 0: r=0
		else: r=d-n
		for i in range (r,d+n+1):
			if node[str(i)] is not None:
				process(word,n,node[str(i)])
	process(word,n)
	return wordlist


	



if os.path.exists("tree.json"):
	print "Reading tree"
	f=open("tree.json","r")
	root=json.loads(f.read())
	f.close()
else:

	f=open("Common.txt","r")
	words=f.read()
	words=words.split('\n')
	root=Bktree(words[0])

	for i in range(1,len(words)):
		addword(root,words[i])
	t=open("tree.json","w")
	t.write(json.dumps(root))
	t.close()
	f.close()

