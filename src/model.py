import mysql.connector
from dotenv import load_dotenv
import os
import json

def connect():
    load_dotenv()

    global mydb
    mydb = mysql.connector.connect(
        host='localhost',
        user=os.environ.get('mysql_user'),
        password=os.environ.get('mysql_password'),
        database='rpg_stat_tracker_test'
    )

    global cursor
    cursor = mydb.cursor(buffered=True)

def checkGuildExists(guild) -> bool:
    query = "SELECT COUNT(id) FROM discord_server WHERE id=%s;"
    cursor.execute(query, (guild,))
    return cursor.fetchall()[0][0] == 1

def registerServer(guild):
    query = "INSERT INTO discord_server (id) VALUES (%s);"
    cursor.execute(query, (guild,))
    mydb.commit()

def checkCampaignExists(guild, campaign) -> bool:
    query = """ SELECT COUNT(id) FROM campaign WHERE fk_discord_server_id=%s AND campaign_name=%s; """
    cursor.execute(query, (guild, campaign))
    return cursor.fetchall()[0][0] == 1

def createCampaign(guild, name):
    query = """ INSERT INTO campaign 
    (fk_discord_server_id, campaign_name) VALUES (%s,%s); """
    cursor.execute(query, (guild, name))
    mydb.commit()

def selectCampaign(guild, name):
    query = """ 
    UPDATE discord_server 
    INNER JOIN campaign ON discord_server.id=campaign.fk_discord_server_id
    SET discord_server.fk_campaign_id=campaign.id
    WHERE discord_server.id=%s AND campaign.campaign_name=%s;
    """
    cursor.execute(query, (guild, name))
    mydb.commit()

def getCampaign(guild) -> tuple[int,str]:
    query = """SELECT campaign.id,campaign_name
                FROM campaign 
                INNER JOIN discord_server 
                ON campaign.id=discord_server.fk_campaign_id
                WHERE discord_server.id=%s 
                AND campaign_name IS NOT NULL;
                """
    cursor.execute(query, (guild,))
    result = cursor.fetchall()
    if len(result) != 0:
        return result[0]
    else:
        return None

def listCampaigns(guild) -> list[tuple[str]]:
    query = """
            SELECT campaign_name
            FROM campaign
            WHERE fk_discord_server_id=%s;
            """
    cursor.execute(query, (guild,))
    results = cursor.fetchall()
    if len(results) != 0:
        return results
    else:
        return None

def deleteCampaign(guild, name):
    query = """
            DELETE FROM campaign WHERE fk_discord_server_id=%s AND campaign_name=%s; 
            """
    cursor.execute(query, (guild, name))
    mydb.commit()

def checkUserExists(guild, user) -> bool:
    query = """
            SELECT COUNT(id)
            FROM discord_server_user
            WHERE fk_discord_server_id=%s AND discord_id=%s;
            """
    cursor.execute(query, (guild, user))
    return cursor.fetchall()[0][0] == 1

def registerUser(guild, user):
    query = """
            INSERT INTO discord_server_user (fk_discord_server_id, discord_id) VALUES (%s,%s);
            """
    cursor.execute(query, (guild, user))
    mydb.commit()

def checkCharacterExists(campaign, name) -> bool:
    query = """
            SELECT COUNT(id)
            FROM rpg_character
            WHERE fk_campaign_id=%s AND character_name=%s;
            """
    cursor.execute(query, (campaign, name))
    return cursor.fetchall()[0][0] == 1

def createCharacter(campaign, name):
    query = """
            INSERT INTO rpg_character
            (character_name,fk_campaign_id)
            VALUES (%s,%s)
            """
    cursor.execute(query, (name, campaign))
    mydb.commit()        

def selectCharacter(user, character_id):
    query = """ 
            UPDATE discord_server_user 
            SET fk_rpg_character_id=%s
            WHERE discord_id=%s
            """
    cursor.execute(query, (character_id, user))
    mydb.commit()

def getCharacter(user, campaign) -> tuple[int,str]:
    query = """SELECT rpg_character.id,character_name
                FROM rpg_character 
                INNER JOIN discord_server_user
                ON rpg_character.id=discord_server_user.fk_rpg_character_id
                WHERE discord_server_user.discord_id=%s 
                AND rpg_character.fk_campaign_id=%s
                AND character_name IS NOT NULL;
                """
    cursor.execute(query, (user,campaign))
    result = cursor.fetchall()
    if len(result) != 0:
        return result[0]
    else:
        return None

def getCharacterByName(campaign, name) -> tuple[int, str]:
    query = """SELECT id,character_name
            FROM rpg_character
            WHERE character_name=%s
            AND fk_campaign_id=%s
            """
    cursor.execute(query, (name, campaign))
    result = cursor.fetchall()
    if len(result) != 0:
        return result[0]
    else:
        return None

def listCharacters(campaign):
    query = """
            SELECT character_name
            FROM rpg_character
            WHERE fk_campaign_id=%s;
            """
    cursor.execute(query, (campaign,))
    results = cursor.fetchall()
    if len(results) != 0:
        return results
    else:
        return None

def deleteCharacter(campaign, name):
    query =  """
            DELETE FROM rpg_character WHERE fk_campaign_id=%s AND character_name=%s; 
            """
    cursor.execute(query, (campaign, name))
    mydb.commit()

def getRPGStatGetter(column_name):
    return f"""
            SELECT {column_name}
            FROM rpg_character
            WHERE id=%s
            """

def getRPGStatSetter(column_name):
    return f"""
            UPDATE rpg_character 
            SET {column_name}=%s
            WHERE id=%s
            """
def getRPGStat(column_name, id) -> int:
    query = getRPGStatGetter(column_name)
    cursor.execute(query, (id,))
    return cursor.fetchall()[0][0]

def setRPGStat(column_name, id, value):
    query = getRPGStatSetter(column_name)
    cursor.execute(query, (value, id))
    mydb.commit()

def getKills(id):
    return getRPGStat("kills", id)

def setKills(id, value):
    setRPGStat("kills", id, value)

def getDowns(id):
    return getRPGStat("downs", id)

def setDowns(id, value):
    setRPGStat("downs", id, value)

def getDeaths(id):
    return getRPGStat("deaths", id)

def setDeaths(id, value):
    setRPGStat("deaths", id, value)

def getDamageDealt(id):
    return getRPGStat("damage_dealt", id)

def setDamageDealt(id, value):
    setRPGStat("damage_dealt", id, value)

def getDamageReceived(id):
    return getRPGStat("damage_received", id)

def setDamageReceived(id, value):
    setRPGStat("damage_received", id, value)

def getHealingPerformed(id):
    return getRPGStat("healing_performed", id)

def setHealingPerformed(id, value):
    setRPGStat("healing_performed", id, value)

def getHealingReceived(id):
    return getRPGStat("healing_received", id)

def setHealingReceived(id, value):
    setRPGStat("healing_received", id, value)