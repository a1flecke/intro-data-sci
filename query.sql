sqlite3 -csv reuters.db 'select a.docid, b.docid, sum(a.count * b.count) from frequency as a join frequency as b on a.term = b.term where a.docid < b.docid group by a.docid, b.docid;' > results.txt
