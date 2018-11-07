import writeSingle8
import time


def main():

    TaskList = [writeSingle8]

    for task in TaskList:
        task.setUp()
        res = task.runTest()
        task.tearDown()
        if(res):
            print("Success")
        else:
            print(task)
            print("Fail")


        time.sleep(1)

if __name__ == '__main__':
    main()