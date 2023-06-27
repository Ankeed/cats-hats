# One day you decide to arrange all your cats in a giant circle.
# Initially, none of your cats have any hats on. You walk around
# the circle 100 times, always starting at the same spot,
# with the first cat (cat # 1). Every time you stop at a cat,
# you either put a hat on it if it doesn’t have one on,
# or you take its hat off if it has one on.

# In The first round, you stop at every cat, placing a hat on each one.
# In The second round, you only stop at every second cat (#2, #4, #6, #8, etc.).
# In The third round, you only stop at every third cat(#3, #6, #9, #12, etc.).
# You continue this process until you’ve made 100 rounds around the cats (e.g., you only visit the 100th cat).


def hats_switch(cats, rounds):
    cats_hats = {i:0 for i in range(1, cats + 1)}  # 0 = without hat; 1 = with hat
    round_counter = 1
    while round_counter <=rounds:
        for cat in cats_hats:
            if cat % round_counter == 0:
                if cats_hats[cat] == 0:
                    cats_hats[cat] = 1
                else:
                    cats_hats[cat] = 0
        round_counter += 1
    cats_with_hats = {c:cats_hats[c] for c in cats_hats if cats_hats[c] == 1}
    return list(cats_with_hats.keys())

cats_qty = int(input('How many cats?: '))
rounds = int(input('How many rounds?: '))
print(f'The next cats are with hats! {hats_switch(cats_qty, rounds)}')

# Complexity? 
# Times: as for two loops: O(n**2)
# Space: as for 2 dicts with constants(?): O(n)
