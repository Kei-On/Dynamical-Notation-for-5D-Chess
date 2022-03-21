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
* A **turn** is a natural number with the prefix "T". 
* A **line** is an integer with the prefix "L". 
* A **move** is the creation of
* The operation **#** is defined `A#B:=A+0.5-0.5^B (for a=n/2, n=2,3,4,5...), A#B:=-((-A)#B) (for A=-n/2, n=2,3,4,5...)`. The expression `A#B` is read as "the B-th A". 
* A **step** is a number `s=a#b`, where `a` is a 
