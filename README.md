# Krakenmagen's Dynamical Notation for 5D-Chess
A dynamical notation for 5D-Chess-with-Multiverse-Time-Travel based on **Shad's 5D chess algebraic notation**

## Pro and Cons
### Pros
* Flexible. Can be easily modified by codes. 
* Can be demonstrated both algebraically and topologically. 
* Contains information of parallel actions during one turn. 
* Contains information of which action causes creation of which board/timeline. 

### Cons
* More text needed, which causes hardness for nearsighted people to read. 
* The topological presentation involves a huge amount of spaces, which rapidly increases the file size.  

### VS
#### Shad's Notation
``1. (0T1)Nd3 / (0T1)Nc5
2. (0T2)Nxc5+ / (0T2)bxc5
3. (0T3)g3 / (0T3)g4
4. (0T4)Bg2 / (0T4)d5
5. (0T5)O-O {to the right} / (0T5)Be5
6. (0T6)Nb1>>(0T5)b3 / (1T5)Bb6
7. (1T6)Nc3 / (0T6)Ne7>(1T6)e5
8. (0T7)a4 (1T7)O-O {to the right} / (0T7)Be5>>(0T6)e4
9. (-1T7)Bxe4 / (-1T7)dxe4 (1T7)c4``

#### Dynamical Notation algebraical presentation
``<0T1>1[Nd3]
<0T1>1.5[Nc5]
<0T2>2[Nxc5+]
<0T2>2.5[bxc5]
<0T3>3[g3]
<0T3>3.5[g4]
<0T4>4[Bg2]
<0T4>4.5[d5]
<0T5>5[O-O]
<0T5>5.5[Be5]
<0T6>6[Nb1>>(0T5)b3]
<1T5>6.5[Bb6]
<1T6>7[Nc3]
<0T6>7.5[Ne7>(1T6)e5]
<0T7>8[a4]
<1T7>8#2[O-O]
<0T7>8.5[Be5>>(0T6)e4]
<-1T7>9[Bxe4]
<-1T7>9.5[dxe4]
<1T7>9.5#2[c4]``

#### Dynamical Notation topological presentation
``                                                 <0T1>1[Nd3] / <0T1>1.5[Nc5]                                                                                                     
                                                 <0T2>2[Nxc5+] / <0T2>2.5[bxc5]                                                                                                  
                                                 <0T3>3[g3] / <0T3>3.5[g4]                                                                                                       
                                                 <0T4>4[Bg2] / <0T4>4.5[d5]                                                                                                      
-<1T5>-6[(0T6)Nb1>>(0T5)b3] / <1T5>6.5[Bb6]      <0T5>5[O-O] / <0T5>5.5[Be5] / -<0T5>-6[(0T6)Nb1>>(0T5)b3@(1T5)]+                                                                
 <1T6>7[Nc3] / -<1T6>-7.5[(0T6)Ne7>(1T6)e5]      <0T6>6[Nb1>>(0T5)b3]+ / <0T6>7.5[Ne7>(1T6)e5]+ / -<0T6>-8.5[(0T7)Be5>>(0T6)e4@(-1T6)]+     -<-1T6>-8.5[(0T7)Be5>>(0T6)e4]       
 <1T7>8#2[O-O] / <1T7>9.5#2[c4]                  <0T7>8[a4] / <0T7>8.5[Be5>>(0T6)e4]+                                                        <-1T7>9[Bxe4] / <-1T7>9.5[dxe4]     ``

## Recall: [Shad's 5D Chess Algebraic Notation](https://github.com/adri326/5dchess-notation/)
 
