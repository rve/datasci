    SELECT A.row_num, A.col_num, sum(A.value * B.value)  AS value 
    FROM A, B 
    WHERE A.col_num = B.row_num AND A.row_num = 2 AND B.col_num = 3
    GROUP BY A.row_num, B.col_num
;
