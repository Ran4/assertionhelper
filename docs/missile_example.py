import logging

from assertionhelper import assert_type

logging.basicConfig(filename="logs.log", level=logging.DEBUG)

class Target:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

class Missile:
    def __init__(self, target: Target):
        self.target = target
        
    def fire(self):
        if self.target:
            msg = "Missile was fired towards target {}!".format(self.target)
        else:
            msg = "Missile exploded on itself!"
        return msg

class MissileFactory:
    def create_missile(self, target: 'Target'):
        return Missile(target=target)

def fire_missile_at_target(target: Target, missile_factory: MissileFactory) -> None:
    assert_type(target, Target, "No missile was fired since target isn't valid")
    missile = missile_factory.create_missile(target=target)
    status_msg = missile.fire()
    logging.info(status_msg)
    print(status_msg)



print("First, fire missile with a valid target:")
fire_missile_at_target(target=Target(4, 5), missile_factory=MissileFactory())

print("Then, we try to fire a missile with an invalid target:")
fire_missile_at_target(target=None, missile_factory=MissileFactory())