> Shad’s notation is meant to work with his engine, which means machine readability was a primary concern when creating the notation. The examples of this notation contain a header which mimics PGN. 
> 
> The symbols that are used in this notation are + for check * for softmate # for checkmate > for a temporal move >> for a branching move, and ~ for a move that rewinds the present. the symbol x is also used to denote a capture of a piece for all types of moves.
In all of the examples listed at the above link, moves are listed by layer ascending for black and descending for white. This is not an explicit rule however.
aside from this, turns are separated with /.
>
> In my opinion this notation is extremely clean and clear. Sincesince it is so verbose, it avoids a lot of edge cases that may be problems in other notations. This notation is definitely my #2 favorite and a gatekeeper/ benchmark for which to compare other notations. My only complaint is the notation does not bring up the problem of order mattering when branching multiple times in one turn.
>
> *quoted from [5D Chess Notation Standard Proposal](https://docs.google.com/document/d/1-SnsdYIzrGao0ToyGXSaoEd_0tYKxYePO1C-Bp5ziXA/edit#)*

## Recall from [Shad's Notation](https://github.com/adri326/5dchess-notation/)
* A **turn** is an alternation between white's sub-turn and black's sub-turn. Each player may only make moves during their (sub-)turn. This differs from a board step, as playing on some boards becomes optionnal when new timelines are created.
* A **move** happens when a player moves one of their pieces to a legal position. Moves that were not submitted with the submit button yet are referred to as temporary moves, but we will only consider moves that were already submitted.
* A **board** is the state of the chess board at any point in time. Each time a player moves a piece, one or two new board(s) is/are created, with the new piece disposition(s).
* A **multiverse** or a **timeline** is an alternate version of one of the game's universe. A new multiverse is created when a piece from another dimension or from the future jumps to an already-played board. Each game starts with at least one multiverse.
* A **jump** is when a piece moves outside of its board; if it jumps to another board whose turn is the current player's turn, no new multiverse is created. Otherwise, a new multiverse is created containing the piece that jumped.
* A **step** is the unit of time between board states. It is made up of two sub-steps, each being a board in time.
* **Physical** coordinates and moves are coordinates and moves within a single board.
* **Super-physical** coordinates and moves are those that span across boards. Both time- and multiverse travels are super-physical moves or jumps.

## Term Extension
We want to overwrite some terms, and add some new terms. 
* A **turn** is a integer writen with the prefix "T". 
* A **line** is an integer writen with the prefix "L". If writen along with a **turn**, the prefix "L" can be omitted. 
* A **time-space coordinate** is a **line** writen along with a **turn**. For instance `L4T5` or `4T5 (recommended)`, if the **line** prefix is omitted. 
* A **cell's coordinate** is a **time-space coordinate** writen between `<` and `>`. For instance `<4T5>`. 
* A **flat move** is a **physical move** from Shad's notation, writen between `[` and `]`. For instance `[(0T0)e3]` is a **physical move**. 
* A **spacial move** is a **move** from Shad's notation that involves time traveling but doesn't create new timeline (noted with a `>`), writen between `[` between and `]`. For instance `[(0T6)Ne7>(1T6)e5]` is a **spacial move**. 
* A **timely move** is a **move** from Shad's notation that involves time traveling and creates a new timeline, writen between `[` between and `]`. For instance, `[(0T7)Be5>>(0T6)e4]` is a **timely move**. 
* A **detailed timely move** is a **move** from Shad's notation that involves time traveling and creates a new timeline, writen behind a `[` and followed by a `@`, a **super-physical coordinate** that directs to the beginning of the created **timeline**, and a `]`. For instance, `[(0T7)Be5>>(0T6)e4@(-1T6)]` is a **detailed timely move**. **Detailed timely moves** are also seen as **timely moves**. 
* The operation **#** is defined by `A#B:=A+0.5-0.5^B (if A>=0), A#B:=-((-A)#B) (if A<0)`. The expression `A#B` is read as "the B-th A". Note that `A#1=A`, `A#B<A#C if B<C`, `A#B<C#B if A<C`, and `A#B-A-1 converges to +0 when B converges to +inf`. 
* A **step** is a rational number `S=A#B, where A=n/2, n and B are integers`, writen with the prefix "S". If writen between a **cell's coordinate** and a **move**, the prefix "S" can be omitted(recommanded). Steps can be writen only in its decimal form or its `A#B` form, where `A=n/2, n and B are integers`. For example `<4T5>S5.5#2[e3]`, `<4T5>S5.75[e3]`, `<4T5>5.5#2[e3]`(recommanded), and `<4T5>5.75[e3]` are all equivalent. 
* A **cell** is a **cell's coordinate** writen along with a **step** and a **move** with no space added in between. If the **cell's coordinate** is equal to the **super-physical coordinate** right after `[` in the **move**, the **super-physical coordinate** can be omitted. For example, `<4T5>5.5#2[(4T5)e3]` and `<4T5>5.5#2[e3]`(recommanded) are considered equivalent. 
* The python expression `"<{}T{}>{}#{}[{}]".format(turn,line,step,substep,move)` returns a **legal cell**, if `turn` and `line` are integers, `step=n/2, n and substep are integers`, and `move` is a legal move from Shad's notation, and otherwise returns an **illegal cell**. 
* A **(Krakenmagen's) dynamical notation (for 5D chess)** is a text that contains at least one **legal cell**. 

## Syntax

## 


