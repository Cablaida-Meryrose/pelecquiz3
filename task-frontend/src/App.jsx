import { useEffect, useState } from "react";

const API_URL = "http://127.0.0.1:8000/api/";

export default function App() {
  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState("");

  // FETCH TASKS
  const fetchTasks = async () => {
    try {
      const res = await fetch(API_URL);
      const data = await res.json();
      setTasks(data);
    } catch (error) {
      console.log("Error fetching tasks:", error);
    }
  };

  // ADD TASK
  const addTask = async () => {
    if (!title.trim()) return;

    try {
      await fetch(API_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          title: title,
          is_completed: true,
        }),
      });

      setTitle("");
      fetchTasks(); // refresh list
    } catch (error) {
      console.log("Error adding task:", error);
    }
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  return (
    <div style={styles.container}>
      <h1>Task Management System</h1>

      {/* INPUT SECTION */}
      <div style={styles.inputBox}>
        <input
          type="text"
          placeholder="Enter task..."
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          style={styles.input}
        />

        <button onClick={addTask} style={styles.button}>
          Add Task
        </button>
      </div>

      {/* TASK LIST */}
      <div style={{ marginTop: "20px" }}>
        {tasks.length === 0 ? (
          <p>No tasks yet</p>
        ) : (
          tasks.map((task) => (
            <div key={task.id} style={styles.task}>
              <span>{task.title}</span>
              <span>{task.is_completed ? "✅" : "❌"}</span>
            </div>
          ))
        )}
      </div>
    </div>
  );
}

// SIMPLE STYLES
const styles = {
  container: {
    maxWidth: "500px",
    margin: "50px auto",
    fontFamily: "Arial",
  },
  inputBox: {
    display: "flex",
    gap: "10px",
  },
  input: {
    flex: 1,
    padding: "10px",
  },
  button: {
    padding: "10px",
    cursor: "pointer",
  },
  task: {
    display: "flex",
    justifyContent: "space-between",
    padding: "10px",
    borderBottom: "1px solid #ddd",
  },
};