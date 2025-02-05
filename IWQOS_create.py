import os
import hmac
import hashlib
import pickle
from Crypto.Cipher import AES
#keyword

#build
####10K-83
###20K--166
###40K-333
##80k--666
###160K--1333


#add
###### 2K 16
###### 4K 33
###### 8K 66
###### 16K 123
###### 32K 246

kw=["Accounting", "Financial_Planning", "Human_Resource", "Management Consulting", "Data Entry", "Project Management", "Transcription", "Web Research", "Customer Service", "Technical Support", "Data Extraction", "Data Visualization", "Machine Learning", "Animation", "Audio Production", "Motion Graphics", "Photography", "Information Security", "Contract Law","Criminal Law"]

for i in range(len(kw)):
    kw[i]=kw[i].encode(('utf-8'))
    if len(kw[i])>30:
        print("overflow")
    kw[i]=int.from_bytes(kw[i], byteorder='big')

for k in kw:
    print(k)
exit(0)
###############################################################任务数量##############################
each_kw_task_num=8

######build时的broker-kw-任务索引
#############broker1
bro1={}
for i in kw:
    bro1[i]=[]

for i in range(each_kw_task_num):
    for w in kw:
        bro1[w].append(os.urandom(32))

############broker2
bro2={}
for i in kw:
    bro2[i]=[]

for i in range(each_kw_task_num):
    for w in kw:
        bro2[w].append(os.urandom(32))

##########broker3
bro3={}
for i in kw:
    bro3[i]=[]

for i in range(each_kw_task_num):
    for w in kw:
        bro3[w].append(os.urandom(32))


########broker4

bro4={}
for i in kw:
    bro4[i]=[]

for i in range(each_kw_task_num):
    for w in kw:
        bro4[w].append(os.urandom(32))

########broker5

bro5={}
for i in kw:
    bro5[i]=[]

for i in range(each_kw_task_num):
    for w in kw:
        bro5[w].append(os.urandom(32))

########broker4

bro6={}
for i in kw:
    bro6[i]=[]

for i in range(each_kw_task_num):
    for w in kw:
        bro6[w].append(os.urandom(32))

bro7={}
for i in kw:
    bro7[i]=[]

for i in range(each_kw_task_num):
    for w in kw:
        bro7[w].append(os.urandom(32))


bro8={}
for i in kw:
    bro8[i]=[]

for i in range(each_kw_task_num):
    for w in kw:
        bro8[w].append(os.urandom(32))

bro9={}
for i in kw:
    bro9[i]=[]

for i in range(each_kw_task_num):
    for w in kw:
        bro9[w].append(os.urandom(32))

bro10={}
for i in kw:
    bro10[i]=[]

for i in range(each_kw_task_num):
    for w in kw:
        bro10[w].append(os.urandom(32))

bro11={}
for i in kw:
    bro11[i]=[]

for i in range(each_kw_task_num):
    for w in kw:
        bro11[w].append(os.urandom(32))

bro12={}
for i in kw:
    bro12[i]=[]

for i in range(each_kw_task_num):
    for w in kw:
        bro12[w].append(os.urandom(32))

bro13 = {}
for i in kw:
    bro13[i] = []

for i in range(each_kw_task_num):
    for w in kw:
        bro13[w].append(os.urandom(32))

bro14 = {}
for i in kw:
    bro14[i] = []

for i in range(each_kw_task_num):
    for w in kw:
        bro14[w].append(os.urandom(32))




####生成broker
broker=[]
broker.append(bro1)
broker.append(bro2)
broker.append(bro3)
broker.append(bro4)
broker.append(bro5)
broker.append(bro6)
# broker.append(bro7)
# broker.append(bro8)
# broker.append(bro9)
# broker.append(bro10)
# broker.append(bro11)
# broker.append(bro12)
# broker.append(bro13)
# broker.append(bro14)



f_broker=open('./data/broker.txt','wb')
pickle.dump(broker, f_broker, 0)
f_broker.close()



model = AES.MODE_ECB

############################################################################生成授权
#每个 broker 两个 master key + secret key
#broker1  生成k
master_key1_b1=hmac.new(b'b1master1', digestmod='md5').digest()
master_key2_b1=hmac.new(b'b1master2', digestmod='md5').digest()
secret_key_b1=hmac.new(b'b1secret', digestmod='md5').digest()
Ib1='broker1ID0000000'
IDb1=Ib1.encode('utf-8')



