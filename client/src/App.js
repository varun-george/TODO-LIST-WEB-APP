import './App.css';
import React, {useEffect,useState} from 'react';
import axios from 'axios'
import TodoView from './components/TodoListView';

function App() {

  const [todoList, setTodoList] = useState([{}])
  const [todo, setTodo] = useState('') 
  const [desc, setDesc] = useState('')


  useEffect(() => {
    axios.get('http://localhost:8000/todo-list')
      .then(res => {
        setTodoList(res.data)
      })
  });

  // Post a todo
  const addTodoHandler = () => {
    axios.post('http://localhost:8000/todo-list/', { 'todo': todo, 'description': desc })
      .then(res => console.log(res))
    };

  return (
    <div className="App list-group-item  justify-content-center align-items-center mx-auto" style={{"width":"400px", "backgroundColor":"white", "marginTop":"15px"}} >
      <h1 className="card text-white bg-primary mb-1" stylename="max-width: 20rem;">Task Manager</h1>
     <div className="card-body">
      <h5 className="card text-black bg-secondary mb-3">Add Your Task</h5>
      <span className="card-text"> 
        <input className="mb-2 form-control titleIn" onChange={event => setTodo(event.target.value)} placeholder='Title'/> 
        <input className="mb-2 form-control desIn" onChange={event => setDesc(event.target.value)}   placeholder='Description'/>
      <button className="btn btn-outline-primary mx-2 mb-3" style={{'borderRadius':'50px',"font-weight":"bold"}}  onClick={addTodoHandler}>Add Task</button>
      </span>
      <h5 className="card text-white bg-success mb-3">Your Tasks</h5>
      <div >
      <TodoView todoList={todoList} />
      </div>
      </div>
    </div>
  );
}

export default App;
