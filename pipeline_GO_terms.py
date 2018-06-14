
ref = open('input.txt', 'r')   #input file from step 1. Change name!!
info = open('go_id.txt', 'r')


gb = [] #list of the GB terms from input file
for l in ref:
    l=l.strip('\n')
    i = l[0]    #making sure to only pull GB term
    for i in l: #redundant
        gb.append(i)

ref.close()

go={}   #empty dict for filtered GB:GO
count= 0
for l in info:  #second input file
    l=l.strip('\n').split('\t')
    i = l[0]        #GB
    term = l[-1]    #GO
    cor = str(term + ';')
    if i in gb:     #if the GB term is in your filtered input file
        if go.has_key(i):
            go[i].append( cor )
        else:
            go[i] = [cor]
    else:
        count +=1   #count number of excluded GB's
info.close()

new_file = open('filtered_gbid_to_go.tab', 'w')     #your output file. feel free to change the name
new_file.write('V1' + '\t' + 'V2' + '\n')           #required header for most analyses

for i in go:
    new_file.write(i + '\t')
    keys = go[i]
    keyz = keys[:-1]        #select all GO except for last one
    for x in keys:
        new_file.write(x)   #making sure no spaces between terms
    last = keys[-1].rstrip(';') #making sure the last ; is removed
    new_file.write(last +'\n')


print count, ' GO terms excluded.'