#aes1 = AES.new(master_key1_b1, model)
Fb1pie = hmac.new(master_key1_b1, IDb1, digestmod=hashlib.sha256).digest()
Fb1_1 = hmac.new(master_key2_b1, IDb1, digestmod=hashlib.sha256).digest()
Fb1_2 = hmac.new(secret_key_b1, IDb1, digestmod=hashlib.sha256).digest()

#Fb1pie=aes1.encrypt(IDb1)
#aes2 = AES.new(master_key2_b1, model)
#Fb1_1=aes2.encrypt(IDb1)
#aes3 = AES.new(secret_key_b1, model)
#Fb1_2=aes3.encrypt(IDb1)


#print("zheng", Fb1pie)
Fb1pie=int.from_bytes(Fb1pie, byteorder='big')
Fb1_1=int.from_bytes(Fb1_1, byteorder='big')
Fb1_2=int.from_bytes(Fb1_2, byteorder='big')
#Fb1piefan=(Fb1pie).to_bytes(16, byteorder="big", signed=True)
#print("fan",Fb1piefan)
b1=[Fb1pie, Fb1_1, Fb1_2]
#print(b1)

#broker2
master_key1_b2=hmac.new(b'b2master1', digestmod='md5').digest()
master_key2_b2=hmac.new(b'b2master2', digestmod='md5').digest()
secret_key_b2=hmac.new(b'b2secret', digestmod='md5').digest()
Ib2='broker2ID0000000'
IDb2=Ib2.encode('utf-8')


Fb2pie = hmac.new(master_key1_b2, IDb2, digestmod=hashlib.sha256).digest()
Fb2_1 = hmac.new(master_key2_b2, IDb2, digestmod=hashlib.sha256).digest()
Fb2_2 = hmac.new(secret_key_b2, IDb2, digestmod=hashlib.sha256).digest()


Fb2pie=int.from_bytes(Fb2pie, byteorder='big')
Fb2_1=int.from_bytes(Fb2_1, byteorder='big')
Fb2_2=int.from_bytes(Fb2_2, byteorder='big')
b2=[Fb2pie, Fb2_1, Fb2_2]
#print(b2)


#broker3
master_key1_b3=hmac.new(b'b3master1', digestmod='md5').digest()
master_key2_b3=hmac.new(b'b3master2', digestmod='md5').digest()
secret_key_b3=hmac.new(b'b3secret', digestmod='md5').digest()
Ib3='broker3ID0000000'
IDb3=Ib3.encode('utf-8')


Fb3pie = hmac.new(master_key1_b3, IDb3, digestmod=hashlib.sha256).digest()
Fb3_1 = hmac.new(master_key2_b3, IDb3, digestmod=hashlib.sha256).digest()
Fb3_2 = hmac.new(secret_key_b3, IDb3, digestmod=hashlib.sha256).digest()


Fb3pie=int.from_bytes(Fb3pie, byteorder='big')
Fb3_1=int.from_bytes(Fb3_1, byteorder='big')
Fb3_2=int.from_bytes(Fb3_2, byteorder='big')

b3=[Fb3pie, Fb3_1, Fb3_2]
#print(b3)



#broker4
master_key1_b4=hmac.new(b'b4master1', digestmod='md5').digest()
master_key2_b4=hmac.new(b'b4master2', digestmod='md5').digest()
secret_key_b4=hmac.new(b'b4secret', digestmod='md5').digest()
Ib4='broker4ID0000000'
IDb4=Ib4.encode('utf-8')


Fb4pie = hmac.new(master_key1_b4, IDb4, digestmod=hashlib.sha256).digest()
Fb4_1 = hmac.new(master_key2_b4, IDb4, digestmod=hashlib.sha256).digest()
Fb4_2 = hmac.new(secret_key_b4, IDb4, digestmod=hashlib.sha256).digest()

Fb4pie=int.from_bytes(Fb4pie, byteorder='big')
Fb4_1=int.from_bytes(Fb4_1, byteorder='big')
Fb4_2=int.from_bytes(Fb4_2, byteorder='big')

b4=[Fb4pie, Fb4_1, Fb4_2]
#print(b4)




