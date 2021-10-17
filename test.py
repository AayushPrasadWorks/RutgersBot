from os import major

import json


f =  open('class_data-1.json') 
d = json.load(f)

def classes_by_major(major):
   try:
      d[major]
   except:
      return None
   res = [{}]
   for i in d[major]:
       res.append(i['title'])
   return res

def classes_by_dep_course_level(major,cnum):
   try:
      d[major]
   except:
      return None
   res = [{}]
   
   for i in d[major]:
       if int(i['courseNumber'])>= int(cnum) and int(i['courseNumber'])<= int(cnum)+100 :
           res.append(i['title'])
   return res

def classes_by_dep_course_number(major,cnum):
   try:
      d[major]
   except:
       return None
   res = [{}]
   for i in d[major]:
       if int(i['courseNumber'])== int(cnum):
           res.append(i['title'])
           return res
   return res
