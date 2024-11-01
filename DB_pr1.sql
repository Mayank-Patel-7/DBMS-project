create database ISTE;
select* from copy ofisteorganizers;
SELECT * FROM iste.`list`;

RENAME TABLE `iste`.`copy of iste organizers` TO `iste`.`list`;
rename table iste.`list` to iste.`organizers`;

use iste;
ALTER TABLE organizers DROP COLUMN TimeStamp;


select * from organizers;