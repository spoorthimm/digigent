SELECT
    u.name          AS user_name,
    u.city          AS city,
    o.order_id      AS order_id,
    o.order_date    AS order_date,
    p.name          AS product_name,
    oi.quantity     AS quantity,
    p.price         AS price,
    pay.amount      AS amount,
    pay.payment_method AS payment_method,
    pay.status      AS status
FROM users u
JOIN orders o ON u.user_id = o.user_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
JOIN payments pay ON pay.order_id = o.order_id
ORDER BY o.order_date DESC;
