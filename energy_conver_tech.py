# Class Definition of Energy Conversion Technology
# Version 1.2, Edward, 181004

__version__ = 1.2

if __name__ == '__main__':
    print('!!! energy_conver_tech.py is being run by itself.\n')
else:
    print('!!! energy_conver_tech.py is imported from another file.\n')


class EnergyConverTech:
    """Class Definition of Energy Conversion Technology"""
    number_ect = 0

    def __init__(self, identifier, name, output):
        self.id = identifier
        self.name = name
        self.type = output  # if "1", Energy2Elec; if "2", Energy2Heat
        EnergyConverTech.number_ect += 1

    def print(self):
        """Print the common feature of energy conversion technology"""
        type_text = ["Energy to Elec", "Energy to Heat", "Energy to Elec and Heat"]
        print('Energy Conversion Technology: {}, type: {}, id: {},'
              .format(self.name, type_text[self.type], self.id), end=" ")

    @classmethod
    def print_number(cls):
        print('Database have {} type(s) of energy conversion technology'.format(EnergyConverTech.number_ect))


class Energy2ElecConverter(EnergyConverTech):
    """Class Definition of Energy to Electricity Technology in Energy Conversion Technology"""
    number = 0

    def __init__(self, identifier, name, output, efficiency):
        EnergyConverTech.__init__(self, identifier, name, output)
        self.efficiency = efficiency
        Energy2ElecConverter.number += 1
        print('You have profiled a new energy to electricity technology. \n')
        Energy2ElecConverter.print_number()

    def print(self):
        """Print the feature of energy to electricity conversion technology"""
        EnergyConverTech.print(self)
        print('efficiency: {}.\n'.format(self.efficiency))

    @classmethod
    def print_number(cls):
        print('Number of profiled energy to electricity converters is {}.'.format(Energy2ElecConverter.number))

    @classmethod
    def create_input(cls, identifier_ect):
        print('You are profiling a new product, which can convert energy to electricity.')
        return cls(identifier_ect,
                   input('Name: '),
                   int(1),
                   int(input('Efficiency(%): '))
                   )


class Energy2HeatConverter(EnergyConverTech):
    """Class Definition of Energy to Heat Technology in Energy Conversion Technology"""
    number = 0

    def __init__(self, identifier, name, output, efficiency):
        EnergyConverTech.__init__(self, identifier, name, output)
        self.efficiency = efficiency
        Energy2HeatConverter.number += 1
        print('You have profiled a new energy to heat tech. \n'
              'Number of profiled energy to heat technology is {}. \n'.format(Energy2HeatConverter.number))

    def print(self):
        """Print the feature of energy to heat conversion technology"""
        EnergyConverTech.print(self)
        print('efficiency: {}.\n'.format(self.efficiency))

    @classmethod
    def create_input(cls, identifier_ect):
        print('You are profiling a new product, which can convert energy to heat.')
        return cls(identifier_ect,
                   input('Name: '),
                   int(2),
                   int(input('Efficiency(%): '))
                   )


class Energy2ElecHeatConverter(EnergyConverTech):
    """Class Definition of Energy to Electricity & Heat Technology in Energy Conversion Technology"""
    number = 0

    def __init__(self, identifier, name, output, efficiency_e2e, efficiency_e2h):
        EnergyConverTech.__init__(self, identifier, name, output)
        self.efficiency_e2e = efficiency_e2e
        self.efficiency_e2h = efficiency_e2h
        Energy2ElecHeatConverter.number += 1
        print('You have profiled a new energy to electricity and heat technology. \n'
              'Number of profiled energy to electricity and heat technology is {}. \n'
              .format(Energy2ElecHeatConverter.number))

    def print(self):
        """Print the feature of energy to electricity conversion technology"""
        EnergyConverTech.print(self)
        print('e2e efficiency: {}, e2h: efficiency {}. \n'.format(self.efficiency_e2e, self.efficiency_e2h))

    @classmethod
    def create_input(cls, identifier_ect):
        print('You are profiling a new product, which can convert energy to electricity and heat.')
        return cls(identifier_ect,
                   input('Name: '),
                   int(3),
                   int(input('Energy to Electricity Efficiency(%): ')),
                   int(input('Energy to Heat Efficiency(%): '))
                   )


