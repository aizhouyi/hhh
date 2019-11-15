## 第一章 sql语言概述
### 1.1 数据库基本概念
1. 数据（data）：描述事物的符号记录。
2. 数据库（databases），简称db：存放数据的仓库，所有的数据按照一定的格式在计算机上进行保存。
3. 数据库管理系统（database management system，简称dbms）：科学组织和存放数据。高效获取和维护数据。提供了数据操作语言(data manipulation language)，用户可以使用dml操作数据，实现对数据库的基本操作，增、删、查、改。
4. 数据库系统（database system，简称dbs）：在计算机系统中引入数据库后的系统。这是一个复杂的，一般由数据库，数据库管理系统（及其开发工具），应用系统，数据库管理员（负责数据库的建立、使用、维护）构成。
### 1.2 sql概述
1. sql（structured query langusge），结构化查询语言是数据库的标准语言。
2. sql语言功能基本功能包括数据查询、数据操纵、数据定义、数据控制四个部分。
3. 核心功能6个动词，select、 create、 insert、 update、 delete、grant（revoke）
### 1.3 sql语言组成
数据操作类sql语句
| 语句   | 功能                         |
| ------ | ---------------------------- |
| select | 从数据表中检索数据行和列     |
| insert | 把新的数据记录添加到数据库中 |
| delete | 从数据库中删除数据记录       |
| update | 修改现有数据库中的数据       |
数据定义类sql语句
| 语句             | 功能                             |
| ---------------- | -------------------------------- |
| create table     | 在数据库中创建一个表             |
| drop table       | 丛数据库中删除一个表             |
| alter table      | 修改一个现存表的结构             |
| create view      | 把一个新的视图添加到数据中       |
| drop view        | 丛数据库中删除视图               |
| create index     | 为数据库表中的一个字段创建索引   |
| drop index       | 从数据库中表的一个字段中删除索引 |
| create procedure | 在数据库中创建一个存储过程       |
| drop procedure   | 从数据库中删除存储过程           |
| create trigger   | 创建一个触发器                   |
| drop trigger     | 从数据库中删除触发器             |
| create schema    | 向数据库中创建一个新模式         |
| drop schema      | 从数据库中删除一个模式           |
| create domain    | 创建一个数值值域                 |
| alter domain     | 改变域定义                       |
| drop domain      | 从数据库中删除一个域             |
数据控制类sql语句
| 语句   | 功能             |
| ------ | ---------------- |
| grant  | 授予用户访问权限 |
| deny   | 拒绝用户访问     |
| revoke | 删除用户访权限   |
事物控制类sql语句
| 语句            | 功能                     |
| --------------- | ------------------------ |
| commit          | 结束当前事务             |
| rollback        | 回滚事务                 |
| set transctiona | 定义当前事务数据访问特征 |
程序化sql语句
| 语句     | 功能                     |
| -------- | ------------------------ |
| declare  | 定义查询游标             |
| explan   | 描述查询数据访问计划     |
| open     | 检索查询结果打开一个游标 |
| fetch    | 检索一条查询结果记录     |
| close    | 关闭游标                 |
| prepare  | 为动态执行准备sql语句    |
| execute  | 动态执行sql语句          |
| describe | 描述准备好的查询         |
### sql语句结构
每条sql语句均由一个谓词（verb）开始，显然的，该谓词描述这条语句要产生的动作。谓词之后紧跟一条或多条子句（clause），字句中给出了被谓词作用的数据或提供谓词动作的详细信息。
```sql
select 子句
[info 子句]
from 子句
[where 子句]
[group by 子句]
[having 子句]
[order by 子句];
```
## 第二章 简单查询
### 2.1 selete语句基本结构
1. 使用selete语句可以从数据表中或视图中进行查询，并将查询结构以表格形式返回，这个返回的结果叫做结果集。在sql中，关键字不缺分大小写
```sql
select select_list-- 指定需要查询的列
[info new_table]-- 创建的新表并将查询行插入新表new_table中,mysql不支持这个,用create table newtable1(select goods_id from goods);或者用insert语句
from table_name-- 指定需要查询的表，也称来源表
[where seatch_condition]-- 限制返回的行搜索条件
[group by group_by_expression]-- 根据group_by_expression列中值将结果分组
[having search_condition]--指定组或聚合的搜索条件。逻辑上将，having字句从中间结果集进行筛选，这些中间结果集是用select语句的from，where或group by字句创建的。通常与group by一起使用，但是并不是非得要group by
[order by order_expression [asc|desc]];-- 按照order_expression定义结果集中的行排列的顺序升序asc和降序desc
```
### 2.2 单列查询
```sql
select select_list from table_nmae;
```
查询单列
### 2.3 多列查询
```sql
select select_list1,...,select_list26 from table_nmae;
```
只需要用英文逗号隔开列名即可，按照选择顺序显示结果集  
### 2.4 所有列查询
```sql
select * from table_name;
```
有时候需要对所有列查询，用"*"符号
### 2.5 别名应用
1. 创建数据表时候，表的名字会千奇百怪，查询的时候我们希望可以使用别名来代替
   - 使用引号，单双引号都可以
    ```sql
    select goods_name "名称" from goods;
    select goods_name '名称' from goods;
    ```
   - 也可以直接不使用引号
    ```sql
    select goods_nmae 名称 from goods;
    ```
   - 使用as关键字
    ```sql
    select goods_name as "名称" from goods;
    ```
2. 多个表中可能会有相同的名字
    - 例子   
    注意：当不同的表里有相同名字的列时候，同时查询时候需要详细声明，即表.列名去选择
    ```sql
    select user_address.mobile as "订单表中的电话号码",
    users.mobile as "用户收货信息表的电话号码",
    user_address.address
    from user_address, users
    where user_address.user_id = users.user_id;
    ```
3. 为计算结果设置别名的列
    - 例子   
    注意：如果没有设置别名，那么默认值是计算式子
    ```sql
    select goods_name,market_price as 市场价,cost_price as 成本价,
    (market_price - cost_price) as 商品盈利 
    from good
    ```
4. 计算聚合函数的列设置别名
    - 例子   
    ```sql
    select max(market_price) as "市场价最高",min(market_price) as "市场价最低" 
    from goods; 
    ```
### 2.6 删除重复数据
使用关键字distinct，这个关键字是只能用在所有选择的列名前面，而且只能用一次！  
这个关键字不是指某一列，而是指不重复select输出的所有列！！
```sql
select consignee,address,mobile from orderform;
select distinct consignee,address,mobile from orderform;
```
简单来说，只有完全一样的才会删除，distinct就是指输出独一无二的
### 2.7 限制查询结果
如果由100万行的数据，用"*"就非常的浪费时间，可以限制查询。
- sql server 
    top关键字，top n指的就是前n行
    
    ```sql
    select top 5 goods_name,market_price
    from goods;
    ```
- mysql
    使用limit关键字,limit n一个数字就是前n条，limit m,n就是从第m+1开始的之后的n条数据，包括第m+1条，limit n offset m 一样的效果，n条数据
    ```sql
    SELECT goods_name,market_price
    FROM shop.goods
    LIMIT 5;
    SELECT goods_name,market_price
    FROM shop.goods
    LIMIT 2,5; 
    SELECT goods_name,market_price
    FROM shop.goods
    LIMIT 5 OFFSET 2; 
    ```
- oracle
    ```sql
    SELECT "goods_name", "market_price"
    FROM "goods"
    WHERE ROWNUM <= 5;
    ```
## 第三章
### 3.1 连接列值
中文排序，拼音首字母，先转码gbk  
select address from user_address order by convert(address using gbk); 
## 第十章 行数据过滤
### 10.2
1. 查询空值   
    ```sql
    select user_id, email, nickname from users where nickname is null;
    ```
2. 查询非空值
    ```sql
    select user_id, email, nickname from users where nickname is not null;
    ```
3. 对空值的处理函数   
    详细来说有四个，isnull(expr), nullif(expr1, expr2),ifnull(expr1,expr2),if(expr1, expr2, expr2)   
    - 在sql server中isnull有两个参数，isnull(expr,a),expr是null则a，否则是expr。
    mysql只有一个，isnull(expr)，expr是null则返回1，否则是0。
    ```sql
    select user_id, email, isnull(nickname) as nickname from users;
    ```
    - nullif(expr1, expr2)，如果expr1和expr2相等，则返回null，否则返回expr1。
    ```sql
    select user_id, email, nullif(nickname, "Andy") as nickname from users;
    ```
    - 想要实现sql server的isnull功能，mssql是有一个ifnull(expr1, expr2)可以实现，如果expr1是null则返回expr2，否则返回expr1。
    ```sql
    select BookName, Writer, ifnull(newbook, 0) as newbook from bookinfo_zerobasis;
    ```
    - 还有一个更加全面的if(expr1, expr2, expr3)，如果expr1是True，则返回expr2,否则返回expr3。
    ```sql
    SELECT user_id,email, nickname,if(nickname, 1 , -1) as flag FROM users;  -- 这样写没用的，全是-1,不理解这里，这里只能这样写，其他俩个都是没起作用的
    SELECT user_id, email, nickname,if(isnull(nickname), 1 , -1) as flag FROM users; 
    ```
