import random, pgzrun

WIDTH = 1000
HEIGHT = 800

TITLE = "star_wars_falling_game"

#ready,play,game over, game compleet
game_state = "play"

ITEMS = ["darth_maul","darth_vader","Kylo_ren",]

lvl = 1

items = []
animations = []

def draw():
  screen.blit("bground", (0,0))
  for i in items:
    i.draw()
    
def update():
  global items
  if len(items) == 0:
    items = make_items(lvl)

def make_items(lvl):
  items_to_create = nmbr_items(lvl)
  new_items = create_item(items_to_create)
  layout(new_items)
  return new_items


def nmbr_items(lvl):
  items_to_create = ["yoda.png"]
  for i in range(lvl):
    items_to_create.append(random.choice(ITEMS))
  return items_to_create

def create_item(items_to_create):
  new_items = []
  for i in items_to_create:
    new_items.append(Actor(i))
  return new_items

def layout(new_items):
  number_of_gaps = len(new_items)+1
  gap_size = WIDTH / number_of_gaps
  random.shuffle(new_items)
  for i,v in enumerate(new_items):
    v.x = (i + 1) * gap_size

  





pgzrun.go()