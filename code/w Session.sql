-- 1.1
select * from goods order by goods_id desc;
-- 2.1
create table newtable1(select goods_id from goods);
select * from newtable1;
-- 2.2
select goods_name from goods;
-- 2.3SELECT order_id,order_sn,total_amount
FROM orderform 
WHERE order_id NOT IN (SELECT TOP 8 order_id FROM orderform);
select goods_id, goods_name, market_price from goods;
-- 2.4
select * from goods_type;
-- 2.5
SELECT goods_name AS"商品名称",
market_price AS "市场价",
shop_price AS "本店价",
click_count 
FROM goods;
SELECT user_address.mobile AS "订单表中的电话号码",
users.mobile AS "用户收货信息表的电话号码",
user_address.address
FROM user_address, users
WHERE user_address.user_id = users.user_id;
SELECT goods_name,market_price AS 市场价,cost_price AS 成本价,
(market_price - cost_price) AS 商品盈利 
FROM goods;
SELECT MAX(market_price) AS "市场价最高",MIN(market_price) AS "市场价最低" 
FROM goods; 
-- 2.6
select consignee, address, mobile from orderform;
select DISTINCT consignee, address, mobile from orderform;
-- 2.7
SELECT TOP 5 goods_name,market_price
FROM goods;
SELECT goods_name,market_price
FROM shop.goods
LIMIT 5;
SELECT goods_name,market_price
FROM shop.goods
LIMIT 2,5; 
SELECT goods_name,market_price
FROM shop.goods
LIMIT 5 OFFSET 2; 
SELECT "goods_name", "market_price"
FROM "goods"
WHERE ROWNUM <= 5; 
-- 3.1
select name + cat_name AS '品牌信息' from brand;-- sql server
select concat(name, cat_name) AS '品牌信息' from brand;-- mysql
select concat_ws("", name, cat_name) as 品牌信息 from brand;
select cat_name, count(id), group_concat(name) as 分组 from brand group by cat_name;-- mysql
create table brandsssss(select cat_name, id from brand);
select * from brandsssss;
-- 3.2
SELECT goods_id AS 商品ID,goods_name AS 商品名称,
(shop_price - cost_price) AS 销售利润 
FROM goods;
SELECT goods_id AS 商品ID,goods_name AS 商品名称,
(shop_price * sales_sum) AS 销售额 
FROM goods;
SELECT goods_id AS 商品ID,goods_name AS 商品名称,
(sales_sum*shop_price - cost_price*sales_sum)/sales_sum AS 销售利润 
FROM goods
WHERE sales_sum <> 0;
-- 3.3
SELECT goods_id AS 商品ID,goods_name AS 商品名称,
cost_price + 50 AS 进价加50
FROM goods;
SELECT goods_id AS 商品ID,goods_name AS 商品名称,
concat(sales_sum, '个') AS 销售数量,
concat(shop_price, '元') AS 商场价格 FROM goods; 
SELECT goods_id AS 商品ID,goods_name AS 商品名称,1+1,concat('字符',"串列") as "字符串列"
FROM goods;
-- 4.2
SELECT * FROM goods WHERE goods_id = 106;
SELECT goods_id,goods_name,click_count FROM goods 
WHERE click_count > 50;
SELECT goods_id,goods_name,store_count FROM goods 
WHERE store_count < 1000;
SELECT goods_id,goods_name,sales_sum 
FROM goods 
WHERE sales_sum >= 5;
SELECT goods_id,goods_name,click_count
FROM goods 
WHERE click_count <= 20;
SELECT goods_id,goods_name,shop_price
FROM goods 
WHERE shop_price <= 2000; 
SELECT goods_id,goods_name,shop_price
FROM goods 
WHERE shop_price >= 2000; 
SELECT goods_id,goods_name,is_new FROM goods WHERE is_new != 0;
SELECT goods_id,goods_name,is_new FROM goods WHERE is_new <> 0;
-- 5.1
SELECT goods_id AS 商品ID,goods_name AS 商品名称,market_price AS 市场价
FROM goods
WHERE market_price BETWEEN 1000 AND 3000; 
-- 5.2
SELECT ISBN,bookname,INTime AS 数据录入时间 FROM bookinfo_zerobasis 
WHERE INTime
BETWEEN '2017-12-1' AND '2018-12-1';
-- 5.3
SELECT ISBN,BookName,INTime 数据录入时间 FROM bookinfo_zerobasis WHERE INTime 
BETWEEN
DATE_ADD(DAY,-1,GETDATE()) 
AND
GETDATE();-- sql setver
select ISBN, BookName,INTime 数据录入时间 from bookinfo_zerobasis
where INTime between date_sub(now(), interval 15616 day) and now();
-- 5.4
SELECT goods_id,goods_name,market_price 
FROM goods 
WHERE market_price NOT BETWEEN 2000 AND 3000; 
-- 5.5
--查询明日图书表中所有图书信息
SELECT ISBN,bookname,writer,price,intime FROM bookinfo ORDER BY ISBN;
--把长日期格式数据转化为短日期格式数据
SELECT ISBN,bookname, CONVERT(char(10),intime,120) AS 数据录入日期 
FROM bookinfo ORDER BY ISBN;-- sql server
--将日期格式中的“-”转化为“/”
SELECT ISBN,bookname, REPLACE(CONVERT(char(10),intime,120),'-','/') 
AS 数据录入日期 
FROM bookinfo ORDER BY ISBN;-- sql server
select ISBN, BookName, date_format(INTime, "%Y-%m-%d")
from bookinfo
order by ISBN;
select ISBN, BookName, date_format(INTime, "%Y\%m\%d")
from bookinfo
order by ISBN;
SELECT 书号,书名,
CONVERT(char(10),出版日期,120) 出版日期,
CONVERT(char(10),下一次出版日期,120) 下一次出版日期,
DATEDIFF(day,出版日期,下一次出版日期) 两次出版相差的天数
FROM bookpub;-- sql server
select 书号, 书名,
date_format(出版日期, "%Y-%m-%d") as "出版日期",
date_format(下一次出版日期, "%Y-%m-%d") as "下一次出版日期",
datediff(下一次出版日期, 出版日期) as 再次出版相差日期
from bookpub;
SELECT BookName,Type,pDate FROM bookinfo
WHERE MONTH(pDate)=10 AND YEAR(pDate)=2017
AND Type = '零基础系列';
select BookName, Type, pDate
from bookinfo
where date_format(pDate, "%m") = 10
and Type = "零基础系列";
-- 6.1
SELECT goods_id,goods_name,shop_price 
FROM goods 
WHERE shop_price > 3000 AND shop_price < 6000;
SELECT goods_name,click_count,store_count,shop_price
FROM goods 
WHERE click_count > 20 AND store_count = 1000 AND shop_price > 2000;
-- 6.2
SELECT ISBN,BookName,Writer,Price
FROM bookinfo_zerobasis
WHERE BookName = '零基础学Java' OR BookName = '零基础学PHP';
SELECT BookName,Price,pDate 
FROM bookinfo 
WHERE BookName LIKE '%PHP%' OR BookName LIKE '%Oracle%' OR BookName LIKE '%Android%';
-- 6.3
SELECT goods_id,goods_name,store_count 
FROM goods 
WHERE NOT store_count = 1000;
-- 6.4
SELECT goods_id,goods_name,store_count 
FROM goods 
WHERE store_count != 1000;
SELECT cat_id,goods_name,shop_price 
FROM goods 
WHERE cat_id = 191 OR cat_id = 123 AND shop_price > 2000;
SELECT cat_id,goods_name,shop_price 
FROM goods 
WHERE (cat_id = 191 OR cat_id = 123) AND shop_price > 2000;
SELECT BookName,publisher,Writer 
FROM bookinfo 
WHERE (BookName LIKE '%PHP%' OR BookName LIKE '%JSP%') AND (NOT publisher = '机械工业出版社');
SELECT cat_id,goods_name,shop_price 
FROM goods 
WHERE (NOT cat_id = 191) AND (NOT cat_id = 123);
-- 7.1
SELECT cat_id,goods_name,shop_price
FROM goods 
WHERE cat_id IN (191,123,131);
SELECT name,cat_name 
FROM brand 
WHERE name IN ('OPPO','维维','湾仔码头','华硕/ASUS');
-- 7.2
SELECT goods_name,shop_price 
FROM goods 
WHERE shop_price IN (3799-100,3799,3799+100);
-- 7.3
SELECT goods_name,market_price,shop_price 
FROM goods 
WHERE 3899 IN (market_price,shop_price);
-- 7.4
SELECT BookName,Writer,pDate
FROM bookinfo_zerobasis
WHERE pDate NOT IN ('2017年8月','2017年9月');
SELECT order_id,order_sn,total_amount
FROM orderform 
WHERE order_id NOT IN (SELECT TOP 8 order_id FROM orderform); -- sql server
select order_id, order_sn, total_amount
from orderform
where order_id not in (select order_id from (select order_id from orderform limit 8) as foo);
select order_id, order_sn, total_amount
from orderform
limit 2000 offset 8; -- 这个取得数据没有2000,就会把能取出来的全部取出来
select order_id, order_sn, total_amount
from orderform
limit 8, 2000;
-- 8.1
SELECT TOP 6 user_id,email,CONVERT(VARCHAR(10),reg_time,120) AS reg_time 
FROM users; -- sql server
SELECT user_id,email,DATE_FORMAT(reg_time,'%Y/%m/%d') AS reg_time 
FROM shop.users 
LIMIT 6;
-- 8.2
SELECT  user_id,email,CAST(total_amount AS int) AS total_amount 
FROM users
limit 6;
-- 8.3
SELECT address_id,LTRIM(consignee) AS consignee 
FROM user_address
limit 6;
-- 9.2
SELECT goods_id,goods_name,shop_price 
FROM goods 
WHERE goods_name LIKE '%华为%';
-- 9.3
SELECT address_id,LTRIM(consignee) AS consignee,address
FROM user_address 
WHERE LTRIM(consignee) LIKE '___';
-- 9.4
SELECT id,name,cat_name 
FROM brand
WHERE name LIKE '[A-Z]%'; -- 只有sql server和access可以使用[]创建集合
-- mysql使用正则表达式，且regexp调用的是search方法
select id, name, cat_name 
from brand
where name regexp "^[A-Z]"
limit 6; 
SELECT order_id,order_sn,total_amount
FROM orderform 
WHERE order_sn regexp '[6-9]$';
-- 9.5
SELECT id,name,cat_name
FROM brand 
WHERE name regexp '^[^A-Z]'
limit 6;
-- 9.6
SELECT user_id,email,CONVERT(VARCHAR(10),birthday,120) AS birthday
FROM users 
WHERE email LIKE '%/_%' ESCAPE '/'; -- sql server
select user_id, email, date_format(birthday, "%Y-%m-%d") as birthday
from users
where email like "%/_%" escape "/";
select user_id, email, date_format(birthday, "%Y-%m-%d") as birthday
from users 
where email regexp "_"; 
--10.1
SELECT goods_id,goods_name,shop_price FROM (SELECT TOP 6 * FROM goods) aa
WHERE NOT EXISTS (SELECT * FROM (SELECT TOP 5 * FROM goods) bb 
WHERE aa.goods_id=bb.goods_id); -- sql server
select goods_id, goods_name, shop_price 
from goods 
limit 1 offset 5; 
select goods_id, goods_name, shop_price 
from goods 
limit 5, 1; 
SELECT TOP 1 goods_id,cat_id,goods_name FROM goods order by NEWID();
SELECT TOP 1 goods_id,cat_id,goods_name FROM goods order by NEWID();
SELECT goods_id,cat_id,goods_name 
FROM goods 
ORDER BY RAND() 
LIMIT 6, 2; -- 这样的限制是不够准确的，每次排序都是随机排序过一次的
-- 要想从第七条开始就用子查询，在limit 2
SELECT "goods_id","cat_id","goods_name" FROM (
SELECT "goods_id","cat_id","goods_name" FROM "goods" ORDER BY DBMS_RANDOM.VALUE()) 
WHERE ROWNUM=1;
SELECT
  (
    SELECT
      COUNT(order_id)
    FROM
      orderform as A
    WHERE
      A.order_id >= B.order_id
  ) as 编号,
  order_id,
  order_sn,
  total_amount
