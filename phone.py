def main():
    phone = '01923-616-285'
    print(phone[0:3])#print from 0 index to 3rd index
#First number is inclusive 2nd is exclusive '019'
    print(phone[:3])
#2nd is exclusive '019'
    print(phone[8:12])
#First inclusive '6-28'
    print(phone[8:])
#index -1 starts at the end of the string '-285' 
    print(phone[-4:])
    
main()