--// 이름으로 그룹핑하기
-- SELECT user_name, COUNT(user_name) AS ucount
-- FROM userall
-- GROUP BY user_name 
-- ORDER BY ucount DESC;


--// 동명이 2개 이상인 이용자 찾기
-- SELECT user_name, ucount
-- FROM 
--     (SELECT user_name, COUNT(user_name) ucount
--     FROM "userall"
--     GROUP BY user_name) foo
-- WHERE ucount > 2;


--// 동명이 5개나 있는 이용자 이용자번호 확인
-- SELECT user_no, user_name
-- FROM userall
-- WHERE user_name = '이지은';


--//## 충전금액현황
-- SELECT module_result_code, module_result_msg, COUNT(module_result_msg), SUM(charge_amt)
-- FROM chargeall
-- WHERE target_dt = '20211201'
-- GROUP BY module_result_code, module_result_msg
-- ORDER BY module_result_code ASC;


--// 권종별충전현황
-- SELECT module_result_code, module_result_msg, charge_amt, COUNT(user_no)
-- FROM chargeall
-- WHERE target_dt = '20211201' AND module_result_code = '0000'
-- GROUP BY module_result_code, module_result_msg, charge_amt
-- ORDER BY charge_amt;


--// 1. 조회 결과(충전총액)에서 2. 충전총액이 50만이상이면서 21년도 고객만 조회
-- SELECT * FROM
-- 	(SELECT userall.user_no, userall.user_name, SUM(chargeall.charge_amt) amt, COUNT(chargeall.updt_date)
-- 	FROM chargeall
-- 	RIGHT JOIN userall ON chargeall.user_no=userall.user_no 
-- 	GROUP BY userall.user_no, userall.user_name) foo 
-- WHERE amt > '500000' AND user_no > '21';



--// 211206
--// 테스트 테이블 만들기
-- CREATE TABLE IF NOT EXISTS public.charge10
-- (
--     auto_target_seq VARCHAR(20),
--     pub_company_id VARCHAR(12),
--     user_no VARCHAR(14),
--     target_dt DATE,
--     target_tm character varying COLLATE pg_catalog."default",
--     charge_type character varying COLLATE pg_catalog."default",
--     charge_dt character varying COLLATE pg_catalog."default",
--     cur_amt character varying COLLATE pg_catalog."default",
--     charge_amt INTEGER,
--     debit_card_seq character varying COLLATE pg_catalog."default",
--     support_overcharge_yn character varying COLLATE pg_catalog."default",
--     use_yn character varying COLLATE pg_catalog."default",
--     target_order_id character varying COLLATE pg_catalog."default",
--     target_order_detail_seq character varying COLLATE pg_catalog."default",
--     auto_order_id character varying COLLATE pg_catalog."default",
--     auto_order_detail_seq character varying COLLATE pg_catalog."default",
--     module_result_code character varying COLLATE pg_catalog."default",
--     module_result_msg character varying COLLATE pg_catalog."default",
--     inst_id character varying COLLATE pg_catalog."default",
--     inst_date TIMESTAMP WITHOUT TIME ZONE,
--     updt_id character varying COLLATE pg_catalog."default",
--     updt_date TIMESTAMP WITHOUT TIME ZONE,
--     localpay_id character varying COLLATE pg_catalog."default",
--     will_charge_amt INTEGER,
--     target_wallet_no character varying COLLATE pg_catalog."default",
--     target_cur_amt character varying COLLATE pg_catalog."default",
--     target_sort_no character varying COLLATE pg_catalog."default",
--     target_order_cnt character varying COLLATE pg_catalog."default",
--     process_duration INTEGER
-- );

--// 테스트 테이블 삭제하기
-- DROP TABLE charge10;

--// import
-- COPY public.charge10 FROM '/var/lib/postgresql/files/charge10.csv' WITH DELIMITER ',' CSV HEADER

-- SELECT * FROM charge10 LIMIT 10;

--// 날짜 시간
-- SELECT CURRENT_DATE, CURRENT_TIME, CURRENT_TIME(2);


-- ALTER TABLE userall 
-- ALTER COLUMN change_tm TYPE time;

-- SELECT LOCALTIME(change_tm) FROM userall LIMIT 10;
-- SELECT TIME("12:00:00");
SELECT LOCALTIME(2);


SELECT
    LOCALTIME,
    EXTRACT (HOUR FROM LOCALTIME) as hour,
    EXTRACT (MINUTE FROM LOCALTIME) as minute, 
    EXTRACT (SECOND FROM LOCALTIME) as second,
    EXTRACT (milliseconds FROM LOCALTIME) as milliseconds; 
