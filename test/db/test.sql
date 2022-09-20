USE rpg_stat_tracker_test;

INSERT INTO discord_server VALUES (23452345, DEFAULT);

INSERT INTO discord_server_user VALUES (DEFAULT, "stinky", 23452345, DEFAULT);

INSERT INTO discord_server_user VALUES (DEFAULT, "donkey", 23452345, DEFAULT);

INSERT INTO campaign VALUES (DEFAULT, 23452345, "Porgenheim");

INSERT INTO rpg_character (
    character_name,
    fk_discord_server_user_id, 
    fk_campaign_id)
    VALUES (
    "charles", 
    1, 
    1);

