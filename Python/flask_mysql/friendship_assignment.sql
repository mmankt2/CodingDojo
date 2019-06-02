select concat(u.first_name, " ",u.last_name) as user, concat(f.first_name, " ", f.last_name) as friend from users u join friendships fs on u.id = fs.user_id join users f on f.id = fs.friend_id;

--1.Return all users who are friends with Kermit, make sure their names are displayed in the results.
select concat(u.first_name, " ", u.last_name) as user, concat(f.first_name, " ",f.last_name) as friend from users u join friendships fs on u.id = fs.user_id join users f on f.id = fs.friend_id where f.first_name = 'Kermit';

--2.Return the count of all friendships
select count(*) from friendships;

--3.Find out who has the most friends and return the count of their friends.
select u.first_name, u.last_name, count(fs.id) as num_friends from users u join friendships fs on u.id = fs.user_id group by 1,2 order by num_friends desc;

--4.Create a new user and make them friends with Eli Byers, Kermit The Frog, and Marky Mark
insert into users (first_name, last_name, created_at, updated_at) values ('melissa', 'littleton', NOW(), NOW());
insert into friendships (user_id, friend_id, created_at, updated_at) values (6,2,NOW(), NOW());
insert into friendships (user_id, friend_id, created_at, updated_at) values (6,4,NOW(), NOW());
insert into friendships (user_id, friend_id, created_at, updated_at) values (6,5,NOW(), NOW());
select concat(u.first_name, " ", u.last_name) as user, concat(f.first_name, " ",f.last_name) as friend from users u join friendships fs on u.id = fs.user_id join users f on f.id = fs.friend_id where u.first_name = 'melissa';

--5.Return the friends of Eli in alphabetical order
select concat(u.first_name, " ", u.last_name) as user, concat(f.first_name, " ",f.last_name) as friend from users u join friendships fs on u.id = fs.user_id join users f on f.id = fs.friend_id where u.first_name = 'Eli' order by friend;

--6.Remove Marky Mark from Eli’s friends.
delete from friendships where user_id = 2 and friend_id = 5;

7.Return all friendships, displaying just the first and last name of both friends
select concat(u.first_name, " ", u.last_name) as user, concat(f.first_name, " ",f.last_name) as friend from users u join friendships fs on u.id = fs.user_id join users f on f.id = fs.friend_id;
