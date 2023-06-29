import requests

# Get the list of all leetcode problems
url = "https://leetcode.com/problems/"
response = requests.get(url)
problems = response.json()
# Sort the problems by difficulty
'''problems.sort(key=lambda problem: problem["difficulty"])

# Print the list of problems
for problem in problems:
  print(problem["title"])'''