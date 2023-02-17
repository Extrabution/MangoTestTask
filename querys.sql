create table users(
    user_id bigserial not null,
    phone_number text unique not null  ,
    password text not null,
    about_me text not null,
    pin_chats_ids integer[] not null,
    PRIMARY KEY (user_id));
create index users_user_id on users using hash(user_id);
create index users_phone_number on users using hash(phone_number);

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

