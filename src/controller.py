import model as m
from typing import Callable

could_not_register_server_text = "Could not register the discord server with the database."
no_active_campaign_text="""There is no active campaign!
     See the list of campaigns with /listCampaigns.\n
     Select one with /selectCampaign <campaign>
    """

no_active_character="""There is no active character!
    See the list of your characters with /listCharacters.\n
    Select one with /selectCharacter <character>
    """

def character_not_exist(name):
    return f"No characters named {name}!"

def connect():
    m.connect()
    
def tryRegisterServer(guild):
    if not m.checkGuildExists(guild):
        m.registerServer(guild)

def tryRegisterUser(guild, user):
    if not m.checkUserExists(guild, user):
        m.registerUser(guild, user)

def createCampaign(guild, name) -> str:
    tryRegisterServer(guild)
    if not m.checkCampaignExists(guild, name):
        m.createCampaign(guild, name)
        return f"Campaign named {name} created."
    else:
        return f"A campaign with the name {name} already exists!"

def selectCampaign(guild, name) -> str:
    tryRegisterServer(guild)
    returnval = ""
    if not m.checkCampaignExists(guild, name):
        returnval+= createCampaign(guild, name) + "\n"
    m.selectCampaign(guild, name)
    returnval+= f"Selected campaign {name}."
    return returnval

def getCampaign(guild) -> str:
    tryRegisterServer(guild)
    campaign = m.getCampaign(guild)
    if campaign is not None:
        return campaign[1]
    else: return no_active_campaign_text

def listCampaigns(guild) -> str:
    tryRegisterServer(guild)
    campaigns = m.listCampaigns(guild)
    if campaigns is not None:
        return '\n'.join(map(str, campaigns))
    else:return "There are no campaigns on this server!"

def deleteCampaign(guild, name) -> str:
    tryRegisterServer(guild)
    if m.checkCampaignExists(guild, name):
        m.deleteCampaign(guild, name)
        return f"Deleted campaign {name}"
    else:return f"Campaign named {name} does not exist!"

def createCharacter(guild, name) -> str:
    tryRegisterServer(guild)
    campaign = m.getCampaign(guild)
    if campaign is not None:
        m.createCharacter(campaign[0], name)
        return f"Created character named {name}."
    else: return no_active_campaign_text

def selectCharacter(guild, user, name) -> str:
    tryRegisterServer(guild)
    tryRegisterUser(guild, user)
    campaign = m.getCampaign(guild)
    returnval = ""
    if campaign is not None:
        character = m.getCharacterByName(campaign[0], name)
        if character is None:        
            returnval+= createCharacter(campaign[0], name) + "\n"
            character = m.getCharacterByName(campaign[0], name)  
        m.selectCharacter(user, character[0])
        returnval+= f"Selected character named {name}"
    else:returnval = no_active_campaign_text
    return returnval

def getCharacter(guild, user) -> str:
    tryRegisterServer(guild)
    tryRegisterUser(guild, user)
    campaign = m.getCampaign(guild)
    if campaign is not None:
        character = m.getCharacter(user, campaign[0])
        if character is not None:
            return character[1]
        else: return no_active_character_text
    else: return no_active_campaign_text

def listCharacters(guild) -> str:
    tryRegisterServer(guild)
    campaign = m.getCampaign(guild)
    if campaign is not None:
        characters = m.listCharacters(campaign[0])
        if characters is not None:
            characters = list(map(''.join, characters))
            return '\n'.join(characters)
        else:return f"There are no characters for the campaign {campaign[1]}!"
    else: return no_active_campaign_text

def deleteCharacter(guild, name) -> str:
    tryRegisterServer(guild)
    campaign = m.getCampaign(guild)
    if campaign is not None:
        if m.checkCharacterExists(campaign[0], name):
            m.deleteCharacter(campaign, name)
        else:return f"There is no character named {name}!"

def getRPGStat(guild, user, name: str, stat: str, func: Callable) -> str:
    tryRegisterServer(guild)
    campaign = m.getCampaign(guild)
    if campaign is not None:
        character = None
        if name is None:
            character = m.getCharacter(user, campaign[0])
            if character is None:
                return no_active_character_text 
        else:
            character = m.getCharacterByName(campaign[0], name)
            if character is None:
                return character_not_exist(name)
        value = func(character[0])
        return f"{character[1]} has {value} {stat}."
    else: return no_active_campaign_text

def getCampaignRPGStat(guild, stat: str, func: Callable) -> str:
    tryRegisterServer(guild)
    campaign = m.getCampaign(guild)
    if campaign is not None:
        values = func(campaign[0])
        ret =stat + "\n"
        ret+="- - - - - - - - - -\n"
        for value in values:
            ret+= ":       ".join(map(str, value)) + "\n"
        return ret
    else: return no_active_campaign_text

def setRPGStat(guild, user, value: int, name: str,  stat: str, setter: Callable, getter: Callable) -> str:
    tryRegisterServer(guild)
    campaign = m.getCampaign(guild)
    if campaign is not None:
        character = None
        if name is None:
            character = m.getCharacter(user, campaign[0])
            if character is None:
                return no_active_character_text
        else:
            character = m.getCharacterByName(campaign[0], name)
            if character is None:
                return character_not_exist(name)
        setter(character[0], value),
        value_out = getter(character[0])
        return f"{character[1]} now has {value_out} {stat}."
    else: return no_active_campaign_text

