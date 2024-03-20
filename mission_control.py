from mission import Mission
import pdb


class MissionControl:
    """
    Represents a control center for managing space missions.

    Attributes:
        missions (list): A list to store instances of Mission class representing active missions.

    Methods:
        start(): Static method to start the Mission Control.
        start_control(): Initiates the Mission Control loop for managing multiple missions.
        run_mission(): Runs a single mission by creating a new Mission instance, printing the mission plan, fetching mission name, starting the mission, and displaying the mission summary.
        display_mission_summary(summary): Displays the summary of a single mission.
        display_summary(): Displays the summary for all missions combined.
        format_time(time): Formats the given time in seconds into HH:MM:SS format.
        prompt(message): Static method to prompt the user for input and return True for 'yes' responses, False otherwise.
    """

    def __init__(self):
        """
        Initializes a new MissionControl object with an empty list of missions.
        """
        self.missions = []

    @staticmethod
    def start():
        """
        Static method to start the Mission Control.
        """
        MissionControl().start_control()

    def start_control(self):
        """
        Initiates the Mission Control loop for managing multiple missions.
        """
        print("Welcome to Mission Control!")

        while True:
            if not self.run_mission():
                break

        self.display_summary()
        print("Exiting Mission Control. Goodbye!")

    def run_mission(self):
        """
        Runs a single mission by creating a new Mission instance, printing the mission plan, fetching mission name,
        starting the mission, and displaying the mission summary.

        Returns:
            bool: True if the user wants to run another mission, False otherwise.
        """
        mission = Mission()
        mission.print_plan()
        mission.fetch_mission_name()

        if mission.proceed():
            mission.start()
            self.display_mission_summary(mission.summary)

        self.missions.append(mission)
        return self.prompt("Would you like to run another mission? (y/n): ")

    def display_mission_summary(self, summary):
        """
        Displays the summary of a single mission.

        Args:
            summary (dict): Dictionary containing summary information for the mission.
        """
        print(summary)
        pdb.set_trace()
        print("Mission summary:")
        print(f"  Total distance traveled: {summary['total_distance']:.2f} km")
        print(f"  Number of abort and retries: {summary['no_abort_retries']}")
        print(f"  Number of explosions: {summary['no_explosions']}")
        print(f"  Total fuel burned: {summary['total_fuel_burned']} liters")
        print(f"  Flight time: {self.format_time(summary['flight_time'])}")

    def display_summary(self):
        """
        Displays the summary for all missions combined.
        """
        print("Final Summary:")
        total_distance = sum(mission.summary["total_distance"] for mission in self.missions)
        total_abort_retries = sum(mission.summary["no_abort_retries"] for mission in self.missions)
        total_explosions = sum(mission.summary["no_explosions"] for mission in self.missions)
        total_fuel_burned = sum(mission.summary["total_fuel_burned"] for mission in self.missions)
        total_flight_time = sum(mission.summary["flight_time"] for mission in self.missions)

        print(f"  Total distance traveled (for all missions combined): {total_distance:.2f} km")
        print(f"  Number of abort and retries (for all missions combined): {total_abort_retries}")
        print(f"  Number of explosions (for all missions combined): {total_explosions}")
        print(f"  Total fuel burned (for all missions combined): {total_fuel_burned} liters")
        print(f"  Total flight time (for all missions combined): {self.format_time(total_flight_time)}")

    @staticmethod
    def format_time(time):
        """
        Formats the given time in seconds into HH:MM:SS format.

        Args:
            time (int): Time in seconds.

        Returns:
            str: Formatted time string in HH:MM:SS format.
        """
        hours = time // 3600
        minutes = (time % 3600) // 60
        seconds = time % 60
        return f"{hours}:{minutes}:{seconds}"

    @staticmethod
    def prompt(message):
        """
        Static method to prompt the user for input and return True for 'yes' responses, False otherwise.

        Args:
            message (str): The message to display to the user.

        Returns:
            bool: True if the user responds with 'yes', False otherwise.
        """
        response = input(message).strip().lower()
        return response == "y"  # Assuming 'y' indicates Yes, and anything else indicates No