FROM
  orderform as B
ORDER BY
  1;
-- mariaDB支持row_number() over()函数哦，上面的还可以写的更加简单点
select row_number() over(order by order_id desc) as 编号, order_id, order_sn, total_amount from orderform;

SELECT 编号,ISBN,BookName,Writer FROM (
SELECT ROW_NUMBER() OVER(ORDER BY ISBN) 编号,ISBN,BookName,Writer
FROM bookinfo_zerobasis) a WHERE a.编号%2=1;
SELECT 编号,ISBN,BookName,Writer FROM (
SELECT ROW_NUMBER() OVER(ORDER BY ISBN) 编号,ISBN,BookName,Writer
FROM bookinfo_zerobasis) a WHERE a.编号 BETWEEN 3 AND 6;
-- 10.2
SELECT user_id,email,nickname 
FROM users 
WHERE nickname IS NULL;
SELECT user_id,email,nickname 
FROM users 
WHERE nickname IS NOT NULL;
SELECT BookName,Writer,ISNULL(newbook,0) AS newbook
FROM bookinfo_zerobasis; -- sql server
SELECT user_id,email,ISNULL(nickname) AS nickname 
FROM users;
SELECT user_id,email,NULLIF(nickname,'Andy') AS nickname 
FROM users;









select * from goods where 3899 in (shop_price) or 2799 in (shop_price);  
select * from goods where shop_price=3899 or shop_price=2799;  
select consignee from user_address