select ub.title as TITLE
, ub.board_id as BOARD_ID
, ur.reply_id as REPLY_ID
, ur.writer_id as WRITER_ID
, ur.contents as CONTENTS
, date_format(ur.created_date, "%Y-%m-%d") as CREATED_DATE
from used_goods_board as ub
join used_goods_reply as ur on ub.board_id=ur.board_id
where ub.created_date like "2022-10%"
order by ur.created_date asc, ub.title asc