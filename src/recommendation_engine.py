def calculate_recovery_score(sleep_hours, resting_hr_delta, fatigue_level, intense_training_yesterday):
    score = 100

    if sleep_hours < 6:
        score -= 25
    elif sleep_hours < 7:
        score -= 10

    if resting_hr_delta > 8:
        score -= 25
    elif resting_hr_delta > 4:
        score -= 10

    if fatigue_level >= 8:
        score -= 25
    elif fatigue_level >= 5:
        score -= 10

    if intense_training_yesterday:
        score -= 15

    return max(0, min(score, 100))


def recommend_workout(recovery_score, planned_workout):
    if recovery_score >= 75:
        return planned_workout

    if recovery_score >= 50:
        return "Easy run: 30-40 minutes at conversational pace"

    if recovery_score >= 30:
        return "Active recovery: mobility, stretching, or light walk"

    return "Rest day: focus on sleep, hydration, and recovery"


def main():
    planned_workout = "Interval session: 8 x 400m"

    recovery_score = calculate_recovery_score(
        sleep_hours=5.5,
        resting_hr_delta=7,
        fatigue_level=8,
        intense_training_yesterday=True
    )

    recommendation = recommend_workout(recovery_score, planned_workout)

    print("Recovery score:", recovery_score)
    print("Planned workout:", planned_workout)
    print("Recommendation:", recommendation)


if __name__ == "__main__":
    main()