## 第十一章 数据排序
### 11.1 数值排序
sql中读取数据表的行引入了索引，结果集的行可能会按照索引来进行排列，并不一定。  
如果想要精准控制顺序，order by关键字   
order by {order_by_expression [asc|desc]} [,...n]   
order_by_expression是指定的排序的列名或别名，可以指定多个排序列   
asc是默认升序，desc是降序
1. 升序和降序   
    ```sql
    SELECT goods_id,goods_name,sales_sum 
    FROM goods 
    ORDER BY sales_sum DESC;
    ```
2. 按列的别名排序
    ```sql
    SELECT goods_id 商品编号,goods_name 商品名称,sales_sum 商品销量 
    FROM goods 
    ORDER BY 商品销量 DESC;
    ```
    只要order by后面的字段有引号排序就失去作用，避免空格！！！干  
    ~~SELECT goods_id 商品编号,goods_name 商品名称,sales_sum "商品  销量"
    FROM goods
    ORDER BY "商品  销量" DESC;~~
    原来用反引号，我干！！！
    ```sql
    SELECT goods_id 商品编号,goods_name 商品名称,sales_sum `商品  销量` 
    FROM goods  
    ORDER BY `商品  销量` DESC; 
    ```
3. 多列排序
    多个排序，主排列有重复值情况才会再去按照副排列去排列
    ```sql
    SELECT goods_id,goods_name,shop_price
    FROM goods
    ORDER BY shop_price,goods_name;
    select goods_id, goods_name, shop_price 
    from goods 
    order by shop_price desc 
    limit 3;  
    select goods_id, goods_name, shop_price 
    from goods 
    order by shop_price  
    limit 1; 
    ```
### 11.2 汉字排序
~~SELECT TOP 3 goods_id,goods_name,shop_price
    FROM goods
    ORDER BY shop_price DESC;
    SELECT TOP 1 goods_id,goods_name,shop_price
    FROM goods
    ORDER BY shop_price;
    SELECT * FROM
    (SELECT "goods_id", "goods_name", "shop_price"
    FROM "goods" 
    ORDER BY "shop_price" DESC)
    WHERE rownum <= 3;
    SELECT "goods_id", "goods_name", "shop_price"
    FROM (SELECT "goods_id", "goods_name", "shop_price" FROM "goods" ORDER BY "shop_price") 
    WHERE rownum = 1;
    SELECT * FROM tb_name;
    SELECT *
    FROM tb_name
    ORDER BY LEFT(name,1) COLLATE Chinese_PRC_Stroke_CS_AS_KS_WS DESC;
    SELECT * FROM tb_name;
    SELECT *
    FROM tb_name
    ORDER BY LEFT(name, 1) COLLATE Chinese_PRC_CS_AS_KS_WS DESC;~~
## 第十二章 数据简单统计分析
### 12.1 聚合函数
聚合函数一定是对一组值进行计算然后返回一个单一的值，也被称作聚集函数或者统计函数。   
具体有count(),sum(),avg(),max(),min()   
count(*)求出所有记录，即多少行。
### 12.2 求平均值
1. avg()函数
    avg([distinct] expression)  
    对非重复值进行计算  
    参与计算的类型必须为数值型，并且不允许谓聚合函数和子查询
    - 一般用法
    ```sql
    SELECT AVG(shop_price) AS 平均值
    FROM goods; 
    SELECT cast(AVG(shop_price) as decimal(10,3)) AS 平均值
    FROM goods;
    SELECT cast(AVG(shop_price) as decimal) AS 平均值
    FROM goods;
    SELECT cast(avg(shop_price) as int) AS 平均值
    FROM goods;
    ```
    ~~SELECT cast(avg(shop_price) as real) AS 平均值
    FROM goods;~~
2. 使用where字句去限制函数统计的行
    ```sql
    SELECT AVG(shop_price) AS 平均值
    FROM goods
    WHERE shop_price > 3000;
    SELECT cast(AVG(shop_price) as decimal(18,2)) AS 平均值
    FROM goods
    where shop_price > 3000;
    select goods_name, store_count, shop_price 
    from goods 
    where shop_price > (select avg(shop_price) from goods);
    ```
### 12.3 获取结果集合行数  
1. count()函数是一种总计函数，对于count()函数处理行的个数是没有限制的    
    count([distinct] *|expression)
    - count(*)是返回表的所有行，不管是不是重复，不管是不是包含null
    ```sql
    SELECT COUNT(*) AS 商品个数
    FROM goods
    WHERE (shop_price > 3000);
    ```
    - count(expression)是对表达式的返回值进行处理，只对不是null进行计数,这个null值就会不纳入计数当中了
    ```sql
    select goods_name, cat_id from goods;  
    select distinct goods_name, cat_id from goods;  
    select distinct cat_id from goods;  
    SELECT COUNT(cat_id) AS 商品种类 FROM goods;
    select count(distinct cat_id)from goods;  
    ```
    - 实际上，count()函数参数可以是实际的字符串和数字，count()函数的参数都不会是null值，所以count()函数对所有的参数都进行统计。说人话就是，仍旧返回整个表的行数
    ```sql
    select count(213213) from goods; 
    select count("sss") from goods; 
    ```
### 12.4 最值
1. 这个参数类型可以是数字，字符，日期！！！  
    max([disttinct]expression)  
    min([disttinct]expression)
    返回数据类型和参数一致  
    将会忽略null，只要有一个非null，否则返回null值。  
    ```sql
    SELECT AVG(shop_price) AS 去掉最大值与最小值的平均值 FROM goods 
    WHERE goods_name LIKE '%液晶电视%'
    AND shop_price NOT IN(
    (SELECT MIN(shop_price) AS 最小值 FROM goods WHERE goods_name LIKE '%液晶电视%')
    ,
    (SELECT max(shop_price) AS 最大值 FROM goods WHERE goods_name LIKE '%液晶电视%'));
    ```
    ```sql
    SELECT AVG(shop_price) AS 去掉最大值与最小值的平均值 FROM goods 
    WHERE goods_name LIKE '%液晶电视%'
    AND shop_price NOT IN(
    SELECT MIN(shop_price) AS 最小值 FROM goods WHERE goods_name LIKE '%液晶电视%'
    union
    SELECT max(shop_price) AS 最大值 FROM goods WHERE goods_name LIKE '%液晶电视%');
    ```
    提一句，通过上面的例子可以看出，in操作符号后面是一定用括号括起来可以是一列表，但是在使用子查询组合union时候注意不要给子查询打括号，这时候应该先union合并成一个结果集合再去in过滤  
    ```sql
    select avg(shop_price) 
    from goods 
    where (goods_name like "%液晶电视%") 
    and (shop_price>(select min(shop_price) from goods where goods_name like "%液晶电视%") and shop_price<(select max(shop_price) from goods where goods_name like "%液晶电视%"));
    ```
### 12.5 对多行求和
1. sum([distinct]expression)对所有非null值相加
    ```sql
    SELECT SUM(shop_price) AS 所有商品价格总和
    FROM goods;
    SELECT SUM(shop_price-cost_price) AS 所有商品的总盈利
    FROM goods;
    ```
### 12.6 where子句使用
1. 首先还是要说，聚合函数返回的是一个单一的值，可以把这个值作为where子句的条件进行查询。但是聚合函数是不能与字段进行比较，也就是  
    ```sql
    select shop_price<max(shop_price) from goods;
    ```
    这样的的结果只有一个1或者0  
    聚合函数可以放在子查询中，就像在12.5中例子一样  
    ```sql
    SELECT user_id,email, date(birthday) birthday, total_amount
    FROM users WHERE (birthday BETWEEN '1985-01-01' AND '1990-12-31') 
    AND (total_amount > (SELECT AVG(total_amount) FROM users));
    ```
### 12.7 oracle数据库
~~SELECT NVL("Type",'没有分类') 丛书系列名称,
    COUNT(NVL("Type",'没有分类')) 系列中图书个数
    FROM "bookinfo"
    GROUP BY NVL("Type",'没有分类');~~
### 12.8 关于多个聚合函数
1. sql server和MySql都是不允许聚合函嵌套的
    - 嵌套，错误
    ```sql
    min(avg(cols))
    ```
    - 聚合函数的的表达式（参数）不能是子查询，错误
    ```sql
    avg(select shop_price from goods)
    ```
    多个聚合函数会使得系统查询效率显著的降低
## 第十三章 分组统计
### 13.1 创建分组
在前面的第12章中学习使用聚合函数对指定数据表中的所有进行计算，且只能返回一个值。  
现在需要获取其中一部分的统计值，这时我们需要group by子句来对列中数据进行分类
1. 使用group by
    ```sql
    select cat_id as 商品种类, count(*) as 数量 from goods group by cat_id;
    ```
    此时的count(*)就会针对分组去得到计数
    既然是已经通过一个列来分组了，那么其他选择的就只能返回一个，要不然结果无法显示  
    也就是只要存在group by子句进行分组，select查询的列要么就是分组句中，要不就只能包含在聚合函数中，举个例子
    ```sql
    select cat_id, min(shop_price) 最低售价, max(cost_price) 最大成本, avg(shop_price) 平均售价, count(*) 数量 
    from goods 
    group by cat_id 
    order by 最大成本 desc; 
    ```
    尽管在mysql中不会报错，但是最后得到的结果是不符合逻辑的  
    我们已经以一个列分组了，其他列在这个分组下却有多个值，如何显示呢？mysql是直接取第一个，举例
    ```sql
    select cat_id, shop_price 最低售价, max(cost_price) 最大成本, avg(shop_price) 平均售价, count(*) 数量 
    from goods 
    group by cat_id 
    order by 最大成本 desc;  
    ```
