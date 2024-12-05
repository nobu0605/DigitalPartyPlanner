import sys
from urllib.parse import parse_qs

# Predefined party items with their values
party_items = [
    {"name": "Cake", "value": 20},
    {"name": "Balloons", "value": 21},
    {"name": "Music System", "value": 10},
    {"name": "Lights", "value": 5},
    {"name": "Catering Service", "value": 8},
    {"name": "DJ", "value": 3},
    {"name": "Photo Booth", "value": 15},
    {"name": "Tables", "value": 7},
    {"name": "Chairs", "value": 12},
    {"name": "Drinks", "value": 6},
    {"name": "Party Hats", "value": 9},
    {"name": "Streamers", "value": 18},
    {"name": "Invitation Cards", "value": 4},
    {"name": "Party Games", "value": 2},
    {"name": "Cleaning Service", "value": 11},
]

def calculate_base_code(selected_indices):
    if not selected_indices:
        return 0
    base_code = party_items[selected_indices[0]]["value"]
    for index in selected_indices[1:]:
        base_code &= party_items[index]["value"]
    return base_code

def modify_code(base_code):
    message = ""
    if base_code == 0:
        base_code += 5
        message = "Epic Party Incoming!"
    elif base_code > 5:
        base_code -= 2
        message = "Let's keep it classy!"
    else:
        message = "Chill vibes only!"
    return base_code, message

def generate_html(selected_items, base_code, adjusted_code, message):
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Party Planner Results</title>
    </head>
    <body>
        <h1>Party Planner Results</h1>
        <h2>Selected Items</h2>
        <p>{', '.join(selected_items)}</p>
        <h2>Base Party Code</h2>
        <p>{base_code}</p>
        <h2>Final Party Code</h2>
        <p>{adjusted_code}</p>
        <h2>Message</h2>
        <p>{message}</p>
    </body>
    </html>
    """
    return html

# Main script execution
if __name__ == "__main__":
    # Read query string from command-line arguments
    if len(sys.argv) < 2:
        print("Content-type: text/html\n")
        print("<html><body><h1>Error</h1><p>No query string provided. Please pass query parameters.</p></body></html>")
        sys.exit()

    query_string = sys.argv[1]
    query_params = parse_qs(query_string)

    # Get indices from query parameters
    indices_input = query_params.get("indices[]", [])
    if indices_input:
        try:
            selected_indices = list(map(int, indices_input))
            selected_items = [party_items[i]["name"] for i in selected_indices]
            base_code = calculate_base_code(selected_indices)
            adjusted_code, message = modify_code(base_code)
            print("Content-type: text/html\n")
            print(generate_html(selected_items, base_code, adjusted_code, message))
        except Exception as e:
            print("Content-type: text/html\n")
            print(f"<html><body><h1>Error</h1><p>{e}</p></body></html>")
    else:
        print("Content-type: text/html\n")
        print("<html><body><h1>Error</h1><p>No indices provided. Please select party items.</p></body></html>")
