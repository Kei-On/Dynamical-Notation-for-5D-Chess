# Krakenmagen's Dynamical Notation for 5D-Chess
A dynamical notation for 5D-Chess-with-Multiverse-Time-Travel based on Shad's-5D-chess-algebraic-notation

## [Shad's 5D chess algebraic notation](https://github.com/adri326/5dchess-notation/)
 
> Shad’s notation is meant to work with his engine, which means machine readability was a primary concern when creating the notation. The examples of this notation contain a header which mimics PGN. 
> 
> The symbols that are used in this notation are + for check * for softmate # for checkmate > for a temporal move >> for a branching move, and ~ for a move that rewinds the present. the symbol x is also used to denote a capture of a piece for all types of moves.
In all of the examples listed at the above link, moves are listed by layer ascending for black and descending for white. This is not an explicit rule however.
aside from this, turns are separated with /.
>
> In my opinion this notation is extremely clean and clear. Sincesince it is so verbose, it avoids a lot of edge cases that may be problems in other notations. This notation is definitely my #2 favorite and a gatekeeper/ benchmark for which to compare other notations. My only complaint is the notation does not bring up the problem of order mattering when branching multiple times in one turn.
>
> quoted from [5D Chess Notation Standard Proposal](https://docs.google.com/document/d/1-SnsdYIzrGao0ToyGXSaoEd_0tYKxYePO1C-Bp5ziXA/edit#)

## [Term Recall](https://github.com/adri326/5dchess-notation/)
> * A **turn** is an alternation between white's sub-turn and black's sub-turn. Each player may only make moves during their (sub-)turn. This differs from a board step, as playing on some boards becomes optionnal when new timelines are created.
> 
> * A **move** happens when a player moves one of their pieces to a legal position. Moves that were not submitted with the submit button yet are referred to as temporary moves, but we will only consider moves that were already submitted.
> 
> * A **board** is the state of the chess board at any point in time. Each time a player moves a piece, one or two new board(s) is/are created, with the new piece disposition(s).
> 
> * A **multiverse** or a **timeline** is an alternate version of one of the game's universe. A new multiverse is created when a piece from another dimension or from the future jumps to an already-played board. Each game starts with at least one multiverse.
> 
> * A **jump** is when a piece moves outside of its board; if it jumps to another board whose turn is the current player's turn, no new multiverse is created. Otherwise, a new multiverse is created containing the piece that jumped.
> 
> * A **step** is the unit of time between board states. It is made up of two sub-steps, each being a board in time.
> 
> * **Physical** coordinates and moves are coordinates and moves within a single board.
> 
> * **Super-physical** coordinates and moves are those that span across boards. Both time- and multiverse travels are super-physical moves or jumps.

## Term Extension
We want to overwrite some terms, and add some new terms. 
* A **turn** is a integer writen with the prefix "T". 
* A **line** is an integer writen with the prefix "L". If writen along with a **turn**, the prefix "L" can be omitted. 
* A **time-space coordinate** is a **line** writen along with a **turn**. For instance `L4T5` or `4T5 (recommended)`, if the **line** prefix is omitted. 
* A **cell's coordinate** is a **time-space coordinate** writen between `<` and `>`. For instance `<4T5>`. 
* A **move** is move from Shad's-5D-chess-algebraic-notation, writen between `[` and `]`. 
* The operation **#** is defined by `A#B:=A+0.5-0.5^B (if A>=0), A#B:=-((-A)#B) (if A<0)`. The expression `A#B` is read as "the B-th A". Note that `A#1=A`, `A#B<A#C if B<C`, `A#B<C#B if A<C`, and `A#B-A-1 converges to +0 when B converges to +inf`. 
* A **step** is a rational number `S=A#B, where A=n/2, n and B are natrual numbers`, writen with the prefix "S". If writen between a **cell's coordinate** and a **move**, the prefix "S" can be omitted(recommanded). Steps can be writen only in its decimal form or its `A#B` form, where `A=n/2, n and B are natrual numbers`. For example `<4T5>S5.5#2[e3], <4T5>S5.75[e3], <4T5>5.5#2[e3], and <4T5>5.75[e3]` are all equivalent. 
* A **cell** is **cell's coordinate** writen along with a **step** and a **move** with no spaces in between. For instance, the python expression `"<{}T{}>{}#{}[{}]".format(turn,line,step,substep,move)` returns a **cell**. 
