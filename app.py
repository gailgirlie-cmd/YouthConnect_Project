from flask import Flask, render_template, request
import os

app = Flask(__name__)

# HOME PAGE
@app.route("/")
def home():
    return render_template("index.html")

# ABOUT PAGE
@app.route("/about")
def about():
    return render_template("about.html")

# GUIDANCE PAGE
@app.route("/guidance")
def guidance():
    return render_template("guidance.html")

# DASHBOARD / SYSTEM PAGE
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# REFLECTION PAGE (CORE FUNCTION)
@app.route("/reflection", methods=["GET", "POST"])
def reflection():
    selected = None
    result = None

    responses = {
        "procrastination": {
            "insight": "You are avoiding something that feels mentally heavy.",
            "emotion": "Avoidance often comes from pressure or fear.",
            "action": "Start with just 10 minutes of the task.",
            "reflection": "What is the smallest possible step you can take right now?",
            "grounding": "You are not behind — you are restarting focus.",
            "faith": "Small steps still count as progress."
        },
        "stress": {
            "insight": "Your mind is overloaded with pressure.",
            "emotion": "Stress happens when everything feels urgent.",
            "action": "Write down 3 priorities only.",
            "reflection": "What truly matters today?",
            "grounding": "Pause and breathe slowly for 60 seconds.",
            "faith": "Peace is still available even in pressure."
        },
        "fear": {
            "insight": "Fear is often uncertainty about outcomes.",
            "emotion": "It creates hesitation and self-doubt.",
            "action": "Take one action despite fear.",
            "reflection": "What would you do if fear was smaller?",
            "grounding": "You are safe in this moment.",
            "faith": "Courage grows through small steps."
        },
        "motivation": {
            "insight": "Motivation rises and falls naturally.",
            "emotion": "You may feel stuck or disconnected.",
            "action": "Do one small task immediately.",
            "reflection": "What action would restart momentum?",
            "grounding": "You don’t need motivation to begin.",
            "faith": "Purpose returns through action."
        },
        "identity": {
            "insight": "You are in a phase of self-discovery.",
            "emotion": "Uncertainty is part of growth.",
            "action": "Write down your core values.",
            "reflection": "Who are you becoming?",
            "grounding": "You are forming, not lost.",
            "faith": "You are being shaped with purpose."
        },
        "loneliness": {
            "insight": "You may feel disconnected from others.",
            "emotion": "Loneliness can feel heavy and silent.",
            "action": "Reach out to one person today.",
            "reflection": "Who makes you feel safe?",
            "grounding": "You are not truly alone.",
            "faith": "You are seen and valued."
        },
        "pressure": {
            "insight": "Too many expectations may be weighing you down.",
            "emotion": "Pressure creates mental overload.",
            "action": "Focus on one priority only.",
            "reflection": "What can you ignore for now?",
            "grounding": "Slow down your thoughts.",
            "faith": "You are allowed to breathe."
        }
    }

    if request.method == "POST":
        selected = request.form.get("challenge")
        result = responses.get(selected, {
            "insight": "Processing your reflection...",
            "emotion": "Take a moment to breathe.",
            "action": "Start small today.",
            "reflection": "What is in your control?",
            "grounding": "Pause and reset.",
            "faith": "You are not alone in this process."
        })

    return render_template("reflection.html", selected=selected, result=result)


# RENDER SAFE START
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
