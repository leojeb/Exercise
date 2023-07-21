sig_str = input()
print(sig_str)
print(len(sig_str))

def get_max_signal(sig_str): 
    sig_list = []
    found_duplicated = False
    for i in range(len(sig_str)):
        c = sig_str[i]
        if i == 0: 
            sig_list.append(c)
            continue
        if i == len(sig_str) - 1: 
            if sig_str[i-1] == '1' and (not found_duplicated):
                sig_list[-1] = sig_list[-1] + '0' 
            print("final")
            continue
            
        print("序号", i)
        last_c = sig_str[i-1]
        next_c = sig_str[i+1]
        if c == '0':
            if last_c == '0' and next_c == '0': 
                continue 
            elif last_c == '0' and next_c != '0':
                found_duplicated = False
                sig_list.append(c)
            else :
                if not found_duplicated:
                    sig_list[-1] =  sig_list[-1] + c
                
        else:
            if found_duplicated: continue
            if last_c == '1' or next_c == '1':
                found_duplicated = True
                sig_list.pop()
            else:
                if not found_duplicated :
                    sig_list[-1] = sig_list[-1] + c
            
            
    sig_len_list = [len(sig) for sig in sig_list]
    max = sig_len_list[0]
    max_idx = 0
    for i in range(len(sig_len_list)):
        if sig_len_list[i] > max:
            max = sig_len_list[i]
            max_idx = i
    return sig_list[max_idx]
    
max_sig = get_max_signal(sig_str)
print(max_sig)