2. 使用group by子句创建多列分组  
    这个和order by主次排序不一样，这个意义是变异的distinct，只要这group by后的列中的值都想等就视为一组，举例说明，只有cat_id和brand_id都相等的才会被视为一组
    ```sql
    SELECT cat_id, brand_id, (shop_price) 最低售价,
    (cost_price) 最高成本价 ,(shop_price) 平均售价
    FROM goods;
    SELECT cat_id, brand_id, MIN(shop_price) 最低售价,
    MAX(cost_price) 最高成本价 ,AVG(shop_price) 平均售价, COUNT(*) AS 数量
    FROM goods
    GROUP BY cat_id, brand_id
    ORDER BY MAX(cost_price) DESC;
    ```
    ~~SELECT 收货地址, 联系方式
    FROM (SELECT '收货人：'+ consignee + ' 的地址为: ' + address  AS 收货地址, 
        '联系电话为：' + mobile  AS 联系方式 FROM user_address) a
    GROUP BY 收货地址, 联系方式;
    SELECT e.deptno, d.dname, SUM(e.sal) AS 工资总和
    FROM emp e,dept d
    WHERE e.deptno = d.deptno
    GROUP BY ROLLUP(e.deptno, d.dname);~~   
    注意：如果group by子句使用的是别名，会经常报错，下面这个是不建议的
    ```sql
    select concat("收货人：", consignee, "的地址是：", address) 收货地址, concat("联系电话为：",mobile) 联系电话 
    from user_address 
    group by 收货地址,联系电话; 
    ```
    这时因为group by子句是在from和where子句中寻找结果集中的列进行统计分组的  
    一定要用别名的话，那就嵌套一层子查询,这样是比较好的做法
    ```sql
    select 收货地址, 联系方式 
    from (select concat("收货人：", consignee, "的地址为：", address) 收货地址, 
    concat("联系电话为：", mobile) 联系方式 from user_address) as a
    group by 收货地址, 联系方式;
    select 收货地址, 联系方式 
    from (select concat("收货人：", consignee, "的地址为：", country) 收货地址, 
    concat("联系电话为：", mobile) 联系方式 from user_address) as a
    group by 收货地址, 联系方式;
    ```
### 13.2 使用rollup和cube关键字
1. rollup就是小计功能
    - order by不能在rollup中使用，两者互斥
    - 注意如果有的列中含有null值，显示的结果可能就不正确
    - mysql没有grouping()这个，于是我们尽可能先预处理掉列中的null值，再去做rollup聚合，再使用ifnull()去替换
    ```sql
    select empid, custid, year(orderdate) year, sum(qty) sum
    from rollup
    group by empid, custid, year(orderdate) with rollup;

    select empid, custid, ifnull(year, "小小计") year, sum
    from
    (select ifnull(empid, "总计") empid, ifnull(custid, "小计") custid, year(orderdate) year, sum(qty) sum 
        from rollup 
        group by empid, custid, year(orderdate) with rollup) as temp;

    select ifnull(empid, "总计") empid, ifnull(custid, "小计") custid, ifnull(year, "小小计") year, sum(qty) sum
    from (select empid, custid, year(orderdate) year, qty 
        from rollup) a
    group by empid, custid, year with rollup;
    ```
2. 使用cube把所有可能组合全部聚合一遍，2的n次方分组
    可惜不支持cube，gg
### 13.3 group by子句中的null值处理
1. null值是一个非常特殊的值，既不等于任何值，也不不等于任何值，是一个无法比较的混沌值，只能用is null或者is not null区分
    - 但是在group by子句中，null值被分为一组，空白也是如此，null值和空白区分开
    ```sql
    SELECT oauth AS 第三方付款方式, COUNT(*) AS 个数
    FROM users
    GROUP BY oauth;
    update users
    set oauth = null
    limit 1;
    ```
### 13.4 使用having子句进行过滤分组
1. 看到过滤可能想到where，但是having最不同的地方就是having是数据分组之后进行过滤，而where是数据分组前过滤。   
    使用where限制不需要的行，但是无法限制聚合函数，这时候就用having来了
    SELECT oauth AS 第三方付款方式, email, count(*)
    ```sql
    FROM users
    group by oauth, email;
    SELECT cat_id, shop_price, COUNT(cat_id) AS 个数
    FROM goods
    WHERE (store_count < 1000)
    GROUP BY cat_id,shop_price
    HAVING (shop_price >
            (SELECT AVG(shop_price)
            FROM goods))
    ORDER BY shop_price DESC;
    ```
    总结3点不同：
    - where不能放在group by后面，而having可以
    - having是可以使用聚合函数的
    - where是筛选from数据表中，而having是过滤分组的结果
### 13.5 对统计结果排序
1. 使用order by
    ```sql
    SELECT cat_id, COUNT(cat_id) AS 商品个数
    FROM goods
    GROUP BY cat_id
    ORDER BY 商品个数 DESC;
    ```
### 13.6 group by子句的特殊用法
1. 如果group by子句中的列不一定出现在select列表中
    ```sql
    SELECT AVG(shop_price) AS 平均售价
    FROM goods
    GROUP BY cat_id;
    SELECT cat_id,AVG(shop_price) AS 平均售价
    FROM goods
    GROUP BY cat_id;
    ```
    这样是会被数据库系统接受，但是失去了可读性，还是加入分组的字段名字
### 13.7 写select子句的顺序
| 子句     | 说明                 | 是否必须使用             |
| :------- | :------------------- | :----------------------- |
| select   | 返回列或者表达式     | 是                       |
| from     | 数据表               | 是                       |
| where    | 行级过滤             | 否                       |
| group by | 分组聚合             | 仅在按组计算集合使用     |
| having   | 组级过滤             | 否，一般配合group by使用 |
| order by | 对最后结果集进行排序 | 否                       |
## 第十四章
### 14.1 简单子查询
1. 子查询是select语句中例外一条select语句。通常，语句中有出现表达式的地方就可以使用子查询。子查询可以从任何表中提取数据，只要有权限即可。    
子查询的语法具体如下：  
(select [all|distinct] select_item_list
from table_list
[where srarch_condition]
[group by group_item_list]
[having group_by_search_condition])
这里三种情况
    ```sql
    where 查询表达式 [not] in (子查询)
    where 查询表达式 比较运算符 [any|all] (子查询)
    where [not] exists(子查询)
    -- 上面的这三种要有这几个遵守
    ```
- 子查询必须括号括起来
- 不能包括compute或for browse，不过好像现在都弃用了
- 不可以使用limit，同时在子查询里面使用order by排序没意义，最后的排序还是在外面决定
- 有嵌套层数限制
- 任何可以使用表达式的地方可以使用子查询，只要它返回单个值
- 子查询的列不出现在外查询里，就无法在结果集看见（这不是废话吗。。。）
    ```sql
    SELECT AVG(shop_price) AS 去掉最大值与最小值的平均值 FROM goods 
    WHERE goods_name LIKE '%液晶电视%'
    AND shop_price NOT IN(
    (SELECT MIN(shop_price) AS 最小值 FROM goods WHERE goods_name LIKE '%液晶电视%'
    union
    SELECT max(shop_price) AS 最大值 FROM goods WHERE goods_name LIKE '%液晶电视%'));
    ```
    两个select语句用union合并成一个子查询，顺带提一句，如果两个union字段不一致，直接以第一个命名
### 14.2 标量子查询（包括特殊情况出现在select列表中）
1. 这个子查询只有一行一列，注意，这里的行列意思是，select选择的列（子查询的返回值），where和having最后过滤出来的行，而不是实际上的行列。一个行对应一个列，例子
   严格来说，标量子查询能在的地方就两个地方
   - 实际上这样的在select选择列中一定只能是标量子查询。这里就是一列了,这里一般用于两张表联合查询，因为如果在一张表内，直接group by再使用聚合函数即可
   ```sql
    SELECT tb_book_author,tb_author_department, 
    (SELECT max(book_price)
        FROM tb_book 
        WHERE tb_book_author.tb_book_author=tb_book.tb_book_author) 
        FROM tb_book_author;
   ```
   - where后面的标量子查询那就是一个值了，这里正好name="蓝月亮"的行记录只有一条，如果有多条，还是需要聚合函数，因为单行比较运算符只能是标量。
    ```sql
    SELECT cat_id,goods_name 
    FROM goods
    WHERE cat_id>(
    SELECT cat_id
    FROM brand
    WHERE name='蓝月亮');
    ```
