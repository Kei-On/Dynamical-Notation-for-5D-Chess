class Dyna5D(str):
  INTG = r"(?:[+-]?[1-9]\d*|[+-]?0)"
  NATR = r"(?:+?[1-9]\d*|[+-]?0)"
  REAL = r"(?:(?:(?:\+|-)?(?:[0-9]+)(?:\.[0-9]+)?)|(?:(?:\+|-)?\.?[0-9]+)|(?:[+-]?inf))"
  
  cord = r"(?:\(L?(?P<l>{})T(?P<t>{})\))".format(INTG,INTG)
  CORD = r"(?:\(L?{}T{}\))".format(INTG,INTG)
  POS = r"(?:[a-h][1-8])"
  step = r"(?:(?P<s>{})(?:#(?P<k>{}))?)".format(REAL,INTG)
  STEP = r"(?:{}(?:#{})?)".format(REAL,INTG)


  PIECE = r"(?:[PWKCQYSNRBUD]|(?:QR)|(?:PR))"
  FLAT = r"(?:\[(?:(?:{}[a-h]?[1-8]?x?[a-h][1-8])|(?:[a-h][1-8](?:=?[ABC])?)|(?:[a-h]x[a-h][1-8](?:\s*e\.p\.)?)|(?:O-O(?:-O)?))[+*#]*\??\])".format(PIECE)
  SPACIAL = r"(?:\[(?:{}?{}?{}>x?{}?{})[+*#]*\??\])".format(CORD,PIECE,POS,CORD,POS)
  BRANCH = r"(?:\[(?:{}?{}?{}>>x?{}?{}@{}?)[+*#]*~?\??\])".format(CORD,PIECE,POS,CORD,POS,CORD)

  SHEDFLAT = r"(?:(?:(?:{}?{}[a-h]?[1-8]?x?[a-h][1-8])|(?:{}?[a-h][1-8](?:=?[ABC])?)|(?:{}?[a-h]x[a-h][1-8](?:\s*e\.p\.)?)|(?:{}?O-O(?:-O)?))[+*#]*\??)".format(CORD,PIECE,CORD,CORD,CORD)
  SHEDSPACIAL = r"(?:(?:{}?{}?{}>x?{}?{})[+*#]*\??)".format(CORD,PIECE,POS,CORD,POS)
  SHEDBRANCH = r"(?:(?:{}?{}?{}>>x?{}?{})[+*#]*~?\??)".format(CORD,PIECE,POS,CORD,POS)
  SHEDMOVE = r"(?:{}|{}|{})".format(SHEDBRANCH,SHEDSPACIAL,SHEDFLAT)
  
  STRICTMOVE = r"(?:{}|{}|{})".format(BRANCH,SPACIAL,FLAT)
  MOVE = r"\[.+?\]"

  BLOCK = r"(?:{}\s*(?:{}\s*{}\s*)+)".format(CORD,STEP,MOVE)
  COMPACTBLOCK = r"(?:{}(?:{}{})+)".format(CORD,STEP,MOVE)

  cell = r"(?:(?P<cord>{})\s*(?P<step>{})\s*(?P<move>{}))\s*".format(CORD,STEP,MOVE)

  def s2f(step):
    if step[0]!="-":
      match = re.match(r"(?P<a>{})(?:#(?P<b>{}))?".format(REAL,INTG),step)
      a,b = match.group('a'),match.group('b')
      if b:
        return float(a) + 0.5 - 0.5 ** float(b)
      return float(a)
    else:
      return -step2f(step[1:])
  
  def f2s(step):
    if step>=0:
      n = int(np.floor(step))
      d = step-n
      if d>=0.5:
        d = d-0.5
        n = n+0.5
      substep = int(np.log(0.5-d)/np.log(0.5))
      if substep == 1:
        return str(n)
      return "{}#{}".format(n,substep)
    else:
      return "-"+step2s(-step)

  def loadShed(shed):
    
    metadata = "".join(re.findall("\[.+\]\s*\n",shed))
    dyna = metadata
    shed += "\n"
    shed = re.sub("\{.+?\}","",shed)
    lines = re.findall("\d+\.[^\n]*?{}.+?\n".format(Dyna5D.SHEDMOVE),shed)

    W,B = 1,-1
    for line in lines:
      i = int(re.search("(?P<i>\d+)\.",line).group("i"))
      split = line.split("/")
      white,black = split[0],""
      if len(split)>1:
        black = split[1]
      for j,move in enumerate(re.findall(Dyna5D.SHEDMOVE,white)):
        step = Dyna5D.f2s(Dyna5D.s2f("{}#{}".format(i,j+1)))
        if move[0] == "(":
          cord = re.search(Dyna5D.CORD,move).group(0)
        else:
          cord = "({}T{})".format(0,i)
          move = cord + move
        surfix = re.search("[+*#]*~?\??",move).group(0)
        if re.match(Dyna5D.SHEDBRANCH,move):
         
          target = "({}T{})".format(W,re.search(">>x?\(.+?T(?P<t>.+?)\)",move).group("t"))
          dyna += "{}{}[{}@{}{}]".format(cord,step,re.sub(surfix,"",move),target,surfix)
          dyna += "{}{}[{}@{}{}]".format(target,"-"+step,re.sub(surfix,"",move),target,surfix)
          
          W += 1
        elif re.match(Dyna5D.SHEDSPACIAL,move):
          target = re.search(">x?(?P<t>\(.+?T.+?\))",move).group("t")
          dyna += "{}{}[{}]".format(cord,step,move)
          dyna += "{}{}[{}]".format(target,"-"+step,move)
          
        elif re.match(Dyna5D.SHEDFLAT,move):
          dyna += "{}{}[{}]".format(cord,step,move)
        dyna += " "

      for j,move in enumerate(re.findall(Dyna5D.SHEDMOVE,black)):
        step = Dyna5D.f2s(Dyna5D.s2f("{}#{}".format(i,j+1))+0.5)
        if move[0] == "(":
          cord = re.search(Dyna5D.CORD,move).group(0)
        else:
          cord = "({}T{})".format(0,i)
          move = cord + move
        surfix = re.search("[+*#]*~?\??",move).group(0)
        if re.match(Dyna5D.SHEDBRANCH,move):
         
          target = "({}T{})".format(B,re.search(">>x?\(.+?T(?P<t>.+?)\)",move).group("t"))
          dyna += "{}{}[{}@{}{}]".format(cord,step,re.sub(surfix,"",move),target,surfix)
          dyna += "{}{}[{}@{}{}]".format(target,"-"+step,re.sub(surfix,"",move),target,surfix)
          
          B -= 1
        elif re.match(Dyna5D.SHEDSPACIAL,move):
          target = re.search(">x?(?P<t>\(.+?T.+?\))",move).group("t")
          dyna += "{}{}[{}]".format(cord,step,move)
          dyna += "{}{}[{}]".format(target,"-"+step,move)
          
        elif re.match(Dyna5D.SHEDFLAT,move):
          dyna += "{}{}[{}]".format(cord,step,move)
        dyna += " "
      dyna += "\n"
    return Dyna5D(dyna)

  def __new__(cls, *args, **kw):
    return str.__new__(cls, *args, **kw)
  
  def metadata(self):
    return "".join(re.findall("^(?:\[.+\]\s*\n)+",self))

  def blocks(self):
    return re.findall(Dyna5D.COMPACTBLOCK,re.sub(" ","",self))

  def cells(self):
    blocks = self.blocks()
    cells = []
    for block in blocks:
      cord = re.search(Dyna5D.CORD,block).group(0)
      stepmoves = re.findall(Dyna5D.STEP+Dyna5D.MOVE,block)
      for sm in stepmoves:
        cells.append(cord+sm)

    def key(cell):
      step = re.search(Dyna5D.cell,cell).group("step")
      m = re.search("(?P<s>{})(?:#(?P<k>{}))?".format(Dyna5D.REAL,Dyna5D.INTG),step)
      s,k = float(m.group("s")),1
      if m.group("k"):
        k = int(m.group("k"))
      if s<0:
        return -s+0.5-0.5**k+0.4**(k+1)
      return Dyna5D.s2f(re.search(Dyna5D.cell,cell).group("step"))
    return sorted(cells,key = key)

  def array(self):
    cells = self.cells()
    inf = 100000
    Lmin,Lmax,Tmin,Tmax = inf,-inf,inf,-inf
    for cell in cells:
      cord,step,move = re.match(Dyna5D.cell,cell).group("cord","step","move")
      l,t = re.search(Dyna5D.cord,cord).group("l","t")
      l,t = int(l),int(t)
      Lmin,Lmax,Tmin,Tmax = min(Lmin,l),max(Lmax,l),min(Tmin,t),max(Tmax,t)

    arr = np.empty((Lmax-Lmin+1,Tmax-Tmin+1),dtype = object)
    
    for cell in cells:
      cord,step,move = re.match(Dyna5D.cell,cell).group("cord","step","move")
      l,t = re.search(Dyna5D.cord,cord).group("l","t")
      s = re.search(Dyna5D.step,step).group("s")
      s,l,t = abs(float(s)),int(l),int(t)
      if arr[l-Lmin,t-Tmin]:
        arr[l-Lmin,t-Tmin].append(cell)
      else:
        arr[l-Lmin,t-Tmin]=[cell]
    return arr

  def topo(self,cordwidth = "{:<6}", stepwidth = "{:<7}",movewidth = "{:<20}",space = 3):
    arr = self.array()
    a,b = arr.shape
    A = np.empty((a,b),dtype = object)
    for i in range(a):
      for j in range(b):
        A[i,j] = ''
        if arr[i,j]:
          cord = re.search(Dyna5D.cell,arr[i,j][0]).group("cord")
          l,t = re.match(Dyna5D.cord,cord).group("l","t")
          ans = cordwidth.format("({}T{})".format(l,t))

          for k in range(len(arr[i,j])):
            step,move = re.match(Dyna5D.cell,arr[i,j][k]).group("step","move")
            move = re.sub("\(L?{}T{}\)".format(l,t),"",move)
            ans += stepwidth.format(step)+movewidth.format(move)
          ans = re.sub("\s*$","",ans)
          A[i,j] += ans

    A = A.transpose()
    A = np.flip(A,1)

    mx = np.amax(np.vectorize(len)(A),0)
    ans = self.metadata()
    for i in range(A.shape[0]):
      for j in range(A.shape[1]-1):

        ans += ("{:<"+str(mx[j])+"}").format(A[i,j])
        if A[i,j]!="" or A[i,j+1]!="":
          ans += space * " " + "||" + space * " "
        else:
          ans += (2*space+2)*" "
      ans += ("{:<"+str(mx[A.shape[1]-1])+"}").format(A[i,A.shape[1]-1])
      ans += "\n"
    return ans


      
