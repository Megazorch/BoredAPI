from cement import Controller, ex
import requests
import psycopg
from datetime import datetime
import random


class DatabaseController(Controller):
    class Meta:
        label = 'new'
        stacked_on = 'base'
        stacked_type = 'nested'
        description = 'Fetch a new activity from Bored API and store it in PostgreSQL'

    @ex(
        help='Fetch a new activity and store it in PostgreSQL',
        arguments=[
            (['--type'],
             {'help': 'Activity type',
              'action': 'store',
              'dest': 'type',
              'choices': ["education", "recreational", "social", "diy",
                          "charity", "cooking", "relaxation", "music", "busywork"]
              }
             ),
            (['--participants'], {'help': 'Number of participants'}),
            (['--price_min'], {'help': 'Minimum price', 'type': float}),
            (['--price_max'], {'help': 'Maximum price', 'type': float}),
            (['--accessibility_min'], {'help': 'Minimum accessibility', 'type': float}),
            (['--accessibility_max'], {'help': 'Maximum accessibility', 'type': float}),
        ],
    )
    def _default(self):
        # Check if any parameters were provided
        if (
            self.app.pargs.type is None and
            self.app.pargs.participants is None and
            self.app.pargs.price_min is None and
            self.app.pargs.price_max is None and
            self.app.pargs.accessibility_min is None and
            self.app.pargs.accessibility_max is None
        ):
            # No parameters provided, fetch a random activity
            self._fetch_random_activity()
        else:
            # Parameters provided, fetch an activity based on the specified criteria
            self._fetch_and_store_activity()

    def _fetch_and_store_activity(self):
        # Fetch activity data from Bored API
        params = {
            'type': self.app.pargs.type,
            'participants': self.app.pargs.participants,
            'price': f"{self.app.pargs.price_min}-{self.app.pargs.price_max}",
            'accessibility': f"{self.app.pargs.accessibility_min}-{self.app.pargs.accessibility_max}",
        }
        response = requests.get('https://www.boredapi.com/api/activity', params=params)

        if response.status_code == 200:
            data = response.json()
            # Store the activity data in PostgreSQL
            conn = psycopg.connect(self.app.config.get('database', 'database_url'))
            cur = conn.cursor()
            cur.execute(
                """
                INSERT INTO activities (type, participants, price, accessibility, created_at)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (
                    data['type'],
                    data['participants'],
                    data['price'],
                    data['accessibility'],
                    datetime.now(),
                ),
            )
            conn.commit()
            conn.close()
            self.app.log.info('Activity stored in PostgreSQL.')
        else:
            self.app.log.error('Failed to fetch activity from Bored API.')

    def _fetch_random_activity(self):
        # Fetch a random activity from Bored API
        response = requests.get('https://www.boredapi.com/api/activity')

        if response.status_code == 200:
            data = response.json()
            self.app.log.info(f'Random Activity: {data["activity"]}')
        else:
            self.app.log.error('Failed to fetch a random activity from Bored API.')