### 14.3 多列子查询
1. 多列子查询就是子查询select选择多列，同时需要满足多列属性
    同时需要满足两个属性（也就是子查询中的两列），也叫做成对的比较的列子查询。不过不能简单写成两个and，这样不是成对就容易将一些不需要的也拿进来。
    ```sql
    select orderid, empid, qty
    from rollup
    order by empid;
    select orderid, empid, qty 
    from rollup 
    where (empid, qty) in 
        (select empid, max(qty) 
        from rollup 
        group by empid) 
    order by empid; 
    select orderid, empid, qty 
    from rollup 
    where empid in 
        (select empid 
        from rollup 
        group by empid) 
    and qty in 
        (select max(qty)
        from rollup
        group by empid)
    order by empid; 
    ```
    再次强调一下，排序对子子查询没有意义，完全没做用，子查询只起到一个条件作用，结果集的排序还是要在外查询中。如上
### 14.4 比较子查询
1. 在where子句中可以使用单行比较符来比较某个表达式与子查询的结果  
   这些符号包括：=,>,>=,<,<=,!=,<>并且可以和any，all结合使用
   ```sql
    SELECT cat_id,goods_name 
    FROM goods
    WHERE cat_id>(
        SELECT cat_id 
        FROM brand
        WHERE name='蓝月亮');
   ```
    在比较子查询中，子查询只能返回一个值，废话，比较操作符也只能比较一个值啊，当然返回值必须是一个，子句中的排序是无效的，也是无意义的
### 14.5 在子查询中使用聚合函数
1. 这个其实不知不觉就用了，比如前面的去掉最值
    ```sql
    SELECT AVG(shop_price) AS 去掉最大值与最小值的平均值 FROM goods 
    WHERE goods_name LIKE '%液晶电视%'
    AND shop_price NOT IN(
        SELECT MIN(shop_price) AS 最小值 FROM goods WHERE goods_name LIKE '%液晶电视%'
        union
        SELECT max(shop_price) AS 最大值 FROM goods WHERE goods_name LIKE '%液晶电视%');
    ```
## 第十五章 多行子查询
显然的，这和前面的就是相反，子查询返回值为多行
## 15.1 使用[not] in操作符的多行子查询
其实实际上没有那么多标量子查询，往往子查询初步得到的就是一个集合，in子查询是最常见的  
比较操作符加上all和any就可以完成转变
all是指全部都要满足，any是满足任意一个  
于是有
| 比较操作符加关键字 | 成员操作符 |
| ------------------ | ---------- |
| =any               | in         |
| !=all              | not in     |
显然in和not in，一个可以完成交集，一个可以完成差集  
not in子查询的查询速度很慢，在要求性能时候，是使用***外连接***的方式来替换以提高速度
### 15.2 [not] exists子查询
1. 在这个之前搞清楚什么叫相关子查询和非相关子查询，先来讲什么是非相关子查询好理解。
   - 非相关子查询，非相关子查询的执行不依赖于外部查询，即该子查询是独立与外部查询的  
    流程是这样的，先执行子查询，其结果不显示，作为条件传递给外部查询，然后执行外部查询，该子查询只会执行一次，毕竟只要执行一次就有了条件。
    ```sql
    select cat_id 
    from goods 
    where shop_price > (
        select avg(shop_price) 
        from goods);
    ```
    - 相关子查询，自然就是和外部查询有所依赖    
    执行过程：  
    （1）从外层查询中取出一个元组，将元组相关列的值传给内层查询。  
    （2）执行内层查询，得到子查询操作的值。  
    （3）外查询根据子查询返回的结果或结果集得到满足条件的行。  
    （4）然后外层查询取出下一个元组重复做步骤1-3，直到外层的元组全部处理完毕。    
    相关子查询的执行依赖于外部查询的数据，外部查询执行一行，子查询就执行一次。   
    下面举例说明：
    ```sql
    select distinct goods_name
    from goods
    where cat_id in (
        select cat_id
        from brand
        where cat_id = goods.cat_id
        and name = "索尼/SONY"
    );
    ```
    以上的相关子查询中goods.cat_id就是依赖于外部的数据   
    接下来来理解exists子查询   
    exists子查询是判断子查询的返回结果是否有数据行。实际上这个子查询只会返回True或者False，故跟在exists后的子查询select *，其外层也就不需要指定字段，该部分代码如下形式。
    ```sql
    where exists (
        select *
        from table_name
        []
        []
    )
    ```
    子查询至少返回一行的数据记录则True，即exists成功。注意和null值区分来，null值判断也为True。     
    exists子查询一般和相关子查询一起用。对于外表中每一行，子查询都要运行一遍，同时该行的值需要在子查询中用到。
    ```sql
    select distinct goods_name
    from goods
    where exists (
        select *
        from brand
        where cat_id = goods.cat_id 
        and name = "索尼/SONG"
    );
    ```
    这个和下面的用in查询一样的
    ```sql
    select distinct goods_name
    from goods
    where cat_id in (
        select cat_id
        from brand
        where cat_id = goods.cat_id
        and name = "索尼/SONY"
    );
    ```
    前面我们提到in和=any是一样的效果
    ```sql
    select consignee, country
    from orderform
    where exists (
        select country
        from user_address
        where country = orderform.country
    );
    select consignee, country
    from orderform
    where country = any(
        select country
        from user_address
    );
    ```
    not exists就是完全相反呗，至少有一条数据记录就False
### 15.3 详细解说量词all，some，any来实现多行子查询
1. some和any是一毛一样的，指的至少有一个True就True  
    all就是全部True则True。
    ```sql
    SELECT cat_id,goods_name,shop_price
    FROM goods
    WHERE shop_price < all(
        SELECT AVG(shop_price)
        FROM goods
        GROUP BY cat_id);
    -- 这和下面的是一样的，但是显然下面的一下就复杂了。而且any非常灵活
    select cat_id, goods_name, shop_price 
    from goods 
    where shop_price < (select min(ang) 
        from (select avg(shop_price) as ang from goods group by cat_id) as a); 
    SELECT cat_id,goods_name,shop_price
    FROM goods
    WHERE shop_price > ANY(
        SELECT AVG(shop_price)
        FROM goods
        GROUP BY cat_id);
    ```
## 第十六章 多表连接
### 16.1 内连接
内连接就是使用比较运算符进行表与表之间列的比较，并且列出这些表中与连接条件匹配的数据行。
1. 等值连接
    就是这个连接条件中使用“=”运算符比较被连接的列，连接条件各个连接列的类型必须可比，但不一定要相同，例子，一个是整形，一个是小数，类型不相同，但是确实是可以比较的。   
    为了效率，还是最好同类型的好一点，类型转换很多时间。
    最好还是声明下列具体是哪一个表的   
    ```sql
    SELECT goods_id,goods_name,name 
    FROM goods,goods_type 
    WHERE goods.goods_type=goods_type.id;
    -- 如果没有where条件，就是笛卡尔乘积，直接乘积
    select row_number() over(order by goods_id),  goods_id, goods_name, name 
    from goods, goods_type; 
    ```
    写成内连接方式就更加明显点，语法是用inner join连接两个表，on子句后面就是连接条件。
    ```sql
    SELECT goods_id,goods_name,name 
    FROM goods inner join goods_type 
    ON goods.goods_type=goods_type.id; 
    -- 如果没有where条件，就是笛卡尔乘积，直接乘积
    ```
2. 不等值连接   
    就是在连接条件中使用除了"="的比较运算符
    ```sql
    SELECT a.goods_id,a.goods_name
    FROM goods a INNER JOIN (SELECT * FROM goods_type WHERE name='平板电脑') b
    ON a.goods_type<>b.id;
    select a.goods_id, a.goods_name
    from goods a, (select * from goods_type  where name="平板电脑") b
    where a.goods_type!=b.id;
    ```
3. 自然连接
    这是一种等值连接的特殊形式   
    连接条件是按照两个表中的相同属性进行等值连接，只有两个表中有相同字段的列作为条件，目标中去除掉重复列(其实就是连接条件的列)，称之为自然连接
    ```sql
    SELECT a.user_id,b.user_id,b.address,date(last_login) AS last_login
    FROM users a,user_address b 
    WHERE a.user_id=b.user_id;
    SELECT a.user_id,b.address,date(last_login) AS last_login
    FROM users a,user_address b 
    WHERE a.user_id=b.user_id;
    ```
4. 使用带聚合函数的内连接
    是的，没错，最开始接触到的聚合函数是从一个表中计算，当然也可以和连接一起使用   
    再次提醒一下，count()是计算重复值的   
    但是count(*)包括null，而count(字段)是不计算null
    ```sql
    SELECT a.id,a.name,COUNT(a.id) num
    FROM goods_category a INNER JOIN goods b
    ON a.id=b.cat_id GROUP BY a.id,a.name;
    SELECT a.id,a.name
    FROM goods_category a INNER JOIN goods b
    ON a.id=b.cat_id;
    ```
    理一下，先内连接两个表，得到笛卡尔乘积的一张表，条件过滤，分组两个字段，count()参数必须是分组的字段，最后完成输出结果集
5. 连接多个表
    ```sql
    SELECT a.goods_id,a.goods_name,b.name brand,c.name type
    FROM goods a,brand b,goods_type c 
    WHERE a.brand_id=b.id AND a.goods_type=c.id;
    -- 写成inner join形式如下，这中间的表行记录有20k多
    SELECT a.goods_id,a.goods_name,b.name brand,c.name type
    FROM goods a inner join brand b inner join goods_type c 
    on a.brand_id=b.id AND a.goods_type=c.id;
    -- 可以写成部分先过滤，如下
    select a.goods_id, a.goods_name, b.name as brand, c.name as type
    from (goods a inner join brand b on a.brand_id=b.id) inner join goods_type c on a.goods_type=c.id;
    ```
    经过mycli运行，发现速度是一样的，mariadb做了内部的优化，吗但
