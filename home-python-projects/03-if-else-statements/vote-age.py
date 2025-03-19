Mayengua = 48
Stanlau = 25
Peturksbouipo = 16 

def voting_age():
    
    user_input = int(input('How old are you: '))
    
    if user_input >= Peturksbouipo :
        print('You can vote in Peturksbouipo where the voting age is  ' + str(Peturksbouipo))
    else:
        print('You cannot vote in Peturksbouipo where the voting age is  ' + str(Peturksbouipo))
        
    if user_input >= Stanlau :
        print('You can vote in stanlau where the voting age is ' + str(Stanlau))
    else:
        print('You cannot vote in stanlau where the voting age is ' + str(Stanlau))
        
    if(user_input >= Mayengua):
        print('You can vote in Mayengua where the voting age is ' + str(Mayengua))
    else:
        print('You cannot vote in Mayengua where the voting age is ' + str(Mayengua))
        
        
voting_age()
if __name__ == "main":
    voting_age()