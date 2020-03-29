class Field:
  def __init__(self):
    self.coordinates = {}

  def add_tipsy(self, tipsy, coordinate):
    self.coordinates[tipsy] = coordinate

  def move_tipsy(self, tipsy):
    delta_x, delta_y = tipsy.walk()
    current_coordinate = self.coordinates[tipsy]
    new_coordinate = current_coordinate.move(delta_x, delta_y)

    self.coordinates[tipsy] = new_coordinate

  def get_coordinate(self, tipsy):
    return self.coordinates[tipsy]
