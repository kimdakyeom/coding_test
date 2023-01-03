-- 코드를 입력하세요
SELECT year(s.date) as year, month(s.date) as month, u.gender as gender, count(*) as users
from user_info as u
inner join
(
    select user_id, date_format(sales_date, '%Y-%m-00') as date
    from online_sale
    group by user_id, date_format(sales_date, '%Y-%m')
) as s
on s.user_id=u.user_id
where u.gender is not null
group by year(s.date), month(s.date), u.gender
order by year, month, gender