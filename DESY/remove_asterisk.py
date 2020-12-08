input_file=open("events.txt","r")
output_file=open("desy_eventList_2018_AZh220_eemt_single_elec_trg.txt","w")
lines=input_file.readlines()
result=[]
result2=[]
output_file.write("run,lumi,evtid \n")
for x in lines:
    #result.append(x.split('*'))
    result = x.split('*')
    for i in result:
    #print(i)
        result2.append(i.strip())
        #print(result2)
    output_file.write(result2[2]+","+result2[3]+","+result2[4]+"\n")
    result2 = []     
input_file.close()
output_file.close()
#print(result)
