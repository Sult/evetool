import eveapi
import xml.etree.ElementTree as ET

from apps.characters.models import Skill, SkillGroup, RequiredSkill, SkillBonus



def skill_groups():
    api = eveapi.EVEAPIConnection()
    skilltree = api.eve.SkillTree()
    
    for g in skilltree.skillGroups:
        try:
            SkillGroup.objects.create(
                groupid = g.groupID,
                groupname = g.groupName,
            )
        except:
            pass


    


tree = ET.parse("populate/skilltree.xml")
root = tree.getroot()
#https://docs.python.org/2/library/xml.etree.elementtree.html#xpath-support
def get_description(typeID):
    for result in root.findall("result"):
        for rowset in result.findall("rowset"):
            for row in rowset.findall("row"):
                for rw in row.findall("rowset"):
                    for r in rw.findall("row"):
                        if r.get("typeID") == str(typeID):
                            return r.find("description").text




def skills():
    api = eveapi.EVEAPIConnection()
    skilltree = api.eve.SkillTree()
    
    for g in skilltree.skillGroups:
        #get skillgroup
        skillgroup = SkillGroup.objects.get(groupid=g.groupID)
        
        for skill in g.skills:
            
            try:
                t = type(skill.description)
                if t == unicode:
                    desc = skill.description
                else:
                    desc = get_description(skill.typeID)
                
                
                s = Skill.objects.create(
                    typeid = skill.typeID,
                    typename = skill.typeName,
                    published=skill.published,
                    skillgroup = skillgroup,
                    description = desc,
                    rank = skill.rank,
                    primaryattribute = skill.requiredAttributes.primaryAttribute,
                    secondaryattribute = skill.requiredAttributes.secondaryAttribute,
                )
                
                for bonus in skill.skillBonusCollection:
                    SkillBonus.objects.create(
                        skill = s,
                        bonustype = bonus.bonusType,
                        bonusvalue = bonus.bonusValue,
                    )
            except:
                pass
            
            
            
                
def requirements():
    api = eveapi.EVEAPIConnection()
    skilltree = api.eve.SkillTree()
    
    for g in skilltree.skillGroups:
        #get skillgroup
        
        for skill in g.skills:
            try:
                s = Skill.objects.get(typeid=skill.typeID)

                for req in skill.requiredSkills:
                    RequiredSkill.objects.create(
                        skill = s,
                        required = Skill.objects.get(typeid=req.typeID),
                        skilllevel = req.skillLevel,
                    )
            except:
                pass
        

skill_groups()
skills()
requirements()
