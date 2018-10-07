# Class Definition of Energy Source
# Version: 1.0, Jie Xu, 181006


class EnergySource:
    """ Energy Source

    tell():
    classmethod print():
    """
    number = 0

    def __init__(self, context, info, sustainability):
        self.context = context  # Short name of the profiled condition of sun
        self.info = info  # Other useful information about this profiled sun
        self.sustainability = sustainability

    def tell(self):
        print('An energy source: {}, sustainability: {}.'.format(self.context, self.sustainability))

    @classmethod
    def print_number(cls):
        print('Number of profiled energy sources is {}.'.format(EnergySource.number))


class Sun(EnergySource):
    """Sun_EnergySource"""
    number = 0

    def __init__(self, context, info, sustainability, light, heat, position_fun, height_fun):
        EnergySource.__init__(self, context, info, sustainability)
        self.light = light  # Energy density of light from sun
        self.heat = heat  # Energy density of heat from sun
        self.position_fun = position_fun  # Function for effect of position angle on sun
        self.height_fun = height_fun  # Function for effect of height angle on sun
        Sun.number += 1

    def tell_info(self):
        print('Info of the sun in {} context: {}. \n'.format(self.context, self.info))

    def tell_allinfo(self):
        print('All info about the sun in {} context: {}. \n'
              'Sustainability: {}, Light: {}, Heat: {}, \n'
              'Position Angle Fun: {}, Height Angle Fun: {}. \n'
              .format(self.context, self.info, self.sustainability, self.light, self.heat,
                      self.position_fun, self.height_fun))

    @classmethod
    def create(cls):
        print('You are profiling a new context for sun.')
        return cls(input('Context: '),
                   input('Sustainability ("Y" or "N"): '),
                   input('Info: '),
                   input('Light: '),
                   input('Heat: '),
                   input('Position Angle Function (%):'),
                   input('Height Angle Function (%): '))

    @classmethod
    def tell_number(cls):
        print('There are {} kinds of context for sun.'.format(Sun.number))


class Atmosphere(EnergySource):
    """Different context of atmosphere as source of energy."""
    number = 0

    def __init__(self, context, info, sustainability, kinetic, potential, delta_temp):
        EnergySource.__init__(self, context, info, sustainability)
        self.kinetic = kinetic
        self.potential = potential
        self.delta_temp = delta_temp
        Atmosphere.number += 1

    def tell_info(self):
        print('Info of the atmosphere in {} context: {}. \n'.format(self.context, self.info))

    def tell_allinfo(self):
        print('All info about the sun in {} context: {}. \n'
              'Sustainability: {}, Kinetic Energy: {}, Potential Energy: {}, Delta Temperature: {}.'
              .format(self.context, self.info, self.sustainability,
                      self.kinetic, self.potential, self.delta_temp))

    @classmethod
    def create(cls):
        print('You are creating a new context for atmosphere. \n')
        return cls(input('Context:'),
                   input('Sustainability ("Y" or "N")'),
                   int(input('kinetic: ')),
                   int(input('potential: ')),
                   int(input('Delta temperature: '))
                   )

    @classmethod
    def tell_number(cls):
        print('There are {} kinds of context for atmosphere.'.format(Atmosphere.number))


class Atmosphere(EnergySource):
    """Different context of atmosphere as source of energy."""
    number = 0

    def __init__(self, context, info, sustainability, kinetic, potential, delta_temp):
        EnergySource.__init__(self, context, info, sustainability)
        self.kinetic = kinetic
        self.potential = potential
        self.delta_temp = delta_temp
        Atmosphere.number += 1

    def tell_info(self):
        print('Info of the atmosphere in {} context: {}. \n'.format(self.context, self.info))

    def tell_allinfo(self):
        print('All info about the sun in {} context: {}. \n'
              'Sustainability: {}, Kinetic Energy: {}, Potential Energy: {}, Delta Temperature: {}.'
              .format(self.context, self.info, self.sustainability,
                      self.kinetic, self.potential, self.delta_temp))

    @classmethod
    def create(cls):
        print('You are creating a new context for atmosphere. \n')
        return cls(input('Context:'),
                   input('Sustainability ("Y" or "N")'),
                   int(input('kinetic: ')),
                   int(input('potential: ')),
                   int(input('Delta temperature: '))
                   )

    @classmethod
    def tell_number(cls):
        print('There are {} kinds of context for atmosphere.'.format(Atmosphere.number))