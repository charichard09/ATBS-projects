#  Given you are at position [0][0] in an NxN structure, you can only move in cardinal directions North, East, West, South,
#  return True if you can reach position [N-1][N-1], return false if the path is blocked.
#  empty positions are marked with a '.'
#  occupied positions are marked with a 'W'

def path_finder(maze):
    #  Use split function to split string of maze into a single list of individual rows of maze and assign to maze_split
    maze_split = maze.split("\n")

    #  Assign first position in maze and finish line in maze
    #  TODO: start and end value will will always be '.', I need to find a way to save start and ends index position
    #  rather than the value.
    position = maze_split[0][0]
    finish_line = maze_split[-1][-1]

    #  Hypothesis: From position [0][0], use a loop to check each cardinal direction position, if True, continue, if false
    #  eliminate that possibility. If all return False, no path is found, if position == [N-1][N-1], return True.
    

    return


#  Test path_finder()
test = "\n".join([
          ".W...",
          ".W...",
          ".W.W.",
          "...W.",
          "...W."])

print(f"Path to the end is {bool(path_finder(test))}")

#  Other tests
#test = "\n".join([
#          ".W...",
#          ".W...",
#          ".W.W.",
#          "...WW",
#          "...W."])
#
#test = "\n".join([
#          "..W",
#          ".W.",
#          "W.."])