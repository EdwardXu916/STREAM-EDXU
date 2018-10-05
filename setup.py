# Main

import energy_conver_tech

print('Version of energy_conver_tech.py {}.\n'.format(energy_conver_tech.__version__))

operand_setup_i = 1
while operand_setup_i != 0 and operand_setup_i <= 3:
    option_setup = int(input('Do you want to input ect, input "1": \n'))
    if option_setup == 1:
        energy_conver_tech.profile_ect()
    operand_setup_i += 1

exit('Exit')