#broker5
master_key1_b5=hmac.new(b'b5master1', digestmod='md5').digest()
master_key2_b5=hmac.new(b'b5master2', digestmod='md5').digest()
secret_key_b5=hmac.new(b'b5secret', digestmod='md5').digest()
Ib5='broker5ID0000000'
IDb5=Ib5.encode('utf-8')


Fb5pie = hmac.new(master_key1_b5, IDb5, digestmod=hashlib.sha256).digest()
Fb5_1 = hmac.new(master_key2_b5, IDb5, digestmod=hashlib.sha256).digest()
Fb5_2 = hmac.new(secret_key_b5, IDb5, digestmod=hashlib.sha256).digest()

Fb5pie=int.from_bytes(Fb5pie, byteorder='big')
Fb5_1=int.from_bytes(Fb5_1, byteorder='big')
Fb5_2=int.from_bytes(Fb5_2, byteorder='big')

b5=[Fb5pie, Fb5_1, Fb5_2]
#print(b5)


#broker6
master_key1_b6=hmac.new(b'b6master1', digestmod='md5').digest()
master_key2_b6=hmac.new(b'b6master2', digestmod='md5').digest()
secret_key_b6=hmac.new(b'b6secret', digestmod='md5').digest()
Ib6='broker6ID0000000'
IDb6=Ib6.encode('utf-8')

Fb6pie = hmac.new(master_key1_b6, IDb6, digestmod=hashlib.sha256).digest()
Fb6_1 = hmac.new(master_key2_b6, IDb6, digestmod=hashlib.sha256).digest()
Fb6_2 = hmac.new(secret_key_b6, IDb6, digestmod=hashlib.sha256).digest()


Fb6pie=int.from_bytes(Fb6pie, byteorder='big')
Fb6_1=int.from_bytes(Fb6_1, byteorder='big')
Fb6_2=int.from_bytes(Fb6_2, byteorder='big')

b6=[Fb6pie, Fb6_1, Fb6_2]
#print(b6)


#broker7

master_key1_b7=hmac.new(b'b7master1', digestmod='md5').digest()
master_key2_b7=hmac.new(b'b7master2', digestmod='md5').digest()
secret_key_b7=hmac.new(b'b7secret', digestmod='md5').digest()
Ib7='broker7ID0000000'
IDb7=Ib7.encode('utf-8')



#aes1 = AES.new(master_key1_b1, model)
Fb7pie = hmac.new(master_key1_b7, IDb7, digestmod=hashlib.sha256).digest()
Fb7_1 = hmac.new(master_key2_b7, IDb7, digestmod=hashlib.sha256).digest()
Fb7_2 = hmac.new(secret_key_b7, IDb7, digestmod=hashlib.sha256).digest()

#Fb1pie=aes1.encrypt(IDb1)
#aes2 = AES.new(master_key2_b1, model)
#Fb1_1=aes2.encrypt(IDb1)
#aes3 = AES.new(secret_key_b1, model)
#Fb1_2=aes3.encrypt(IDb1)


#print("zheng", Fb1pie)
Fb7pie=int.from_bytes(Fb7pie, byteorder='big')
Fb7_1=int.from_bytes(Fb7_1, byteorder='big')
Fb7_2=int.from_bytes(Fb7_2, byteorder='big')
#Fb1piefan=(Fb1pie).to_bytes(16, byteorder="big", signed=True)
#print("fan",Fb1piefan)
b7=[Fb7pie, Fb7_1, Fb7_2]

######b8


master_key1_b8=hmac.new(b'b8master1', digestmod='md5').digest()
master_key2_b8=hmac.new(b'b8master2', digestmod='md5').digest()
secret_key_b8=hmac.new(b'b8secret', digestmod='md5').digest()
Ib8='broker8ID0000000'
IDb8=Ib8.encode('utf-8')



#aes1 = AES.new(master_key1_b1, model)
Fb8pie = hmac.new(master_key1_b8, IDb8, digestmod=hashlib.sha256).digest()
Fb8_1 = hmac.new(master_key2_b8, IDb8, digestmod=hashlib.sha256).digest()
Fb8_2 = hmac.new(secret_key_b8, IDb8, digestmod=hashlib.sha256).digest()


Fb8pie=int.from_bytes(Fb8pie, byteorder='big')
Fb8_1=int.from_bytes(Fb8_1, byteorder='big')
Fb8_2=int.from_bytes(Fb8_2, byteorder='big')


