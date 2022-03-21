import chess
import chess.svg
import numpy as np
import re

PHYSICAL = r"((?:(?:O-O[-0]?)|(?:[KQNBR][a-h]?x?[a-h]x?[1-8])|(?:[a-h]x?[a-h]?[1-8]))\+?)((?:(?:O-O[-0]?)|(?:[KQNBR][a-h]?x?[a-h]x?[1-8])|(?:[a-h]x?[a-h]?[1-8]))\+?)"
INTG = r"(?:[+-]?[1-9]\d*|[+-]?0)"
NATR = r"(?:+?[1-9]\d*|[+-]?0)"
REAL = r"(?:(?:(?:\+|-)?(?:[0-9]+)(?:\.[0-9]+)?)|(?:(?:\+|-)?\.?[0-9]+)|(?:[+-]?inf))"


STEP = r"(?:{}(?:#{})?)".format(REAL,INTG)
def step2f(step):
  if step[0]!="-":
    match = re.match(r"(?P<a>{})(?:#(?P<b>{}))?".format(REAL,INTG),step)
    a,b = match.group('a'),match.group('b')
    if b:
      return float(a) + 0.5 - 0.5 ** float(b)
    return float(a)
  else:
    return -step2f(step[1:])
def step2s(step):
  if step>=0:
    n = int(np.floor(step))
    d = step-n
    if d>=0.5:
      d = d-0.5
      n = n+0.5
    return "{}#{}".format(n,int(np.log(0.5-d)/np.log(0.5)))
  else:
    return "-"+step2s(-step)
MAXSUBSTEP = 1
MAXTURN = 1000
while MAXTURN-0.5**(MAXSUBSTEP+1) < MAXTURN-0.5**(MAXSUBSTEP+2):
  MAXSUBSTEP = MAXSUBSTEP+1
# define a#b := a+0.5-0.5^b (for a=n/2, n=2,3,4,5...)
#        a#b := -((-a)#b)   (for a=-n/2, n=2,3,4,5...)

CELLinfo = r"(?P<cell>\<L?(?P<line>{})T(?P<turn>{})\>(?P<step>{})\[(?P<move>.*?)\])".format(INTG,INTG,STEP)
CELL = r"(?:\<L?{}T{}\>{}\[.*?\])".format(INTG,INTG,STEP)
CELLS = r"(?P<cells>(.*{}.*)+)".format(CELL)

def arr2str(arr,space = 5):
  m,n = arr.shape
  mx = np.max(np.vectorize(len)(arr),0)
  ans = ""
  for i in range(m):
    for j in range(n):
      ans += ("{:<"+str(mx[j]+space)+"}").format(arr[i,j])
    ans += "\n"
  return ans
  
