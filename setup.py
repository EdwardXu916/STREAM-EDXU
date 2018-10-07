# Main

import energy_conver_tech
import energy_extract_tech
import energy_source

print('Version of energy_conver_tech.py {}.\n'.format(energy_conver_tech.__version__))

operand_setup_i = 1
while operand_setup_i != 0 and operand_setup_i <= 3:
    option_setup = int(input('Profile an energy conversion technology? input "1": \n'
                             'Profile an energy extraction technology? input "2": \n'))
    if option_setup == 1:
        energy_conver_tech.profile_ect()
    elif option_setup == 2:
        sun_1 = energy_source.Sun.create_input()
        eet_1 = energy_extract_tech.profile(sun_1)
        print('Heat of eet_1 from sun_1: {}'.format(eet_1.source))
        print('Heat of eet_1 from sun_1: {}'.format(eet_1.source.heat))
    operand_setup_i += 1

exit('Exit')