# Initialize default energy technology.
identifier_ect = 'eg_001'
eg_001 = Energy2ElecConverter(identifier_ect, 'Electric Generator 001', 1, 50)
electricGenerators = {'eg_001': eg_001}
identifier_ect = 'he_001'
he_001 = Energy2HeatConverter(identifier_ect, 'Heat Exchanger 001', 2, 50)
heatExchangers = {'he_001': he_001}
identifier_ect = 'chp_001'
chp_001 = Energy2ElecHeatConverter(identifier_ect, 'Combined Heat Power 001', 3, 20, 30)
combinedHeatPowers = {'chp_001': chp_001}
identifier_ect = 'exit'  # Initialize the value of identifier_ect


def check_identifier_ect(identifier_ect):
    """Check if the input identifier already exits."""
    operand_ect_m = 1
    if identifier_ect == 'exit':
        operand_ect_m = 0
    else:
        for all_identifier_ect in {**electricGenerators, **heatExchangers, **combinedHeatPowers}:
            if identifier_ect == all_identifier_ect:
                operand_ect_m = 2
                break
    return operand_ect_m


def profile_ect():
    """Input energy conversion technology from terminal."""
    operand_ect_i = 1
    operand_ect_j = 1
    while operand_ect_i <= 3:
        identifier_ect = input('Do you want profile a new model for energy conversion technology? \n'
                               'Input ID first, or input "exit" to main menu: \n')
        operand_ect_m = check_identifier_ect(identifier_ect)
        if operand_ect_m == 1:
            while operand_ect_j != 0 and operand_ect_j <= 10:
                operand_ect_n = input('Then, input number with following reference to profile '
                                      'a certain type of technology:\n'
                                      'Or input "exit" to exit to main menu. \n'
                                      '1. Profile a product can converse energy to electricity. \n'
                                      ' 1.1 Electric Generator \n'
                                      '2. Profile a product can converse energy to heat. \n'
                                      ' 2.1 Heat Exchanger \n'
                                      '3. Profile a product can converse energy to electricity and heat. \n'
                                      ' 3.1 Combined Heat and Power Plant \n')
                if operand_ect_n == '1.1':
                    electricGenerators[identifier_ect] = Energy2ElecConverter.create_input(identifier_ect)
                    print('The energy to electricity converter profiled is a electric generator.\n')
                    electricGenerators[identifier_ect].print()
                    for electricGenerator in electricGenerators.items():
                        print(electricGenerator)
                    break
                elif operand_ect_n == '2.1':
                    heatExchangers[identifier_ect] = Energy2HeatConverter.create_input(identifier_ect)
                    print('You have profiled a new heat exchanger.\n')
                    heatExchangers[identifier_ect].print()
                    break
                elif operand_ect_n == '3.1':
                    combinedHeatPowers[identifier_ect] = Energy2ElecHeatConverter.create_input(identifier_ect)
                    print('You have profiled a new combine heat and power.\n')
                    combinedHeatPowers[identifier_ect].print()
                    break
                elif operand_ect_n == 'exit':
                    operand_ect_i = 0
                    break
                else:
                    print('\n! Error, following the instruction below: \n')
        elif operand_ect_m == 2:
            print('The ID you input is already used.')
            energyConverTechs = {**electricGenerators, **heatExchangers, **combinedHeatPowers}
            energyConverTechs[identifier_ect].print()
            print('---------- Please input another identifier ---------- \n')
        elif operand_ect_m == 0:
            print('---------- Return to Main Menu ---------- \n')
            break
        operand_ect_i += 1
    if operand_ect_m != 0:
        print('---------- Too many operations. Return to Main Menu ---------- \n')