b8=[Fb8pie, Fb8_1, Fb8_2]


######b9


master_key1_b7=hmac.new(b'b9master1', digestmod='md5').digest()
master_key2_b7=hmac.new(b'b9master2', digestmod='md5').digest()
secret_key_b7=hmac.new(b'b9secret', digestmod='md5').digest()
Ib9='broker9ID0000000'
IDb9=Ib9.encode('utf-8')



#aes1 = AES.new(master_key1_b1, model)
Fb9pie = hmac.new(master_key1_b7, IDb9, digestmod=hashlib.sha256).digest()
Fb9_1 = hmac.new(master_key2_b7, IDb9, digestmod=hashlib.sha256).digest()
Fb9_2 = hmac.new(secret_key_b7, IDb9, digestmod=hashlib.sha256).digest()


Fb9pie=int.from_bytes(Fb9pie, byteorder='big')
Fb9_1=int.from_bytes(Fb9_1, byteorder='big')
Fb9_2=int.from_bytes(Fb9_2, byteorder='big')


b9=[Fb9pie, Fb9_1, Fb9_2]



######b10


master_key1_b10=hmac.new(b'b10master1', digestmod='md5').digest()
master_key2_b10=hmac.new(b'b10master2', digestmod='md5').digest()
secret_key_b10=hmac.new(b'b10secret', digestmod='md5').digest()
Ib10='broker10ID0000000'
IDb10=Ib10.encode('utf-8')



#aes1 = AES.new(master_key1_b1, model)
Fb10pie = hmac.new(master_key1_b10, IDb10, digestmod=hashlib.sha256).digest()
Fb10_1 = hmac.new(master_key2_b10, IDb10, digestmod=hashlib.sha256).digest()
Fb10_2 = hmac.new(secret_key_b10, IDb10, digestmod=hashlib.sha256).digest()


Fb10pie=int.from_bytes(Fb10pie, byteorder='big')
Fb10_1=int.from_bytes(Fb10_1, byteorder='big')
Fb10_2=int.from_bytes(Fb10_2, byteorder='big')


b10=[Fb10pie, Fb10_1, Fb10_2]


######b11


master_key1_b11=hmac.new(b'b11master1', digestmod='md5').digest()
master_key2_b11=hmac.new(b'b11master2', digestmod='md5').digest()
secret_key_b11=hmac.new(b'b11secret', digestmod='md5').digest()
Ib11='broker11ID0000000'
IDb11=Ib11.encode('utf-8')



#aes1 = AES.new(master_key1_b1, model)
Fb11pie = hmac.new(master_key1_b11, IDb11, digestmod=hashlib.sha256).digest()
Fb11_1 = hmac.new(master_key2_b11, IDb11, digestmod=hashlib.sha256).digest()
Fb11_2 = hmac.new(secret_key_b11, IDb11, digestmod=hashlib.sha256).digest()


Fb11pie=int.from_bytes(Fb11pie, byteorder='big')
Fb11_1=int.from_bytes(Fb11_1, byteorder='big')
Fb11_2=int.from_bytes(Fb11_2, byteorder='big')


b11=[Fb11pie, Fb11_1, Fb11_2]


#########b12


master_key1_b12=hmac.new(b'b12master1', digestmod='md5').digest()
master_key2_b12=hmac.new(b'b12master2', digestmod='md5').digest()
secret_key_b12=hmac.new(b'b12secret', digestmod='md5').digest()
Ib12='broker12ID0000000'
IDb12=Ib12.encode('utf-8')



#aes1 = AES.new(master_key1_b1, model)
Fb12pie = hmac.new(master_key1_b12, IDb12, digestmod=hashlib.sha256).digest()
Fb12_1 = hmac.new(master_key2_b12, IDb12, digestmod=hashlib.sha256).digest()
Fb12_2 = hmac.new(secret_key_b12, IDb12, digestmod=hashlib.sha256).digest()


Fb12pie=int.from_bytes(Fb12pie, byteorder='big')
Fb12_1=int.from_bytes(Fb12_1, byteorder='big')
Fb12_2=int.from_bytes(Fb12_2, byteorder='big')


b12=[Fb12pie, Fb12_1, Fb12_2]

###b13

