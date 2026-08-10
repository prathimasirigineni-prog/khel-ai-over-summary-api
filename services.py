from utils import calculate_over_total


INNINGS = {
    1: {
        "innings_id": 1,
        "overs": [
            {
                "over_number": 1,
                "balls": [
                    {
                        "over_ball": "1.1",
                        "runs": 1,
                        "extras": 0,
                        "wicket": False,
                        "label": "1 run"
                    },
                    {
                        "over_ball": "1.2",
                        "runs": 4,
                        "extras": 0,
                        "wicket": False,
                        "label": "FOUR"
                    },
                    {
                        "over_ball": "1.3",
                        "runs": 0,
                        "extras": 0,
                        "wicket": False,
                        "label": "Dot ball"
                    },
                    {
                        "over_ball": "1.4",
                        "runs": 2,
                        "extras": 0,
                        "wicket": False,
                        "label": "2 runs"
                    },
                    {
                        "over_ball": "1.5",
                        "runs": 0,
                        "extras": 0,
                        "wicket": True,
                        "label": "WICKET"
                    },
                    {
                        "over_ball": "1.6",
                        "runs": 1,
                        "extras": 0,
                        "wicket": False,
                        "label": "1 run"
                    }
                ]
            },
            {
                "over_number": 2,
                "balls": [
                    {
                        "over_ball": "2.1",
                        "runs": 2,
                        "extras": 0,
                        "wicket": False,
                        "label": "2 runs"
                    },
                    {
                        "over_ball": "2.2",
                        "runs": 1,
                        "extras": 0,
                        "wicket": False,
                        "label": "1 run"
                    },
                    {
                        "over_ball": "2.3",
                        "runs": 4,
                        "extras": 0,
                        "wicket": False,
                        "label": "FOUR"
                    },
                    {
                        "over_ball": "2.4",
                        "runs": 0,
                        "extras": 0,
                        "wicket": False,
                        "label": "Dot ball"
                    },
                    {
                        "over_ball": "2.5",
                        "runs": 1,
                        "extras": 1,
                        "wicket": False,
                        "label": "Wide"
                    },
                    {
                        "over_ball": "2.6",
                        "runs": 3,
                        "extras": 0,
                        "wicket": False,
                        "label": "3 runs"
                    }
                ]
            }
        ]
    }
}


def get_over_summary(innings_id: int):
    innings = INNINGS.get(innings_id)

    if innings is None:
        return None

    summaries = []

    for over in innings["overs"]:
        runs, wickets, extras = calculate_over_total(
            over["balls"]
        )

        summaries.append({
            "over_number": over["over_number"],
            "runs": runs,
            "wickets": wickets,
            "extras": extras,
            "balls": over["balls"]
        })

    return summaries