import struct, zlib, decimal

INT_16_SIZE = 2
INT_32_SIZE = 4

def to_int(b:bytes):
    "convert little endian bytes into unsigned int "
    return int.from_bytes(b, "little", signed=False)

def to_float(b:bytes):
    "convert little endian bytes into float "
    return struct.unpack('<f', b)[0] #little endian

def to_decimal(b:bytes):
    "convert little endian bytes into float with six digits "
    return decimal.Decimal('{0:.6f}'.format(struct.unpack('<f', b)[0])) #little endian

def to_b_int32(i:int):
    return i.to_bytes(length=INT_32_SIZE, byteorder='little', signed=False)

def to_b_int16(i:int):
    return i.to_bytes(length=INT_16_SIZE, byteorder='little', signed=False)

def unzlib_it(data: bytes):
    return zlib.decompress(data)

def zlib_it(data: bytes,compression: int):
    return zlib.compress(data,compression)

def file_read(file: str):
    '''
    Gets a file and return a byte array with his content
    '''
    with open(file, 'rb') as f:
        file_contents  = bytearray(f.read())
    return file_contents

def zero_fill_right_shift(val, n):
    return (val % 0x100000000) >> n

def get_offset(start_address : int, size : int, idx : int):
    return start_address + size * idx