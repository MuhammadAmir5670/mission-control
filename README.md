## Mission Control

We would like to thank you for taking the time to complete this assignment. We believe this to be an effective way of allowing you to show us your skills, on your own time, without the pressure of someone looking over your shoulder. Your code will be used to help us decide if we'd like to proceed with the interview process. Please understand that completing this assignment doesn't guarantee follow up interviews. We will keep you posted either way. Reach out to your point of contact at Doximity with any questions.

_Even though there is no strict time limit, you should expect to take 3-5 hours to complete the assignment. Have fun!_

## How to Submit your Completed Assignment

1. Fork the `mission-control` repository by visiting [this page](https://gitlab.com/doximity-review/mission-control/-/forks) and clicking the fork button on the top right.

   (FYI, we use Gitlab instead of GitHub for this assignment, because it allows forking without making all forks publicly visible.)
2. Create a new branch by visiting https://gitlab.com/`YOUR-GITLAB`/mission-control/-/branches - name your branch after your `firstname-lastname`.
3. At this point, you can grab the SSH URL at the top of https://gitlab.com/`YOUR-GITLAB`/mission-control, clone the repository locally, and do your work on the newly created branch.
4. Visit https://gitlab.com/`YOUR-GITLAB`/mission-control/-/project_members under "Invite Member" type in `doximity-review` under "GitLab member", select a role of `Maintainer`, and click "Invite".
5. Visit https://gitlab.com/<YOUR_USERNAME>/mission-control/edit and enable: Merge Requests (don't forget to save) under Visibility, Project Features, Permissions.
6. Once you are ready to submit your work, go back to https://gitlab.com/`YOUR-GITLAB`/mission-control and click on "Create merge Request" on the top right.
7. From the page above, title and describe your assignment. Then select `doximity-review` from the "Assignee" dropdown, and click the "Submit merge request" button.

## Launch Requirements

1. **Use Python**. Follow PEP 8 for style guidelines. Use 4 spaces for indentation.
2. Utilize proper object-oriented principles, abstraction, and design patterns.
3. Focus on creating a text-based game rather than a physics simulation.
4. Implement a CLI (Command Line Interface) for the game. The player should be able to play multiple missions. Display a summary of each mission at the end and a final summary for all missions.
5. The game should be implemented with an in-memory data store.

## Mission Specifications

#### Conducting the Flight into Low Earth Orbit

1. Travel Distance: 160 kilometers
2. Payload capacity: 50,000 kilograms including the rocket itself
3. Fuel capacity: 1,514,100 liters of fuel, already included in the payload total
4. Burn rate: 168,233 liters per minute
5. Average speed: 1500 kilometers/hr

#### Rocket Launch System Stages

1. Enable stage 1 afterburner
2. Disengage release structure
3. Cross-checks
4. Launch

#### Active Mission Controls

1. Manually transition between launch stages in the expected order.
2. Ability to safely abort the launch after stage 1 and retry.
3. One in every 3rd launch will require an abort and retry after stage 1. Randomize when it happens.
4. One in every 5th launch will explode. Randomize when it occurs.

#### Instrumentation Information at the End of Each Mission

1. Total distance traveled (0 if aborted, random if exploded).
2. Total travel time (same as above).

#### Final Summary

1. Total distance traveled for all missions combined.
2. Number of abort and retries for all missions combined.
3. Number of explosions for all missions combined.
4. Total fuel burned for all missions combined.
5. Total flight time for all missions combined.

#### Sample Session:

```
Welcome to Mission Control!
Mission plan:
  Travel distance:  160.0 km
  Payload capacity: 50,000 kg
  Fuel capacity:    1,514,100 liters
  Burn rate:        168,240 liters/min
  Average speed:    1,500 km/h
  Random seed:      12
What is the name of this mission? Minerva
Would you like to proceed? (Y/n) Y
Engage afterburner? (Y/n) Y
Afterburner engaged!
Release support structures? (Y/n) Y
Support structures released!
Perform cross-checks? (Y/n) Y
Cross-checks performed!
Launch? (Y/n) Y
Launched!
Mission status:
  Current fuel burn rate: 151,416 liters/min
  Current speed: 1,350 km/h
  Current distance traveled: 12.5 km
  Elapsed time: 0:00:30
  Time to destination: 0:05:54
Mission status:
  Current fuel burn rate: 153,098 liters/min
  Current speed: 1,365 km/h
  Current distance traveled: 24.82 km
  Elapsed time: 0:01:00
  Time to destination: 0:05:27

(...)

Mission status:
  Current fuel burn rate: 164,875 liters/min
  Current speed: 1,470 km/h
  Current distance traveled: 137.34 km
  Elapsed time: 0:05:30
  Time to destination: 0:00:55
Mission status:
  Current fuel burn rate: 154,780 liters/min
  Current speed: 1,380 km/h
  Current distance traveled: 149.93 km
  Elapsed time: 0:06:00
  Time to destination: 0:00:25
Mission summary:
  Total distance traveled: 160.36 km
  Number of abort and retries: 0/0
  Number of explosions: 0
  Total fuel burned: 1,079,091 liters
  Flight time: 0:06:25
Would you like to run another mission? (Y/n) Y
Mission plan:
  Travel distance:  160.0 km
  Payload capacity: 50,000 kg
  Fuel capacity:    1,514,100 liters
  Burn rate:        168,240 liters/min
  Average speed:    1,500 km/h
  Random seed:      12
What is the name of this mission? Minerva II
Would you like to proceed? (Y/n) Y
Engage afterburner? (Y/n) Y
Afterburner engaged!
Release support structures? (Y/n) Y
Support structures released!
Perform cross-checks? (Y/n) Y
Cross-checks performed!
Launch? (Y/n) Y
Mission aborted!
Mission summary:
  Total distance traveled: 160.36 km
  Number of abort and retries: 1/1
  Number of explosions: 0
  Total fuel burned: 1,079,091 liters
  Flight time: 0:06:25
Would you like to run another mission? (Y/n) n
```

### Conclusion

By following these specifications, we can create a Python version of the rocket launch game, allowing users to experience the thrill of conducting a space mission from the comfort of their command line.
