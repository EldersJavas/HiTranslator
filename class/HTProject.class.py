class HTProject :
    """
    HTProject class
    """
    IsNew=False
    File=''
    #def __init__(self):

    
 #   def Crate(self,con) :   
#        Item[con]=self.
    Res={}

    ProjectConfig={
        'ProjectName':'',
        'ResoureLanguage':'',
        'Author':[],
        'Member':[],
        'Contributor':[],
        'HTVersion':'1.0',
        'PVersion':'',
        'BuildTime':'',
        'LastChange':'',
        'License':'',
        'describtion':'',
        'Website':'',
        'HTsite':'',
        'ProjectLocal':'..',
        'IsClock':False,
        'IsFinish':False,
        'NeedCheck':True
        }
    
    Res=[]        
#    def __init__(self,IsNew,ProjectName, ResoureLanguage, Author,Member,Contributor,HTVersion,PVersion, BuildTime, LastChange, License, describtion, Website, HTsite, ProjectLocal,IsClock,IsFinish,NeedCheck) :
 #       if (IsNew) :
  #          self.ProjectName=ProjectName
   #         self.ResoureLanguage=ResourceLanguage
    #        
#
 #       else :
  #          open()


    class TranItem :
        
        Item={
            'Resource':'',
            'TransResource':{},
            'Tag':'',
            'Translator':[],
            'TransTime':'',
            'IsClock':False,
            'Checker':[],
            'CheckTime':''}

        def UpdateRes(self):
            """
            docstring
            """
            

        #def __init__() :
            
    #def __init__() :
    
    class Rule :
        ReaderRuleFile=''
        WriterRuleFile=''
        CustomFile=''
        ReaderRule=[]
        WriterRule=[]
        Custom={ 
            'func':[] ,
            'string':[] 
                }



    def __init__(self,IsNew):
        if (IsNew):
            self.IsNew=IsNew

    def ChangeConfig(self,chance,ac=False) :
        for i in chance.keys():
            print(i)
            if (chance[i]!='') :
                self.ProjectConfig[i]=chance[i]
                ac=True

        return ac

    def AddRes(self,ID='',ac=False) :
        if ID == "" :
            
            self.Res.append()               
        return ac

    def DelRes(self,ID='',Name='',ac=False):
        if ID != '' :
            del self.Res[ID]
        else:
            self.Res.remove(Name)

    def UpdateRes(self,ID='',ORes='',NRes,ac=False):
        if ID=='':
            self.Res[ID]
        else:
            for i in self.Res :
                if self.Res[i].__dict__['Resource']==ORes:
                    self.Res[i]
                else:
                    return "Error Find Resource"
        
                
        

        




h=HTProject(True)

print(h.__dict__)
print(h.__doc__)
print(h.ChangeConfig({'ResoureLanguage':'Hello'}))