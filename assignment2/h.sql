SELECT sum(f1.count * f2.count ) 
FROM Frequency AS f1, Frequency AS f2
WHERE f1.term = f2.term AND f1.docid = "10080_txt_crude" AND f2.docid = "17035_txt_earn"
GROUP BY f1.docid, f2.docid
;

