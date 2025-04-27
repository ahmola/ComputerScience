select product.product_code as product_code,
    sum(offline_sale.sales_amount)*product.price as sales
from offline_sale
join product on product.product_id=offline_sale.product_id
group by offline_sale.product_id
order by sales desc, product_code asc