# Parallelepipeds Calculation

## 📌 Project Overview
This project calculates various geometric properties of parallelepipeds, such as diagonal length, volume, surface area, and angles. It reads input dimensions from a JSON file, processes them using Python scripts, and saves the results in output JSON files.

## 📂 Project Structure
```
my_project/
│-- main.py
│-- utils/
│   │-- functions.py
│   │-- statistics.py
│-- parallelepipeds.json
│-- outputs/
│   │-- characteristics.json (generated)
│   │-- statistics.json (generated)
│-- .gitignore
│-- README.md
```

### 📜 Files Explanation
- **main.py** - The main script that loads input data, processes calculations, and generates JSON output.
- **utils/functions.py** - Contains functions to calculate diagonal, volume, surface area, and other properties.
- **utils/statistics.py** - Computes average values from processed data.
- **parallelepipeds.json** - Input file containing parallelepiped dimensions.
- **outputs/** - Stores generated JSON files (`characteristics.json` and `statistics.json`).
- **.gitignore** - Prevents output JSON files from being committed to Git.
- **README.md** - Documentation for the project.

## 🚀 How to Run
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/Nurslatip/parallelepipeds.git
cd parallelepipeds
```

### 2️⃣ Install Python (if not installed)
Ensure you have Python 3 installed.
```sh
python --version
```

### 3️⃣ Run the Script
```sh
python main.py
```

### 4️⃣ Check Output Files
Once executed, the following output files will be generated inside `outputs/`:
- **characteristics.json** - Contains detailed calculations for each parallelepiped.
- **statistics.json** - Contains average characteristics.

## 🔥 Example JSON Input (`parallelepipeds.json`)
```json
{
  "box1": {"a": 3, "b": 4, "c": 5},
  "box2": {"a": 6, "b": 8, "c": 10}
}
```

## 📌 Git Usage Guide
### Ignore Output Files
Ensure your `.gitignore` includes:
```
outputs/*.json
```

### Push Changes to GitHub
```sh
git add .
git commit -m "Updated scripts"
git push origin main
```

## 📬 Contact
If you have any questions, feel free to reach out! 🚀

