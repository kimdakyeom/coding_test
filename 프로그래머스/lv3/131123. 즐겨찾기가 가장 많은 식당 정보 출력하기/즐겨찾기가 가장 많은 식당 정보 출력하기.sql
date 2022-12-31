-- 코드를 입력하세요
SELECT a.food_type, a.rest_id, a.rest_name, a.favorites
from rest_info a
join (
    select food_type, max(favorites) as favorites
    from rest_info
    group by food_type
) b
on a.favorites=b.favorites and a.food_type=b.food_type
order by a.food_type desc