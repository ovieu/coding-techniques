
def listAllSubset(list):
    choices = [];
    listAllSubsetRec(choices, list)

def listAllSubsetRec(choices = [], list = []):
    if not list:
        print(choices)
    else:
        # select the element, remove from copy the li & explore
        selectedItem = list[0]
        new_choices = [];
        new_choices = choices.append(selectedItem)
        list.pop(0)
        remaining_choices = list
        listAllSubsetRec(new_choices, remaining_choices)

        # dont select the element and explore
        mchoices = choices
        mremaining_choices = remaining_choices
        listAllSubsetRec(choices, mremaining_choices)

def lenOfStr(s):
    """
    :type s: str
    :return: int
    """
    s.capitalize();
    return len(s)

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x}, {self.y}'

    def __lt__(self, other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (self.x ** 2) + (self.y ** 2)
        return self_mag < other_mag


if __name__ == "__main__":
    # list = ["kagan", "breyer", "alito", "ginsburgh"]
    # listAllSubset(list)
    p1 = Point(1, 1)
    p3 = Point(1, 1)
    p2 = Point(4, 5)
    print(p1 < p2)
    print(p1 == p3)
