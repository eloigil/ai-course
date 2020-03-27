from bokeh.plotting import figure, show

from tipsy import ClassicTipsy
from field import Field
from coordinate import Coordinate


def walk(field, tipsy, steps):
  start = field.get_coordinate(tipsy)

  for _ in range(steps):
    field.move_tipsy(tipsy)

  return start.distance(field.get_coordinate(tipsy))

def simulate_walk(steps, attemps_n, tipsy_type):
  tipsy = tipsy_type('Tomasin')
  origin = Coordinate(0, 0)
  distances = []

  for _ in range(attemps_n):
    field = Field()
    field.add_tipsy(tipsy, origin)
    walk_simulation = walk(field, tipsy, steps)
    distances.append(round(walk_simulation, 1))

  return distances

def data_visualization(x, y):
  graphic = figure(title = 'Random path', x_axis_label = 'steps', y_axis_label = 'distance')
  graphic.line(x, y, legend='medium distance')

  show(graphic)

def main(walk_distances, attemps_n, tipsy_type):
  medium_distances_for_walk = []
  for steps in walk_distances:
    distances = simulate_walk(steps, attemps_n, tipsy_type)
    medium_distance = round(sum(distances) / len(distances), 4)
    max_distance = max(distances)
    min_distance = min(distances)

    medium_distances_for_walk.append(medium_distance)

    print(f'{tipsy_type.__name__} random walk of {steps} steps')
    print(f'Medium = {medium_distance}')
    print(f'Max = {max_distance}')
    print(f'Min = {min_distance}')
  
  data_visualization(walk_distances, medium_distances_for_walk)


if __name__ == "__main__":
  walk_distances = [10, 100, 1000, 10000]
  attemps_n = 100

  main(walk_distances, attemps_n, ClassicTipsy)