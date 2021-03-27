import yaml
import json
import os
import xmltodict
class HTProject :
    """
    HTProject class
    """
    IsNew=False
    File=''
    #def __init__(self):

    
 #   def Crate(self,con) :   
#        Item[con]=self.

    

    
    
       
#    def __init__(self,IsNew,ProjectName, ResoureLanguage, Author,Member,Contributor,HTVersion,PVersion, BuildTime, LastChange, License, describtion, Website, HTsite, ProjectLocal,IsClock,IsFinish,NeedCheck) :
 #       if (IsNew) :
  #          self.ProjectName=ProjectName
   #         self.ResoureLanguage=ResourceLanguage
    #        
#
 #       else :
  #          open()


    class TranItem :

        def UpdateRes(self):
            """
            docstring
            """
            
        def ChangeTag(self,ntag,ac=False):
            """
            Tag change
            """    
            self.Item['Tag']=ntag
            return ac

        def __init__(self,ID,Resource):
            """
            docstring
            """
            self.Item={
                'ID':ID,
                'Resource':Resource,
                'TransResource':{},
                'Tag':'UnTr',
                'Translator':[],
                'TransTime':'',
                'IsClock':False,
                'Checker':[],
                'CheckTime':''
                }        
        def Add_lang(self,str):
            """
            docstring
            """
            self.Item['TransResource'][str]=''
        #def __init__() :
            
    #def __init__() :



    def ChangeCustom(self,Cf=[],Cs=[]):
        if Cf!=[]:
            self.Rule['Custom']['func']==Cf
            if Cs!=[]:
                self.Rule['Custom']['string']==Cs
            else :
                return False
        
    def ChangeRule(self,chance,ac=False):
        for i in chance.keys():
            #print(i)
            if (chance[i]!='') :
                ac=True
                #
                #
                if (i=='ReaderRule' or i=="WriterRule"):
                    self.Rule[i].append(chance[i])
                elif (i=='Custom'):
                    self.ChangeCustom(chance[i])
                else:    
                    self.Rule[i]=chance[i]    
                
                
            else:
                return False

        return ac


            
    def LoadProject(self, file):
        """
        LoadProject
        """
        open(file)        

    def ChangeConfig(self,chance,ac=False) :
        for i in chance.keys():
            #print(i)
            if (chance[i]!='') :
                self.ProjectConfig[i]=chance[i]
                ac=True

        return ac

    def AddRes(self,resource,ID='',ac=False) :
        if ID == "" :
            self.Res.append(self.TranItem(len(self.Res) + 1,resource))    
            #print(self.Res)
        else:
            self.Res.append(self.TranItem(ID,resource))
            #self.Res['']            
        return ac

    def Temp_Find_TransRes(self,temp,ID='',Res='',lang='en'):
        if ID!='':
            for i in self.Res:
                if i['Item']['ID']==ID:
                    return i['Item']['TransResource'][lang]
                else:
                    return "Not Found(ID)"
        elif Res!='':
            for i in self.Res:
                if i['Item']['Resource']==Res:
                    return i['Item']['TransResource'][lang]
                else:
                    return "Not Found(OrginRes)"
        else:
            return "Not Found(ID or OrginRes Empty)"

    def DelRes(self,ID='',Name='',ac=False):
        if ID != '' :
            del self.Res[ID]
        else:
            self.Res.remove(Name)

    def UpdateRes(self,NRes,ID='',ORes='',ac=False):
        if ID=='':
            self.Res[ID]
        else:
            for i in self.Res :
                if self.Res[i].__dict__['Resource']==ORes:
                    self.Res[i]
                else:
                    return "Error Find Resource"
        
    def ReturnDict(self,back={}):
        """
        docstring
        """
        back={
            'Res':{}
        }
        for i in self.Res:
            back['Res'][i.__dict__['Item']['ID']]=i.__dict__

        back['ProjectConfig']=self.__dict__['ProjectConfig']
        back['Rule']=self.__dict__['Rule']
        return back

    def __init__(self,IsNew,file=''):
        if (IsNew):
            self.IsNew=IsNew
            self.ProjectConfig={
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
                'TrLanguage:{},
                'ProjectLocal':'..',
                'IsClock':False,
                'IsFinish':False,
                'NeedCheck':True
                }
            self.Rule={
                'ReaderRuleFile':'',
                'WriterRuleFile':'',
                'CustomFile':'',
                'ReaderRule':[],
                'WriterRule':[],
                'Custom':{ 
                    'func':[] ,
                    'string':[] 
                        }
                }
            self.Res=[]  
    
        else:
            self.LoadProject(file)

h=HTProject(True)


#print(h.__doc__)
#print(h.ChangeConfig({'ResoureLanguage':'Hello'}))
#print(h.ProjectConfig)
#print(h.Rule)
#print(h.Res)

h.AddRes("HeyTranser")
h.AddRes("Hello,World!")
h.AddRes("Welcome!")
p=h.ReturnDict()
print(p)
#f = open(r"testProject.yaml",encoding='utf-8')
#data = f.read()


print(yaml.safe_dump(p))
f= open("test.yaml","w+")
f.write(yaml.safe_dump(p))
f.close
#print(yaml.load(data))
#先将yaml转换为dict格式



for idi in p['Res']:
    del p['Res'][idi]['Item']['Tag']
    del p['Res'][idi]['Item']['TransTime']
    del p['Res'][idi]['Item']['IsClock']
    del p['Res'][idi]['Item']['Checker']
    del p['Res'][idi]['Item']['CheckTime']
    #del p['Res'][idi]['Item']['TransResource']
    p['Res'][idi]['Item']['TransResource']=p['Res'][idi]['Item']['TransResource'][]

readydict={
    'Resource':p['Res'],
    'Contributor':p['ProjectConfig']['Contributor'],
    'Author':p['ProjectConfig']['Author'],
    'Member':p['ProjectConfig']['Member'],
    'ProjectName':p['ProjectConfig']['ProjectName']
        }


generate_json =json.dumps(readydict,sort_keys=False,indent=4,separators=(',',': '))

print(readydict,type(readydict))

f1 = open("test.json","w+")
f1.write(generate_json)
f1.close


xml_str = xmltodict.unparse({'xml':readydict}, pretty=True)
fxml = open("test.xml","w+")
fxml.write(xml_str)
fxml.close