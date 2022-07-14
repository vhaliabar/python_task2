#!/usr/bin/env python3

import sys
lst_of_passwords = sys.argv[1]

def password_check(all_pass):
    result_list = []
    
    for passwd in all_pass.split(','):
        print(f'Testing... {passwd} ')        
        val = True
        if not any(char.isupper() for char in passwd) or not any(char.islower() for char in passwd):
            val = False     
                
        elif not any(char.isdigit() for char in passwd):
            val = False
        
        elif any(' ' in char for char in passwd):
            val = False
            
        elif not any(char in '*#+@' for char in passwd):
            val = False
        
        elif len(passwd) < 4 or len(passwd) > 6:
            val = False    
        
        elif val:
            result_list.append(passwd)
    print(f'\nFinal test result: ')   
    for result in result_list:
        print(result, end=',') 

#lst_of_passwords = 'Abc@1,a B1#,2w3E*,2We#3345' 
#Driver Code        
if __name__ == '__main__': password_check(lst_of_passwords)