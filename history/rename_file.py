import os

folder=os.path.join(os.getcwd(),"strategicregions")
file:list = os.listdir(folder)



 # Lettere maiuscole
special_characters:list = ['À', 'Á', 'Â', 'Ã', 'Ä', 'Å', 'Ā', 'Ă', 'Ą', 'Æ', 'Ç', 'Ć', 'Č', 'Ď', 'Đ','È', 'É', 'Ê', 'Ë', 'Ē', 'Ė', 'Ę', 'Ě', 'Ĕ','Ģ', 'Ğ','Î', 'Í', 'Ì', 'Į', 'Ī', 'Ï','Ķ','Ł', 'Ļ', 'Ĺ','Ň', 'Ņ', 'Ń', 'Ñ','Õ', 'Ô', 'Ó', 'Ò', 'Ő', 'Ø', 'Ö', 'Œ','Ŕ', 'Ř','Ś', 'Š', 'Ş','Þ', 'Ť', 'Ț', 'Ţ','Ü', 'Û', 'Ú', 'Ù', 'Ų', 'Ű', 'Ů', 'Ū','Ý', 'Ÿ','Ź', 'Ż', 'Ž']    

# Lettere minuscole
special_characters_2:list = ['à', 'á', 'â', 'ã', 'ä', 'å', 'ā', 'ă', 'ą', 'æ', 'ç', 'ć', 'č', 'ď', 'đ', 'è', 'é', 'ê', 'ë', 'ē', 'ė', 'ę', 'ě', 'ĕ', 'ģ', 'ğ', 'î', 'í', 'ì', 'į', 'ī', 'ï', 'ķ', 'ł', 'ļ', 'ĺ', 'ň', 'ņ', 'ń', 'ñ', 'õ', 'ô', 'ó', 'ò', 'ő', 'ø', 'ö', 'œ', 'ŕ', 'ř', 'ś', 'š', 'ş', 'þ', 'ť', 'ț', 'ţ', 'ü', 'û', 'ú', 'ù', 'ų', 'ű', 'ů', 'ū', 'ý', 'ÿ', 'ź', 'ż', 'ž']
new_names:list=[]
    
def char_map(char):
    if char in special_characters[0:10]:
        return "A"
    elif char in special_characters_2[0:10]:
        return "a"
    
    if char in special_characters[10:13]:
        return "C"
    elif char in special_characters_2[10:13]:
        return "c"
    
    if char in special_characters[13:15]:
        return "D"
    elif char in special_characters_2[13:15]:
        return "d"
    
    if char in special_characters[15:24]:
        return "E"
    elif char in special_characters_2[15:24]:
        return "e"
    
    if char in special_characters[24:26]:
        return "G"
    elif char in special_characters_2[24:26]:
        return "g"
    
    if char in special_characters[26:32]:
        return "I"
    elif char in special_characters_2[26:32]:
        return "i"

    if char in special_characters[32:33]:
        return "K"
    elif char in special_characters_2[26:33]:
        return "k"

    if char in special_characters[33:36]:
        return "L"
    elif char in special_characters_2[33:36]:
        return "l"
    
    if char in special_characters[36:40]:
        return "N"
    elif char in special_characters_2[36:40]:
        return "n"
    
    if char in special_characters[40:47]:
        return "O"
    elif char in special_characters_2[40:47]:
        return "o"

    if char in special_characters[47:48]:
        return "OE"
    elif char in special_characters_2[47:48]:
        return "oe"
    
    if char in special_characters[48:50]:
        return "R"
    elif char in special_characters_2[48:50]:
        return "r"
    
    if char in special_characters[50:53]:
        return "S"
    elif char in special_characters_2[50:53]:
        return "s"
    
    if char in special_characters[53:54]:
        return "P"
    elif char in special_characters_2[53:54]:
        return "p"

    if char in special_characters[54:57]:
        return "T"
    elif char in special_characters_2[54:57]:
        return "t"
    
    if char in special_characters[57:65]:
        return "U"
    elif char in special_characters_2[57:65]:
        return "u"

    if char in special_characters[65:67]:
        return "Y"
    elif char in special_characters_2[65:67]:
        return "y"

    if char in special_characters[67:70]:
        return "Z"
    elif char in special_characters_2[67:70]:
        return "z"
    


def replace_chars(str:str):
    out = ""
    for c in str:
        if (c in special_characters) or (c in special_characters_2):
            out += char_map(c)
        else:
            out += c

    return out

for f in file:
    os.rename(os.path.join(folder,f),os.path.join(folder,replace_chars(f)))  