master_key1_b13=hmac.new(b'b13master1', digestmod='md5').digest()
master_key2_b13=hmac.new(b'b13master2', digestmod='md5').digest()
secret_key_b13=hmac.new(b'b13secret', digestmod='md5').digest()
Ib13='broker13ID0000000'
IDb13=Ib13.encode('utf-8')



#aes1 = AES.new(master_key1_b1, model)
Fb13pie = hmac.new(master_key1_b13, IDb13, digestmod=hashlib.sha256).digest()
Fb13_1 = hmac.new(master_key2_b13, IDb13, digestmod=hashlib.sha256).digest()
Fb13_2 = hmac.new(secret_key_b13, IDb13, digestmod=hashlib.sha256).digest()


Fb13pie=int.from_bytes(Fb13pie, byteorder='big')
Fb13_1=int.from_bytes(Fb13_1, byteorder='big')
Fb13_2=int.from_bytes(Fb13_2, byteorder='big')


b13=[Fb13pie, Fb13_1, Fb13_2]


###b14

master_key1_b14=hmac.new(b'b14master1', digestmod='md5').digest()
master_key2_b14=hmac.new(b'b14master2', digestmod='md5').digest()
secret_key_b14=hmac.new(b'b14secret', digestmod='md5').digest()
Ib14='broker14ID0000000'
IDb14=Ib14.encode('utf-8')



#aes1 = AES.new(master_key1_b1, model)
Fb14pie = hmac.new(master_key1_b14, IDb14, digestmod=hashlib.sha256).digest()
Fb14_1 = hmac.new(master_key2_b14, IDb14, digestmod=hashlib.sha256).digest()
Fb14_2 = hmac.new(secret_key_b14, IDb14, digestmod=hashlib.sha256).digest()


Fb14pie=int.from_bytes(Fb14pie, byteorder='big')
Fb14_1=int.from_bytes(Fb14_1, byteorder='big')
Fb14_2=int.from_bytes(Fb14_2, byteorder='big')


b14=[Fb14pie, Fb14_1, Fb14_2]







# broker_key=[b1,b2]

# broker_key=[b1,b2,b3,b4]
#
broker_key=[b1,b2,b3,b4,b5,b6]

# broker_key=[b1,b2,b3,b4,b5,b6,b7,b8]
# #
# broker_key=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10]

# broker_key=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12]

# broker_key=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14]




# print(broker_key)

f_broker_key=open('./data/broker_key.txt','wb')
pickle.dump(broker_key, f_broker_key, 0)
f_broker_key.close()





##############################添加索引时的broker-kw-任务索引
addeach_kw_task_num=1
#############broker14
addbro1={}
for i in kw:
    addbro1[i]=[]

# for i in range(addeach_kw_task_num):
#     for w in kw:
#         addbro1[w].append(os.urandom(32))



for i in range(addeach_kw_task_num):
    addbro1[308787214124473614167655].append(os.urandom(32))
    # addbro1[6133736384721188680745832161050472860970599].append(os.urandom(32))
    # addbro1[1469637038130182918335437370188645].append(os.urandom(32))
    # addbro1[322918641029749419569785].append(os.urandom(32))
    # addbro1[27047760750386508672659514216].append(os.urandom(32))

############broker2
addbro2={}
for i in kw:
    addbro2[i]=[]

# for i in range(addeach_kw_task_num):
#     for w in kw:
#         addbro2[w].append(os.urandom(32))

for i in range(addeach_kw_task_num):
    # addbro2[308787214124473614167655].append(os.urandom(32))
    # addbro2[6133736384721188680745832161050472860970599].append(os.urandom(32))
    addbro2[1469637038130182918335437370188645].append(os.urandom(32))
    # addbro2[322918641029749419569785].append(os.urandom(32))
    # addbro2[27047760750386508672659514216].append(os.urandom(32))

##########broker3
addbro3={}
for i in kw:
    addbro3[i]=[]

# for i in range(addeach_kw_task_num):
#     for w in kw:
#         addbro3[w].append(os.urandom(32))

for i in range(addeach_kw_task_num):
    # addbro3[308787214124473614167655].append(os.urandom(32))
    addbro3[6133736384721188680745832161050472860970599].append(os.urandom(32))
    # addbro3[1469637038130182918335437370188645].append(os.urandom(32))
    # addbro3[322918641029749419569785].append(os.urandom(32))
    # addbro3[27047760750386508672659514216].append(os.urandom(32))

########broker4

