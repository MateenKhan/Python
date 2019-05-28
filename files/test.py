from pathlib import Path

path = Path("../excercise")
for file in path.glob("*.py"):
    print(file)