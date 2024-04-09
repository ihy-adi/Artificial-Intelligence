#code for graph coloring problem

regions = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q", "NSW"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["NT", "SA", "Q", "V"],
    "V": ["SA", "NSW"],
    "T": []
}


colors = ["red", "green", "blue"]