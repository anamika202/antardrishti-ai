# Antardrishti AI (अन्तर्दृष्टि AI)
> **Empathetic, Privacy-First Reflective AI Journaling Companion**  
> *Built for Google Cloud Gen AI Academy APAC Hackathon*

---

## 🌟 Overview
**Antardrishti AI** is a full-stack mental well-being companion designed to provide private, mindful journaling with intelligent emotional reflection. Leveraging Google Cloud's modern serverless stack, Firebase, and Gemini models, it allows users to safely log thoughts, track emotional patterns over time, and receive gentle, empathetic guidance.

---

## 🏗️ Architecture & Tech Stack

- **Frontend:** Vanilla JS / Responsive Single Page Application (SPA), Tailwind CSS, Firebase SDK (Web).
- **Authentication:** Firebase Authentication (Email/Password & Google Sign-In with isolated user contexts).
- **Database:** Google Cloud Firestore (Strict per-user collection isolation via Security Rules).
- **Backend & Model Reasoning:** Python (Flask/FastAPI) powered by **Gemini 1.5 Flash** for low-latency multi-turn reflective chats.
- **Key Extensions:** Multi-dimensional emotional sentiment pattern analytics & semantic journal reflection.
- **Secrets Management:** Secured environment variables & Google Cloud Secret Manager (`GEMINI_API_KEY`).
- **Containerization & Deployment:** Dockerized container built for **Google Cloud Run**.

---

## 🔒 Security & Firestore Tenant Isolation

Each journal entry is stored within isolated user collections protected by strict Firestore Security Rules, ensuring zero cross-tenant data leakage:

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /users/{userId}/journals/{journalId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
  }
}