class Dyna5D(str):
  def __new__(cls, *args, **kw):  
    return str.__new__(cls, *args, **kw)
  
  def findall(self):
    return re.findall(CELLinfo,self)
  
  def sorted(self):
    lst = self.findall()
    key = lambda X: abs(step2f(X[3]))
    lst = sorted(lst,key = key)
    return lst
  
  def algebraic(self,joint = " "):
    return joint.join([c[0] for c in self.sorted()])

  def hash(self):
    map = {}
    inf = 100000
    Lmin,Lmax,Tmin,Tmax = inf,-inf,inf,-inf
    lst = self.sorted()
    blines,wlines=-1,1
    for cell,L,T,stepS,move in lst:
      L,T = int(L),int(T)

      def addnote(cell):
        w = wlines
        b = blines
        if ">" in move and stepS[0]!='-':
          match = re.search("\(L?(?P<L>{})T(?P<T>{})\)".format(INTG,INTG),move)
          l,t = match.group("L"),match.group("T")
          note1 = "<{}T{}>{}[({}T{}){}]".format(l,t,"-"+stepS,L,T,move,t)
          if ">>" in move:
            if int(step2f(stepS))==step2f(stepS):
              note = "<{}T{}>{}[({}T{}){}]".format(wlines,t,"-"+stepS,L,T,move)
              note1 = "<{}T{}>{}[({}T{}){}@({}T{})]".format(l,t,"-"+stepS,L,T,move,wlines,t)
              if "{}T{}".format(wlines,t) in map.keys():
                map["{}T{}".format(wlines,t)]["-"+stepS] = note
              else:
                map["{}T{}".format(wlines,t)] = {"-"+stepS:note}
              w = wlines + 1
            else:
              note = "<{}T{}>{}[({}T{}){}]".format(blines,t,"-"+stepS,L,T,move)
              note1 = "<{}T{}>{}[({}T{}){}@({}T{})]".format(l,t,"-"+stepS,L,T,move,blines,t)
              if "{}T{}".format(blines,t) in map.keys():
                map["{}T{}".format(blines,t)]["-"+stepS] = note
              else:
                map["{}T{}".format(blines,t)] = {"-"+stepS:note}
              b = blines - 1

          if "{}T{}".format(l,t) in map.keys():
            map["{}T{}".format(l,t)]["-"+stepS] = note1
          else:
            map["{}T{}".format(l,t)] = {"-"+stepS:note1}

          
        if "{}T{}".format(L,T) in map.keys():
          map["{}T{}".format(L,T)][stepS] = cell
        else:
          map["{}T{}".format(L,T)] = {stepS:cell}
        return w,b

      if "{}T{}".format(L,T) in map.keys():
        wline,blines = addnote(cell)
      else:
        wline,blines = addnote(cell)

      Lmin,Lmax,Tmin,Tmax = min(Lmin,L),max(Lmax,L),min(Tmin,T),max(Tmax,T)
    return map,Lmin,Lmax,Tmin,Tmax

  def topologicArr(self,length = "{:<60}",head = ""):
      map,Lmin,Lmax,Tmin,Tmax = self.hash()
      arr = np.empty((Lmax-Lmin+1,Tmax-Tmin+1),dtype = object)
      for L in range(Lmin,Lmax+1):
        for T in range(Tmin,Tmax+1):
          LT = "{}T{}".format(L,T)
          if LT in map.keys():
            steps = map[LT].keys()
            steps = sorted(steps,key = lambda step:abs(step2f(step)))
            a = ""
            head = ""
            if step2f(steps[0])<0: 
              a = a + head + "-" + map[LT][steps[0]]
              if "@" in re.match(CELLinfo,map[LT][steps[0]]).group("move"):
                a = a + "+"
            else:
              a = a + head + " " + map[LT][steps[0]]
              if ">" in re.match(CELLinfo,map[LT][steps[0]]).group("move"):
                a = a + "+"
            for i in range(1,len(steps)):
              if step2f(steps[i])<0: 
                a = a + " / -" + map[LT][steps[i]]
                if "@" in re.match(CELLinfo,map[LT][steps[i]]).group("move"):
                  a = a + "+"
              else:
                a = a + " / " + map[LT][steps[i]]
                if ">" in re.match(CELLinfo,map[LT][steps[i]]).group("move"):
                  a = a + "+"
            arr[L-Lmin,T-Tmin] = a
          else:
            arr[L-Lmin,T-Tmin] = ""
      return arr
  
  def topologic(self,T = 1,flip = 1,space = 5,head = "default"):
    
    if head=="default":
      if T:
        head = ""
      else:
        head = "|"
    arr = self.topologicArr(head = head)
    if T:
      arr = arr.transpose()
    if flip:
      arr = np.flip(arr,1)
    return arr2str(arr,space)
  def shed2dyna(notation,joint = "\n"):
  ans = ""
  notation = re.sub("\{.*?\}","",notation)
  for line,i in re.findall(r"((\d+)\..+\n)",notation):
    if "/" in line:
      white,black = line.split("/")
      pat = "\s\(.+?\)[^\s]+"
      W = re.findall(pat,white)
      B = re.findall(pat,black)
      pater = "\(L?(?P<line>{})T(?P<turn>{})\)(?P<move>.+)".format(INTG,INTG)

      for j,w in enumerate(W):
        match = re.search(pater,w)
        L,T,move = match.group("line","turn","move")
        step = step2s(int(i)+0.5-0.5**(j+1))
        step = re.sub("#1","",step)
        ans+="<{}T{}>{}[{}] ".format(L,T,step,move)
        

      ans+="/ "
      for j,b in enumerate(B):
        match = re.search(pater,b)
        L,T,move = match.group("line","turn","move")
        step = step2s(int(i)+0.5+0.5-0.5**(j+1))
        step = re.sub("#1","",step)
        ans+="<{}T{}>{}[{}] ".format(L,T,step,move)
        
      ans+="\n"
  return Dyna5D(ans)
