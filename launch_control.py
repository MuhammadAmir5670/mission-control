import random


class LaunchControl:
    """
    Manages the launch process and control for a space mission.

    Attributes:
        aborted (bool): Indicates if the launch has been aborted.
        abort_count (int): The number of times the launch has been aborted and retried.
        explode_result (bool): Indicates the result of the explosion check.

    Methods:
        prepare_for_launch(): Performs pre-launch checks and preparations.
        launch(): Determines if the launch should proceed or be aborted.
        explode(): Checks if the mission should result in an explosion.
        rand_launch_iteration(distance, current_speed): Generates a random launch iteration based on the distance and current speed.
        abort_and_retry(): Determines if the launch should be aborted and retried.
        abort_launch(): Aborts the launch process and increments the abort count.
        disengage_release_structure(): Checks if the support structures should be released.
        engage_afterburner(): Checks if the afterburner should be engaged.
        perform_cross_checks(): Checks if cross-checks should be performed.
    """

    def __init__(self):
        """
        Initializes a new LaunchControl object with default attributes.
        """
        self.aborted = False
        self.abort_count = 0
        self.explode_result = None

    def prepare_for_launch(self):
        """
        Performs pre-launch checks and preparations.

        Returns:
            bool: True if preparation is successful, False otherwise.
        """
        if self.engage_afterburner() and self.disengage_release_structure() and self.perform_cross_checks():
            return True
        else:
            self.abort_launch()
            return False

    def launch(self):
        """
        Determines if the launch should proceed or be aborted.

        Returns:
            bool: True if the launch proceeds, False otherwise.
        """
        if self.aborted:
            return False

        launch_decision = input("Launch? (yes/no): ").strip().lower()
        if launch_decision == "yes":
            if self.abort_and_retry() and self.abort_launch():
                return False
            else:
                print("Launched!")
                return True
        else:
            return False

    def explode(self):
        """
        Checks if the mission should result in an explosion.

        Returns:
            bool: True if the mission explodes, False otherwise.
        """
        if self.aborted:
            return False

        if self.explode_result:
            return self.explode_result

        self.explode_result = random.randint(0, 1) == 0
        return self.explode_result

    def rand_launch_iteration(self, distance, current_speed):
        """
        Generates a random launch iteration based on the distance and current speed.

        Args:
            distance (float): The total distance the rocket needs to travel.
            current_speed (float): The current speed of the rocket.

        Returns:
            int: A random launch iteration.
        """
        total_iterations = (distance / current_speed).__ceil__()
        return random.randint(0, total_iterations - 2)

    def abort_and_retry(self):
        """
        Determines if the launch should be aborted and retried.

        Returns:
            bool: True if the launch should be aborted and retried, False otherwise.
        """
        return random.randint(0, 2) == 0

    def abort_launch(self):
        """
        Aborts the launch process and increments the abort count.

        Returns:
            bool: Always returns True.
        """
        print("Mission aborted!")
        self.aborted = True
        self.abort_count += 1
        return True

    def disengage_release_structure(self):
        """
        Checks if the support structures should be released.

        Returns:
            bool: True if the support structures are released, False otherwise.
        """
        release_decision = input("Release support structures? (yes/no): ").strip().lower()
        if release_decision == "yes":
            print("Support structures released!")
            return True
        else:
            return False

    def engage_afterburner(self):
        """
        Checks if the afterburner should be engaged.

        Returns:
            bool: True if the afterburner is engaged, False otherwise.
        """
        engage_decision = input("Engage afterburner? (yes/no): ").strip().lower()
        if engage_decision == "yes":
            print("Afterburner engaged!")
            return True
        else:
            retry_decision = input("Retry? (yes/no): ").strip().lower()
            if retry_decision == "yes":
                print("Safe Abort!")
                self.abort_count += 1
                return self.engage_afterburner()
            else:
                return False

    def perform_cross_checks(self):
        """
        Checks if cross-checks should be performed.

        Returns:
            bool: True if cross-checks are performed, False otherwise.
        """
        cross_check_decision = input("Perform cross-checks? (yes/no): ").strip().lower()
        if cross_check_decision == "yes":
            print("Cross-checks performed!")
            return True
        else:
            return False
