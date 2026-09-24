import { useEffect, useState } from 'react';

function App() {
  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState('');

  useEffect(() => {
    fetch('http://localhost:8000/api/tasks/')
      .then(res => res.json())
      .then(data => setTasks(data));
  }, []);

  const addTask = async (e) => {
    e.preventDefault();
    const res = await fetch('http://localhost:8000/api/tasks/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title }),
    });
    const newTask = await res.json();
    setTasks([...tasks, newTask]);
    setTitle('');
  };

  const toggleDone = async (task) => {
    const res = await fetch(`http://localhost:8000/api/tasks/${task.id}/`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        title: task.title,
        description: task.description,
        is_done: !task.is_done,
      }),
    });
    const updatedTask = await res.json();
    console.log('Updated task:', updatedTask);
    setTasks(tasks.map(t => t.id === updatedTask.id ? updatedTask : t));
  };

  return (
    <div>
      <h1>Tasks</h1>
      <form onSubmit={addTask}>
        <input
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="New task"
        />
        <button type="submit">Add</button>
      </form>
      <ul>
        {tasks.map((t) => (
          <li key={t.id}>
            {t.title} {t.is_done ? '✅' : '⏳'}
            <button onClick={() => toggleDone(t)}>
              {t.is_done ? 'Mark Undone' : 'Mark Done'}
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;