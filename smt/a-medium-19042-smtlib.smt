(set-logic UFNIA)
(set-option :produce-models true)
(set-option :produce-assignments true)
(declare-const V0 Int)
(declare-const V1 Int)
(declare-const V2 Int)
(declare-const V3 Int)
(declare-const V4 Int)
(declare-const V5 Int)
(declare-const V6 Int)
(declare-const V7 Int)
(declare-const V8 Int)
(declare-const V9 Int)
(declare-const V10 Int)
(declare-const V11 Int)
(declare-const V12 Int)
(declare-const V13 Int)
(declare-const V14 Int)
(declare-const V15 Int)
(declare-const V16 Int)
(declare-const V17 Int)
(declare-const V18 Int)
(declare-const V19 Int)
(declare-const V20 Int)
(declare-const V21 Int)
(declare-const V22 Int)
(declare-const V23 Int)
(declare-const V24 Int)
(declare-const V25 Int)
(declare-const V26 Int)
(declare-const V27 Int)
(declare-const V28 Int)
(declare-const V29 Int)
(declare-const V30 Int)
(declare-const V31 Int)
(declare-const V32 Int)
(declare-const V33 Int)
(declare-const V34 Int)
(declare-const V35 Int)
(declare-const V36 Int)
(declare-const V37 Int)
(declare-const V38 Int)
(declare-const V39 Int)
(declare-const V40 Int)
(declare-const V41 Int)
(declare-const V42 Int)
(declare-const V43 Int)
(declare-const V44 Int)
(declare-const V45 Int)
(declare-const V46 Int)
(declare-const V47 Int)
(declare-const V48 Int)
(assert (and (> V0 0) (< V0 8)))
(assert (and (> V1 0) (< V1 8)))
(assert (and (> V2 0) (< V2 8)))
(assert (and (> V3 0) (< V3 8)))
(assert (and (> V4 0) (< V4 8)))
(assert (and (> V5 0) (< V5 8)))
(assert (and (> V6 0) (< V6 8)))
(assert (and (> V7 0) (< V7 8)))
(assert (and (> V8 0) (< V8 8)))
(assert (and (> V9 0) (< V9 8)))
(assert (and (> V10 0) (< V10 8)))
(assert (and (> V11 0) (< V11 8)))
(assert (and (> V12 0) (< V12 8)))
(assert (and (> V13 0) (< V13 8)))
(assert (and (> V14 0) (< V14 8)))
(assert (and (> V15 0) (< V15 8)))
(assert (and (> V16 0) (< V16 8)))
(assert (and (> V17 0) (< V17 8)))
(assert (and (> V18 0) (< V18 8)))
(assert (and (> V19 0) (< V19 8)))
(assert (and (> V20 0) (< V20 8)))
(assert (and (> V21 0) (< V21 8)))
(assert (and (> V22 0) (< V22 8)))
(assert (and (> V23 0) (< V23 8)))
(assert (and (> V24 0) (< V24 8)))
(assert (and (> V25 0) (< V25 8)))
(assert (and (> V26 0) (< V26 8)))
(assert (and (> V27 0) (< V27 8)))
(assert (and (> V28 0) (< V28 8)))
(assert (and (> V29 0) (< V29 8)))
(assert (and (> V30 0) (< V30 8)))
(assert (and (> V31 0) (< V31 8)))
(assert (and (> V32 0) (< V32 8)))
(assert (and (> V33 0) (< V33 8)))
(assert (and (> V34 0) (< V34 8)))
(assert (and (> V35 0) (< V35 8)))
(assert (and (> V36 0) (< V36 8)))
(assert (and (> V37 0) (< V37 8)))
(assert (and (> V38 0) (< V38 8)))
(assert (and (> V39 0) (< V39 8)))
(assert (and (> V40 0) (< V40 8)))
(assert (and (> V41 0) (< V41 8)))
(assert (and (> V42 0) (< V42 8)))
(assert (and (> V43 0) (< V43 8)))
(assert (and (> V44 0) (< V44 8)))
(assert (and (> V45 0) (< V45 8)))
(assert (and (> V46 0) (< V46 8)))
(assert (and (> V47 0) (< V47 8)))
(assert (and (> V48 0) (< V48 8)))
(assert (distinct V0 V1 V2 V3 V4 V5 V6 ))
(assert (distinct V7 V8 V9 V10 V11 V12 V13 ))
(assert (distinct V14 V15 V16 V17 V18 V19 V20 ))
(assert (distinct V21 V22 V23 V24 V25 V26 V27 ))
(assert (distinct V28 V29 V30 V31 V32 V33 V34 ))
(assert (distinct V35 V36 V37 V38 V39 V40 V41 ))
(assert (distinct V42 V43 V44 V45 V46 V47 V48 ))
(assert (distinct V0 V7 V14 V21 V28 V35 V42 ))
(assert (distinct V1 V8 V15 V22 V29 V36 V43 ))
(assert (distinct V2 V9 V16 V23 V30 V37 V44 ))
(assert (distinct V3 V10 V17 V24 V31 V38 V45 ))
(assert (distinct V4 V11 V18 V25 V32 V39 V46 ))
(assert (distinct V5 V12 V19 V26 V33 V40 V47 ))
(assert (distinct V6 V13 V20 V27 V34 V41 V48 ))
(assert (= 10 (+ V1 V2))) ; Region 2
(assert (= 6 (+ V3 V4))) ; Region 3
(assert (= 6 (+ V5 V6))) ; Region 4
(assert (= 3 (+ V7 V8))) ; Region 5
(assert (= 11 (+ V9 V10))) ; Region 6
(assert (= 13 (+ V11 V18))) ; Region 7
(assert (= 8 (+ V12 V13))) ; Region 8
(assert (= 12 (+ V14 V15 V22))) ; Region 9
(assert (= 7 (+ V16 V23))) ; Region 10
(assert (= 10 (+ V17 V24 V25))) ; Region 11
(assert (= 6 (+ V19 V26))) ; Region 12
(assert (= 10 (+ V20 V27))) ; Region 13
(assert (= 6 (+ V21 V28))) ; Region 14
(assert (= 5 (+ V29 V30))) ; Region 15
(assert (= 4 (+ V31 V38))) ; Region 16
(assert (= 8 (+ V32 V39))) ; Region 17
(assert (= 11 (+ V33 V40))) ; Region 18
(assert (= 8 (+ V34 V41))) ; Region 19
(assert (= 13 (+ V35 V36))) ; Region 20
(assert (= 7 (+ V37 V44))) ; Region 21
(assert (= 8 (+ V42 V43))) ; Region 22
(assert (= 18 (+ V45 V46 V47 V48))) ; Region 23
(check-sat)
(get-value (V0 V1 V2 V3 V4 V5 V6 V7 V8 V9 V10 V11 V12 V13 V14 V15 V16 V17 V18 V19 V20 V21 V22 V23 V24 V25 V26 V27 V28 V29 V30 V31 V32 V33 V34 V35 V36 V37 V38 V39 V40 V41 V42 V43 V44 V45 V46 V47 V48))
(exit)