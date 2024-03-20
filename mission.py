from rocket import Rocket


class Mission:
    """
    Represents a space mission with customizable parameters.

    Attributes:
        travel_distance (int): The distance to be traveled by the rocket (default: 160 km).
        payload_capacity (int): The maximum payload capacity of the rocket (default: 50000 kg).
        fuel_capacity (int): The fuel capacity of the rocket (default: 1514100 liters).
        burn_rate (int): The fuel burn rate of the rocket (default: 168233 liters/min).
        average_speed (int): The average speed of the rocket (default: 1500 km/h).

    Methods:
        print_plan(): Prints the mission plan with the configured parameters.
        fetch_mission_name(): Asks for user input to set the mission name.
        proceed(): Asks for user confirmation to proceed with the mission.
        start(): Initiates the rocket launch and displays the mission status.
        display_mission_status(status): Displays the current status of the mission.
        format_time(time): Formats the elapsed time into HH:MM:SS format.
    """

    def __init__(
        self,
        travel_distance=160,
        payload_capacity=50000,
        fuel_capacity=1514100,
        burn_rate=168233,
        average_speed=1500,
    ):
        """
        Initializes a new Mission object with default or provided parameters.

        Args:
            travel_distance (int): The distance to be traveled by the rocket (default: 160 km).
            payload_capacity (int): The maximum payload capacity of the rocket (default: 50000 kg).
            fuel_capacity (int): The fuel capacity of the rocket (default: 1514100 liters).
            burn_rate (int): The fuel burn rate of the rocket (default: 168233 liters/min).
            average_speed (int): The average speed of the rocket (default: 1500 km/h).
        """
        self.travel_distance = travel_distance
        self.payload_capacity = payload_capacity
        self.fuel_capacity = fuel_capacity
        self.burn_rate = burn_rate
        self.average_speed = average_speed
        self.random_seed = 12
        self.summary = {}

    def print_plan(self):
        """
        Prints the mission plan with the configured parameters.
        """
        print("Mission plan:")
        print(f"  Travel distance: {self.travel_distance} km")
        print(f"  Payload capacity: {self.payload_capacity} kg")
        print(f"  Fuel capacity: {self.fuel_capacity} liters")
        print(f"  Burn rate: {self.burn_rate} liters/min")
        print(f"  Average speed: {self.average_speed} km/h")
        print(f"  Random seed: {self.random_seed}")

    def fetch_mission_name(self):
        """
        Asks for user input to set the mission name.
        """
        self.mission_name = input("What is the name of this mission? ")

    def proceed(self):
        """
        Asks for user confirmation to proceed with the mission.

        Returns:
            bool: True if user wants to proceed, False otherwise.
        """
        return input("Would you like to proceed? (y/n): ").strip().lower() == "y"

    def start(self):
        """
        Initiates the rocket launch and displays the mission status.
        """
        rocket = Rocket.prepare_for_launch(distance=160, burn_rate=168240, average_speed=1500)

        if rocket.launch():
            for status in rocket.launch():
                self.display_mission_status(status)

        self.summary = rocket.summary()

    def display_mission_status(self, status):
        """
        Displays the current status of the mission.

        Args:
            status (dict): Dictionary containing status information.
        """
        print("Mission status:")
        print(f"  Current fuel burn rate: {status['current_fuel_burn_rate']} liters/min")
        print(f"  Current speed: {status['current_speed']} km/h")
        print(f"  Current distance traveled: {status['distance_traveled']} km")
        print(f"  Elapsed time: {self.format_time(status['elapsed_time'])}")
        print(f"  Time to destination: {self.format_time(status['time_to_destination'])}")

    @staticmethod
    def format_time(time):
        """
        Formats the elapsed time into HH:MM:SS format.

        Args:
            time (int): Elapsed time in seconds.

        Returns:
            str: Formatted time string in HH:MM:SS format.
        """
        hours = time // 3600
        minutes = (time % 3600) // 60
        seconds = time % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
