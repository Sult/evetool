from collections import OrderedDict

from django.db import models



class SkillGroup(models.Model):
    """ All skill groups """
    
    #skillGroups
    groupid = models.BigIntegerField(unique=True)
    groupname = models.CharField(max_length=254, unique=True)
    
    def __unicode__(self):
        return self.groupname
    
    #create skilltree dictionary for template
    @staticmethod
    def skilltree_dict():
        temp = OrderedDict()
        
        for g in SkillGroup.objects.exclude(groupname="Fake Skills").order_by("groupname"):
            temp[g.groupname] = Skill.objects.filter(skillgroup=g, published=1).order_by("typename")
        
        return temp
    


class Skill(models.Model):
    """ An eve online skill """
    
    #skills
    typeid = models.BigIntegerField(unique=True)
    typename = models.CharField(max_length=254)
    published = models.IntegerField()
    skillgroup = models.ForeignKey(SkillGroup)
    description = models.TextField()
    rank = models.IntegerField()
    primaryattribute = models.CharField(max_length=254)
    secondaryattribute = models.CharField(max_length=254)
    
    def __unicode__(self):
        return self.typename
    
    #get skilltree path of skill (needed for template)
    def skilltree(self, path):
        pk = int(path.split("/")[3])
        skill = Skill.objects.get(pk=pk)
        return skill.skillgroup.groupname
    
    
    
class RequiredSkill(models.Model):
    """ skill requirements """
    
    skill = models.ForeignKey(Skill, related_name="required_skills")
    required = models.ForeignKey(Skill, related_name="required")
    skilllevel = models.IntegerField()

    def __unicode__(self):
        return "requirement for %s" % self.skill.typename
        
        
    #show level in roman
    def show_level(self):
        if self.skilllevel == 1:
            return "I"
        elif self.skilllevel == 2:
            return "II"
        elif self.skilllevel == 3:
            return "III"
        elif self.skilllevel == 4:
            return "IV"
        elif self.skilllevel == 5:
            return "V"
    
    

class SkillBonus(models.Model):
    """ bonus values of skills (per skilllevel) """
    
    skill = models.ForeignKey(Skill)
    bonustype = models.CharField(max_length=254)
    bonusvalue = models.FloatField()
    
    
        
        
        
        
        
        
        
        
    
    
