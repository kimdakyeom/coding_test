SELECT b.BOOK_ID, a.AUTHOR_NAME, date_format(b.PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
from book b 
join author a on b.author_id = a.author_id
where b.category = '경제'
order by b.PUBLISHED_DATE