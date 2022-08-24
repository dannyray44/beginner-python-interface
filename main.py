import json
from rapid_api import API_Football, Arbitrage_Betting_Calculator
from datetime import datetime, timedelta

def future_date_string(days_in_future = 1) -> str:
    return datetime.strftime(datetime.now() + timedelta(days=days_in_future), "%Y-%m-%d")

def get_future_odds(days_in_future = 1):
    date_str = future_date_string(days_in_future)
    raw_future_data = API_Football(f"/v3/odds?date={date_str}").send_json()
    return json.loads(raw_future_data)

def get_fixture_details(fixture_id: int):
    raw_fixture_data = API_Football(f"/v3/fixtures?id={fixture_id}").send_json()
    py_fixture_data = json.loads(raw_fixture_data)
    return py_fixture_data

def send_event_to_calculator(event):

    #format event to be accepted by calculator API
    formatted_event = {
        'bookmakers': event['bookmakers']
    }
    event = formatted_event
    json_string = json.dumps(event, indent=2)

    raw_results_data = Arbitrage_Betting_Calculator("/Soccer", "POST").send_json(json_string)
    py_results_data = json.loads(raw_results_data)
    return py_results_data

def main():
    future_events_data = get_future_odds()['response']

    for event_index, event_data in enumerate(future_events_data):
        optimal_betting_strat = send_event_to_calculator(event_data)
        if optimal_betting_strat['profit'] >= 0:
            details = get_fixture_details(event_data['fixture']['id'])

            output_message = json.dumps(optimal_betting_strat, indent=4) + '\n\n' + json.dumps(details, indent=4)

            with open(f"Result_{event_index}", 'w') as file:
                file.write(output_message)

            print("\n\n\n\n")
            print(output_message)
            

if __name__ == "__main__":
    main()