dyna = Dyna5D.loadShed('''[White "Teln0"]
[Black "Shad Amethyst"]
[Board "Simple - No Queens"]
[Size "7x7"]
[Date "2020.08.14"]
[Result "1-0"]
[Mode "5D"]

1. (0T1)Nd3 / (0T1)Nc5
2. (0T2)Nxc5+ / (0T2)bxc5
3. (0T3)g3 / (0T3)g4
4. (0T4)Bg2 / (0T4)d5
5. (0T5)O-O {to the right} / (0T5)Be5
6. (0T6)Nb1>>(0T5)b3 / (1T5)Bb6
7. (1T6)Nc3 / (0T6)Ne7>(1T6)e5
8. (0T7)a4 (1T7)O-O {to the right} / (0T7)Be5>>(0T6)e4
9. (-1T7)Bxe4 / (-1T7)dxe4 (1T7)c4
10. (1T8)Nb3>(0T8)d3 (-1T8)a4 / (-1T8)Bd4 (0T8)Kd7>(1T8)d6
11. (-1T9)Ra3 (0T9)Ra3 (1T9)b3 / (-1T9)Bd4>x(0T9)d3 (1T9)cxb3
12. (-1T10)d3 (0T10)cxd3 (1T10)Ba3 / (-1T10)Nd5 (0T10)Rb7 (1T10)c5?
13. (-1T11)dxe4 (0T11)Rc3 (1T11)axb3 / (0T11)Rg5 (1T11)Ne5>x(-1T11)e4
14. (-1T12)Rd3 (0T12)d4 (1T12)b4 / (-1T12)c4 (0T12)c4 (1T12)cxb4
15. (-1T13)Rd4 (0T13)d3 (1T13)Ba4+ / (-1T13)O-O-O {to the left} (0T13)cxd3 (1T13)Bc5
16. (-1T14)Rxe4 (0T14)exd3 (1T14)Bxc5+ / (0T14)Bg2 (-1T14)Nd5>x(1T14)c5
17. (-1T15)Rc4 (0T15)Rc6 (1T15)Ra5 / (-1T15)e5 (0T15)Bd3+ (1T15)Ne4
18. (-1T16)Rb4+ (0T16)Kg1 (1T16)Nxe4 / (-1T16)Kb7>x(0T16)c6 (1T16)dxe4
19. (-1T17)Rb4>(1T17)b4 (0T17)Bxg5 / (-1T17)Bc4 (0T17)Bc4 (1T17)Nd5
20. (-1T18)Be3 (0T18)Rc1 (1T18)Rd4 / (-1T18)Rd7 (0T18)Kc6>(1T18)b6?
21. (-1T19)Bb6+ {checks (1T19)d6} (0T19)Rb1 (1T19)Raxd5+ / (-1T19)c6>(0T19)c6 {blocks (-1T20)Bb6>>x(1T20)d6 1-0} (1T19)exd5
22. (-1T20)Bb6>x(0T20)b7+ {checks (1T20)d7} (1T20)Rxd5+ / (-1T20)Bc4>>x(-1T18)a4
23. (-2T19)Bb6 / (-2T19)Rb7
24. (-2T20)Bb6>>x(-1T20)a6+ {checks (1T20)b6, (2T20)b6 also checks (1T19)b6} 1-0 {Black forfeits}
''')
print(dyna.topo())
