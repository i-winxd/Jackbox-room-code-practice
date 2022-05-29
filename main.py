"""A script to get you to type jackbox codes
as QUICKLY as possible. No external
plugins are required.
"""
import random
import time

RANDOM_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NEWLINES = 10
INFORMATIONAL = """
A Jackbox room code will appear sometime
in the next 2-15 seconds. The place where
the Jackbox code will be put will be
unpredictable. Be ready. Make sure your
mouse is focused on the command line,
and you have clicked on it once.
When the room code appears, type
it as QUICK AS POSSIBLE and
press enters. It is NOT case-sensitive.
"""


def generate_random_letters() -> str:
    """Return a string of length 4, each time
    randomly selected from RANDOM_LETTERS,
    with replacement allowed."""
    list_so_far = []
    for i in range(0, 4):
        list_so_far.append(random.choice(RANDOM_LETTERS))
    return ''.join(list_so_far)


def generate_room_code_string(room_code: str) -> str:
    """Generate a room code string."""
    the_list = ['🍞🍞🍞🍞🍞🍞🍞🍞🍞' for _ in range(0, NEWLINES)]
    the_index = random.randint(0, NEWLINES - 1)
    the_list[the_index] = room_code
    return '\n'.join(the_list)


def practice() -> None:
    """This is where the pain starts."""
    tr = generate_random_letters()
    rc_string = generate_room_code_string(tr)
    time.sleep(random.randint(2, 15))
    time_start = time.perf_counter()
    print('THE ROOM CODE IS')
    tempp = input(rc_string).strip()
    print(tempp)
    time_end = time.perf_counter()
    total_time = time_end - time_start

    if tempp.upper() == tr:
        print('✅✅ YOU TYPED THE CODE CORRECTLY!!! ✅✅')
    else:
        print('❌❌ WRONG WRONG WRONG ❌❌')

    print(f'You took {total_time} to do this.')

if __name__ == '__main__':
    practice()
