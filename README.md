# RunSmart AI — adaptive-running-coach

Final project for the Building AI course: AI-powered personalized running coach for adaptive training and recovery recommendations.

![image of RunSmart AI](/runsmart-ai-banner.png.png)

## Summary

RunSmart AI is an AI-powered running coach that dynamically adapts training plans based on a runner’s physical condition, recovery, sleep, fatigue, and activity history. Instead of following a fixed program, the system continuously personalizes recommendations for any race distance or running goal.

## Background

Many running plans available online are static. They assume that every runner progresses in the same way and can follow identical sessions regardless of lifestyle, recovery, stress, or other physical activities.

In reality, runners often face changing conditions:

* poor sleep
* muscle fatigue
* stress or lack of recovery
* injuries or pain
* additional sports activities (CrossFit, cycling, gym, etc.)
* changing fitness levels

This can lead to overtraining, injury, or slow progress.

My personal motivation comes from practicing sports regularly and seeing how difficult it can be to follow rigid training plans while balancing recovery and other activities. Training should adapt to people, not the opposite.

This topic is interesting because personalized coaching is still limited and AI can help create adaptive recommendations based on real-world data.

## How is it used?

Users define a goal:

* run a 5 km race
* prepare for a 10 km
* train for a half marathon
* improve endurance
* simply become more active

The user connects different data sources such as smart watches, activity trackers or manually enters information.

RunSmart AI analyzes the data continuously and adjusts the plan.

Example:

* today's plan includes interval training
* the user slept poorly
* resting heart rate is unusually high
* yesterday included a demanding CrossFit session
* fatigue level is high

Instead of forcing an intense workout, RunSmart AI may recommend:

* an easy recovery run
* mobility exercises
* complete rest
* a lighter session

Potential users:

* beginner runners
* intermediate runners
* multi-sport athletes
* people preparing races
* health-conscious users

## Data sources and AI methods

Possible data sources:

| Data               | Source               | Usage               |
| ------------------ | -------------------- | ------------------- |
| Distance           | Smart watch          | Training load       |
| Pace               | Running applications | Progress tracking   |
| Heart rate         | Smart watch          | Recovery estimation |
| Sleep duration     | Smart watch          | Fatigue detection   |
| Weight             | Smart scale          | Fitness monitoring  |
| Muscle mass        | Smart scale          | Physical condition  |
| Previous sessions  | Sports applications  | Training history    |
| User fatigue       | Manual input         | Subjective recovery |
| Pain or discomfort | Manual input         | Injury prevention   |

Potential AI methods:

* fatigue prediction
* recommendation systems
* classification models
* anomaly detection
* personalized learning
* time-series analysis

A first prototype could use simple rules:

```
Sleep < 6h → increase fatigue score
High resting heart rate → possible poor recovery
Intense session yesterday → reduce workload
Pain reported → reduce intensity
```

Later versions could use machine learning models trained on historical user data.

## Challenges

RunSmart AI does not replace doctors, physiotherapists or certified coaches.

Limitations:

* wearable devices may provide inaccurate measurements
* fatigue is partly subjective
* recommendations may not generalize between users
* health data requires strong privacy protection
* injuries cannot be fully predicted

Ethical considerations:

* users should control their personal data
* recommendations should remain conservative
* transparency is important so users understand decisions

## What next?

Possible future improvements:

1. Build a manual prototype
2. Connect wearable devices APIs
3. Create a fatigue score
4. Generate adaptive weekly plans
5. Add nutritional recommendations
6. Test with real users
7. Improve recommendations using machine learning
8. Add conversational AI features

Long-term, RunSmart AI could become a complete digital coach for endurance athletes.

Skills needed:

* machine learning
* data science
* sports science
* mobile development
* data visualization

## Acknowledgments

Sources of inspiration:

* Garmin Connect
* Strava
* Apple Health
* endurance training principles
* Building AI course

No external code or datasets are used in the first version of this project.

Future open-source resources and contributors will be properly credited.
