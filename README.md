# Umbrella Decision Agent ☔️

A simple AI agent that checks the live weather for any city and provides a clear, helpful recommendation on whether to carry an umbrella. This project demonstrates the use of external APIs, serverless functions, and a simple reasoning engine.

---

## Live Demo & Screenshot

**Try the live agent here:** [**https://umbrella-decision-agent-rho.vercel.app/**](https://umbrella-decision-agent-rho.vercel.app/)

*(Remember to replace the URL above with your own Vercel URL!)*

<br>

![App Screenshot](https://i.imgur.com/w1oB5uQ.png)

*(To add your own screenshot, just drag and drop your image file into this text editor on GitHub!)*

---

## How It Works

This application functions as a simple agent by following a clear logic loop:
1.  **Observe:** It takes the user's input (a city name).
2.  **Gather Data:** It fetches real-time weather data for that city from the OpenWeatherMap API.
3.  **Reason:** It analyzes the data based on a simple set of rules (e.g., if the weather condition is "Rain," "Drizzle," or "Thunderstorm," an umbrella is needed).
4.  **Execute:** It presents a clear "Yes" or "No" recommendation to the user in a clean and simple UI.

---

## Tech Stack

-   **Frontend:** HTML, CSS, Vanilla JavaScript
-   **Backend:** Python Serverless Function
-   **Framework:** Flask
-   **API:** OpenWeatherMap API for live weather data
-   **Deployment:** Vercel

---

## Running The Project Locally

To run this project on your own machine, follow these steps:

**1. Clone the repository:**
```bash
git clone [https://github.com/krish-23CH10035/umbrella-decision-agent.git](https://github.com/krish-23CH10035/umbrella-decision-agent.git)
cd umbrella-decision-agent
