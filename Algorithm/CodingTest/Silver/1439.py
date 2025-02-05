def is_all_same(bit) :
    if all(b == '1' for b in bit) :
        return True
    elif all(b == '0' for b in bit) :
        return True
    else :
        return False

bit = input("")

if is_all_same(bit) :
    print(0)
else :
    bit_zero = bit.split("1")
    bit_zero = [z for z in bit_zero if z != ""]
    bit_one = bit.split("0")
    bit_one = [o for o in bit_one if o != ""]

    count = 0
    if len(bit_zero) > len(bit_one) :
        for one in bit_one :
            for o in one :
                o = "0"
            count += 1
    else :
        for zero in bit_zero :
            for z in zero :
                z = "1"
            count += 1
    
    print(count)