def addRPGStat(guild, user, value: int, name: str, stat: str, setter: Callable, getter: Callable) -> str:
    tryRegisterServer(guild)
    campaign = m.getCampaign(guild)
    if campaign is not None:
        character = None
        if name is None:
            character = m.getCharacter(user, campaign[0])
            if character is None:
                return no_active_character_text
        else:
            character = m.getCharacterByName(campaign[0], name)
            if character is None:
                return character_not_exist(name)
        val_orig = getter(character[0])
        setter(character[0], value + val_orig),
        value_out = getter(character[0])
        return f"{character[1]} now has {value_out} {stat}."
    else: return no_active_campaign_text


def campaignOverview(guild):
    tryRegisterServer(guild)
    campaign = m.getCampaign(guild)
    if campaign is not None:
        ret = f"{campaign[1]}\n"
        ret+= "- - - - - - - - - - - - - - - - - - - -\n"
        ret+="           NAME     KILLS     DOWNS    DEATHS   DAMAGE DEALT     DAMAGE RECEIVED   HEALING PERFORMED    HEALING RECEIVED\n"
        values = m.getCampaignOverview(campaign[0])
        for e1,e2,e3,e4,e5,e6,e7,e8 in values:
             ret+= f"{str(e1).rjust(15, ' ')}{str(e2).rjust(10, ' ')}{str(e3).rjust(10, ' ')}{str(e4).rjust(10, ' ')}{str(e5).rjust(15, ' ')}{str(e6).rjust(20, ' ')}{str(e7).rjust(20, ' ')}{str(e8).rjust(20, ' ')}\n"
        return ret
    else: return no_active_campaign_text

def campaignKills(guild):
    return getCampaignRPGStat(guild, "Kills", m.getCampaignKills)

def getKills(guild, user, name):
    return getRPGStat(guild, user, name, "kills", m.getKills)

def addKills(guild, user, name, kills):
    return addRPGStat(guild, user, kills, name, "kills", m.setKills, m.getKills)

def setKills(guild, user, kills, name):
    return setRPGStat(guild, user, kills, name, "kills", m.setKills, m.getKills)

def campaignDowns(guild):
    return getCampaignRPGStat(guild, "downs", m.getCampaignDowns)

def getDowns(guild, user, name):
    return getRPGStat(guild, user, name, "downs", m.getDowns)

def addDowns(guild, user, downs, name):
    return addRPGStat(guild, user, downs, name, "downs", m.setDowns, m.getDowns)

def setDowns(guild, user, downs, name):
    return setRPGStat(guild, user, downs, name, "downs", m.setDowns, m.getDowns)

def campaignDeaths(guild):
    return getCampaignRPGStat(guild, "Deaths", m.getCampaignDeaths)

def getDeaths(guild, user, name):
    return getRPGStat(guild, user, name, "deaths", m.getDeaths)

def addDeaths(guild, user, deaths, name):
    return addRPGStat(guild, user, deaths, name, "deaths", m.setDeaths, m.getDeaths)

def setDeaths(guild, user, deaths, name):
    return setRPGStat(guild, user, deaths, name, "deaths", m.setDeaths, m.getDeaths)

def campaignDamageDealt(guild):
    return getCampaignRPGStat(guild, "Damage Dealt", m.getCampaignDamageDealt)

def getDamageDealt(guild, user, name):
    return getRPGStat(guild, user, name, "damage dealt", m.getDamageDealt)

def addDamageDealt(guild, user, dmg, name):
    return addRPGStat(guild, user, dmg, name, "damage dealt", m.setDamageDealt, m.getDamageDealt)

def setDamageDealt(guild, user, dmg, name):
    return setRPGStat(guild, user, dmg, name, "damage dealt", m.setDamageDealt, m.getDamageDealt)

def campaignDamageReceived(guild):
    return getCampaignRPGStat(guild, "Damage Received", m.getCampaignDamageReceived)

def getDamageReceived(guild, user, name):
    return getRPGStat(guild, user, name, "damage received", m.getDamageReceived)

def addDamageReceived(guild, user, dmg, name):
    return addRPGStat(guild, user, dmg, name, "damage received", m.setDamageReceived, m.getDamageReceived)

def setDamageReceived(guild, user, dmg, name):
    return setRPGStat(guild, user, dmg, name, "damage received", m.setDamageReceived, m.getDamageReceived)

def campaignHealingPerformed(guild):
    return getCampaignRPGStat(guild, "Healing Performed", m.getCampaignHealingPerformed)

def getHealingPerformed(guild, user, name):
    return getRPGStat(guild, user, name, "healing performed", m.getHealingPerformed)

def addHealingPerformed(guild, user, hp, name):
    return addRPGStat(guild, user, hp, name, "healing performed", m.setHealingPerformed, m.getHealingPerformed)

def setHealingPerformed(guild, user, hp, name):
    return setRPGStat(guild, user, hp, name, "healing performed", m.setHealingPerformed, m.getHealingPerformed)

def campaignHealingReceived(guild):
    return getCampaignRPGStat(guild, "Healing Received", m.getCampaignHealingReceived)

def getHealingReceived(guild, user, name):
    return getRPGStat(guild, user, name, "healing received", m.getHealingReceived)

def addHealingReceived(guild, user, hp, name):
    return addRPGStat(guild, user, hp, name, "healing received", m.setHealingReceived, m.getHealingReceived)

def setHealingReceived(guild, user, hp, name):
    return setRPGStat(guild, user, hp, name, "healing received", m.setHealingReceived, m.getHealingReceived)
