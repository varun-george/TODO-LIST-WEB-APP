import axios from 'axios'
import React from 'react'

function TodoItem(props) {
    const deleteTodoHandler = (todo) => {
    axios.delete('http://localhost:8000/todo-list/${todo}')
        .then(res => console.log(res.data)) }
  
    return (
        <div>
            <p>
                <span style={{ fontWeight: 'bold, underline' }}>{props.todo.todo} : </span> {props.todo.description} 
                <button onClick={() => deleteTodoHandler(props.todo.todo)} className="btn btn-outline-danger my-2 mx-2" style={{'borderRadius':'50px',}}>del</button>
                <hr></hr>
            </p>
        </div>
    )
}

export default TodoItem;

