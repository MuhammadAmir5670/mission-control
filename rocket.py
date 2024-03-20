import time
from launch_control import LaunchControl


class Rocket:
    """
    Represents a rocket used for space missions.

    Attributes:
        launch_control (LaunchControl): An instance of LaunchControl managing the launch process.
        distance (float): The total distance the rocket needs to travel.
        burn_rate (float): The fuel burn rate of the rocket in liters per minute.
        average_speed (float): The average speed of the rocket in kilometers per hour.
        distance_traveled (float): The distance traveled by the rocket.
        elapsed_time (int): The elapsed time since launch in seconds.
        __flight_time (float): The start time of the rocket's flight.

    Methods:
        prepare_for_launch(): Prepares the rocket for launch by initializing LaunchControl.
        launch(): Initiates the rocket launch process and yields status information.
        summary(): Retrieves the summary of the mission after completion.
        explode_iteration(): Calculates the iteration at which the rocket will explode, if applicable.
        flight_time(): Calculates the elapsed flight time of the rocket.
        status(): Retrieves the current status of the rocket.
        reached_destination(): Checks if the rocket has reached its destination.
        current_speed(): Calculates the current speed of the rocket.
        calculate_time_to_destination(): Calculates the estimated time remaining to reach the destination.
        calculate_distance_traveled(): Calculates the distance traveled by the rocket.
        calculate_total_fuel_burned(): Calculates the total amount of fuel burned by the rocket.
    """

    def __init__(self, distance, burn_rate, average_speed):
        """
        Initializes a new Rocket object with provided parameters.

        Args:
            distance (float): The total distance the rocket needs to travel.
            burn_rate (float): The fuel burn rate of the rocket in liters per minute.
            average_speed (float): The average speed of the rocket in kilometers per hour.
        """
        self.launch_control = LaunchControl()
        self.distance = distance
        self.burn_rate = burn_rate
        self.average_speed = average_speed
        self.distance_traveled = 0
        self.elapsed_time = 0
        self.__flight_time = None

    @classmethod
    def prepare_for_launch(cls, distance, burn_rate, average_speed):
        """
        Creates a new instance of the Rocket class and prepares it for launch.

        Args:
            distance (float): The total distance the rocket needs to travel.
            burn_rate (float): The fuel burn rate of the rocket in liters per minute.
            average_speed (float): The average speed of the rocket in kilometers per hour.

        Returns:
            Rocket: A new instance of the Rocket class.
        """
        rocket = cls(distance, burn_rate, average_speed)
        rocket()

        return rocket

    def __call__(self):
        """
        Prepares the rocket for launch by initializing LaunchControl.
        """
        self.launch_control.prepare_for_launch()

    def launch(self):
        """
        Initiates the rocket launch process and yields status information.

        Yields:
            dict: Status information containing current rocket parameters.
        """
        self.elapsed_time = 0
        self.distance_traveled = 0
        self.__flight_time = time.time()

        while not self.reached_destination():
            if self.explode_iteration() == self.elapsed_time:
                print("Exploded!")
                break

            self.elapsed_time += 1
            self.distance_traveled += self.calculate_distance_traveled()
            yield self.status()
            time.sleep(1)

    def summary(self):
        """
        Retrieves the summary of the mission after completion.

        Returns:
            dict: A dictionary containing summary information of the mission.
        """
        return {
            "total_distance": self.distance_traveled,
            "no_abort_retries": self.launch_control.abort_count,
            "no_explosions": 1 if self.launch_control.explode() else 0,
            "total_fuel_burned": self.calculate_total_fuel_burned(),
            "flight_time": self.flight_time,
        }

    def explode_iteration(self):
        """
        Calculates the iteration at which the rocket will explode, if applicable.

        Returns:
            int: The iteration at which the rocket will explode.
        """
        return self.launch_control.rand_launch_iteration(self.distance, self.current_speed())

    @property
    def flight_time(self):
        """
        Calculates the elapsed flight time of the rocket.

        Returns:
            float: The elapsed flight time in seconds.
        """
        return time.time() - self.__flight_time

    def status(self):
        """
        Retrieves the current status of the rocket.

        Returns:
            dict: Current status information including elapsed time, distance traveled, etc.
        """
        return {
            "elapsed_time": self.elapsed_time,
            "distance_traveled": self.distance_traveled,
            "current_fuel_burn_rate": self.burn_rate / 60,
            "current_speed": self.average_speed,
            "time_to_destination": self.calculate_time_to_destination(),
        }

    def reached_destination(self):
        """
        Checks if the rocket has reached its destination.

        Returns:
            bool: True if the rocket has reached its destination, False otherwise.
        """
        return self.distance_traveled >= self.distance

    def current_speed(self):
        """
        Calculates the current speed of the rocket.

        Returns:
            float: The current speed of the rocket in kilometers per minute.
        """
        return self.average_speed / 60

    def calculate_time_to_destination(self):
        """
        Calculates the estimated time remaining to reach the destination.

        Returns:
            int: The estimated time remaining to reach the destination in seconds.
        """
        remaining_distance = self.distance - self.distance_traveled
        remaining_time = remaining_distance / self.average_speed
        return int(remaining_time)

    def calculate_distance_traveled(self):
        """
        Calculates the distance traveled by the rocket.

        Returns:
            float: The distance traveled by the rocket.
        """
        return self.current_speed() * self.elapsed_time

    def calculate_total_fuel_burned(self):
        """
        Calculates the total amount of fuel burned by the rocket.

        Returns:
            float: The total amount of fuel burned by the rocket in liters.
        """
        return (self.burn_rate * self.elapsed_time) / 60
