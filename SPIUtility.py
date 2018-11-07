import numpy as np

BASE_ADDRESS = 0x80000000
ZERO_ADDRESS = 0x00
OP_READ_32          = 0x32
OP_WRITE_32         = 0x33
OP_READ_8           = 0x20
OP_WRITE_8          = 0x24
OP_READ_BURST_8     = 0x22
OP_WRITE_BURST_8    = 0x26
OP_READ_IMAGE_8     = 0x50

########## Address
def resetDefaultAddress():
    #combine opcode +address +image_data_listlist -> tx_data
    addr = 0x20000008
    addr = [int(addr >> i & 0xff) for i in (24,16,8,0)] 
    
    tx_data = [OP_WRITE_32]
    tx_data.extend(addr) 
    data = [0x80,0,0,0]
    for i in range(len(data)):
        tx_data.append(int(data[i]))
    print("[resetDefaultAddress] tx_data:", tx_data)
    return tx_data

def setDefaultAddress(addr):
    #combine opcode +address +image_data_listlist -> tx_data
    addr = [int(addr >> i & 0xff) for i in (24,16,8,0)] 
    
    tx_data = [OP_WRITE_32]
    tx_data.extend(addr) 
    data = [0x80,0,0,0]
    for i in range(len(data)):
        tx_data.append(int(data[i]))
    print("[setDefaultAddress] tx_data:", tx_data)
    return tx_data

def getDefaultAddress():
    #combine opcode +address +image_data_listlist -> tx_data
    addr = 0x20000008
    addr = [int(addr >> i & 0xff) for i in (24,16,8,0)] 
    
    tx_data = [OP_READ_32]
    tx_data.extend(addr) 
    data = [0,0,0,0]
    for i in range(len(data)):
        tx_data.append(int(data[i]))
    print("[getDefaultAddress] tx_data:", tx_data)
    return tx_data


########## mode 0/3
def setSPIMode0():
    #combine opcode +address +image_data_listlist -> tx_data
    addr = 0x20000000
    addr = [int(addr >> i & 0xff) for i in (24,16,8,0)] 
    
    tx_data = [OP_WRITE_32]
    tx_data.extend(addr) 
    data = [0,0,0,0]
    for i in range(len(data)):
        tx_data.append(int(data[i]))
    print("[setSPIMode0] tx_data:", tx_data)
    return tx_data

def setSPIMode3():
    #combine opcode +address +image_data_listlist -> tx_data
    addr = 0x20000000
    addr = [int(addr >> i & 0xff) for i in (24,16,8,0)] 
    
    tx_data = [OP_WRITE_32]
    tx_data.extend(addr) 
    data = [1,1,1,1]
    for i in range(len(data)):
        tx_data.append(int(data[i]))
    print("[setSPIMode3] tx_data:", tx_data)
    return tx_data

def getSPIMode():
    addr = 0x20000000
    addr = [int(addr >> i & 0xff) for i in (24,16,8,0)] 

    rx_data = [OP_READ_32]
    rx_data.extend(addr) 

    for i in range(4):
        rx_data.append(0)
    print("[getSPIMode] rx_data:", rx_data)
    return rx_data;

########## Single32
def readSingle32(address, data_length):
    #combine opcode +address +zero_padding -> rx_data
    addr = BASE_ADDRESS + address
    #print("[readSingle32] address :" + hex(addr))
    addr = [int(addr >> i & 0xff) for i in (24,16,8,0)] 

    rx_data = [OP_READ_32]
    rx_data.extend(addr) 

    for i in range(data_length):
        rx_data.append(0)
    #print("rx_data:", rx_data)
    return rx_data

def writeSingle32(address, data):
    #combine opcode +address +image_data_listlist -> tx_data
    addr = BASE_ADDRESS + address
    #print("[writeSingle32] address :" + hex(addr))
    addr = [int(addr >> i & 0xff) for i in (24,16,8,0)] 
    
    tx_data = [OP_WRITE_32]
    tx_data.extend(addr) 

    for i in range(len(data)):
        tx_data.append(int(data[i]))
    #print("tx_data:", tx_data)
    return tx_data

########## Single8
def readSingle8(address):
    #combine opcode +address +zero_padding -> rx_data
    addr = ZERO_ADDRESS + address
    print("[readSingle8] address :" + hex(addr))

    rx_data = [OP_READ_8, addr, 0x00] 
    print("rx_data:", rx_data)
    return rx_data

def writeSingle8(address, data):
    #combine opcode +address +image_data_listlist -> tx_data
    addr = ZERO_ADDRESS + address
    #print("[writeSingle8] address :" + hex(addr))
    
    tx_data = [OP_WRITE_8, addr, data]
    #print("tx_data:", tx_data)
    return tx_data

########## Burst8
def readBurst8(address, data_length):
    #combine opcode +address +zero_padding -> rx_data
    addr = ZERO_ADDRESS + address
    #print("[readBurst8] address :" + hex(addr))
    
    rx_data = [OP_READ_BURST_8, addr]

    for i in range(data_length):
        rx_data.append(0)
    #print("rx_data:", rx_data)
    return rx_data

def writeBurst8(address, data):
    #combine opcode +address +image_data_listlist -> tx_data
    addr = ZERO_ADDRESS + address
    #print("[writeBurst8] address :" + hex(addr))
    
    tx_data = [OP_WRITE_BURST_8, addr]

    for i in range(len(data)):
        tx_data.append(int(data[i]))
    #print("tx_data:", tx_data)
    return tx_data

########## Image
def readImage(data_length):
    #combine opcode +address +zero_padding -> rx_data
    rx_data = [OP_READ_IMAGE_8]

    for i in range(data_length):
        rx_data.append(0)
    #print("rx_data:", rx_data)
    return rx_data
 