addbro4={}
for i in kw:
    addbro4[i]=[]

# for i in range(addeach_kw_task_num):
#     for w in kw:
#         addbro4[w].append(os.urandom(32))


for i in range(addeach_kw_task_num):
    # addbro4[308787214124473614167655].append(os.urandom(32))
    addbro4[6133736384721188680745832161050472860970599].append(os.urandom(32))
    # addbro4[1469637038130182918335437370188645].append(os.urandom(32))
    # addbro4[322918641029749419569785].append(os.urandom(32))
    # addbro4[27047760750386508672659514216].append(os.urandom(32))

########broker5

addbro5={}
for i in kw:
    addbro5[i]=[]

# for i in range(addeach_kw_task_num):
#     for w in kw:
#         addbro5[w].append(os.urandom(32))

for i in range(addeach_kw_task_num):
    # addbro5[308787214124473614167655].append(os.urandom(32))
    addbro5[6133736384721188680745832161050472860970599].append(os.urandom(32))
    # addbro5[1469637038130182918335437370188645].append(os.urandom(32))
    # addbro5[322918641029749419569785].append(os.urandom(32))
    # addbro5[27047760750386508672659514216].append(os.urandom(32))

########broker6

addbro6={}
for i in kw:
    addbro6[i]=[]

for i in range(addeach_kw_task_num):
    # addbro6[308787214124473614167655].append(os.urandom(32))
    addbro6[6133736384721188680745832161050472860970599].append(os.urandom(32))
    # addbro6[1469637038130182918335437370188645].append(os.urandom(32))
    # addbro6[322918641029749419569785].append(os.urandom(32))
    # addbro6[27047760750386508672659514216].append(os.urandom(32))

addbro7={}
for i in kw:
    addbro7[i]=[]

for i in range(addeach_kw_task_num):
    # addbro7[308787214124473614167655].append(os.urandom(32))
    addbro7[1469637038130182918335437370188645].append(os.urandom(32))
    addbro7[322918641029749419569785].append(os.urandom(32))
    addbro7[27047760750386508672659514216].append(os.urandom(32))




addbro8={}
for i in kw:
    addbro8[i]=[]

for i in range(addeach_kw_task_num):
    addbro8[308787214124473614167655].append(os.urandom(32))
    # addbro8[6133736384721188680745832161050472860970599].append(os.urandom(32))
    # addbro8[1469637038130182918335437370188645].append(os.urandom(32))
    # addbro8[322918641029749419569785].append(os.urandom(32))
    # addbro8[27047760750386508672659514216].append(os.urandom(32))

addbro9={}
for i in kw:
    addbro9[i]=[]

for i in range(addeach_kw_task_num):
    addbro9[308787214124473614167655].append(os.urandom(32))




addbro10={}
for i in kw:
    addbro10[i]=[]

for i in range(addeach_kw_task_num):
    addbro10[308787214124473614167655].append(os.urandom(32))



addbro11={}
for i in kw:
    addbro11[i]=[]

for i in range(addeach_kw_task_num):
    addbro11[308787214124473614167655].append(os.urandom(32))


addbro12={}
for i in kw:
    addbro12[i]=[]

for i in range(addeach_kw_task_num):
    addbro12[308787214124473614167655].append(os.urandom(32))

addbro13={}
for i in kw:
    addbro13[i]=[]

for i in range(addeach_kw_task_num):
    addbro13[308787214124473614167655].append(os.urandom(32))


addbro14={}
for i in kw:
    addbro14[i]=[]

for i in range(addeach_kw_task_num):
    addbro14[308787214124473614167655].append(os.urandom(32))



####生成broker
addbrokertask=[]
addbrokertask.append(addbro1)
addbrokertask.append(addbro2)
addbrokertask.append(addbro3)
addbrokertask.append(addbro4)
addbrokertask.append(addbro5)
addbrokertask.append(addbro6)
# addbrokertask.append(addbro7)
# addbrokertask.append(addbro8)
# addbrokertask.append(addbro9)
# addbrokertask.append(addbro10)
# addbrokertask.append(addbro11)
# addbrokertask.append(addbro12)
# addbrokertask.append(addbro13)
# addbrokertask.append(addbro14)

f_addbrokertask=open('./data/addbrokertask.txt','wb')
pickle.dump(addbrokertask, f_addbrokertask, 0)
f_addbrokertask.close()



