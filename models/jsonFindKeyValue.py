data = {
  "squadName" : "Super hero squad",
  "homeTown" : "Metro City",
  "formed" : 2016,
  "secretBase" : "Super tower",
  "active" : True,
  "members" : [
    {
      "name" : "Molecule Man",
      "age" : 29,
      "secretIdentity" : "Dan Jukes",
      "powers" : [
        "Radiation resistance",
        "Turning tiny",
        "Radiation blast"
      ]
    },
    {
      "name" : "Madame Uppercut",
      "age" : 39,
      "secretIdentity" : "Jane Wilson",
      "powers" : [
        "Million tonne punch",
        "Damage resistance",
        "Superhuman reflexes"
      ]
    },
    {
      "name" : "Eternal Flame",
      "age" : 1000000,
      "secretIdentity" : "Unknown",
      "powers" : [
        "Immortality",
        "Heat Immunity",
        "Inferno",
        "Teleportation",
        "Interdimensional travel"
      ]
    }
  ]
}

name = []
# 找出相對應的key,value
def getValue(key,value):
    if key == 'name' :
       name.append({
           'name' : value
       })

# 使用遞迴方式找尋想要資料
def findKeyValue(dictData):
    for key, value in dictData.items():
        if not(isinstance(value, (str,bool,int,float))):
            if isinstance(value, (list)):
                for idx , val in enumerate(value):
                    if isinstance(val, (str,bool,int,float)) :
                        getValue(key+'[' + str(idx) + ']',val)
                    else :
                        findKeyValue(val)
            if isinstance(value, (dict)):
                findKeyValue(value)
        else:
            getValue(key,value)

findKeyValue(data)
print(name)