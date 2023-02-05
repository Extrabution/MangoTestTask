drop table users;
create table users(
    user_id bigserial not null,
    phone_number text unique not null  ,
    password text not null,
    about_me text not null,
    pin_chats_ids integer[] not null,
    PRIMARY KEY (user_id));
create index users_user_id on users using hash(user_id);
create index users_phone_number on users using hash(phone_number);
insert into users(phone_number, password, about_me, pin_chats_ids)
values('admin', '$2b$12$PeXpd1jKCrxv/ujDGaQX0.tUFvPgjcWCgq5EwstafrXoSppIXzhn.',
       'Im developer Ivan', '{}');

delete from users where password='admin';

create table chats(
    chat_id bigserial not null,
    members integer[]  not null,
    name text  not null,
    last_message_at timestamp not null,
    PRIMARY KEY (chat_id));

create index chats_members on chats using gin(members);

create table messages(
    message_id bigserial not null,
    chat_id integer not null,
    author_id integer not null,
    created_at timestamp not null,
    message_type text not null,
    content text not null,
    liked_by_ids integer[],
    PRIMARY KEY (message_id)
);

create index messages_created_at_chat_id on messages using btree(created_at desc, chat_id);

select chats.chat_id
from chats
where 2=ANY(chats.members);

update users
set pin_chats_ids = array_append(pin_chats_ids, 2)
where user_id=1;

select users.phone_number
from users
where users.user_id = ANY((select chats.members from chats where chats.chat_id = 17)::bigint[]);


select * from messages as m
where m.chat_id = 1
order by m.created_at desc
limit 5 offset 0
