if __name__ == '__main__':
    import os
    for i in range(34,101):
        mkdir = "/Users/chenak/Desktop/chenak/project/workbook/exercise_{0:03d}.py".format(i)
        with open(mkdir, "w") as f:
            pass
        # os.remove(mkdir)