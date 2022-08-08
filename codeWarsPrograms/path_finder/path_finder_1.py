#  Given you are at position [0][0] in an NxN structure, you can only move in cardinal directions North, East, West, South,
#  return True if you can reach position [N-1][N-1], return false if the path is blocked.
#  empty positions are marked with a '.'
#  occupied positions are marked with a 'W'

def path_finder(maze):
    position = maze[0][0]
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