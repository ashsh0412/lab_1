from pakuri import Pakuri

class Pakudex:
    def __init__(self, capacity=20):
        self._capacity = capacity
        self._pakuri = []

    def get_size(self):
        return len(self._pakuri)

    def get_capacity(self):
        return self._capacity

    def get_species_array(self):
        if not self._pakuri:
            return None
        return [p.get_species() for p in self._pakuri]

    def get_stats(self, species):
        for pakuri in self._pakuri:
            if pakuri.get_species() == species:
                return [pakuri.get_attack(), pakuri.get_defense(), pakuri.get_speed()]
        return None

    def sort_pakuri(self):
        self._pakuri.sort(key=lambda x: x.get_species())

    def add_pakuri(self, species):
        if self.get_size() >= self._capacity:
            return False
        
        # Check for duplicates
        if any(p.get_species() == species for p in self._pakuri):
            return False
            
        self._pakuri.append(Pakuri(species))
        return True

    def evolve_species(self, species):
        for pakuri in self._pakuri:
            if pakuri.get_species() == species:
                pakuri.evolve()
                return True
        return False