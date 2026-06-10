import React, { useState } from "react";
import "./App.css";

function App() {
  const [page, setPage] = useState("home");

  const renderPage = () => {
    switch (page) {
      case "training":
        return <Training />;
      case "security":
        return <Security />;
      case "dashboard":
        return <Dashboard />;
      default:
        return <Home setPage={setPage} />;
    }
  };

  return (
    <div>
      <nav>
        <button onClick={() => setPage("home")}>Home</button>
        <button onClick={() => setPage("training")}>Training</button>
        <button onClick={() => setPage("security")}>Security</button>
        <button onClick={() => setPage("dashboard")}>Dashboard</button>
      </nav>

      {renderPage()}

      <footer>
        Digital Literacy Assistant | Anantapur Community Service Project
      </footer>
    </div>
  );
}

function Home({ setPage }) {
  return (
    <div className="container">
      <div className="hero">
        <h1>Digital Literacy Assistant</h1>
        <p>Empowering Communities Through Digital Education</p>
      </div>

      <div className="card">
        <h2>About the Project</h2>
        <p>
          This project helps community members learn smartphone usage,
          digital payments, online services, and cyber security practices.
        </p>
      </div>

      <div className="card">
        <button onClick={() => setPage("training")}>
          Digital Payment Training
        </button>

        <button onClick={() => setPage("security")}>
          Cyber Security Guide
        </button>

        <button onClick={() => setPage("dashboard")}>
          View Dashboard
        </button>
      </div>
    </div>
  );
}

function Training() {
  return (
    <div className="container">
      <div className="hero">
        <h1>Digital Payment Training</h1>
      </div>

      <div className="card">
        <h2>Step 1: Install UPI App</h2>
        <p>Download PhonePe, Google Pay, Paytm or BHIM.</p>
      </div>

      <div className="card">
        <h2>Step 2: Link Bank Account</h2>
        <p>Verify your registered mobile number.</p>
      </div>

      <div className="card">
        <h2>Step 3: Create UPI PIN</h2>
        <p>Create a secure PIN and never share it.</p>
      </div>
    </div>
  );
}

function Security() {
  const tips = [
    "Never Share OTP",
    "Use Strong Passwords",
    "Avoid Unknown Links",
    "Keep Apps Updated",
    "Verify Websites Before Login"
  ];

  return (
    <div className="container">
      <div className="hero">
        <h1>Cyber Security Safety Guide</h1>
      </div>

      {tips.map((tip, index) => (
        <div className="card" key={index}>
          <h2>{tip}</h2>
        </div>
      ))}
    </div>
  );
}

function Dashboard() {
  return (
    <div className="container">
      <div className="hero">
        <h1>Training Results Dashboard</h1>
      </div>

      <div className="card">
        <h2>Metrics & Growth</h2>

        <p>UPI Users Growth</p>
        <progress value="87" max="100"></progress>

        <p>Online Service Users Growth</p>
        <progress value="90" max="100"></progress>

        <p>Email Users Growth</p>
        <progress value="85" max="100"></progress>
      </div>
    </div>
  );
}

export default App;