### 16.2 外连接
通过内连接是保留符合连接条件的，外连接则是内连接查询的扩展，外连接可以包括那些不符合连接条件的记录。所以当然的这没有连接条件就逻辑不通了，一定要有连接条件
1. 左外连接  
    顾名思义，左外连接就是保留第一个表的所有行，但是对于第二个表值包含能够符合连接条件的行，而第二个表的空行由null值填充    
    完全来说，结果就是内连接加上没有匹配成功的行，用null补齐
    ```sql
    SELECT goods_id,goods_name,name
    FROM goods LEFT JOIN goods_type
    ON goods.goods_type=goods_type.id ORDER BY goods_id DESC;
    SELECT goods_id,goods_name,name
    FROM goods inner JOIN goods_type
    ON goods.goods_type=goods_type.id ORDER BY goods_id DESC;
    ```
2. 右外连接
    ```sql
    SELECT goods_id,goods_name,name
    FROM goods RIGHT JOIN goods_type
    ON goods.goods_type=goods_type.id;
    -- 总结一下，所谓的左右之分就是看表顺序，join左右先后之分，调换位置即可完成转变，例如
    SELECT goods_id,goods_name,name
    FROM goods_type left JOIN goods
    ON goods.goods_type=goods_type.id;
    ```
3. 全外连接    
    这个就是左右外连接结果合并去掉重复行，其实就是union
    ```sql
    (SELECT goods_id,goods_name,name
    FROM goods left JOIN goods_type
    ON goods.goods_type=goods_type.id ORDER BY goods_id)
    union
    (SELECT goods_id,goods_name,name
    FROM goods right JOIN goods_type
    ON goods.goods_type=goods_type.id ORDER BY goods_id)
    ```
4. 外连接的多表联合查询（嵌套）
    ```sql
    SELECT goods_id,goods_name,brand.name brand,goods_type.name type
    FROM (goods LEFT JOIN brand ON goods.brand_id=brand.id)
    LEFT JOIN goods_type ON goods.goods_type=goods_type.id;
    ```
### 16.3 其他连接
1. 自连接，注意和自然连接区分，这是自身表进行连接
    自连接是同一个表自身进行连接。我们来剖析一个例子，设这个表m×n
    ```sql
    SELECT b1.id,b1.name,b1.cat_name
    FROM brand b1,brand b2
    WHERE b1.cat_name=b2.cat_name
    AND b2.name='OPPO';
    -- 首先看from，自连接是两个独立的副本，故需要不同的别名。然后笛卡尔乘积
    SELECT b1.id,b1.name,b1.cat_name,b2.id,b2.name,b2.cat_name
    FROM brand b1, brand b2;
    -- 这会有6列，n*n行，看这不是自然连接，不会去除重复列！！！113569
    SELECT b1.id,b1.name,b1.cat_name
    FROM brand b1,brand b2
    WHERE b1.cat_name=b2.cat_name;
    -- 条件来了，只有条件成立才会选取，这里有3列，sum(count(cat_name)*(cat_name)行，好好想下这里select cat_name, count(cat_name) num from brand group by cat_name;得到每一个品牌的个数，然后求平方和。SELECT sum(num*num) from (select cat_name, count(cat_name) num from brand group by cat_name) as ab;
    -- 然后and再得到b2.name="OPPO"，得到count(cat_name)行5941
    SELECT b1.id,b1.name,b1.cat_name
    FROM brand b1,brand b2
    WHERE b1.cat_name=b2.cat_name
    AND b2.name='OPPO';
    ```
    这和rollup有点同样的道理，分组内连接再筛选，这相比来说有点难理解，为什么不用子查询呢？    
    ```sql
    select id, name, cat_name 
    from brand
    where cat_name = (select cat_name from brand where name="OPPO");
    -- 复习下exists，牢记外部依赖
    select id, name, cat_name 
    from brand a
    where exists (select * from brand where a.cat_name LIKE "%手机%");
    select id, name, cat_name 
    from brand a
    where exists (select * from brand where a.cat_name=(select cat_name from brand where name="OPPO"));
    ```
2. 交叉连接（两个表的笛卡尔乘积）   
    交叉连接就是两个表的笛卡尔乘积的另外一个名称
    ```sql
    select a.name, a.cat_name, b.goods_name
    from brand a cross join goods b;
    select a.name, a.cat_name, b.goods_name
    from brand a inner goods b;
    ```
### 16.4 组合查询
union，列一样，行相加
关键3点
- 进行组合查询必须由两个或者两个以上的select语句组成，语句之间用union关键字分隔
- 要求每个select语句中的列的数目必须相，对应的列数据类型必须相同或者兼容
- 结果集的列名字由第一个select语句的列名决定
1. union
    ```sql
    SELECT cat_id,goods_name,shop_price
    FROM goods
    WHERE cat_id IN (123,131);

    SELECT cat_id,goods_name,shop_price
    FROM goods
    WHERE goods_name LIKE '%华为%';

    SELECT cat_id,goods_name,shop_price
    FROM goods
    WHERE cat_id IN (123,131)
    UNION
    SELECT cat_id,goods_name,shop_price
    FROM goods
    WHERE goods_name LIKE '%华为%';
    ```
    当然也可以对不同表的进行组合查询，如下
    ```sql
    SELECT BookName,Writer,Price
    FROM bookinfo
    WHERE Price = 59.80
    UNION
    SELECT BookName,Writer,Price
    FROM bookinfo_zerobasis
    WHERE Price = 69.80;
   ```
2. union all    
    union是默认去掉重复的行的，加上all就不会去重了
    ```sql
    SELECT BookName,Writer,Price,pDate
    FROM bookinfo_zerobasis
    WHERE Price = 69.80
    UNION ALL
    SELECT BookName,Writer,Price,pDate
    FROM bookinfo_zerobasis
    WHERE pDate = '2017年9月';
    ```
3. 组合查询的排序规则    
    查询结果是对select列表中的列从左到右的顺序自动排序。   
    如果需要指定order by，该子句只能放在最后一个select语句之后，而排序关键字必须是第一个select语句中的列名
    ```sql
    SELECT cat_id,goods_name,shop_price
    FROM goods
    WHERE cat_id IN (123,131)
    UNION
    SELECT cat_id,goods_name,shop_price
    FROM goods
    WHERE goods_name LIKE '%华为%'
    ORDER BY shop_price;
    ```
## 第十七章 插入数据
### 17.1 插入单行数据
1. inser语句基本语法
    ```sql
    insert into table_or_view [(column_list)] values (value_list)
    ```
    table_or_view：表名或者视图名   
    column_list：由逗号分隔开的列名列表   
    value_list：作为一行或者多行数据插入   
2. 插入整行数据
    用户会给数据表的所有列都插入值，夜色就是这一行数据每一列都要插入值   
    而column_list参数则有：
    - 列出所有列名
    - 直接省略，但是这样不便于理解
    插入值的数据类型当然需要保持一支，否则错误
    ```sql
    INSERT INTO brand 
    (id,name,logo,`describe`,url,sort,cat_name,parent_cat_id,cat_id,is_hot)
    VALUES (350,'创维/Skyworth',
    '/Public/upload/brand/2016/04-01/347586936.jpg','凝聚健康科技',
    'www.Skyworth.com',50,'手机、数码、配件',1,1,0);
    -- 这里的describe要用反引号
    SELECT * FROM brand; 
    insert into brand
    values (366,'创维/Skyworth',
    '/Public/upload/brand/2016/04-01/347586936.jpg','凝聚健康科技',
    'www.Skyworth.com',50,'手机、数码、配件',1,1,0);
    -- 省略了列名，按照顺序需要每一列都需要提供一个值，如果某一列没有值且该列允许为null值，则可以使用null值进行填充
    ```
3. 插入部分数据
    如果某一列允许为null值，则可以省略该列，于是就可以只插入部分行数据   
    例子
    cat_name允许为null值，于是这里省略该列名字，于是这里不给该列插入值也不会报错
    这里会去插入默认值，也就是下面的情况
    ```sql
    INSERT INTO brand
    (id,name,logo,`describe`,url,sort,parent_cat_id,cat_id,is_hot)   
    VALUES(348,'台电/Teclast',
    '/Public/upload/brand/2016/04-01/348396236.jpg','商科集团旗下品牌',
    'www.teclast.com',50,1,1,0);
    ```
4. 插入默认值
    用户在创建数据表允许通过default关键字来为列定义默认值，于是在没有提供数据情况下，会插入默认值
    ```sql
    INSERT INTO brand
    (id,name,logo,`describe`,url,cat_name)
    VALUES(349,'酷开/Coocaa',
    '/Public/upload/brand/2016/04-01/350396326.jpg','酷开网络科技',
    'www.coocaa.com','手机、数码、配件');
    ```
