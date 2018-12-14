def parsenode(str):
    id,node,subrack,slot,board,port='','','','','',''
    strs=str.split('-')
    id = strs[0]
    index=0
    for tmp in strs[1:]:
        index+= 1
        if tmp.__contains__('子架'):
            node=node[0:node.__len__()-1]
            break
        else :
            node += tmp+'-'
    subrack=strs[index]
    slot=strs[index+1]
    board=strs[index+2]
    port=str[str.find('-',str.find(board))+1:]
    return id,node,subrack,slot,board,port

# str='800-关中环四张家堡-zhuyong-beiyong-子架1-4-11OMCA-2(收渭南主用800-0-13-OAU-MON)'
# id,node,subrack,slot,board,port=parsenode(str)
# print(id,node,subrack,slot,board,port)
# sou=id+'-'+node+'-'+subrack+'-'+slot+'-'+board+'-'+port
# print(sou)
# if str==sou:
#     print(True)
# else:
#     print(False)

#搜索本网元所有的线路板,对应的对端的线路板
