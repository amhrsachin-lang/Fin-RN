# Project Blueprint: Virtual Trading Android App

## 1. Tech Stack & Architecture

| Layer | Technology | Primary Purpose |
| :--- | :--- | :--- |
| **Mobile App (Frontend)** | React Native (Expo) | Cross-platform UI, rapid Android development. |
| **Charting Library** | `react-native-wagmi-charts` or `react-native-gifted-charts` | Smooth, interactive candlestick and line charts for stock/NAV data. |
| **State Management** | Zustand | Lightweight, un-opinionated state management for the user's wallet balance and active screen state. |
| **Database & Auth** | Firebase (Firestore & Auth) | Google Auth integration, real-time ledger updates, NoSQL document storage. |
| **Backend Engine** | Python (FastAPI) | Acts as a middleman to fetch real-time market data securely, calculate metrics, and update Firestore. |
| **Market Data** | `MFapi.in` & `yfinance` | Free, no-key data sources for Indian Mutual Funds and real-time stock quotes. |

---

## 2. Database Schema (Firestore)

### Collection: `users`
Stores the user profile and their current liquid virtual cash.
*   `uid` (String, Primary Key)
*   `displayName` (String)
*   `email` (String)
*   `liquidBalance` (Number) - *Starts at ₹1,00,000*
*   `totalPortfolioValue` (Number) - *Updated daily via backend*
*   `createdAt` (Timestamp)

### Collection: `holdings` (Sub-collection under `users/{uid}`)
Tracks currently owned assets to populate the user's portfolio UI.
*   `assetTicker` (String)
*   `assetName` (String)
*   `assetType` (String) - *Enum: "STOCK" or "MUTUAL_FUND"*
*   `averageBuyPrice` (Number)
*   `quantity` (Number)
*   `lastUpdated` (Timestamp)

### Collection: `transactions` (Sub-collection under `users/{uid}`)
An immutable ledger of every trade made by the user.
*   `transactionId` (String, Auto-ID)
*   `assetTicker` (String)
*   `type` (String) - *Enum: "BUY" or "SELL"*
*   `quantity` (Number)
*   `executionPrice` (Number)
*   `totalAmount` (Number)
*   `timestamp` (Timestamp)

---

## 3. App Screens & UI Flow

1.  **Authentication Screen:** Single button: "Sign in with Google". On first login, a Cloud Function automatically provisions their `users` document with ₹1,00,000.
2.  **Dashboard (Home):** Total Portfolio Value + Liquid Cash Available. A 7-day historical performance chart. Flat list of currently owned assets.
3.  **Market / Search Screen:** A search bar that queries your Python backend for stock tickers or mutual fund names. List of trending assets.
4.  **Asset Detail & Trade Screen:** Full-screen interactive price chart. Prominent BUY and SELL buttons. A bottom sheet to enter the quantity.

---

## 4. Backend Engineering (Python FastAPI)

### Core API Endpoints
*   `GET /api/search?q={query}` - Returns a clean list of matching assets.
*   `GET /api/asset/{ticker}` - Returns market price, day-change percentage, and chart data.
*   `POST /api/trade` - Validates `liquidBalance`, calculates total cost, deducts balance, updates `holdings`, and writes a log to `transactions`.

### Cron Jobs (Automated Tasks)
*   **End of Day (EOD) Sync:** Runs at 4:00 PM IST. Pulls closing prices for all holdings, recalculates `totalPortfolioValue`, and updates Firestore.

---

## 5. Development Phases

*   **Phase 1: Environment Setup** - Initialize Expo, configure Firebase Auth, build navigation shell.
*   **Phase 2: Backend & Database** - Deploy FastAPI script, write `yfinance` extraction logic, set up `/api/trade`.
*   **Phase 3: UI & Data Binding** - Build Asset Detail screen, integrate charts, connect Zustand, wire Buy/Sell buttons.
*   **Phase 4: Polish** - Add haptic feedback, implement Leaderboard, prepare Android APK/AAB.