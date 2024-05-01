'''Python: Advanced

70 points

This assignment will develop your ability to manipulate data.
We expect that this assignment will equip you to understand
    Python tutorials.

Please refer to the file `advanced_sample_data.py` for examples of:
- the `social_graph` parameter for the relationship_status item
- the `board` parameter for the tic_tac_toe item
- the `route_map` parameter for the eta item
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see `advanced_sample_data.py` for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if from_member follows to_member,
        "followed by" if from_member is followed by to_member,
        "friends" if from_member and to_member follow each other,
        "no relationship" if neither from_member nor to_member follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    def relationship_status(from_member, to_member, social_graph):
    
    if to_member in social_graph.get(from_member, {}).get("following", []):
        if from_member in social_graph.get(to_member,{}).get("following",[]):
            return "friends"
        else:
            return "follower"
    elif from_member in social_graph.get(to_member,{}).get("following",[]):
        return "followed by"
    else:
        return "no relationship"

social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}

from_member = str(input("Enter the first user"))
to_member = str(input("Enter the second user"))
relationship = relationship_status(from_member, to_member, social_graph)

if relationship == "friends":
    print(f"{from_member} and {to_member} are {relationship}.")
elif relationship == "follower":
    print(f"{from_member} is a {relationship} of {to_member}.")
elif relationship == "followed by":
    print(f"{from_member} is {relationship} {to_member}.")
else:
    print(f"{from_member} and {to_member} have {relationship}.")

"--------------------------------------------------------------------------------------------------------------------------------------"

def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see `advanced_sample_data.py` for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner, or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
def tic_tac_toe(board):
  board_size = len(board)

  for i in range(board_size):
    if all(board[i][j] == board[i][0] and board[i][0] != "" for j in range(board_size)):
      return board[i][0]
    if all(board[j][i] == board[0][i] and board[0][i] != "" for j in range(board_size)):
      return board[0][i]

  if all(board[i][i] == board[0][0] and board[0][0] != "" for i in range(board_size)):
    return board[0][0]
  if all(board[i][board_size - 1 - i] == board[0][board_size - 1] and board[0][board_size - 1] != "" for i in range(board_size)):
    return board[0][board_size - 1]

  if all(symbol != "" for row in board for symbol in row):
    return "NO WINNER"

  return "NO WINNER"

"--------------------------------------------------------------------------------------------------------------------------------------"

def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see `advanced_sample_data.py` for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    def eta(first_stop, second_stop, route_map):
    total_travel_time = 0
    current_stop = first_stop

    while current_stop != second_stop:
        if (current_stop, second_stop) in route_map:
            travel_time = route_map[(current_stop, second_stop)]['travel_time_mins']
            total_travel_time += travel_time
            break
        else:
            for key in route_map.keys():
                if key[0] == current_stop:
                    travel_time = route_map[key]['travel_time_mins']
                    total_travel_time += travel_time
                    current_stop = key[1]
                    break
                
    return total_travel_time
