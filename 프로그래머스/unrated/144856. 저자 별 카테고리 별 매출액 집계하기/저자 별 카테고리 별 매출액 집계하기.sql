select 
    b.author_id, 
    a.author_name, 
    b.category, 
    (sum(b.price * s.sales)) as total_sales
from book as b
left join book_sales as s
on b.book_id=s.book_id
left join author as a
on b.author_id=a.author_id
where year(s.sales_date)=2022 and month(s.sales_date)=1
group by b.author_id, b.category
order by b.author_id, b.category desc