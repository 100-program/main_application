import React, { useState } from "react";

function TaskList() {
  const [tasks, setTasks] = useState([
    { id: 1, text: "ストレッチする", completed: false },
    { id: 2, text: "水を飲む", completed: false },
    { id: 3, text: "5分間集中する", completed: false },
  ]);

  const toggleComplete = (id) => {
    setTasks((prev) =>
      prev.map((task) =>
        task.id === id ? { ...task, completed: !task.completed } : task
      )
    );
  };

  const deleteTask = (id) => {
    setTasks((prev) => prev.filter((task) => task.id !== id));
  };

  return (
    <div className="task-list">
      <h2>タスク一覧</h2>
      <ul>
        {tasks.map((task) => (
          <li key={task.id} className={task.completed ? "completed-task" : ""}>
            <span>{task.text}</span>
            <button onClick={() => toggleComplete(task.id)}>
              {task.completed ? "未完了に戻す" : "完了"}
            </button>
            <button onClick={() => deleteTask(task.id)}>削除</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TaskList;
