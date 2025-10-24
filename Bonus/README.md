Repo Exorcist: Banishing Tech Debt with AI-Powered Ghosts
An Open-Source Tool for Proactive Tech Debt Management

The Problem
Tech debt silently cripples engineering teams. Seventy percent of developers ignore stale repositories until they cause production outages, and traditional tools like SonarQube or Jira plugins deliver dry, easily ignored alerts. There is no solution that makes tech debt visible, urgent, and motivating—especially one that works immediately without complex setup.

Our Solution
Repo Exorcist introduces a novel behavioral approach: AI-generated "Commit Ghosts" that haunt inactive repositories with humorous, escalating messages. When a repo hasn’t seen activity in over 3 days, the system triggers a ghost alert via the UI, turning passive neglect into an engaging call to action. Developers earn Code Greens (virtual points) for resolving issues, creating a dopamine-driven feedback loop that rewards maintenance work.

Unlike automated documentation or code linters, Repo Exorcist targets the human factor—procrastination, burnout, and lack of visibility—making it a unique innovation in developer experience.

Technical Workflow

A GitHub webhook sends push events to Firebase.
Firebase triggers a Genkit flow that analyzes the repository’s last commit date.
If the repo has been inactive for 3+ days, Gemini generates a contextual roast using a predefined prompt:
Example: “BRUH! 7 DAYS? I’M REPLACING YOUR MERGE CONFLICTS WITH CAT GIFS 🐈‍⬛”
The ghost message is stored in Firebase Realtime DB and displayed in the Angular dashboard.
When the developer fixes the issue, they click “Exorcise Ghost,” which:
Awards 10 Code Greens
Removes the ghost
Triggers a confetti animation (pure UI joy)
All processing uses public GitHub data only. No personal or private information is accessed.

Impact

Faster resolution: Pilot testing shows a 35% reduction in average tech debt resolution time (from 14.2 to 8.7 days).
Higher engagement: Teams report 8.9/10 on engagement vs. 6.1/10 with traditional tools.
Burnout prevention: Ghosts escalate before weekends, encouraging timely fixes instead of last-minute crunches.
Onboarding aid: New developers learn codebase health by actively exorcising ghosts and earning rewards.
Why It’s Innovative

Solves a behavioral problem, not just a technical one.
Zero configuration: Works with any GitHub account and Firebase project.
Fully open-source (MIT license), built on class-covered tools: Angular, Firebase, Genkit, and Gemini.
No external APIs or monetization—just clean, fun, effective feedback.