### 17.2 插入多行数据
1. 一样的语法，用逗号隔开多行数据
    ```sql
    insert into 
    table_or_view 
    [(column_list)] 
    values 
    (value_list1),(value_list2)

    INSERT INTO brand
    (id,name,logo,`describe`,url,sort,cat_name,parent_cat_id,cat_id,is_hot)
    VALUES
    (350,'海力/horion',
    '/Public/upload/brand/2016/04-01/351396632.jpg','',
    '',50,'手机、数码、配件',1,1,0),
    (351,'长虹/CHANGHONG',
    '/Public/upload/brand/2016/04-01/352366226.jpg','',
    '',50,'手机、数码、配件',1,1,0);
    ```
2. 通过查询语句来插入多行数据
    当然这表的结构需要一致，但是并不要求列名匹配  
    主键是不可以重复的
    ```sql
    SELECT * FROM brand; 
    CREATE TABLE brand_new(
            id int NOT NULL PRIMARY KEY,
            name varchar(60) NOT NULL DEFAULT '',
            logo varchar(80) NOT NULL DEFAULT '',
            `describe` text NOT NULL,
            url varchar(255) NOT NULL DEFAULT '',
            sort int NOT NULL DEFAULT 50,
            cat_name varchar(128) NULL DEFAULT '',
            parent_cat_id int NULL DEFAULT 0,
            cat_id int NULL DEFAULT 0,
            is_hot int NULL DEFAULT 0
    );
    INSERT INTO brand_new
    SELECT * FROM brand
    WHERE cat_name = '手机、数码、配件';
    
    SELECT id,name,cat_name FROM brand_new; 
    ```
### 17.3 表中数据的复制
1. sql server中的操作
    ```sql 
    SELECT BookName,Type,Writer
    INTO bookinfo_project
    FROM bookinfo WHERE Type = '项目入门系列';

    SELECT BookName,Type,Writer
    FROM bookinfo_project;
    ```
2. MySQL复制表数据   
    语法如下  
    new_table是新表的名字，故不能存在相同名字的数据表，就是完全创造一个新表  
    ```sql
    create table new_tabel as 
    select [select_list]
    from table_name
    where search_condition
    
    CREATE TABLE newbrand AS
    SELECT id,name,cat_name
    FROM brand WHERE cat_name='手机、数码、配件';

    SELECT id,name,cat_name 
    FROM newbrand;
    ```
## 第十八章 更新和删除数据
### 18.1 update语句
1. update语句基本语法
    ```sql
    update table_name
    set columu1 = value1, column2 = value2,...
    where search_condition
    ```
2. 更新列
    ```sql
    UPDATE brand
    SET cat_name = '手机、数码、配件'
    WHERE name = '台电/Teclast';

    SELECT * FROM brand
    WHERE name = '台电/Teclast';
    -- 一行单列
    UPDATE brand
    SET `describe` = '人工智能电视',cat_name = '大小家电、厨电、汽车',is_hot = 1
    WHERE name = '长虹/CHANGHONG';

    SELECT name,`describe`,cat_name,is_hot FROM brand
    WHERE name = '长虹/CHANGHONG';
    -- 一行多列
    UPDATE brand
    SET is_hot = 1;
    
    SELECT id,name,cat_name,is_hot FROM brand; 
    -- 没有where子句，就是全部行
    ```
3. 和前面的插入数据一样，同样可以依靠外表来更新数据   
    ```sql
    UPDATE goods
    SET store_count = store_count + 1000 
    WHERE cat_id = (SELECT id FROM goods_category WHERE name = '平板电脑');

    SELECT goods_id,goods_name,store_count
    FROM goods
    WHERE cat_id = (SELECT id FROM goods_category WHERE name = '平板电脑'); 
    ```
### 18.2 delete语句
1. delete语句基本语法
    ```sql
    delete from table_or_view_name
    [where search_conditions]
    ```
2. 删除整行
    ```sql
    DELETE FROM brand 
    WHERE name = '长虹/CHANGHONG';

    SELECT * FROM brand 
    WHERE name = '长虹/CHANGHONG'; 
    -- 该条数据已经被删除了
    DELETE FROM brand
    WHERE name IN ('台电/Teclast','酷开/Coocaa','海力/horion');

    SELECT * FROM brand 
    WHERE name IN ('台电/Teclast','酷开/Coocaa','海力/horion');
    --  同样如此
    ```
    ~~SELECT * INTO newgoods_type
    FROM goods_type;~~
    ```sql
    create table newgoods_type as
    select * 
    from goods_type;
    
    DELETE FROM newgoods_type;
    truncate table newgoods_type;

    drop table newgoods_type;

    SELECT * FROM newgoods_type;
    ```
    delecte语句是以一行数据为单位进行删除   
3. 使用truncate table语句进行删除数据    
    turncate table语句用来删除表中所有所有行。与delete语句相比，使用turncate table语句不但删除了数据，而且所删除的数据在事务处理日志中还会做相应的记录。  
    delete慢，直接`turncate table table_name`，更加快，效率也高。
## 第十九章 使用视图   
视图是一种数据库对象，他将查询的结果以虚拟表的形式存在。视图并不在数据库中以存储数据集的形式存在。视图的结构和内容是建立在对表的查询基础上，和表一样包括行和列，这些行列数据都来源于其引用的表，并且在引用视图过程中动态生成的。
- 视图是虚拟的表
- 视图中看见的数据存储在创建视图的表中，而不是存在视图本身。
### 19.1 视图概览
视图中的内容是查询定义来的，视图和查询都是用过SQL语句定义的，有相同自然也有不同之处
- 存储：视图存储是数据库设计的一部分，而查询不是。视图可以禁止所有用户访问数据库中的基表，而要求用户只能通过视图操作数据。这样的方法可以保护用户和应用程序不受某些数据库修改的影响，同时保护数据表的安全性。
- 排序：可以排序任何查询结果，但是只有当视图包括top子句（limit子句）才能排序
- 加密：可以加密视图，查询不能加密     

视图的优点：
1. 简化操作：视图可以使比较复杂的多表关联查询，用查询视图语句简化列操作。对一个视图的访问比多个表的访问要容易。
2. 建立前台和后台的缓冲：在数据库开发过程中，可以通过调用视图来实现查询功能，通过对视图的调用吗，在数据库结构改变时候，只要视图的输出列不发生改变，就可以避免对应用程序的修改。提高数据库的开发效率，降低了开发成本。
3. 合并分割数据：通过视图可以对表中的数据进行水平分割或者垂直分割。用户可以对一个表或者多个表中的数据列惊醒有选择的查看，简化数据结构。
4. 提高安全性：视图可以作为一种安全机制，通过视图可以限定用户查看和修改的数据表或者列，其他的数据信息只能是有房温泉先的用户才能查看和修改。例如：对于工资表中信息，一般员工只能看到表中的姓名、办公室、工作电视和部门等，只有负责相关操作的人可以区查看和修改。如果某一用户想要访问视图的结果集，必须被授予访问权限，视图所引用的表访问权限与视图权限的设置是独立的。这一点在数据库的开发设计时，对于不同级别的用户共用一个数据库时候，应用及其广泛。
### 19.2 视图的创建
语法
```sql
create view view_name [(column_name)]
as select_statement
[with check option]
```


| 参数             | 说明                                                                                                                                                                                                      |
| :--------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| view_name        | 视图的名称，视图名称必须符合有关标识符的规则。可以选择是否指定视图所有者名称                                                                                                                              |
| column_name      | 定义视图中的字段名，如果没有指定，则获得select语句中的字段名。但是这3种情况必须指定字段名：1.视图是多个表中产生的，存在重名。2.当列是算数表达式、函数或常量派生得到。3.视图中的某列不同于源表中的名称时候 |
| as               | 指定视图要执行的操作                                                                                                                                                                                      |
| select_statement | 定义视图的select语句，该语句可以引用多个表或则其他视图                                                                                                                                                    |
| check option     | 规定在视图上执行的所有数据修改语句都必须符合由select_statement设置的准则。通过视图修改记录，with check option可确保提交修改后，仍可以通过视图看到修改的数据                                               |


```sql
CREATE VIEW GoodsPrice
AS
SELECT goods_id,goods_name,shop_price
FROM goods;

SELECT * FROM GoodsPrice;
```
### 19.3 删除视图
通过`drop view`语句删除数据库中不需要的视图。`drop table`是删除表，而`drop view`只是删除该视图，并没有删除数据表。    
用逗号分隔，可以同时删除多个
```sql
drop view GoodsPrice;
```
### 19.4 视图的应用
1. 通过视图简化复杂的查询    
    视图的一个重要的用途就是进行复杂的SQL数据处理。通过创建视图，可以实现多表之间的复杂连接。利用视图可以编写一个复杂的查询语句，然后根据需要多次利用。    
    查询大多数情况下都是联合查询，所以创建视图比重复输入相同的复杂的查询语句要方便，极大简化sql语句使用。
    ```sql
    CREATE VIEW GoodsBrandType
    AS
    SELECT goods.goods_id,goods.goods_name,brand.name brand,goods_type.name type
    FROM goods,brand,goods_type 
    WHERE goods.brand_id=brand.id AND goods.goods_type=goods_type.id;

    SELECT * FROM GoodsBrandType
    WHERE type = '电视';

    CREATE VIEW NNNNNNNNNNNNNNNGoodsBrandType (id, gname, bname, ty)
    AS
    SELECT goods.goods_id,goods.goods_name,brand.name brand,goods_type.name type
    FROM goods,brand,goods_type 
    WHERE goods.brand_id=brand.id AND goods.goods_type=goods_type.id;

    select * from NNNNNNNNNNNNNNNGoodsBrandType
    where ty = "电视";
    ```
