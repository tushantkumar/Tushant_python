import json
team_data={
  1: {
    "Team": {
      "1": "Aus",
      "2": "India"
    },
    "Aus_Team": {
      "Captain": {
        "Aaron": "Captain",
        "Age": 34,
        "Score": [
          {
            "T20": "Na"
          }
        ]
      }
    },
    "India_team": {
      "Captain": {
        "Virat":"Captain",
        "Age":32,
        "Score": [
          {
            "T20": 40
          }
        ]
      }
    }
  }
}

print(team_data)      

with open('D:\\Sify documents\\Python training\\Assignment\\Day5 Assignment\\team.json','w') as obj:
    json.dump(team_data, obj)

