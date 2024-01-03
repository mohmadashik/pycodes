import time
import binascii

def time_in_hex():
    # Get the current time in seconds (floating-point number)
    current_time = time.time()
    print(f' current_time : {current_time}')

    # Convert the current time to milliseconds and cast it to an integer
    current_time_ms = int(current_time * 1000)
    print(f' current_time_ms : {current_time_ms}')

    # Convert the integer representation of time to a string
    current_time_ms_str = str(current_time_ms)
    print(f' current_time_ms_str : {current_time_ms_str}')

    # Encode the string as bytes using UTF-8 encoding
    t_s = current_time_ms_str.encode('utf-8')
    print(f' t_s : {t_s}')

    # Convert the bytes to a hexadecimal representation
    bts = binascii.hexlify(t_s).decode('utf-8')
    print(f' bts : {bts}')

    # Convert the hexadecimal representation to a list of integers
    bts_l = list(binascii.unhexlify(bts))
    print(f' bts_l : {bts_l}')

    print('finally')
    print(f' (bts_l,current_time_ms_str): {bts_l},{current_time_ms_str}')

    # Return the list of integers and the original string representation of time in milliseconds
    return bts_l, current_time_ms_str
time_in_hex()
