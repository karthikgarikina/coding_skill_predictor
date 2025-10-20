# 🧠 Coding Skill Predictor

The **Coding Skill Predictor** is a Machine Learning web application built using **Streamlit**.  
It predicts a user's coding skill level — *Beginner*, *Intermediate*, or *Advanced* — based on their performance across platforms like **LeetCode**, **GeeksforGeeks**, **CodeChef**, and **HackerRank**.

---

## 🚀 Live Demo  
🎯 **Try it here:** [Coding Skill Predictor (Live App)](https://codingskillpredictor-fusudw95jpr5vogbmhdu2m.streamlit.app/)

---

## 🧩 Features
- Predicts skill level based on multiple platform stats.  
- Simple and interactive web interface.  
- Built using a trained Machine Learning model.  
- Lightweight and deployable via Streamlit Cloud.

---

## 🧠 Tech Stack
- **Frontend:** Streamlit  
- **Backend / ML:** Python, Scikit-learn, Pandas, NumPy  
- **Deployment:** Streamlit Cloud  
- **Version Control:** Git & GitHub  

---

## 📊 Input Features
| Platform | Feature | Example |
|-----------|----------|----------|
| LeetCode | Total Problems Solved | 120 |
| GeeksforGeeks | Total Problems | 60 |
| CodeChef | Rating | 1300 |
| HackerRank | Badges | 5 |

---

## 🧮 Skill Classification
| Level | Criteria |
|--------|-----------|
| **Beginner** | Below standard thresholds |
| **Intermediate** | LeetCode 100–150, GFG ≥ 50, CodeChef ≈ 1200–1300, HR badges ≥ 5 |
| **Advanced** | LeetCode ≥ 250, GFG ≥ 100, CodeChef ≥ 1400, HR badges ≥ 5 |

> ⚠️ Note: "Advanced" means the user is ready to learn advanced topics — not necessarily an expert yet.

---

## ⚙️ Installation (For Local Setup)

```bash
# Clone the repository
git clone https://github.com/your-username/coding-skill-predictor.git

# Navigate to project directory
cd coding-skill-predictor

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
