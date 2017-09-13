from collections import namedtuple

Query = namedtuple("Query", ("x", "y"))
Transition = namedtuple("Transition", ("x", "y", "state"))
ALIVE = "*"
EMPTY = "-"
TICK = object()


def count_neighbours(x, y):
    """
    Count active neighbours of a given cell
    """
    n_dict = {}
    cnt = 0
    
    n_dict["n_"] = yield Query(x, y + 1)
    n_dict["ne"] = yield Query(x + 1, y + 1)
    n_dict["e_"] = yield Query(x + 1, y)
    n_dict["se"] = yield Query(x + 1, y - 1)
    n_dict["s_"] = yield Query(x, y - 1)
    n_dict["sw"] = yield Query(x - 1, y - 1)
    n_dict["w_"] = yield Query(x - 1, y)
    n_dict["nw"] = yield Query(x - 1, y + 1)

    for _, v in n_dict.items():
        cnt += 1 if v == ALIVE else 0
    return cnt
    
    
def game_logic(state, cnt_n):
    """
    Implementation of the game logic
    """
    if state == ALIVE:
        if cnt_n < 2:
            return EMPTY
        if cnt_n > 3:
            return EMPTY
    else:
        if cnt_n == 3:
            return ALIVE
    return state
    
    
def step_cell(x, y):
    """
    Calulate next state for cell based on circumstances
    """
    state = yield Query(x, y)
    cnt_n = yield from count_neighbours(x, y)
    next_state = game_logic(state, cnt_n)
    yield Transition(x, y, next_state)


def simulate(height, width):
    """
    Simulate over a given grid
    """
    while True:
        for x in range(width):
            for y in range(height):
                yield from step_cell(x, y)
        yield TICK
        
        
class Grid(object):
    """
    Implementing the grid to hold the states
    """
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.rows = []
        for _ in range(self.height):
            self.rows.append([EMPTY] * self.width)
            
    def query(self, x, y):
        return self.rows[y % self.height][x % self.width]
    
    def assign(self, x, y, state):
        self.rows[y % self.height][x % self.width] = state
        
    def __str__(self):
        output = ""
        for row in self.rows:
            for cell in row:
                output += cell
            output += "\n"
        return output
        
        
def live_a_generation(grid, sim):
    """
    Simulate one generation
    """
    progeny = Grid(grid.height, grid.width)
    item = next(sim)
    while item is not TICK:
        if isinstance(item, Query):
            state = grid.query(item.x, item.y)
            item = sim.send(state)
        else:
            progeny.assign(item.x, item.y, item.state)
            item = next(sim)
    return progeny
    
    
class Life():
    """
    Class to encapsulate multiple generations
    """
    def __init__(self, grid, sim, n_iter):
        self.iters = []
        self.current = grid
        self.iters.append(self.current)
        self.n_iter = n_iter
        self.sim = sim

    def __call__(self):
        for _ in range(self.n_iter):
            progeny = live_a_generation(self.current, self.sim)
            self.iters.append(progeny)
            self.current = progeny
            
            
if __name__ == "__main__":
    # set parameters
    H = 5
    W = 9
    g = Grid(H, W)
    actives = [
        (1, 4),
        (2, 5), 
        (3, 3),
        (3, 4),
        (3, 5)
    ]
    for a in actives:
        g.assign(a[1], a[0], ALIVE)
    sim = simulate(H, W)
    
    # create a life
    L10 = Life(g, sim, 10)
    
    # run the simulation
    L10()
    
    # print the result
    for i in L10.iters:
        print(i)