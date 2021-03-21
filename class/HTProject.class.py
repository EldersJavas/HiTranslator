import os
test
def test(h):
    h=HTProject(True)    
    

class HTProject :
    IsNew=False
    File=''
    #def __init__(self):
    def __init__(self,IsNew):
        if (IsNew):
            self.IsNew=IsNew

    #def Crate(self,con) :   
        #con=self.ProjectConfig(ProjectName)
                     
    class ProjectConfig :

        ProjectName=''
        ResoureLanguage=''
        Author=[]
        Member=[]
        Contributor=[]
        HTVersion='1.0'
        PVersion=''
        BuildTime=''
        LastChange=''
        License=''
        describtion=''
        Website=''
        HTsite=''
        ProjectLocal='..'
        IsClock=False
        IsFinish=False
        NeedCheck=True
        
        def __init__(self,IsNew,ProjectName, ResoureLanguage, Author,Member,Contributor,HTVersion,PVersion, BuildTime, LastChange, License, describtion, Website, HTsite, ProjectLocal,IsClock,IsFinish,NeedCheck) :
            if (IsNew) :
                self.ProjectName=ProjectName
            else :
                open()


    class TranItem :
        
        Resource=''
        TransResource={}
        Tag=''
        Translator=[]
        TransTime=''
        IsClock=False
        Checker=[]
        CheckTime=''


        #def __init__() :
        
    #def __init__() :
    class Rule :
        ReaderRuleFile=''
        WriterRuleFile=''
        CustomFile=''
        ReaderRule=[]
        WriterRule=[]
        Custom={ 'func':[] , 'string':[] }
