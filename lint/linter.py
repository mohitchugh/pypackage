from . import rule1

def footest():
    print("called footest2")
    print("calling rule1 via footest")
    rule1.rule1test()
