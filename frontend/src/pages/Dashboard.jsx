import React from "react";
import Timer from "../components/StopWatch";
import TaskList from "../components/TaskList";
import Avatar from "../components/Avatar";

function Dashboard() {
  return (
    <div className="app-container">
      <header className="app-header">
        <h1 className="app-title">My Avatar Timer</h1>
        <div className="gem-display">
          💎 <span>100</span>
        </div>
      </header>

      <main className="app-main">
        <section className="stopwatch-section">
          <Timer />
        </section>

        <section className="avatar-section">
          <Avatar />
        </section>

        <section className="task-section">
          <TaskList />
        </section>
      </main>
    </div>
  );
}

export default Dashboard;
