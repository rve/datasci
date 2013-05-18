SELECT f1.docid,sum(f1.count * f2.count ) as count
FROM 
Frequency 
AS f1,
(
    SELECT 'q' as docid, 'washington' as term, 1 as count 
    UNION
    SELECT 'q' as docid, 'taxes' as term, 1 as count
    UNION 
    SELECT 'q' as docid, 'treasury' as term, 1 as count
) AS f2
WHERE f1.term = f2.term 
GROUP BY f1.docid, f2.docid
ORDER BY count DESC
limit 1
;

