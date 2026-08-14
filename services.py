from collections import defaultdict


def get_over_summary(innings):
    if not innings.ball_events:
        return None

    overs = defaultdict(list)

    for ball in innings.ball_events:
        over_number = int(ball.over_ball.split(".")[0])
        overs[over_number].append(ball)

    summaries = []

    for over_number in sorted(overs):
        balls = overs[over_number]

        total_runs = sum(
            ball.runs
            for ball in balls
        )

        total_wickets = sum(
            1
            for ball in balls
            if ball.wicket
        )

        total_extras = sum(
            ball.extras
            for ball in balls
        )

        ball_summaries = []

        for ball in balls:
            ball_summaries.append({
                "over_ball": ball.over_ball,
                "striker": ball.striker,
                "bowler": ball.bowler,
                "runs": ball.runs,
                "extras": ball.extras,
                "wicket": ball.wicket,
                "label": ball.label,
            })

        summaries.append({
            "over_number": over_number,
            "runs": total_runs,
            "wickets": total_wickets,
            "extras": total_extras,
            "balls": ball_summaries,
        })

    return summaries