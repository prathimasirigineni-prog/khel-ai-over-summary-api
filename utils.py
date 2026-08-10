def calculate_over_total(balls: list):
    total_runs = 0
    wickets = 0
    extras = 0

    for ball in balls:
        total_runs += ball.get("runs", 0)
        extras += ball.get("extras", 0)

        if ball.get("wicket", False):
            wickets += 1

    return total_runs, wickets, extras