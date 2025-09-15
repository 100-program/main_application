import React from "react";
import TopBar from "../components/TopBar";
import StopWatch from "../components/StopWatch";
import TaskList from "../components/TaskList";
import Avatar from "../components/Avatar";

function Dashboard() {
  return (
    <div className="app-container">
      <header className="TopBar">
        <TopBar />
      </header>

      <main className="app-main">
        <section className="stopwatch-section">
          <StopWatch />
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
