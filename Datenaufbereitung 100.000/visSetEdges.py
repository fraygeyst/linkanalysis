i = 0
j = 1
k = 2
l = 3
m = 4
a = [0	,1	,2	,3	,4	,5	,20	,7	,8	,9	,10	,11	,12	,5	,13	,14	,15	,16	,216,9	,167,15	,16	,17	,18	,19	,20	,15	,21	,22	,23	,24	,25	,26	,27	,11	,31	,5	,31	,32	,33	,34	,35	,36	,37	,38	,39	,0	,13	,42	,0	,43	,44	,31	,45	,46	,15	,0	,47	,48	,49	,105,51	,52	,53	,54	,55	,56	,57	,58	,59	,60	,61	,62	,63	,64	,65	,66	,67	,68	,69	,70	,71	,72	,73	,74	,75	,76	,77	,0	,78	,79	,5	,80	,13	,81	,76	,82	,83	,84	,85	,86	,72	,15	,87	,88	,60	,89	,90	,15	,91	,92	,93	,94	,50	,95	,13	,96	,97	,0	,31	,98	,15	,99	,100,101,15	,0	,102,103,104,105,123,106,76	,108,15	,0	,109,110,111,112,15	,113,114,115,116,117,15	,0	,118,119,15	,120,121,122,123,124,125,26	,126,127,5	,128,96	,129,130,15	,29	,131,132,133,134,53	,135,84	,72	,136,6	,137,138,60	,139,140,141,142,15	,31	,143,144,145,146,147,148,149,150,151,152,15	,153,154,155,156,157,158,96	,159,31	,15	,96	,160,161,162,163,164,110,126,165,100,5	,166,167,15	,168,169,170,171,172,173,174,175,176,177,214,15	,178,10	,179,180,181,15	,182,183,184,185,186,15	,187,188,189,31	,15	,190,11	,45	,13	,30	,191,192,193,100,33	,194,195,196,197,126,41	,198,199,200,201,202,53	,203,204,205,15	,206,207,217,15	,60	,208,209,210,211,212,215,5	,213,28	,214,15	,30	,15	,0	,5	,13	,40	,]


for x in range (1,61):
    # print('Topic: '+ str(x))
    print('{"from": ' + str(a[i]) + ', "to": ' + str(a[j]) + "},")
    print('{"from": ' + str(a[i]) + ', "to": ' + str(a[k]) + "},")
    print('{"from": ' + str(a[i]) + ', "to": ' + str(a[l]) + "},")
    print('{"from": ' + str(a[i]) + ', "to": ' + str(a[m]) + "},")
    print('{"from": ' + str(a[j]) + ', "to": ' + str(a[k]) + "},")
    print('{"from": ' + str(a[j]) + ', "to": ' + str(a[l]) + "},")
    print('{"from": ' + str(a[j]) + ', "to": ' + str(a[m]) + "},")
    print('{"from": ' + str(a[k]) + ', "to": ' + str(a[l]) + "},")
    print('{"from": ' + str(a[k]) + ', "to": ' + str(a[m]) + "},")
    print('{"from": ' + str(a[l]) + ', "to": ' + str(a[m]) + "},")
    i = i + 5
    j = j + 5
    k = k + 5
    l = l + 5
    m = m + 5
    x = x + 1



