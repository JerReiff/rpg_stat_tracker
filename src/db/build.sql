CREATE TABLE IF NOT EXISTS discord_server(
    id BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    fk_campaign_id INT UNSIGNED

-- defined below after table creation
    -- FOREIGN KEY (fk_campaign_id)
    --     REFERENCES campaign(id)
    --     ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS campaign(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    fk_discord_server_id BIGINT UNSIGNED NOT NULL,
    campaign_name VARCHAR(35) NOT NULL,

    INDEX disc_srv_id (fk_discord_server_id),
    UNIQUE INDEX server_campaign (fk_discord_server_id, campaign_name),

    FOREIGN KEY (fk_discord_server_id)
        REFERENCES discord_server(id)
        ON UPDATE CASCADE ON DELETE CASCADE
);

ALTER TABLE discord_server
    ADD FOREIGN KEY (fk_campaign_id)
        REFERENCES campaign(id)
        ON UPDATE CASCADE ON DELETE SET NULL;

CREATE TABLE IF NOT EXISTS discord_server_user(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    discord_id BIGINT NOT NULL,
    fk_discord_server_id BIGINT UNSIGNED NOT NULL,
    fk_rpg_character_id INT UNSIGNED,

    INDEX disc_srv_id (fk_discord_server_id),
    INDEX char_id (fk_rpg_character_id),
    UNIQUE INDEX (fk_discord_server_id, discord_id),

    FOREIGN KEY (fk_discord_server_id)
        REFERENCES discord_server(id)
        ON UPDATE CASCADE ON DELETE CASCADE

-- defined below after table creation
    -- FOREIGN KEY (fk_rpg_character_id)
    --     REFERENCES rpg_character(id)
    --     ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS rpg_character(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    character_name VARCHAR (40) NOT NULL, 
    fk_campaign_id INT UNSIGNED NOT NULL,
    kills INT UNSIGNED NOT NULL DEFAULT 0,
    downs INT UNSIGNED NOT NULL DEFAULT 0,
    deaths INT UNSIGNED NOT NULL DEFAULT 0,
    damage_dealt INT UNSIGNED NOT NULL DEFAULT 0,
    damage_received INT UNSIGNED NOT NULL DEFAULT 0,
    healing_performed INT UNSIGNED NOT NULL DEFAULT 0,
    healing_received INT UNSIGNED NOT NULL DEFAULT 0,
    
    INDEX campaign_id (fk_campaign_id),
    UNIQUE INDEX campaign_char (fk_campaign_id, character_name),

    FOREIGN KEY (fk_campaign_id)
        REFERENCES campaign(id)
        ON UPDATE CASCADE ON DELETE CASCADE
);

ALTER TABLE discord_server_user 
    ADD FOREIGN KEY (fk_rpg_character_id)
        REFERENCES rpg_character(id)
        ON UPDATE CASCADE ON DELETE SET NULL;