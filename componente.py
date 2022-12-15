class Componente:
    def __init__(self, name, t_max, area, heat):
        self.name = name
        self.t_max = t_max 
        self.area = area
        self.heat = heat
        self.flux = heat/area