2. 使用视图过滤不需要的数据
    就是where子句
    ```sql
    CREATE VIEW ZeroBook
    AS
    SELECT ISBN,BookName,Writer,newbook
    FROM bookinfo_zerobasis 
    WHERE newbook IS NOT NULL;

    SELECT * FROM ZeroBook;
    ```
3. 通过视图显示函数的结果    
    视图不仅可以显示保存在表中的值，而且可以显示表达式和函数的值    
    ~~当视图只显示来自底层表的数据时，DBMS可使用基表列的名称作为视图中的列名   
    但视图列中有聚合函数时候，就必须要指定列名了~~
    mariadb没有这个问题，一样基层
    ```sql
    CREATE VIEW BookGroup
    AS
    SELECT Type,COUNT(*) number,MAX(Price) maxprice
    FROM bookinfo
    WHERE Type IS NOT NULL
    GROUP BY Type;

    SELECT * FROM BookGroup;
    ```
4. 通过视图添加数据到基表中   
    在视图上使用insert语句向数据表添加数据时   
    这个视图数据是不会变得，是向数据表中插入数据
    要符合以下规则：
    1. 使用insert语句向数据表中插入插入数据时，用户必须有插入数据的权限
    2. 由于视图可能只会引用表中部分字段，和向数据表插入数据一样，没有列出的字段要设置默认值，否则报错
    ```sql
    CREATE VIEW GoodsType
    AS
    SELECT goods.goods_id,goods.goods_name,goods_type.id type_id,goods_type.name type
    FROM goods,goods_type
    WHERE goods.goods_type=goods_type.id;

    INSERT INTO GoodsType
    (goods_id,goods_name)
    VALUES(115,'海尔EB60Z2WD 洗衣机')
    INSERT INTO GoodsType
    (type_id,type)
    VALUES(30,'洗衣机');
    ```
    3. 视图中不能包含多个字段组合，或者统计函数
    4. 不能包含distinct或者group by子句
    5. 如果视图中使用了with check option，那么插入的数据必须符合规定
    6. 视图引用了多个数据表，就使用多个insert子句


5. 通过视图更新数据
    ```sql
    update view_name
    set column1=expr1[,...]
    [where search condition]

    CREATE VIEW GoodsBrand
    AS
    SELECT goods.goods_id,goods.goods_name,brand.name brand
    FROM goods,brand
    WHERE goods.brand_id=brand.id;

    UPDATE GoodsBrand
    SET goods_name = '康佳R6000U 液晶电视'
    WHERE goods_id = 57;
    UPDATE GoodsBrand
    SET brand = '康佳/KONKA'
    WHERE goods_id = 57;

    select * from goods_type;
    ```
6. 通过视图删除数据   
    也是有几个规则：   
    1. 如果视图应用了两个或里两个以上的数据表，则不允许删除
    2. 不能违背视图定义的条件，废话，首先数据要在定义内
    3. 在删除记录时候，要保证视图或者基表中不存在自连接，否则无法删除    
    语法如下
    ```sql
    delete view_name where search_condition
    ```
    ```sql
    CREATE VIEW Type
    AS
    SELECT * FROM goods_type;

    DELETE From Type
    WHERE name = '洗衣机';

    select * from Type;
    select * from goods_type;
    ```
7. 在视图中使用with check option   
    如果在创建视图时使用了with check option子句，那么对通过视图上插入或者更新操作都必须符合定义视图时候的设置的查询条件！！！否则DBMS直接终该语句并返回错误信息！！！
    ```sql
    CREATE VIEW GoodsStore
    AS
    SELECT goods_id,goods_name,store_count
    FROM goods
    WHERE store_count < 1000
    WITH CHECK OPTION;

    SELECT * FROM GoodsStore;

    UPDATE GoodsStore
    SET store_count = store_count + 400;

    SELECT * FROM GoodsStore;
    select goods_id, goods_name, store_count
    from goods;
    ```
## 第二十章 使用存储过程
### 20.1 存储过程概述
1. 存储过程的概念
    存储过程可以改变SQL语句的运行性能，提高运行效率。还可以作为一种安全机制，是使用户通过它来访问未授权的表或者视图。   
    存储过程（Stored Procedure）是一组预先编译好的Transact-SQL语句。   
    将其放在服务器上，由用户通过指定存储过程的名字来执行它。存储过程可以作为一个独立的数据库对象，也可以作为一个单元被用户的应用程序调用。
    存储过程可以接收和输出参数，返回执行存储过程的状态值，还可以嵌套调用。   
    存储过程和其他语言中的面向过程类似
    - 存储过程可以接收参数，并以接收参数的形式返回多个参数给存储过程和批处理
    - 包含执行数据库的编程语句，也可以调用其他的存储过程
    - 向调用过程或者批处理返回状态值，以次反映存储过程的执行过程
2. 存储过程的功能    
    可以理解存储过程是打包好的一连串命令
    - 条件执行：在存储过程中录入一套Transact-SQL语句后，使用if...then...else结构根据存储过程中其他语句的执行返回的结果来决定执行过程中的某条语句
    - 循环控制结构：while和for循环。loop循环和repeat until循环。直到循环被终止
    - 命名变量：在存储过程中放入一条或更多T-SQL语句并添加条件执行和循环控制结构，可以为存储过程起一个名称，并通过正式的输入输出参数把数据传入过程或者从过程中传出数据，就是封装，经过定义和编译后，可通过名称在触发器中调用。
    - 语句块：和程序中调用子程序一样，通过调用存储过程可以让DBMS执行一系列SQL语句，执行一条语句，可以完成很复杂的任务
## 20.2 SQL Server
## 20.3 Oracle
## 20.4 MySQL，MariaDB数据库下创建存储过程
1. 创建存储过程   
    在MysSQL中穿创建存储过程的语法，举一个例子来比较好  
    ```sql
    create procedure name_procedure (in parameter integer)
    begin
    declare variable varchar(20);-- 声明局部变量，仅仅作用于语句块的，分号结束
    if parameter = 1 then
    set variable = "SQL"; -- 控制语句if成立执行的语句
    else
    set variable = "MySQL"; -- 控制语句if不成立执行语句
    end if;
    insert into ta_table (tb_name) values (variable); --插入数据到ta_table表中，列名tb_name，值是variable
    end; -- end结束
    ```
    name_proceducre是这个存储过程的名字。  
    [in|out|inout]
    | in                                   | out                              | inout                                            |
    | :----------------------------------- | :------------------------------- | :----------------------------------------------- |
    | 存储过程默认就是in传入参数           | 向外传出参数                     | 表示定义的参数传入存储过程并经过存储过程修改传出 |
    | 传入的值可以是字面量（常量）或者变量 | 传出值可以有多个，但都必须是变量 | 值只能变量                                       |
    parameter参数名字，面向过程，参数的类型也要定义      
    语句块从begin开始，以end结束。语句体中包含声明变量，控制语句和sel查询语句等。   
    几种情况说明一下   
    - 在mysql命令行模式中输入就需要用delimiter关键字来临时改分隔符，默认的是分号;，当然最后需要改回去。
    ***（或者delimiter \\\\）***
    ```sql
    delimiter $$
    create procedure cre (in x integer)
    begin
    if x = 1 then
    select * from goods_type;
    else
    select * from brand;
    end if;
    end;
    $$
    delimiter ;
    ```
    - 使用mycli工具则没有delimiter这个选项，F3打开多行模式multiline，再F4切换成VI模式，就可以多行;输入
    ```sql
    create procedure cre (in x integer)
    begin
    if x = 1 then
    select * from goods_type;
    else
    select * from brand;
    end if;
    end;
    ```
    - 在vscode中使用query
    ```sql
    create procedure cre (in x integer)
    begin
    if x = 1 then
    select * from goods_type;
    else
    select * from brand;
    end if;
    end;
    ```
    - 使用dbeaver一个gui界面软件来创建存储过程   
    直接找到存储过程选项卡新建就好    
    ```sql
    show databases; -- 展示当前用户下所有数据库
    use shop; -- 选择数据库shop
    show tables; -- 展示选择的数据库下所有表
    show procedure status [like "pattern"|where exprssion]; -- 显示已选择数据库所有的存储过程的状态信息，包括Db，name，
    show create procedure name_procedure; --  显示该存储过程的详细信息包括源代码
    show create procedure cre_pro; --  显示该存储过程详细具体信息源代码
    ```
    MySQL存储过程和函数的信息存储在information_schema数据库下的Routines表中   
    ```sql
    SELECT * FROM information_schema.ROUTINES 
    WHERE ROUTINE_NAME = 'cre_pro';
    ```
    ```sql
    delimiter $$
    create procedure cre_pro ()
    begin
    select * from brand where cat_name = "生鲜食品";
    end;
    $$
    call cre_pro ();
    ```
    对于已经存在的存储过程，在不同的会话管理中是一样的，但是变量有所不同   
    mysql系统变量，用户变量（自定义变量），局部变量，系统变量按照作用域不同又分为会话变量和全局变量。
    |                                                                                                                                                        系统变量                                                                                                                                                         |                                                                                                                                                   会话变量                                                                                                                                                   |                                                                               自定义变量                                                                                |                                                                                     局部变量                                                                                     |
    | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
    |                                                                                                                                                    global variables                                                                                                                                                     |                                                                                                                                              session variables                                                                                                                                               |                                                                                用户变量                                                                                 |                                                                                     局部变量                                                                                     |
    | 全局变量影响服务器整体操作。当服务器启动时，它将所有全局变量初始化为默认值。这些默认值可以在选项文件中或在命令行中指定的选项进行更改。要想更改全局变量，必须具有SUPER权限。全局变量作用于server的整个生命周期，但是不能跨重启。即重启后所有设置的全局变量均失效。要想让全局变量重启后继续生效，需要更改相应的配置文件。 | 服务器为每个连接的客户端维护一系列会话变量。在客户端连接时，使用相应全局变量的当前值对客户端的会话变量进行初始化。设置会话变量不需要特殊权限，但客户端只能更改自己的会话变量，而不能更改其它客户端的会话变量。会话变量的作用域与用户变量一样，仅限于当前连接。当当前连接断开后，其设置的所有会话变量均失效。 | 用户变量的作用域要比局部变量要广。用户变量可以作用于当前整个连接，但是当当前连接断开后，其所定义的用户变量都会消失。用户变量使用，这里我们无须使用declare关键字进行定义 | 局部变量一般用在sql语句块中，比如存储过程的begin/end。其作用域仅限于该语句块，在该语句块执行完毕后，局部变量就消失了。局部变量一般用declare来声明，可以使用default来说明默认值。 |
    |                                                                                                                                `set global v_name = value;set @@ global.v_name = value`                                                                                                                                 |                                                                                                                          `set session v_name = value;set @@ session.v_name = value`                                                                                                                          |                                                                   `set @v1 = 1;select @ v2 := "abc"`                                                                    |                                                                      begin开始`declare a int default value`                                                                      |
    |                                                                                                                                                          show                                                                                                                                                           |                                                                                                                                                     show                                                                                                                                                     |                                                                                show命令                                                                                 |                                                                               这个语句块结束就没了                                                                               |
