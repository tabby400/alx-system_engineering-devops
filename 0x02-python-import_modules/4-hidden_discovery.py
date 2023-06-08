#!/usr/bin/python3

if __name__ == "__main__":  # not executed when imported
    import hidden_4
    for name in sorted(dir(hidden_4)):  # in alpha order
        if name[:2] != "__":
            print(name)
