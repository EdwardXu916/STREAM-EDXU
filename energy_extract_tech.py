# Class Definition of Energy Extraction Technology
# Version 1.0, Edward Xu, 181006

__Version__ = 1.0

if __name__ == '__main__':
    print('!!! energy_extract_tech.py is being run by itself.\n')
else:
    print('!!! energy_extract_tech.py is imported from another file.\n')


class EnergyExtractTech:
    """Class definition of energy extraction technology"""
    number = 0

    def __init__(self, identifier, name, source, outcome):
        self.id = identifier
        self.name = name
        self.source = source
        self.outcome = outcome
        EnergyExtractTech.number += 1

    def print(self):
        """Print the common feature of energy extraction technology"""
        text_source = ["Coal", "Crude", "Biomass", "Sun", "Wind"]
        text_outcome = ["Mechanical Energy", "Chemical Energy", "Heat"]
        print('Energy Conversion Technology: {}, source: {}, output: {}, id: {}, '
              .format(self.name, text_source[self.source], text_outcome[self.outcome], self.id), end=" ")


class MechaExtractor(EnergyExtractTech):
    """One kind of Energy extraction technologies, extracting mechanical energy

    kind: wind blade, wind vibrator, tidal blade, tidal vibrator
    outcome: text_outcome
    """
    number = 0

    text_mechaExtractorKind = ['wind blade', 'wind vibrator', 'tidal blade', 'tidal vibrator']

    def __init__(self, identifier, name, source, outcome, kind, efficiency):
        EnergyExtractTech.__init__(self, identifier, name, source, outcome)
        self.kind = kind
        self.efficiency = efficiency
        MechaExtractor.number += 1
        print("You have profiled a new mechanical energy extractors. ")
        MechaExtractor.print_number()

    def __str__(self):
        return 'This mechanical extractor is {}'.format(self.name)

    def tell(self):
        print("efficiency: {}.".format(self.efficiency))

    @classmethod
    def tell_number(cls):
        print("The number of mechanical energy extractors is {}.".format(MechaExtractor.number))

    @classmethod
    def summary_kind(cls, windBlades, windVibrators, tidalBlades, tidalVibrators):
        print('Summary all kinds of mechanical energy extractor: \n',
              MechaExtractor.text_mechaExtractorKind[1], 'number: {}'.format()
              )


    @classmethod
    def profile(cls, identifier_eet, energy_source, kind_me):
        print('You are profiling a new mechanical energy extractor.')
        return cls(identifier_eet,
                   input('Name: '),
                   energy_source,
                   int(1),
                   kind_me,
                   int(input('Efficiency(%): '))
                   )

    @classmethod
    def profile_mean(cls, identifier_eet_mean, energy_source, kind_me, efficiency_mean):
        print('You are profiling a mean mechanical energy extractor.')
        return cls(identifier_eet_mean,
                   (input('Name: + "_mean"'), '_mean'),
                   energy_source,
                   int(1),
                   kind_me,
                   int(efficiency_mean)
                   )


class HeatExtractor(EnergyExtractTech):
    """One kind of Energy extraction technologies, extracting heat"""
    number = 0

    def __init__(self, identifier, name, source, outcome, kind, efficiency):
        EnergyExtractTech.__init__(self, identifier, name, source, outcome)
        self.kind = kind
        self.efficiency = efficiency
        HeatExtractor.number += 1
        print("You have profiled a new heat energy extractors. ")
        HeatExtractor.print_number()

    def print(self):
        print("efficiency: {}.".format(self.efficiency))

    @classmethod
    def print_number(cls):
        print("The number of heat energy extractors is {}.".format(HeatExtractor.number))

    @classmethod
    def create_input(cls, identifier_eet, source, kind_me):
        print('You are profiling a new heat energy extractor.')
        return cls(identifier_eet,
                   input('Name: '),
                   source,
                   int(1),
                   kind_me,
                   int(input('Efficiency(%): '))
                   )


class ChemicalExtractor(EnergyExtractTech):
    """One kind of Energy extraction technologies, extracting heat"""
    number = 0

    def __init__(self, identifier, name, source, outcome, kind, efficiency):
        EnergyExtractTech.__init__(self, identifier, name, source, outcome)
        self.kind = kind
        self.efficiency = efficiency
        ChemicalExtractor.number += 1
        print("You have profiled a new chemical energy extractors. ")
        ChemicalExtractor.print_number()

    def print(self):
        print("efficiency: {}.".format(self.efficiency))

    @classmethod
    def print_number(cls):
        print("The number of chemical energy extractors is {}.".format(ChemicalExtractor.number))

    @classmethod
    def create_input(cls, identifier_eet, kind_me):
        print('You are profiling a new chemical energy extractor.')
        return cls(identifier_eet,
                   input('Name: '),
                   input('Source: '),
                   int(1),
                   kind_me,
                   int(input('Efficiency(%): '))
                   )


def profile(source):
    identifier_eet = 'STC'
    kind_me = 'Solar Thermal Concentration'
    HeatExtractor.create_input(identifier_eet, source, kind_me)