## 第二十一章 简单使用游标
游标提供了一种嗯从表中检索数据并进行操作的的灵活手段。  
游标主要用在服务器上吗，处理由客户端发送给服务器的sql语句，或者批处理，存储过程，触发器中的数据处理请求。  
游标的有点就是可以具体操作结果集中某一行，并对该行数据执行。  
完整的游标有这及几部分：  
1. 声明游标declare cursor_name cursor;
2. 打开游标open cursor_name;
3. 读取游标，具体操作根据需求来，fetch
4. 关闭游标close cursor_name;
5. 释放游标，deallocate cursor_name;只有sql server有这个   

游标的使用场景有   
存储过程   
函数   
触发器   
事件   
### 21.1 声明游标
sql server和mysql
```sql
declare cursor_name cursor for
select_statement;
```
~~oracle~~
### 21.2 `open cursor_name;`
### 21.3 读取游标数据
这里的sql server和mysql区别就非常大
前者是
```sql
fetch 
    [[next|prior|first|last]
        from
    ]
    cursor_name
[into @variable_name[,..n]]
```
next是默认值，返回当前行的下一行，并且当前行递增为结果行。如果第一次对游标操作，即是第一行  
prior则是相反，返回当前行的上一行，并且当前行递减为结果行。如果是第一次读取游标，那么显然是没有返回值，并且此时游标位置放到第一行之前
first则是直接返回游标中的第一行并将其作为第一行   
lat则是和first相反，最后一行   
cursor_name有全局和局部之分，默认没有关键字global就是局部    
into则是将某一行放到局部变量。列表中的各个变量从左往右与游标结果集列相关联列。数据类型最好一致或者支持隐形转换。   
@@fetch_status这是一个全局变量，用来返回上次执行fetch命令状态。  
返回值为0：成功
返回值为-1：失败或者此行不在结果集中
返回值为-2：被提取的行不存在
释放游标deallocate，这个是sql server特有的   
mysql则是，必须声明变量来放这个读取到的数据行，`declare var_name varchar(120);`
```sql
fetch cursor_name into var_name [，var_name ]...;
```
结合循环来用    
while ... do ... end while;   
repeat ... end repeat;   
loop ... end loop;   
### 21.4 关闭游标`close cursor_name;`
使用游标十分的占用内存，容易死锁  
## 第二十二章 事务处理
### 22.1 事务概述
事务是由一系列sql语句构成的逻辑工作单元。把多条sql语句封装起来，和存储过程有点类似，但是事务最大的不同就是具有acid属性。   
原子性（atomic）：事务是一个整体的工作单元，事务对于数据库的操作要么全部执行，要么全部取消。只要其他有一条语句执行失败，所有语句全部回滚。   
一致性（consistent）：事务在完成时，必须使所有的数据保持一致。事务成功，则所有数据变为一个新的状态，事务失败，则是保持事务开始之前的状态。   
隔离性（isolated）：由事务所作的更改与其他事务所有的修改隔离。事务查看数据状态时，要么是另外一个并发事务修改之前，要么之后，不存在查看中间状态。   
持久性（durability）：事务提交后，写入硬盘，数据库的更改会永久保存下来。   
事务中一旦发生问题，直接恢复到开始状态。所以不管事务是否成功，数据库总是完整的。    
### 22.2 显式事务和隐式事务
sql server和mysql使用的关键字有一点点不一样
```sql
begin transaction;
...
commit transaction;


bein;
commit;
start transaction; -- 这和begin;是一样的
```
显式事务就是用户自定义或用户指定的事务。mysql默认是自动提交的，也就是该变量是1,是on的，会话变量或者说系统变量
```sql
show variables like "autocommit";
set autocommit = 0 -- 这就是默认修改会话变量，和@@autocommit或者@@session.autocommit相同的，默认值就是开启，值是1
```
事务的过程，首先看是否是自动提交语句，再由`begin;`或者`start transaction;`开始事务，事务的结束只两种，一种是`commit;`提交，也就是确保事务的修改（`insert update delete`）都被保存，写入硬盘数据库，同时释放事务使用锁。或者`rollback;`回滚事务，用于事务在执行失败情况下，事务回滚到起点或者保存点。   
回滚就是update insert delete，不能回滚select（这也没有意义），不能回滚create，drop语句   
```sql
begin;
update goods set store_count = 116
where goods_id = 106;
ROLLBACK;
commit;
select goods_id, goods_name, store_count from goods;
```
对于事务有着以上的特点，于是就有编写有效事务的几个原则：
1. 事务处理期间不要用户输入，在事务启动之前就获得所有的输入
2. 在浏览数时候，不要打开事务
3. 事务尽可能短，及时提交和回滚，保持逻辑清晰
4. 灵活使用更低的事务隔离级别
5. 事务尽可能访问数据量小
6. 谨慎使用隐式事务，autocommit值是0情况。特别是并发事务时候    
7. 事务中允许的和不允许的    
事务中允许和不允许的，这是sql server的，mysql会有点不同

|SQL语句|功能|
|:--:|:--:|
|set transaction|设置下一个执行事务的属性，就是设置事务的隔离级别|
|start tarnsaction|开始事务|
|set constrains|约束模式|
|savepoint|保存点，断点|
|release savepoint|释放保存点|
|rollback|回滚|
|commit|提交事务|
不允许的 

|语句|功能|
|:--:|:--:|
|alter database||
|create database||
|disk init||
|drop database||
|dump tarnsaction||
|load database||
|reconfigre||
|restore database||
|restore log||
|update statistics||
### 22.3 事务操作
提交事务，`commit;`语句，我们有必要重新提一下事务，只有提交了事务才是永久性的改变，这是永久性，在当前会话可以看到改变，但是如果没有提交，在其他的新建会话是没有存储的，在其他的事务也是没有改变的    
数据库都是自动提交的，mysql是默认自动提交的    
任何一条有效的sql语句都默认自动提交，发生错误自动回滚并返回错误信息    
```sql
INSERT INTO bookinfo
(ISBN,BookName) VALUES('7-110-12151-1','Java从入门到精通');
INSERT INTO bookinfo
(ISBN,BookName) VALUES('7-110-12151-2','Oracle从入门到精通');
INSERT INTO bookinfo
(ISBN,BookName) VALUES('7-110-12151-2','Oracle从入门到精通');
```
比如上述三条语句，前面两条确实是执行成功了的，第三条不行   
如果如同等情况下，我们使用事务来执行的话，原子性，整个事务都不会执行。例子
```sql
begin;
INSERT INTO bookinfo
(ISBN,BookName) VALUES('12151-1','Java从入门到精通');
INSERT INTO bookinfo
(ISBN,BookName) VALUES('12151-2','Oracle从入门到精通');
INSERT INTO bookinfo
(ISBN,BookName) VALUES('12151-2','Oracle从入门到精通');
```
