import random, pgzrun

WIDTH = 1000
HEIGHT = 800

TITLE = "falling_game"

#ready,play,game over, game compleet
game_state = "play"

ITEMS = ["battery","chips","bottle","bag"]

lvl = 1

items = []
animations = []

def draw():
  screen.blit("bground", (0,0))
  if game_state == "play":
    for i in items:
      i.draw()
  elif game_state == "completed":
    screen.draw.text("woho you won the game", fontsize = 30, color = "black", center = (WIDTH / 2, HEIGHT / 2))
  elif game_state == "game_over":
    screen.draw.text("better luck next time", fontsize = 30, color = "black", center = (WIDTH / 2, HEIGHT / 2))

    
def update():
  global items
  if game_state == "play":
   if len(items) == 0:
    items = make_items(lvl)

def make_items(lvl):
  items_to_create = nmbr_items(lvl)
  new_items = create_item(items_to_create)
  layout(new_items)
  animate_items(new_items)
  return new_items


def nmbr_items(lvl):
  items_to_create = ["paper"]
  for i in range(lvl):
    items_to_create.append(random.choice(ITEMS))
  return items_to_create

def create_item(items_to_create):
  new_items = []
  for i in items_to_create:
    new_items.append(Actor(i + "img"))
  return new_items

def layout(new_items):
  number_of_gaps = len(new_items)+1
  gap_size = WIDTH / number_of_gaps
  random.shuffle(new_items)
  for i,v in enumerate(new_items):
    v.x = (i + 1) * gap_size

def animate_items(new_items):
  global animations
  for i in new_items:  
    dur = 10 - lvl
    i.anchor = ("center","bottom")
    animation = animate(i, duration = dur, y = HEIGHT, on_finished = handle_game_over)
    animations.append(animation)

def handle_game_over():
  global game_state
  game_state = "game_over"
  print(game_state)
def on_mouse_down(pos):
  global items, lvl
  for i in items:
    if i.collidepoint(pos):
      if "paperimg" in i.image:
        lvl_complete() 
      else:
        handle_game_over()

def lvl_complete():
  global lvl, items, animations, game_state
  stop_animation(animations)
  if lvl == 6:
    game_state = "completed" 
    animations = [] 
    items = []
  else:
    lvl += 1
    animations = []
    items = []
  print(lvl)
def stop_animation(anim):
  for i in anim:
    if i.running:
      i.stop()


pgzrun.go()