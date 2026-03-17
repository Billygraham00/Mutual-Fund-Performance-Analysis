<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Mutual Fund Performance & Risk Analysis</title>
</head>
<body>

<h1>📊 Mutual Fund Performance & Risk Analysis</h1>

<h2>📌 Project Overview</h2>
<p>
This project focuses on <b>data cleaning, transformation, and analysis of mutual fund datasets</b> 
to derive meaningful insights related to performance and risk metrics.
</p>

<p>The pipeline includes:</p>
<ul>
    <li>Data preprocessing using Python</li>
    <li>Logging for tracking execution</li>
    <li>Cleaned dataset generation for further analysis (Power BI dashboards)</li>
</ul>

<hr>

<h2>📁 Project Structure</h2>
<pre>
📦 Mutual-Fund-Performance-Analysis
 ┣ 📂 data/
 ┃ ┣ raw_data.csv
 ┃ ┗ cleaned_data.csv
 ┣ 📂 src/
 ┃ ┣ main.py
 ┃ ┗ log_code.py
 ┣ 📂 dashboard/
 ┃ ┗ dashboard.pbix
 ┣ 📂 logs/
 ┣ 📂 assets/
 ┗ README.md
</pre>

<hr>

<h2>⚙️ Technologies Used</h2>
<ul>
    <li>Python 🐍</li>
    <li>Pandas</li>
    <li>NumPy</li>
    <li>Logging Module</li>
    <li>Power BI 📊</li>
</ul>

<hr>

<h2>🔧 Features</h2>

<h3>✅ Data Cleaning Pipeline</h3>
<ul>
    <li>Handles missing values ("-", "Nil", etc.)</li>
    <li>Converts percentage columns to numeric</li>
    <li>Standardizes financial metrics</li>
    <li>Converts date columns to proper format</li>
    <li>Removes inconsistencies and duplicates</li>
</ul>

<h3>✅ Logging System</h3>
<ul>
    <li>Tracks each step of execution</li>
    <li>Helps debug errors efficiently</li>
    <li>Log files generated per script</li>
</ul>

<hr>

<h2>📊 Data Processing Workflow</h2>
<ol>
    <li>Load dataset</li>
    <li>Clean missing & invalid values</li>
    <li>Convert data types (percentages, numeric, dates)</li>
    <li>Handle categorical inconsistencies</li>
    <li>Save cleaned dataset</li>
</ol>

<hr>

<h2>🚀 How to Run the Project</h2>

<h3>1️⃣ Clone the Repository</h3>
<pre>
git clone https://github.com/your-username/mutual-fund-analysis.git
cd mutual-fund-analysis
</pre>

<h3>2️⃣ Install Dependencies</h3>
<pre>
pip install pandas numpy
</pre>

<h3>3️⃣ Run the Script</h3>
<pre>
python src/main.py
</pre>

<hr>

<h2>📂 Input & Output</h2>

<h3>Input</h3>
<ul>
    <li>Raw dataset: <b>data/raw_data.csv</b></li>
</ul>

<h3>Output</h3>
<ul>
    <li>Cleaned dataset: <b>data/cleaned_data.csv</b></li>
    <li>Log files generated in <b>/logs</b> directory</li>
</ul>

<hr>

<h2>📊 Dashboard</h2>
<p>
The cleaned dataset is used to build an interactive <b>Power BI dashboard</b> including:
</p>
<ul>
    <li>Fund performance comparison</li>
    <li>Risk metrics (Sharpe, Beta, Alpha)</li>
    <li>Asset allocation insights</li>
    <li>Time-based returns analysis</li>
</ul>

<h3>📸 Dashboard Preview</h3>

<img src="assets/Dashboard 1.jpg" width="800"/>
<br><br>

<img src="assets/dashboard2.png" width="800"/>
<br><br>

<img src="assets/dashboard3.png" width="800"/>
<br><br>

<img src="assets/dashboard4.png" width="800"/>
<br><br>

<img src="assets/dashboard5.png" width="800"/>

<hr>

<h2>📈 Key Insights</h2>
<ul>
    <li>Funds with higher returns generally show higher volatility (risk-return tradeoff)</li>
    <li>Lower expense ratio funds tend to perform better in the long term</li>
    <li>Large-cap funds are more stable compared to small-cap funds</li>
    <li>Sharpe ratio is crucial for evaluating risk-adjusted performance</li>
</ul>

<hr>

<h2>🧠 Learning Outcomes</h2>
<ul>
    <li>Real-world data cleaning techniques</li>
    <li>Handling financial datasets</li>
    <li>Building scalable data pipelines</li>
    <li>Integrating Python with Power BI</li>
</ul>

<hr>

<h2>📬 Contact</h2>
<p>
If you have any questions or suggestions, feel free to connect!
</p>

<hr>

<h2>⭐ If you like this project</h2>
<p>Give it a ⭐ on GitHub!</p>

</body>
</html>
