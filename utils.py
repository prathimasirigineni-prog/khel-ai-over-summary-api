def calculate_over_total(balls: list):
    total_runs = 0
    wickets = 0
    extras = 0

    for ball in balls:
        total_runs += ball.runs
        extras += ball.extras

        if ball.wicket:
            wickets += 1

    return total_runs, wickets, extras