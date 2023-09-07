"""
Code for the items controller.
"""
from cement import Controller, ex
import psycopg
from cement.utils import fs


class New(Controller):
    class Meta:
        label = 'new'
        stacked_type = 'embedded'
        stacked_on = 'base'

    @ex(help='list last 5 activities')
    def list(self):
        pass

    @ex(help='get new activity',
        arguments=[
            (['--type'],
             {'help': 'Type of the activity',
              'action': 'store',
              'choices': ["education", "recreational", "social", "diy",
                          "charity", "cooking", "relaxation", "music",
                          "busywork"],
              }),
            (['--participants'],
             {'help': 'The number of people that this activity could involve',
              'metavar': '[0,n]',
              'action': 'store',
              'type': int,
              }),
            (['--price',
              '--price_min',
              '--price_max'],
             {'help': 'A factor describing the cost of the event with zero being free',
              'metavar': '[0.0, 1.0]',
              'action': 'store',
              'type': float,
              }),
            (['--accessibility',
              '--accessibility_min',
              '--accessibility_max'],
             {'help': 'A factor describing how possible an event is to do with zero being the most accessible',
              'metavar': '[0.0, 1.0]',
              'action': 'store',
              'type': float,
              }),
            ],
        )
    def new(self):
        pass

