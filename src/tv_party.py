from tv import TV


 # Let's make a TV party!!

class TVParty:

    def __init__(self):
        # TODO: Instantiate the TV object
        tv = TV()

        # TODO: Your first code goes here
        tv.turned_on = True
        tv.channel = 3
        tv.volume_level = 7

        print(
            "Let's watch the Alien Movie. The TV is currently [" + tv.is_on() + "] and it should be [on]."
            + " It's being shown on channel [3], and we're currently on channel [" + str(tv.channel) + "]. "
            + "Your friend Lisa also would like to have the volume set to [7], and we're currently on volume ["
            + str(tv.volume_level) + "]."
        )

        # TODO: Food break! turn the tv off.
        tv.turned_on = False

        print("Food break! The TV should be [off], and it's currently [" + tv.is_on() + "].")

        # TODO: Your second code goes here.
        tv.turned_on = True
        tv.channel = 95
        tv.volume_level = 5
        print(
            "Now let's watch the last season of Game of Thrones. The TV is currently [" + tv.is_on()
            + "] and it should be [on]. "
            + "It's being shown on channel [95], and we're currently on channel [" + str(tv.channel) + "]. "
            + "Your friend Gabriel also would like to have the volume set to [5], and we're currently on volume ["
            + str(tv.volume_level) + "]."
        )


fun = TVParty()
