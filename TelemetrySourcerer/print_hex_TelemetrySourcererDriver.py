def HexView():
        i=0
        mybytes=0
        out=""
        with open('TelemetrySourcererDriver.sys', 'rb') as in_file:
                    while True:
                                    hexdata = in_file.read(1).hex()     # I like to read each bytes
                                    if len(hexdata) == 0:               # breaks loop once no more binary data is read
                                       print("\t\t\t" + out + "\nFINISHED printing " + str(mybytes) + " byte(s)")
                                       break
                                    out+=" 0x" + str(hexdata.upper()) + ","
                                    i+=1
                                    mybytes+=1
                                    if i==16: 
                                       print("\t\t\t"+out)
                                       out=""
                                       i=0
HexView()

