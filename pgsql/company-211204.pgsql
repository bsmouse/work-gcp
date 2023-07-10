--// 가맹점 테이블 만들기
-- CREATE TABLE IF NOT EXISTS public.companyall_test
-- (
--     company_name character varying COLLATE pg_catalog."default",
--     company_owner_name character varying COLLATE pg_catalog."default",
--     company_tel character varying COLLATE pg_catalog."default",
--     company_no character varying COLLATE pg_catalog."default",
--     company_addr character varying COLLATE pg_catalog."default",
--     company_type character varying COLLATE pg_catalog."default",
--     company_bank character varying COLLATE pg_catalog."default",
--     company_account character varying COLLATE pg_catalog."default"
-- )

--// 테이블 삭제하기
-- DROP TABLE companyall_test;


--// 가앱점 엑셀자료 import는 pgAdmin4를 이용해서 업로드함

--// companyall.csv -> table import, export 하기 docker volumn을 설정해야 가능할것 같음.
-- COPY public.companyall_test FROM '/var/lib/postgresql/files/companyall.csv' WITH DELIMITER ',' CSV
-- COPY public.companyall_test TO '/var/lib/postgresql/files/companyall_to.csv' WITH DELIMITER ',' CSV

--// 가맹점수 조회
-- SELECT COUNT(*) FROM companyall;
SELECT * FROM companyall LIMIT 100;


--// 가맹점주가 여러 사업장을 가지고 있는지 조회
-- SELECT company_owner_name, company_no, COUNT(company_owner_name) AS ucount
-- FROM companyall
-- GROUP BY company_owner_name, company_no 
-- ORDER BY ucount DESC
-- LIMIT 100;