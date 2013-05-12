select docid, docCount 
from (
	select docid, sum(count) as 'docCount' 	from frequency 	where term in ('washington', 'taxes', 'treasury') group by docid order by sum(count) desc
		
) as d order by d.docCount desc;
