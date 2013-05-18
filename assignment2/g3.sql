    SELECT A.row_num, A.col_num, B.row_num, B.col_num, A.value ,  B.value , A.value * B.value 
    FROM A, B 
    WHERE A.col_num = B.row_num 
;
