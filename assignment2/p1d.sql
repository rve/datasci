select count(*) from Frequency where  (select count(*)  from Frequency where (select distinct docid  from Frequency)) > 300 ;
